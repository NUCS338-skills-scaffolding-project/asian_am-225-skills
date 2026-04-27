from google import genai

def llm_request(contents):
  client = genai.Client()

  response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=contents
  )
  
  return response
