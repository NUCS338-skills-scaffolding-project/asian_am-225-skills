# fullDemo.py

import json
from google import genai
from pathlib import Path
import importlib.util


# -----------------------------
# Load skills (with optional logic.py)
# -----------------------------
def load_skills():
    skills = {}
    base_path = Path(__file__).resolve().parent.parent / "skills"

    for skill_dir in base_path.iterdir():
        if not skill_dir.is_dir():
            continue

        name = skill_dir.name

        # --- load prompt ---
        prompt_path = skill_dir / "skills.md"
        prompt_text = (
            prompt_path.read_text(encoding="utf-8")
            if prompt_path.exists()
            else ""
        )

        lines = prompt_text.splitlines()
        description = "\n".join(lines[:24])

        # --- try to load logic.py (optional) ---
        logic_path = skill_dir / "logic.py"
        run_fn = None

        if logic_path.exists():
            try:
                spec = importlib.util.spec_from_file_location(
                    f"{name}_logic",
                    logic_path
                )
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                run_fn = getattr(module, "run", None)

            except Exception as e:
                print(f"[WARN] Failed to load logic.py for {name}: {e}")
                run_fn = None

        # --- fallback to default lambda ---
        if run_fn is None:
            run_fn = lambda input_text, llm_request, prompt_text=prompt_text: default_run(
                input_text,
                llm_request,
                prompt_text
            )

        skills[name] = {
            "run": run_fn,
            "prompt": prompt_text,
            "description": description
        }

    return skills


SKILLS = load_skills()


# -----------------------------
# LLM wrapper
# -----------------------------
def llm_request(contents):
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=contents
    )

    return response.candidates[0].content.parts[0].text


# -----------------------------
# Default skill runner
# -----------------------------
def default_run(input_text, llm_request, prompt_text):
    prompt = f"""
{prompt_text}

Input:
{input_text}

Output:
"""
    return llm_request(prompt)


# -----------------------------
# Auto skill selection
# -----------------------------
def decide_next_action(conversation, skills):
    prompt = f"""
You are an agent that selects the next skill.

Available skills:
{skills}

Conversation so far:
{conversation}

Respond ONLY in JSON:
{{
    "skill": "specifier",
    "done": false
}}
"""

    response = llm_request(prompt)

    try:
        return json.loads(response)
    except:
        return {"error": response}


# -----------------------------
# Main agent loop
# -----------------------------
def run_agent(user_input, skill=None, history=None):
    if history is None:
        history = []

    if skill is None:
        raise ValueError("Skill must be provided")

    trace = []

    # 1. add user input
    history.append({
        "role": "user",
        "content": user_input
    })

    # 2. AUTO routing
    if skill.lower() == "auto":
        decision = decide_next_action(history, SKILLS)

        if "error" in decision:
            return {"error": decision["error"]}

        if decision.get("done"):
            return {
                "result": "done",
                "history": history,
                "trace": trace,
                "skill_used": "auto (done)"
            }

        skill_name = decision["skill"]
        skill_obj = SKILLS[skill_name]
    else:
        skill_name = skill
        skill_obj = SKILLS[skill]

    # 3. build context
    context = "\n".join(
        f"{m['role'].upper()}: {m['content']}"
        for m in history
    )

    # 4. run skill
    result = skill_obj["run"](
        context,
        llm_request,
        skill_obj["prompt"]
    )

    # 5. update history
    history.append({
        "role": "assistant",
        "content": result
    })

    trace.append({
        "skill": skill,
        "input": user_input,
        "output": result
    })

    return {
        "result": result,
        "history": history,
        "trace": trace,
        "skill_used": skill_name if skill.lower() == "auto" else skill
    }


# -----------------------------
# CLI entry
# -----------------------------
if __name__ == "__main__":
    user_input = input("Enter your claim: ")
    result = run_agent(user_input)
    print("\nFINAL RESULT:\n")
    print(result)