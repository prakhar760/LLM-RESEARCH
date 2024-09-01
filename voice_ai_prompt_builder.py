import openai
def load_original_prompt(file_path):
    with open(file_path, 'r') as file:
        original_prompt = file.read().strip()
    return original_prompt
def get_user_input(prompt):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    return "\n".join(lines)
def generate_prompt(context, nodes, original_prompt):
    system_message = f"""
You are an AI assistant tasked with creating a conversation flow for a student outreach program.
Take reference from given prompt:
{original_prompt}
Use the following context and conversation states to generate a detailed prompt:
Context:
{context}
Conversation States:
{nodes}
Your task is to create a prompt that guides an AI model to effectively conduct this outreach conversation.
Include specific instructions on tone, language use, and how to handle various scenarios.
"""
    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": "Generate a detailed prompt based on the given context and conversation states."}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error in generating prompt: {str(e)}"
def main():
    original_prompt = load_original_prompt('original_prompt.txt')
    print("Enter the context (press Enter twice to finish):")
    context = get_user_input("")
    print("\nEnter the conversation states/flow (press Enter twice to finish):")
    nodes = get_user_input("")
    # Set your OpenAI API key here
    openai.api_key = 'your-openai-api-key'
    prompt = generate_prompt(context, nodes, original_prompt)
    print("\nGenerated Prompt:")
    print(prompt)
if __name__ == "__main__":
    main()
