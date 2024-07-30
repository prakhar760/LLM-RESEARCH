import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("FIREWORKSAI_API_KEY")

transcript = """
Speaker 0:

Hello, missus. Hello?

Speaker 1:

Hello. Am I speaking to Nikita?

Speaker 0:

Yes.

Speaker 1:

Hey, Nikita. This is for your accommodation at Botanix Studios. I'm calling you from uniaco.com. Yes. Because, actually, I believe you have already made a rent payment, but the account is different.

Actually, that's for Uniaco's account, which you have already paid the rent for. And we have gotten a message that, amount of 1 lakh 70,000 has already been debited.

Speaker 0:

Yeah. Actually, I emailed about the same to the accommodation as well because I I could not recognize that card, but I I I don't know why I just went with it. I kind of don't remember whether I have added a card or not, and it gave me a confirmed, payment notification, but none of my cards have been debited any amount?

Speaker 1:

Yes. Because that was an auto debit setup there, actually. And you clicked on continue. That is the reason the rent got deducted from our account. So, actually, we got an email from the property that why are you paying the rent.

So that is the reason I got in touch with you. So what I can do is, I already have an alternate solution for that. I'll make a payment link for you for the same amount. Mhmm. You can just make the payment to us directly.

So your payment has already gone there. That is fine. We can confirm with the property from the back end as well. You can just pay the amount right now to us so that we can clear the accounts from Arun.

Speaker 0:

I mean, are you sure, can you not take refund on your account and I can make payment from my card?

Speaker 1:

That can't be because I'll tell you as it's already made by the card payment, and they already have their account set up because they have their instant installment plan already. Right? So in Okay. Your end installment plan, it's showing as approved. The payment is in process.

So we cannot take the refund from the k from the property's end, but what we can do is we can generate another link for you, and you can make the payment over here.

Speaker 0:

So I'll be making payment to the Uniaco. Is it like that?

Speaker 1:

Can you repeat that?

Speaker 0:

So I I will be making the payment to the Uniaco.

Speaker 1:

Yes. And, also, we'll give the confirmation for the same. The reason I'll tell you, if you, get a refund for the same from that, it might be the case that you're not paying the rent, and due to that, the booking can be canceled. That is the reason. Because there's a default in the rent payment if you're taking the refund again.

Speaker 0:

Okay. Okay. So is it possible that if I hear back from the general manager of the property first, then I can make the payment?

Speaker 1:

No. We actually have our IR team already involved in the same, and they have said that this cannot be done because immediately I'm so sorry to call you this time, as I know you are in India itself, but IR team is also involved with us, international relations team, and she said that this one has to make the payment directly to you, because of

Speaker 0:

the Uh-huh. Actually, the thing is that I I really want to trust this arrangement that we are having. And I, know that I have clicked on a, you know, card that does not belong to me, and I made the payment. Yes. But, I don't know if I make the payment to you.

Will I be getting the confirmation from future, they would say, okay. We did not receive any of your payment.

Speaker 1:

Don't worry about that. Lumunia.

Speaker 0:

So is it something like that?

Speaker 1:

No. Don't worry about that. I've already had a word regarding your accommodation also. Right? And, also, we are in touch with you constantly the time when you make the payment.

I'll also give you the confirmation that your end installment is paid as you've already gotten the details over there. And Mhmm. Regarding your end installment, which you make it to us, is definitely we'll get the confirmation also. I'll give you both of the confirmation.

Speaker 0:

Okay. Okay. So, actually, I have received one payment confirmation from Botanic Studios. So Okay. I will be getting a further confirmation from Uniaco as well?

Speaker 1:

Yes. You'll be getting the further confirmation from Uniaco also. Don't worry about that. Okay. And I am assuring you by tomorrow, it says you'll get the confirmation of your end payment because it takes 24 hours only to process your, advance end payment which you have made.

So as you make the payment to us right now, I'll also confirm tomorrow that you have made the payment to Uniaco. And also from Botanic, I'll give you confirmation. Your end installment is cleared, the 1st time installment which you made.

Speaker 0:

Okay. Okay. That's fine.

Speaker 1:

So what I can do is Yeah. I can just make another link for you right now of the same amount which you have paid, and you can just pay them.

Speaker 0:

Okay. Okay. Perfect. Please send me the link via can you email me so I can make the payment?

Speaker 1:

Fair enough. Fair enough. I can also email you for the same, and I believe I've already WhatsApp you as well regarding the accommodations.

Speaker 0:

Mhmm. Okay. I I may not have checked that.

Speaker 1:

Remember. You will remember. Can you just yes. Akshay from Union

Speaker 0:

and Co. Nikita. Yes. Yes. I do remember you.

That's what it is. I do remember you.

Speaker 1:

Yes. Yes. So I can just send you another link. Just give me one minute. I'm just making the link now.

Mhmm. Just sending you a survey.

Speaker 0:

Okay.

Speaker 1:

Really sorry for the trouble, actually, but, you know, we were thinking about

Speaker 0:

the case. I'm glad that you reached out, actually. You know, I I was being very, nervous, you know, from where the payment have went. I've been constantly checking my cards, my statement. None of them have had that debit, so I was confused already, sir.

It's nice that you called. Yeah.

Speaker 1:

Just give me one minute. I'm just sending you the link now.

Speaker 0:

Mhmm. Okay.

Speaker 1:

Yes, Nikita. I've sent you the link on WhatsApp. If you can just access

Speaker 0:

that I can see that. Do you mind, Akshat, if I ask for a favor? Yes, ma'am. Can you just, put the same link on an email to me and write the same thing that you are saying right now that, you know, that Uniaco has accidentally made the payment. So, Nikita, you're required to make another payment.

Speaker 1:

No problem. That is fine. I will do that for you now.

Speaker 0:

Yeah. So, you know, just so that, you know, in future, I don't want to be in any kind of trouble. That's all. Nothing personal. Yeah.

Speaker 1:

Yes. No problem. I will I'm just drafting an email right now. I'll send it to you.

Speaker 0:

Mhmm. Okay. Okay. Perfect. Then after

Speaker 1:

I have you be on the call? That's fine?

Speaker 0:

Yeah. That's that's not a problem. I can Okay.

Speaker 1:

Just give me one minute. Mhmm.

Speaker 0:

After making the payment, I'll also remove the card that, you have You've put

Speaker 1:

in on my profile right now. You don't worry about that. I'll be doing the needful. Tomorrow itself, I'll be just deleting the card also, and I'll give you the informations. That's fine?

Okay.

Speaker 0:

Perfect. Yeah.

Speaker 1:

Perfect. In that case, no problem. I've just drafted an email for the same, and I'm just sending it to you. Okay. Yes.

I've sent you, the email on nikita.nk Mhmm. 2812@gmail.com. Can you check that?

Speaker 0:

Hold on a second. Yeah. I got it from. Okay.

Speaker 1:

Yes.

Speaker 0:

Okay. I will see the payment link. Now I'll make the payment.

Speaker 1:

Yes, please. Mhmm.

Speaker 0:

I had made the just a second. I had made the payment I have to make the payment of 1642, but the link that you sent is asking me another platform fee and another thing. So it's 1697 pound it's asking me.

Speaker 1:

Just a minute. I'll check that. I'll check that for you.

Speaker 0:

Mhmm. Yeah.

Speaker 1:

It's 16 so that's 1642. Another is the gateway charge. Gateway charges, I believe, are already included because you're making the payment. So that is why.

Speaker 0:

No. I mean, £1642, I'm supposed to deposit. See, in the app, if I would have, paid via my card, I will not be paying the gateway fee. No. No.

Speaker 1:

So in this case, what happens is even if you make the rent payment by your card, your bank would have been charged the same.

Speaker 0:

A data we see? I mean, I do know that the forex conversion is something that they charge extra, but it's mentioned another £55.

Speaker 1:

That's the gateway we actually I'm not

Speaker 0:

do do are you understanding what I'm trying to say?

Speaker 1:

Yes. Yes. So I'll tell you one thing. Even if you were gonna pay from your card directly over there, your bank would have charged the same. And this is not our charges.

This is the Stripe charge which you're making the payment for. Those are the Stripe charges which you are taking. We aren't taking anything from you. It's just the relevant

Speaker 0:

No. No. No. I I at least, let's say, a pound is 102 or whatever it is. But even if I'll pay via card or something, it will charge me around 107 a pound or something like that.

Right? So, this 1642 pound will already be converted by my card on an extra rate, and then you are charging another £55 for a gateway fee. And No. No. My bank does not do that.

Speaker 1:

So so, eventually, I'll tell you one thing, Every bank does that. Even if there's a transaction of more than one lakh, it does that because international payments actually has some charges. So domestic domestic transactions are okay, but international payment, even if you make No.

Speaker 0:

I get that. Actually, I I make a lot of international transaction US based, so I do know about that. You know, transferring money is never the same. The rate that's mentioned online is not what they transfer on. They charge extra already.

But, you know, with if I would have, proceeded with my card, I don't think it would have charged me another £55. See, the thing is, actually, the payment confirmation that I've got is for 16 42, then I'll not be paying 1697.

Speaker 1:

So okay. No problem. We have an alternate solution for that.

Speaker 0:

Or something like that, then I would be very happy to proceed with it. Or maybe you can take the refund from the fresh, and then I can make my payment.

Speaker 1:

So we have another option for you as you are already in Indian, and we do have some, facility for the Indian students to pay via bank. So you can make a bank transfer also, if that's okay.

Speaker 0:

Okay.

Speaker 1:

So there's no charges then.

Speaker 0:

Okay. So can I make nothing else? Can you share send me the details? See, nothing personal, but I just want you to know that, you know, that £55 is a bit extra on my end because, yeah, I do know that every pound is charged extra already, and I will transfer it from here to there. But, I don't believe that my card would have charged me another gateway fee.

So if you can send me your uni, I suppose, bank detail, I'd be happy to transfer it over there as well.

Speaker 1:

No problem. So shall I send it to you on what on email itself?

Speaker 0:

No. No. On the email only, please reply. I'll, just try to log in to my Internet banking, and we'll send you as soon as possible.

Speaker 1:

Okay. No problem, Nikita. I am just dropping you a email right now with the details of the bank account. I have sent it to you. If you can just check if you received that.

Speaker 0:

Mhmm. I one second. Yeah. I have got the okay. I've got the beneficiary code.

Okay.

Speaker 1:

I'll tell you the amount as well. Amount as well. It's 179132.76. Okay. So if you're in the 9133.

Round

Speaker 0:

2 again. 7?

Speaker 1:

9133.

Speaker 0:

9136. Okay. Divided for 179133 is a payment that I'm supposed to make to

Speaker 1:

you. Yes.

Speaker 0:

Okay. Okay.

Speaker 1:

In the narration list, sir, we could just mention your name, Botanic Studios. Yes. Yes. Yes. So, I could just hang up the call now.

You can make the payment, and then I can get on the call with you.

Speaker 0:

Yeah.

Speaker 1:

But yeah. Thank you. I I believe you can just understand because it's international team is also involved. If you can just make the payment today, I'm I know, it's a bit late.

Speaker 0:

I'm done. But, actually, I'll just hang up the call. I'll open my ICICI app, and I'll make the payment.

Speaker 1:

Okay. No problem. No problem. Perfect. Thank you so much for the cooperation

Speaker 0:

here. Yeah. Yeah. Okay.
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
# Task
1. Analyze the agent based on the provided script.
2. Extract the following information:
    a. Lead ID
    b. Lead Name
    c. Agent Name
    d. Accommodation Preference
    e. Country
    f. University
    g. Intake
    h. Budget
    i. Self-funding or Loan
    j. Move-in Date
    k. Script Follow Score
    l. Sales Pitch Score
    m. Accomodation booking status
$Segments for Script follow$
<Segment 1: Introduction and Verification>
        Script:
        Greeting and verifying the callee's identity.
        Introduction of the caller and purpose of the call.
        Analysis:
        Did the agent greet and verify the student's identity?
        Did the agent introduce themselves and the organization clearly?
<Segment 2: Inquiry Confirmation>
        Script:
        Confirming the details of the inquiry (accommodation near the university).
        Verifying the specific university and intended move-in date.
        Analysis:
        Did the agent accurately confirm the inquiry details?
        Was the intended move-in date clearly discussed?
<Segment 3: Accommodation Preferences>
        Script:
        Asking about the student's accommodation preferences (room type, facilities, etc.).
        Confirming the budget and financial planning.
        Analysis:
        Did the agent gather relevant accommodation information accurately?
        Did the agent confirm the student's budget and financial planning?
<Segment 4: Budget and funding>
        Script:
        Providing an overview of the accommodation costs and additional expenses.
        Asking about the funding method(self-funding or loan).
        Analysis:
        Did the agent provide clear information about costs?
        Did the agent ask about the funding method for the accomodation?
<Segment 5: Accomodation recommendation list>
        Script:
        Recommending accomodation checklist to the customer according to their preference.
        Analysis:
        Did the agent recommend preferred accomodation checklist?
<Segment 6: Final Confirmation and Closing>
        Script:
        Confirming the booking of accomodation.
        Providing final instructions and closing the call.
        Analysis:
        Was the accomodation booking confirmed?
        Did the agent provide clear closing instructions and end the call politely?
<Optional Segment 1: Discounts and offers>
        Script:
        Informing the student about available discounts and offers for accommodation.
        Analysis:
        Did the agent provide information about available discounts and offers?
<Optional Segment 2: Additional Services and Support>
        Script:
        Explaining additional services provided by the organization (e.g., moving assistance, roommate matching).
        Offering support with any other concerns the student might have.
        Analysis:
        Did the agent explain additional services that could benefit the student?
        Was the student encouraged to ask questions about other areas of concern?
<Optional Segment 3: Application status confirmatiom>
        Script:
        Requesting the application status of the customer.
        Analysis:
        Did the agent application status of the customer?
<Overall Recommendations>
        Ensure clarity and engagement throughout the call.
        Provide summaries of key points to confirm understanding.
        Show empathy and flexibility to accommodate the student's schedule.
        Follow up promptly and politely to ensure application status.
        Offer additional information on offers and extra services proactively.

$Segments for Sales Pitch$
<Segment 1: Identification and Addressing by Name
      Script:
      Greeting: "Hello, am I speaking with [Customer's Name]?"
      Introduction: "Hi [Customer's Name], this is [Agent's Name] from UniAcco."
<Segment 2: Reference to Previous Enquiry
      Script:
      Reference to Inquiry: "We received your inquiry about accommodation near [University Name] in [Country Name]."
      Previous Contact Confirmation: "I believe you checked for accomodations on our website on [Date of Website Enquiry]."
<Segment 3: Confirmation of Interest
      Script:
      Interest Confirmation: "I wanted to confirm that you are still interested in securing accommodation near [University Name] starting from [Move-in Date]."
      Clarification: "Is that correct?"
<Segment 4: Addressing Concerns and Reassurances
      Script:
      Acknowledge Concerns: "I understand you might have some concerns about the process."
      Provide Reassurances: "We are here to guide you through every step, from room selection to move-in assistance."
<Segment 5: Highlighting Facilities
      Script:
      Benefits: "Our services include personalized accommodation matching, room tours, and assistance with lease agreements."
      Facilities: "These accomodations provide support for facilities like Wi-Fi, laundry, and gym access."
<Segment 6: Urgency and Scarcity
      Script:
      Urgency: "It's important to book early as the best rooms get occupied quickly."
      Scarcity: "Early bookings also give you more options to choose from."
<Segment 7: Financial Incentives and Offers
      Script:
      Incentives: "We have several offers and discounts available for bookings."
<Segment 8: Explaining the Payment Process and Flexibility
      Script:
      Payment Overview: "The total cost for your accommodation is approximately [Amount], which includes rent and utilities."
      Flexibility: "You can opt for self-funding or apply for an accommodation loan. We also provide guidance on securing loans."
<Segment 9: Encouragement to Commit
      Script:
      Encouragement: "We highly recommend going through all the accomodation options we recommended to discuss your options in detail and take the next steps."
<Segment 10: Openness to Further Discussion
      Script:
      Invitation for Questions: "Do you have any other questions or concerns that I can help address?"
      Open Communication: "Feel free to reach out to us anytime. We are here to assist you throughout the process."

Conversation Transcript:
{transcript}

{result_format}
"""

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
