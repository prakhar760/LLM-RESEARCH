import os
from dotenv import load_dotenv
# from langchain_community.llms import Ollama
from crewai import Agent, Task, Crew, Process

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
groq_api_key = os.getenv('GROQ_API_KEY')

os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["OPENAI_MODEL_NAME"] = 'mixtral-8x7b-32768'#'mixtral-8x7b-32768' #'llama-3.1-70b-versatile'#'llama3.1-405b-8192'#'llama-3.1-70b-versatile'#'llama3-70b-8192'# 'gemma-7b-it'#'llama3-8b-8192'#'llama3-70b-8192'#'gpt-3.5-turbo'#'llama3-groq-70b-8192-tool-use-preview' # Adjust based on available model
os.environ["OPENAI_API_KEY"] =  groq_api_key # openai_api_key

# model = Ollama(model = "llama3")

call_to_be_analyzed = """
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

analyzer = Agent(
    role = "call analysis agent",
    goal = "You are evaluating the performance of a voice AI agent in a customer service context for an educational consultancy specializing in study abroad programs. Your task is to identify any defects, irregularities, or shortcomings in the AI's responses and behaviour during the call.",
    backstory = "You will be provided a transcript of conversation between agent and customer where you have to evaluate the defects or irregularities of agent.",
    verbose = True,
    allow_delegation = False
)

analyze_agent = Task(
    description = f"""
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
{call_to_be_analyzed}
""",
    agent = analyzer,
    expected_output = """
"""
)

crew = Crew(
    agents = [analyzer],
    tasks = [analyze_agent],
    verbose = 2,
    process = Process.sequential
)

output = crew.kickoff()
print(output)