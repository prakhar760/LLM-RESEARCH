import os
from together import Together
from dotenv import load_dotenv

load_dotenv()

result_format = """
$Result Format-Example$(don't include this heading)

I.Script Follow-
   Segment 1: Introduction and Verification
               Answer: Yes
               Reason: The agent greeted the callee, verified their identity, and introduced themselves and the purpose of the call.
               Transcript: "Hello hello. ... Yeah, am I speaking with Venkata"
   Segment 2: Inquiry Confirmation
               Answer: Yes
               Reason: The agent confirmed the study abroad inquiry and verified the intended intake period.
               Transcript: "I think on May eleventh you placed an inquiry on the website for your counselling session with the USA expert for your masters."
   Segment 3: Academic Background and Qualifications
               Answer: Yes
               Reason: The agent gathered relevant academic information and clarified the field of study.
               Transcript: "Your tenth was in which year? ... And then you did your 3 years of bachelor's? ... Information technology."
   Segment 4: Budget and Financial Planning
               Answer: Yes
               Reason: The agent discussed the course cost, living expenses, and funding options with the callee.
               Transcript: "So, overall like 40 lakhs for universities. And living expenses if you include, it goes around 10 lakhs or 1 hour."
   Segment 5: Scheduling Counseling Session
               Answer: Yes Addressing Concerns and Reassurances
               Reason: The agent offered counselling sessions, discussed available time slots, and confirmed the preferred time for the session.
               Transcript: "So, just dropped the hi on WhatsApp. Can you please help me with your resume and your academic mark sheet?"
   Segment 6: Document Verification
               Answer: Yes
               Reason: The agent requested academic documents for verification and explained the purpose of document verification.
               Transcript: "Mark sheet like basically this is to cross verify the information that you have already provided."
   Segment 7: Final Confirmation and Closing
               Answer: Yes
               Reason: The agent confirmed the booking of the counselling session and provided final instructions before closing the call.
               Transcript: "Your slot will be booked on the given mail ID, and you will be getting a notification on the mail ID, okay?"
   Overall Script Follow Score: 7/7
II. Sales Pitch
   Segment 1: Identification and Addressing by Name
               Answer: Yes
               Reason: The agent addressed the customer by their name, venkata, multiple times throughout the call.
               Transcript: "Hi venkata. This call is from Uni Scholars."
   Segment 2: Reference to Previous Communication
               Answer: Yes
               Reason: The agent referenced the customer's previous inquiry on the website.
               Transcript: "We got your inquiry for study abroad for computer engineering for you us."
   Segment 3: Confirmation of Interest
               Answer: Yes
               Reason: The agent confirmed the customer's interest in studying abroad and the specific program they inquired about.
               Transcript: "So I just want to understand that you are planning this for jan 25 in day?"
   Segment 4: Addressing Concerns and Reassurances
               Answer: Yes
               Reason: The agent provided some reassurances about the process but did not address specific concerns.
               Transcript: "I can connect you with a USA export who can help you with the university selection, SOP, aloud, like you know your profile building everything, ok."
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
               Transcript: "Congratulations for the free counselling session from tennis scholar."
   Segment 10: Openness to Further Discussion
               Answer: Yes
               Reason: The agent was open to further discussion and answered the customer's questions.
               Transcript: "Can you please help me with your resume and your academic mark sheet?"
   Overall Sales Pitch Score: 8.5/10
Scores -
   1.Script follow - <its overall score>
   2.Sales Pitch - <its overall score>
Redflags -
   1. Addressing Concerns and Reassurances - Partial:
           Reason of the point
           Improvement for the point
           Transcript snippet
   2. Financial Incentives and Offers - No:
           Reason of the point
           Improvement for the point
           Transcript snippet
   3. Explaining the Payment Process and Flexibility - Partial:
           Reason of the point
           Improvement for the point
           Transcript snippet
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

transcript = """
Speaker 0:

Hello.

