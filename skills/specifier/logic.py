from pathlib import Path
from google import genai


def load_system_prompt():
    path = Path(__file__).resolve().parent / "skills.md"
    content = path.read_text(encoding="utf-8")
    return content.strip()

def llm_request(contents):
  client = genai.Client()

  response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=contents
  )
  
  return response.candidates[0].content.parts[0].text


def run(input):
  """
  student_input: dict like:
  {
      "claim": "...",
      "context": "assignment prompt (optional)"
  }
  """

  system_prompt = load_system_prompt()

  user_prompt = f"""
  Student claim:
  {input.get("claim")}

  Assignment context (if any):
  {input.get("context", "N/A")}

  Task:
  Apply the Specifier skill.
  {system_prompt}
  """

  response = llm_request(user_prompt)

  return response