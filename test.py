# import os
# from dotenv import load_dotenv

# load_dotenv()
extraction = {'Lead Name': 'Prakha', 'Lead Status': 'Not mentioned', 'Counselling Scheduled Status': 'Not mentioned', 'Call Summary': 'Not available', 'Callback Scheduled': 'Yes, mentioned to call back later', 'extract': {}}
# openai_api_key = os.getenv('OPENAI_API_KEY')
# print(openai_api_key)
import json
prompt = """{\"Lead Name\": \"Prakha\", \"Lead Status\": \"Not mentioned\", \"Counselling Scheduled Status\": \"Not mentioned\", \"Call Summary\": \"Not available\", \"Callback Scheduled\": \"Yes, mentioned to call back later\", \"extract\": {}}"""

if isinstance(extraction, dict):
   # extraction = json.dumps(extraction)
   extraction = extraction
prompt = json.loads(prompt)
if 'Callback Scheduleda' in extraction:
   print("heyyy")
   callback_scheduled = extraction['Callback Scheduled']
# print(prompt)
print(type(extraction))
print(extraction)