Speaker 1:

Hello hello.

Speaker 0:

Hi, I am Nancy from Unicolers. Am I speaking with यशवंत?

Speaker 1:

Yes ma'am, yes.

Speaker 0:

Great. Is this a good time to talk regarding your study abroad plans?

Speaker 1:

Yes ma'am.

Speaker 0:

I believe you're interested in studying abroad? Are you looking at Yes. Universities in the USA for January 20 25?

Speaker 1:

Yes ma'am.

Speaker 0:

Have you started your application process?

Speaker 1:

No no, just like after few days I will apply for during English test. Then later on I will apply for colleges.

Speaker 0:

No worries, our expert counselor can help you with all the details based on your preference. Let me connect you with a senior counselor to help plan your study abroad. What time works best for you?

Speaker 1:

Ma'am? I couldn't get that, can you repeat this?

Speaker 0:

Could you please specify a date and time that works for you?

Speaker 1:

Yeah, even tomorrow is fine ma'am.

Speaker 0:

Great. I have you scheduled for a counseling session tomorrow.

Speaker 1:

Yeah, ok ma'am. Thank you

Speaker 0:

for your time यशवंत. I look forward to helping you with your academic journey. Have a great day.

Speaker 1:

Thank you, thank you.

Speaker 0:

Have a great day.
"""

prompt = f"""
# Task:
1. Analyze the agent's performance based on the provided script, using the given result format.
2. Extract the following details:
    a. Lead ID
    b. Lead Name
    c. LQT Name
    d. Passport Status
    e. Course
    f. Country
    g. Intake
    h. Academic Scores/CGPA
    i. Work Experience
    j. Customer Budget
    k. Self-funding or Loan
    l. Counselling Scheduled Status
    m. Competitive Exams Status
    n. Script Follow Score
    o. Sales Pitch Score
    q. Lead Status
$Segments for Script follow$
<Segment 1: Introduction and Verification>
            Script:
            Greeting and verifying the callee's identity.
            Introduction of the caller and purpose of the call.
            Analysis:
            The agent greeted and verified the student's identity.
            The agent introduced themselves and the organisation clearly.
