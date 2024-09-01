import re

def extract_fields(text):
    fields = ["Redflags", "Final Result", "Actions", "Suggestions"]
    extracted_data = {}
    for field in fields:
        if field == "Redflags":
            pattern = re.compile(r"Redflags -\n(.*?)(?=\nInfo Extraction:|\Z)", re.DOTALL)
        else:
            pattern = re.compile(rf"{field}:(.*?)(?=\n[A-Za-z ]+:|\Z)", re.DOTALL)
        match = pattern.search(text)
        if match:
            value = match.group(1).strip()
            if field == "Suggestions":
                value = value.split("$Result Format end here$")[0].strip()
            extracted_data[field] = value
    return extracted_data

def extract_details_from_response(response1):
    details = {}
    # Extract Script Follow Score
    script_follow_score = re.search(r"Script follow: (\d+/\d+)", response1)
    if script_follow_score:
        details['Script Follow Score'] = script_follow_score.group(1)
    # Extract Sales Pitch Score
    sales_pitch_score = re.search(r"Sales Pitch: (\d+/\d+)", response1)
    if sales_pitch_score:
        details['Sales Pitch Score'] = sales_pitch_score.group(1)
    # Extract other details using regular expressions
    fields = [
        'Lead ID', 'Lead Name', 'Agent Name','Accommodation Preference','Budget','Self-funding or Loan', 'Script Follow Score', 'Sales Pitch Score',
        'Move-in Date', 'Lead Status', 'Accommodation booking status', 'Counselling Scheduled Status', 'Call Summary', 'Callback Scheduled'
    ]
    for field in fields:
        pattern = re.compile(rf"{field}:(.*?)(?=\n[A-Za-z ]+:|\Z)", re.DOTALL)
        match = pattern.search(response1)
        if match:
            details[field] = match.group(1).strip().split("\n\n")[0].strip()
    # res =  json.dumps(details, indent=4)
    res = details
    # print(res)
    # res['extract'] = {}
    new_res = extract_fields(response1)
    res['extract'] = new_res
    print(type(res))
    return(f"new:\n\n{res}\n\n")

response = """Scores -
   1. Script follow - 7/7
   2. Sales Pitch - 8/10

Info Extraction:
           Lead ID: Nikhil
           Lead Name: Nikhil
           LQT Name: Harish
           Passport Status: Yes
           Course: Supply Chain Management and Logistics
           Country: Ireland
           Intake: January 2025
           Script Follow Score: 7/7
           Academic Scores/Cumulative GPA (CGPA): 10th: 75%, 12th: 74%, Bachelor's: 76%
           Work Experience: None specified (Fresher)
           Customer Budget: 20 lakhs
           Self-funding or Loan: Self-funding
           Counselling Scheduled Status: Counseling session booked for tomorrow at 5 PM
           Competitive Exams Status: Not specified
           Sales Pitch Score: 8/10
           Lead Status: Qualified   

Final Result: The customer is interested and a call with counsellor is scheduled for tomorrow at 5 PM

Actions: The agent should follow up with the customer to confirm the receipt of documents and ensure the counseling session goes smoothly.

Suggestions: The agent should work on addressing concerns and providing financial incentives to make the offer more attractive. Additionally, the agent should provide detailed information on the payment process to ensure a smooth transaction."""

response2 = """Lead Name: Prakha
Lead Status: Not mentioned
Counselling Scheduled Status: Not mentioned
Call Summary: Not available
Callback Scheduled: Yes, mentioned to call back later"""

print(extract_details_from_response(response2))