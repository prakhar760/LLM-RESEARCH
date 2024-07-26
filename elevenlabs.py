# import requests

# url = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
# api_key = "sk_8a8da54f9ce9c6755a2e2ef2bbc49364a37b57149100c1fa"

# payload = {
#     "text": "",
#     "model_id": "<string>",
#     "language_code": "<string>",
#     "voice_settings": {
#         "stability": 123,
#         "similarity_boost": 123,
#         "style": 123,
#         "use_speaker_boost": True
#     },
#     "seed": 123,
#     "previous_text": "<string>",
#     "next_text": "<string>",
#     "previous_request_ids": [
#         "<string>"
#     ],
#     "next_request_ids": [
#         "<string>"
#     ]
# }

# headers = {
#     "Content-Type": "application/json",
#     "xi-api-key": api_key
# }

# response = requests.post(url, json=payload, headers=headers)

# print(response.text)

import requests

url = "https://api.elevenlabs.io/v1/text-to-speech/Monika"

payload = {"text": "HI this is alisha"}
headers = {
    "xi-api-key": "sk_8a8da54f9ce9c6755a2e2ef2bbc49364a37b57149100c1fa",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)