<Segment 2: Inquiry Confirmation>
            Script:
            Confirming the details of the inquiry (study abroad in Ireland for a master's program).
            Verifying the specific course and intended intake period.
            Analysis:
            The agent accurately confirmed the inquiry details.
            The intended intake period was clearly discussed.
<Segment 3: Academic Background and Qualifications>
            Script:
            Asking about the student's bachelor's degree and current status.
            Confirming previous academic performance (tenth and twelfth grades).
            Analysis:
            The agent gathered relevant academic information accurately.
            The agent ensured no gaps or backlogs in the student's academic history.
<Segment 4: Budget and Financial Planning>
            Script:
            Providing an overview of the course cost and living expenses in Ireland.
            Discussing funding options (self-funding or loan).
            Analysis:
            The agent provided clear information about costs.
            The agent confirmed the student's financial planning approach.
<Segment 5: Scheduling Counseling Session>
            Script:
            Offering a counselling session with a relevant expert.
            Discussing available time slots and confirming the preferred time for the session.
            Analysis:
            The agent offered appropriate time slots.
            The preferred time slot was confirmed, though there was a slight mismatch with the student's availability.
<Segment 6: Document Verification>
            Script:
            Requesting academic documents for verification.
            Explaining the purpose of document verification.
            Analysis:
            The agent requested the necessary documents.
            The purpose of document verification was explained.
<Segment 7: Final Confirmation and Closing>
            Script:
            Confirming the booking of the counselling session.
            Providing final instructions and closing the call.
            Analysis:
            The counselling session booking was confirmed.
            The agent provided clear closing instructions and ended the call politely.
<Optional Segment 1: Scholarship and Financial Aid Information>
            Script:
            Informing the student about available scholarships and financial aid options.
            Discussing the application process for scholarships and deadlines.
            Analysis:
            Did the agent provide information about scholarships and financial aid?
            Was the application process for scholarships clearly explained?
<Optional Segment 2: Additional Services and Support>
            Script:
            Explaining additional services provided by the organisation (e.g., visa assistance, pre-departure orientation).
            Offering support with any other concerns the student might have.
            Analysis:
            Did the agent explain additional services that could benefit the student?
            Was the student encouraged to ask questions about other areas of concern?
<Overall Recommendations:>
            Ensure clarity and engagement throughout the call.
            Provide summaries of key points to confirm understanding.
            Show empathy and flexibility to accommodate the student's schedule.
            Follow up promptly and politely to ensure document submission.
            Offer additional information on scholarships and extra services proactively.
$Segments for Sales Pitch$
        <Segment 1: Identification and Addressing by Name>
            Script:
            Greeting: "Hello, am I speaking with [Customer's Name]?"
            Introduction: "Hi [Customer's Name], this is [Agent's Name] from [Organization Name]."
        <Segment 2: Reference to Previous Communication>
            Script:
            Reference to Inquiry: "We received your inquiry about studying abroad for [Program Name] in [Country Name]."
            Previous Contact Confirmation: "I believe you reached out to us on [Date of Previous Communication]."
        <Segment 3: Confirmation of Interest>
            Script:
            Interest Confirmation: "I wanted to confirm that you are still interested in pursuing your [Degree Program] in [Country Name] starting in [Intake Period]."
            Clarification: "Is that correct?"
        <Segment 4: Addressing Concerns and Reassurances>
            Script:
            Acknowledge Concerns: "I understand you might have some concerns about the process."
            Provide Reassurances: "We are here to guide you through every step, from university selection to visa applications."
        <Segment 5: Highlighting Benefits and Facilities>
            Script:
            Benefits: "Our program offers personalized counseling, university selection, and profile building to ensure you get the best possible opportunities."
            Facilities: "We also provide support for SOP, LORs, and resume building."
        <Segment 6: Urgency and Scarcity>
            Script:
            Urgency: "It's important to apply early as the application deadlines are approaching."
            Scarcity: "Early applications also increase your chances of securing scholarships and financial aid."
        <Segment 7: Financial Incentives and Offers>
            Script:
            Incentives: "We have several scholarships and financial aid options available that you might be eligible for."
            Special Offers: "Additionally, we offer a discount on our counseling services if you sign up before [Deadline Date]."
        <Segment 8: Explaining the Payment Process and Flexibility>
            Script:
            Payment Overview: "The total cost for your program is approximately [Amount], which includes tuition and living expenses."
            Flexibility: "You can opt for self-funding or apply for an education loan. We also provide guidance on securing loans."
        <Segment 9: Encouragement to Commit>
            Script:
            Encouragement: "We highly recommend booking a counseling session to discuss your options in detail and take the next steps."
            Commitment Request: "Would you like to schedule a session now?"
        <Segment 10: Openness to Further Discussion>
            Script:
            Invitation for Questions: "Do you have any other questions or concerns that I can help address?"
            Open Communication: "Feel free to reach out to us anytime. We are here to assist you throughout the process."

Conversation Transcript:
{transcript}

{result_format}
"""

client = Together(api_key=os.getenv('TOGETHER_API_KEY'))

response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
    messages=[
        {
            "role": "user",
            "content": prompt #Hi
        }
    ],
    max_tokens=781,
    temperature=0.1,
    top_p=0.5,
    stream=False
)
# Iterate over the generator to access the streamed content
# print(response.choices[0].message.content)
# for res in response:
#     print("Received response chunk:")
#     print(res)
#     if 'choices' in res and res.choices:
#         print(res.choices[0].message.content)

# Print the content of the first choice if available
if hasattr(response, 'choices') and response.choices:
    print("\nResponse content:")
    print(response.choices[0].message.content)
else:
    print("\nNo choices in response")