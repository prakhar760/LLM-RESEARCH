import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("FIREWORKSAI_API_KEY")

transcript = """
Speaker 0:

Hello?

Speaker 1:

Yes? Hi.

Speaker 0:

I am Nancy from UniCRED. Am I speaking with Rachna?

Speaker 1:

Yes. You're speaking with Rachna.

Speaker 0:

I received your inquiry regarding an education loan for studying abroad. Is this a convenient time to talk about your plans for the loan?

Speaker 1:

Yeah. Please continue. Hello?

Speaker 0:

What's your target country for studying abroad?

Speaker 1:

I'm looking for university in UK.

Speaker 0:

Great. I see you are planning to study in the UK. Let me connect you with our agent for a detailed discussion. What time works best for you?

Speaker 1:

I'm free tomorrow. 10 AM.

Speaker 0:

Perfect. I've got you down for a session on August 30, 2024 at 10 AM. You'll get an email or text soon with all the details.

Speaker 1:

Thank you.

Speaker 0:

Thanks so much for your time, Rachna. We're excited to help you with your study abroad journey. Have a great day ahead.
"""

result_format = """
$Result Format-Example$(don't include this heading)

I. Script Follow
   Segment 1: Introduction and Verification
       Answer: Yes
       Reason: The agent greeted the callee, verified their identity, and introduced themselves and the purpose of the call.
       Transcript: "Hello hello. ... Yeah, am I speaking with Venkata"
   Segment 2: Inquiry Confirmation
       Answer: Yes
       Reason: The agent confirmed the study abroad inquiry and verified the intended intake period.
       Transcript: "I think on May eleventh you placed an inquiry on the website for your counselling session with the USA expert for your masters."
   Segment 3: Accommodation Preferences
       Answer: Yes
       Reason: The agent gathered relevant accommodation information and clarified the field of study.
       Transcript: "Your tenth was in which year? ... And then you did your 3 years of bachelor's? ... Information technology."
   Segment 4: Budget and Financial Planning
       Answer: Yes
       Reason: The agent discussed the course cost, living expenses, and funding options with the callee.
       Transcript: "So, overall like 40 lakhs for universities. And living expenses if you include, it goes around 10 lakhs or 1 hour."
   Segment 5: Accommodation Recommendation List
       Answer: Yes
       Reason: The agent offered accommodation sessions, discussed available time slots, and confirmed the preferred time for the session.
       Transcript: "So, just dropped the hi on WhatsApp. Can you please help me with your resume and your academic mark sheet?"
   Segment 6: Final Confirmation and Closing
       Answer: Yes
       Reason: The agent requested academic documents for verification and explained the purpose of document verification.
       Transcript: "Mark sheet like basically this is to cross verify the information that you have already provided."
   Optional Segment 1: Discounts and Offers
       Answer: Yes
       Reason: The agent confirmed the booking of the counselling session and provided final instructions before closing the call.
       Transcript: "Your slot will be booked on the given mail ID, and you will be getting a notification on the mail ID, okay?"
   Optional Segment 2: Additional Services and Support
       Answer: Yes
       Reason: The agent requested academic documents for verification and explained the purpose of document verification.
       Transcript: "Mark sheet like basically this is to cross verify the information that you have already provided."
   Optional Segment 3: Application Status Confirmation
       Answer: Yes
       Reason: The agent confirmed the booking of the counselling session and provided final instructions before closing the call.
       Transcript: "Your slot will be booked on the given mail ID, and you will be getting a notification on the mail ID, okay?"
      
   Overall Script Follow Score: 6/6

II. Sales Pitch
   Segment 1: Identification and Addressing by Name
       Answer: Yes
       Reason: The agent addressed the customer by their name, Venkata, multiple times throughout the call.
       Transcript: "Hi Venkata. This call is from Uni Scholars."
   Segment 2: Reference to Previous Enquiry
       Answer: Yes
       Reason: The agent referenced the customer's previous inquiry on the website.
       Transcript: "We got your inquiry for study abroad for computer engineering for you us."
   Segment 3: Confirmation of Interest
       Answer: Yes
       Reason: The agent confirmed the customer's interest in studying abroad and the specific program they inquired about.
       Transcript: "So I just want to understand that you are planning this for Jan 25 intake?"
   Segment 4: Addressing Concerns and Reassurances
       Answer: Yes
       Reason: The agent provided some reassurances about the process but did not address specific concerns.
       Transcript: "I can connect you with a USA export who can help you with the university selection, SOP, aloud, like you know your profile building everything, okay."
   Segment 5: Highlighting Benefits and Facilities
       Answer: Yes
       Reason: The agent highlighted the benefits of early application and potential partial qualifications.
       Transcript: "If the early you apply, the early you have the opportunity to apply for partial qualifications."
   Segment 6: Urgency and Scarcity
       Answer: Yes
       Reason: The agent created a sense of urgency by mentioning deadlines and the benefits of early application.
       Transcript: "If the early you apply, the early you have the opportunity to apply for partial qualifications."
   Segment 7: Financial Incentives and Offers
       Answer: No
       Reason: The agent discussed the cost of education and living expenses but did not offer specific financial incentives.
       Transcript: "1 year university fees cost you around 20 lakhs."
   Segment 8: Explaining the Payment Process and Flexibility
       Answer: Partial
       Reason: The agent mentioned funding options but did not provide detailed information on the payment process.
       Transcript: "I believe you are going to take an education loan for this or partially self-fund this side."
   Segment 9: Encouragement to Commit
       Answer: Yes
       Reason: The agent encouraged the customer to proceed with the counseling session booking.
       Transcript: "Congratulations for the free counselling session from Uni Scholars."
   Segment 10: Openness to Further Discussion
       Answer: Yes
       Reason: The agent was open to further discussion and answered the customer's questions.
       Transcript: "Can you please help me with your resume and your academic mark sheet?"

   Overall Sales Pitch Score: 8.5/10

Scores -
   1.Script follow Score - 10/10
   2.Sales Pitch Score - 8.5/10

Redflags -

   1. Addressing Concerns and Reassurances - Partial:
           Reason: The agent did not address specific concerns raised by the customer.
           Improvement: The agent should actively listen to the customer's concerns and provide relevant reassurances and solutions.
           Transcript snippet: "I can connect you with a USA export who can help you with the university selection, SOP, aloud, like you know your profile building everything, okay."
   2. Financial Incentives and Offers - No:
           Reason: The agent discussed costs but did not mention any specific financial incentives or offers.
           Improvement: The agent should highlight any available financial incentives or discounts to encourage the customer.
           Transcript snippet: "1 year university fees cost you around 20 lakhs."
   3. Explaining the Payment Process and Flexibility - Partial:
           Reason: The agent mentioned funding options but did not provide detailed information on the payment process.
           Improvement: The agent should explain the payment process clearly and offer flexibility options to the customer.
           Transcript snippet: "I believe you are going to take an education loan for this or partially self-fund this side."

Info Extraction:
          Lead ID: Venkata
          Lead Name: Venkata
          Agent Name: <Agent Name>
          Accommodation Preference: Single room with private bathroom
          Country: USA
          University: Harvard University
          Intake: September 2024
          Budget: $20,000 per year
          Self-funding or Loan: Partial self-funding and partial education loan discussed
          Move-in Date: August 15, 2024
          Script Follow Score: <its overall score> 
          Sales Pitch Score: <its overall score> 
          Accommodation booking status: Not booked yet
    Final Result: The customer is interested and a call with counsellor is scheduled at what time.
    Actions: Based on your own knowledge, what actions does the agent has to take after the call is completed.
    Suggestions: Based on the transcript, suggested actions for the agent to improve the call.
$Result Format-Ends Here$\
<Overall Recommendations for Result Format>
      1. If the confusion gets cleared throughout the end of the conversation.
      2. Give reason for the red flags given.
      3. If any segment is not applicable because the call ended before but the agent follows the script till that segment, then do not count that segment score for overall analysis as it can impact agent performance.
<Answering and Scoring Instructions>
      1. Answer should be Yes/No/Not applicable.
      2. Scoring should not be considered if the answer is not applicable or there is no reference in the transcript.
      3. If the transcript is not available then answer that segment as not applicable.
      4. Suppose there are 10 segments and one is not applicable then the overall score should be given without counting not applicable segments.
      5. These rules applied on both script follow and sales pitch.
      6. Status of the application should be Qualified (if interested)/ Lost (if not interested)/Can't determine(if confused).
"""

