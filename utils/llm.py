from google import genai
from google.genai import types
import pathlib
from pathlib import Path

FOLDER_NAME = "Class_Materials/PDF_Readings"

def llm_request(contents, readings=False):
  client = genai.Client()

  readingsFilePaths = [f.name for f in Path(FOLDER_NAME).iterdir() if f.is_file()]

  SampleFiles = []

  for filePath in readingsFilePaths:
    sampleFile = client.files.upload(
      file=FOLDER_NAME + "/" + filePath,
    )
    SampleFiles.append(sampleFile)
  
  SampleFiles.append(contents)

  response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=SampleFiles
  )
  
  return response

print(llm_request("Read these documents and write 1 word per document"))
