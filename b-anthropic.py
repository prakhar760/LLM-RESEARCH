import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

# Initialize the Claude client
client = anthropic.Client()

ai_prompt = """
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

Segments for Script follow
 Segment 1: Introduction and Verification
            Script:
            Greeting and verifying the callee's identity.
            Introduction of the caller and purpose of the call.
            Analysis:
            The agent greeted and verified the student's identity.
            The agent introduced themselves and the organisation clearly.

 Segment 2: Inquiry Confirmation
            Script:
            Confirming the details of the inquiry (study abroad in Ireland for a master's program).
            Verifying the specific course and intended intake period.
            Analysis:
            The agent accurately confirmed the inquiry details.
            The intended intake period was clearly discussed.
 Segment 3: Academic Background and Qualifications
            Script:
            Asking about the student's bachelor's degree and current status.
            Confirming previous academic performance (tenth and twelfth grades).
            Analysis:
            The agent gathered relevant academic information accurately.
            The agent ensured no gaps or backlogs in the student's academic history.
 Segment 4: Budget and Financial Planning
            Script:
            Providing an overview of the course cost and living expenses in Ireland.
            Discussing funding options (self-funding or loan).
            Analysis:
            The agent provided clear information about costs.
            The agent confirmed the student's financial planning approach.
 Segment 5: Scheduling Counseling Session
            Script:
            Offering a counselling session with a relevant expert.
            Discussing available time slots and confirming the preferred time for the session.
            Analysis:
            The agent offered appropriate time slots.
            The preferred time slot was confirmed, though there was a slight mismatch with the student's availability.
 Segment 6: Document Verification
            Script:
            Requesting academic documents for verification.
            Explaining the purpose of document verification.
            Analysis:
            The agent requested the necessary documents.
            The purpose of document verification was explained.
 Segment 7: Final Confirmation and Closing
            Script:
            Confirming the booking of the counselling session.
            Providing final instructions and closing the call.
            Analysis:
            The counselling session booking was confirmed.
            The agent provided clear closing instructions and ended the call politely.
 Optional Segment 1: Scholarship and Financial Aid Information
            Script:
            Informing the student about available scholarships and financial aid options.
            Discussing the application process for scholarships and deadlines.
            Analysis:
            Did the agent provide information about scholarships and financial aid?
            Was the application process for scholarships clearly explained?
 Optional Segment 2: Additional Services and Support
            Script:
            Explaining additional services provided by the organisation (e.g., visa assistance, pre-departure orientation).
            Offering support with any other concerns the student might have.
            Analysis:
            Did the agent explain additional services that could benefit the student?
            Was the student encouraged to ask questions about other areas of concern?
 Overall Recommendations:
            Ensure clarity and engagement throughout the call.
            Provide summaries of key points to confirm understanding.
            Show empathy and flexibility to accommodate the student's schedule.
            Follow up promptly and politely to ensure document submission.
            Offer additional information on scholarships and extra services proactively.

 Segments for Sales Pitch
        Segment 1: Identification and Addressing by Name
            Script:
            Greeting: "Hello, am I speaking with [Customer's Name]?"
            Introduction: "Hi [Customer's Name], this is [Agent's Name] from [Organization Name]."
         Segment 2: Reference to Previous Communication
            Script:
            Reference to Inquiry: "We received your inquiry about studying abroad for [Program Name] in [Country Name]."
            Previous Contact Confirmation: "I believe you reached out to us on [Date of Previous Communication]."
         Segment 3: Confirmation of Interest
            Script:
            Interest Confirmation: "I wanted to confirm that you are still interested in pursuing your [Degree Program] in [Country Name] starting in [Intake Period]."
            Clarification: "Is that correct?"
         Segment 4: Addressing Concerns and Reassurances
            Script:
            Acknowledge Concerns: "I understand you might have some concerns about the process."
            Provide Reassurances: "We are here to guide you through every step, from university selection to visa applications."
         Segment 5: Highlighting Benefits and Facilities
            Script:
            Benefits: "Our program offers personalized counseling, university selection, and profile building to ensure you get the best possible opportunities."
            Facilities: "We also provide support for SOP, LORs, and resume building."
         Segment 6: Urgency and Scarcity
            Script:
            Urgency: "It's important to apply early as the application deadlines are approaching."
            Scarcity: "Early applications also increase your chances of securing scholarships and financial aid."
         Segment 7: Financial Incentives and Offers
            Script:
            Incentives: "We have several scholarships and financial aid options available that you might be eligible for."
            Special Offers: "Additionally, we offer a discount on our counseling services if you sign up before [Deadline Date]."
         Segment 8: Explaining the Payment Process and Flexibility
            Script:
            Payment Overview: "The total cost for your program is approximately [Amount], which includes tuition and living expenses."
            Flexibility: "You can opt for self-funding or apply for an education loan. We also provide guidance on securing loans."
         Segment 9: Encouragement to Commit
            Script:
            Encouragement: "We highly recommend booking a counseling session to discuss your options in detail and take the next steps."
            Commitment Request: "Would you like to schedule a session now?"
         Segment 10: Openness to Further Discussion
            Script:
            Invitation for Questions: "Do you have any other questions or concerns that I can help address?"
            Open Communication: "Feel free to reach out to us anytime. We are here to assist you throughout the process."
              
$Result Format-Example$

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

            Lead ID: %'Example - Venkata'%
            Lead Name: %'Example - Venkata'%
            LQT Name: <Agent Name>
            Passport Status: %'Example - Yes,Confirmed to be from Andhra Pradesh'%
            Course: %'Example - Computer Engineering (B.Tech in Information Technology)'%
            Country: %'Example - USA'%
            Intake: %'Example - January 2025'%
            Script Follow Score : <its overall score>  %'Example - 7/7
            Academic Scores/Cumulative GPA (CGPA): %'Example - 10th: 77%, 12th: 74.872%, Bachelor's: CGPA 7.28'%
            Work Experience: %'Example - None specified (Fresher)'%
            Customer Budget: %'Example - Not specified'%
            Self-funding or Loan: %'Example - Partial self-funding and partial education loan discussed'%
            Counselling Scheduled Status: %'Example - Counseling session booked for tomorrow at 5 PM'%
            Competitive Exams Status: %'Example - Not specified'%```
            Sales Pitch Score : <its overall score>
            Lead Status :  %'Example - qualified'% 
                       
    Final Result : The customer is interested and a call with counsellor is scheduled at what time.      

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

Hello? Hello?

Speaker 1:

Hello. Yeah. Am I talking to Nikhil?

Speaker 0:

Yeah. Who is this?

Speaker 1:

Yeah. Nikhil, I'm Harish here from UniScholars. You have placed an inquiry on our website. Right?

Speaker 0:

Yeah. Yeah. Yeah.

Speaker 1:

Yeah. So you are planning to study in Ireland, right, for your master's program? Yes, sir. Okay. And which course you're exactly looking out for?

Speaker 0:

I was looking for supply chain management and logistics.

Speaker 1:

Okay. And you're planning to go this year for the September intake or, like, for the Jan 25 intake?

Speaker 0:

For the Jan intake. 25.

Speaker 1:

Jan intake. Okay. And you're having a valid passport with you. Right?

Speaker 0:

Yeah. Yeah.

Speaker 1:

Okay. And have you appeared for any English proficiency test as of now?

Speaker 0:

No. No. No. No, sir.

Speaker 1:

Okay. And what about your bachelor's, Nickel? What have you done in your bachelor's?

Speaker 0:

So, currently, I'm doing with the BBA, master's degree. I have completed my exams yesterday itself. I'm waiting for the results.

Speaker 1:

So, basically, I've completed a bachelor's this year only. Right? Yeah. Yeah. Okay.

And how much did you score, like, in the last semester? What was the CGP or percentage?

Speaker 0:

It was about, 76, I guess.

Speaker 1:

76. Okay. And what about your 10th 12th?

Speaker 0:

10th and Tuesday was almost about to 75 and 74.

Speaker 1:

Okay. And I hope, Nikhil, you are not having any sort of gaps or backlogs. Right?

Speaker 0:

No. No. No.

Speaker 1:

Okay. And you have completed all your studies from Karnataka state only?

Speaker 0:

Yeah. Yeah.

Speaker 1:

Okay. So, Nikhil, I'll just tell you the budget as well. So in Ireland, you know, the course that you are planning to pursue, it is going to cost you around 20 lakhs. That will be including your living cost as well.

Speaker 0:

Okay.

Speaker 1:

Okay. So this includes your tuition fee and your, like, accommodation cost also.

Speaker 0:

Okay, sir.

Speaker 1:

Yeah. So I hope the budget is fine for you. Right?

Speaker 0:

Yeah. Yeah.

Speaker 1:

Okay. So, Nikhil, the budget that I have told you, your parents, are they going to self fund this amount or they are planning to take a loan?

Speaker 0:

We are planning to be a self funded loan.

Speaker 1:

Okay. So it is going to be a complete self fund only. Right?

Speaker 0:

Yeah. Yeah.

Speaker 1:

Okay. So, Nikhil, like, I'm almost done with your profile now. So I can, you know, connect you with my counselor as well for the counseling session. So, you know, he'll be guiding you about the university selection and the application process as well. So I just wanted to know that today around what time are you going to be available?

Speaker 0:

I'll be available at, 11:7 to 8 PM.

Speaker 1:

Okay. So, Nikhil, like, actually, you know, we are working from 10 to 6 only. So today in the evening around 5 or 5:30 works for you?

Speaker 0:

Okay. You can call me at the Yeah.

Speaker 1:

So, Nikhil, just one last thing, you know, I'll be needing from your end is any 2 of your academical mark sheets, like your 10, 12, or, you know, like any semester mark sheet from your bachelor's. So can you just send me any 2 of your mark sheets on WhatsApp so that, you know, I can just forward your profile to my counselor?

Speaker 0:

Okay. Okay. Kindly, I'm out now. Later, I'm going to home. I'll send you a text.

Speaker 1:

Okay. So in your phone, you're not having anything as of now?

Speaker 0:

No. No. It is a long time. My password, I don't know.

Speaker 1:

Okay. So you're having a resume or something at least, Nikhil?

Speaker 0:

Yeah. Yeah. I have a resume.

Speaker 1:

Yeah. So you can just send me your resume, and you must be having a picture of your passport or something. Right? Yeah. Okay.

I'll send you. Okay. So I've just dropped you a message, Nikhil, right now. So can you just put me on hold and just send it to me right away so that I can just confirm a slot for you?

Speaker 0:

Wait. Currently, I'm, driving the vehicle.

Speaker 1:

Okay. Send it later. Okay. So I've already dropped you a message, Nikhil. So once you are free, you can just send me any 2 things.

So then I'll just connect you with my counselor today only. Okay?

Speaker 0:

Okay. Bye.

Speaker 1:

Yeah. Thank you.
"""

prompt = f"""
    
   
 Analyze the agent's performance based on the provided script, using the given result format.


    ***here are the tasks - {ai_prompt}
    


    
    Transcript: ```{transcript}``` - (analyse this transcript on the basis of above prompt also give extraction part accurately from transcript)

"""

def get_claude_completion(prompt, model="claude-v1", max_tokens=300, temperature=0):
    response = client.messages.create(
        # prompt=prompt,
        model=model,
        max_tokens=max_tokens,
        stop_sequences=["\n\n"],
        temperature=temperature,
        messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "You are agent analyzer who analyses agent performace."
                        }
                    ]
                }
            ]
    )
    
    # Extract relevant data from the response
    completion = response["completion"]
    prompt_tokens = response["prompt_tokens"]
    completion_tokens = response["completion_tokens"]
    total_tokens = prompt_tokens + completion_tokens

    print("Input token count: ", prompt_tokens)
    print("Response token count: ", completion_tokens)
    print("Total tokens: ", total_tokens)
    return completion.strip()

# Get 1 haiku
haiku = get_claude_completion(prompt)
print("Claude:")
print(haiku)