result_format_old = """
$Result Format-Example$(don't include this heading)

Info Extraction:
           Lead ID: Venkata
           Lead Name: Venkata
           LQT Name: <Agent Name>
           Passport Status: Yes,Confirmed to be from Andhra Pradesh
           Course: Computer Engineering (B.Tech in Information Technology)
           Country: USA
           Intake: January 2025
           Script Follow Score: <its overall score> 
           Academic Scores/Cumulative GPA (CGPA): 10th: 77%, 12th: 74.872%, Bachelor's: CGPA 7.28
           Work Experience: None specified (Fresher)
           Customer Budget: Not specified
           Self-funding or Loan: Partial self-funding and partial education loan discussed
           Counselling Scheduled Status: Counseling session booked for tomorrow at 5 PM
           Competitive Exams Status: Not specified
           Sales Pitch Score: <its overall score>
           Lead Status:  qualified
   Final Result: The customer is interested and a call with counsellor is scheduled at what time.
   Actions: Based on your own knowledge, what actions does the agent has to take after the call is completed.
   Suggestions: Based on the transcript, suggested actions for the agent to improve the call.
$Result Format end here$\
<overall recommendations for result format>
       1. if the confusion gets cleared throughout the end of conversation.
       2. give reason for the red flags given.
       3. if any segment is not applicable because call ended before but agent follows script till that segment than do not count that segment score for overall analysis as it can impact agent performance.
<Answering and Scoring instructions>
       1. Answer should be Yes/No/Not applicable
       2. Scoring should not be considered if answer is not applicable or there is no reference in transcript.
       3. if transcript is not available then answer that segment as not applicable.
       4. suppose there are 10 segments and one is not applicable then the overall score should be given without counting not applicable segments.
       5. these rules applied on both script follow and sales pitch.
       6. status of the application should be Qualified (if interested)/ Lost (if not interested)/can't determine(if confused).
"""

