import json
from google import genai
from pathlib import Path
import importlib

def load_skills():
  skills = {}
  base_path = Path(__file__).resolve().parent.parent / "skills"

  for skill_dir in base_path.iterdir():
    if skill_dir.is_dir():
      name = skill_dir.name

      # --- load prompt ---
      prompt_path = skill_dir / "skills.md"
      prompt_text = prompt_path.read_text(encoding="utf-8") if prompt_path.exists() else ""

      lines = prompt_text.splitlines()
      description = "\n".join(lines[:24])

      # --- try to load logic.py (optional) ---
      logic_path = skill_dir / "logic.py"

      if logic_path.exists():
        spec = importlib.util.spec_from_file_location(f"{name}_logic", logic_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        run_fn = module.run
      else:
        def default_run(input_text, llm_request, prompt_text=prompt_text):
          prompt = f"""
          {prompt_text}

          Input:
          {input_text}

          Output:
          """
          return llm_request(prompt)

        run_fn = default_run

      skills[name] = {
        "run": run_fn,
        "prompt": prompt_text,
        "description": description
      }

  return skills


SKILLS = load_skills()


def llm_request(contents):
  client = genai.Client()

  response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=contents
  )
  
  return response.candidates[0].content.parts[0].text

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
      "input": "text to pass to the skill",
      "done": false
  }}
  """

  response = llm_request(prompt)
  return response

def run_agent(user_input):
  conversation = f"User: {user_input}\n"

  decision_raw = decide_next_action(conversation, SKILLS)
  print(decision_raw)

  try:
    decision = json.loads(decision_raw)
  except:
    return f"Failed to parse LLM output:\n{decision_raw}"

  if decision.get("done"):
    return conversation

  skill_name = decision["skill"]
  skill_input = decision["input"]

  if skill_name not in SKILLS:
    return f"Unknown skill: {skill_name}"

  skill = SKILLS[skill_name]

  result = skill["run"](
      skill_input,
      llm_request,
      skill["prompt"]
  )

  conversation += f"\nAgent used {skill_name}:\n{result}\n"


if __name__ == "__main__":
  user_input = input("Enter your claim: ")
  result = run_agent(user_input)
  print("\nFINAL RESULT:\n")
  print(result)