prompt = f"""
Context: You are evaluating the performance of a voice AI agent in a customer service context for an educational consultancy specializing in study abroad programs. Your task is to identify any defects, irregularities, or shortcomings in the AI's responses and behaviour during the call.
Instructions:
1. Analyze the provided call transcript carefully.
2. Identify any defects or issues in the AI agent's performance.
3. Categorize each defect according to the types listed below.
4. Provide a brief explanation and a relevant transcript excerpt for each identified defect.
5. Explicitly ignore and do not report any issues related to:
   - Incorrect name pronunciations or usage
   - Spelling mistakes
   - Minor grammatical errors
   - Slight mispronunciations of words
   These are not considered defects for the purpose of this evaluation.
6. Redflags value should be in string format, you can use \n. Do not use JSON or array format.
Types of AI Defects to Look For:
1. Understanding and Relevance:
   - Misinterpretation of user intent
   - Failure to understand context or nuance
   - Providing irrelevant or off-topic information
   - Failing to address the user's specific question
   Example: User asks about "course fees" but AI responds about "visa fees"
2. Conversational Coherence:
   - Abrupt topic changes
   - Failure to maintain context across multiple turns
   - Unnecessarily repeating information
   - Getting stuck in a loop
   Example: AI asks the same question twice in succession
3. Knowledge and Accuracy:
   - Providing incorrect or outdated information
   - Inability to answer common questions within its domain
   - Providing contradictory information within the same conversation
   Example: AI provides incorrect information about visa requirements
4. Handling Complex Situations:
   - Inability to break down or address multi-part questions
   - Failure to recognize or respond appropriately to user emotions
   - Inappropriate tone or sentiment
   - Failure to recognize when to transfer to a human agent
   Example: User expresses frustration, but AI doesn't offer to connect them with a human
5. Technical Performance:
   - Unnatural pauses or rushed responses
   - Interrupting the user
   - Any other technical glitches in the AI's performance
   Example: AI responds before the user has finished speaking
Result Format:
Redflags:
1. Defect Type: [Type from the list above]
   Description: [Brief explanation of the defect]
   Transcript: [Relevant excerpt from the call]
2. [If applicable]
Recommendations:
1. [Recommendation for improvement]
2. [Recommendation for improvement]
3. [Recommendation for improvement]
If no defects are found, state: "No significant defects were identified in the AI agent's performance during this call."
Important Note: Do not flag any issues related to names, including incorrect usage, pronunciation, or spelling of names. These are not considered defects for this evaluation.

Conversation Transcript:
{transcript}

"""
# {result_format}
url = "https://api.fireworks.ai/inference/v1/chat/completions"
payload = {
  "model": "accounts/fireworks/models/llama-v3p1-405b-instruct",
  "max_tokens": 131072,
  "top_p": 1,
  "top_k": 40,
  "presence_penalty": 0,
  "frequency_penalty": 0,
  "temperature": 0.6,
  "messages": 
    [
        {
            "role": "assistant",
            "content": prompt
        }
    ]
}
headers = {
#   "Accept": "application/json",
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}
response = requests.request("POST", url, headers=headers, json=payload)
response = response.json()
print(response)
print("\n\n-----------------------")
# print(response.text)
# print(response.choices[0].message.content)
