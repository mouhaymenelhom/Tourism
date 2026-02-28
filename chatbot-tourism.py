import openai
from openai import OpenAI

# 1. Initialize the client to point to Groq instead of OpenAI
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    #api_key
    # Note: remove the # from the above line and add your actual Groq API key to authenticate
)

# 2. Function to interact with the model
def get_response(user_input):
    try:
        # Restrict the model to only talk about tourism in Tunisia
        system_prompt = (
            "You are a helpful assistant that ONLY provides advice, tips, "
            "and information about tourism in Tunisia. "
            "Do not talk about anything else. "
            "If the user asks unrelated questions, politely respond that you only talk about tourism in Tunisia."
        )

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            max_tokens=300,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Groq Error: {e}"

# 3. Chat loop
def chat():
    print("Hello! I'm your Groq-powered Tunisia tourism bot. Ask me anything about traveling in Tunisia!")
    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ["quit", "exit"]:
                print("Bot: Goodbye!")
                break

            bot_response = get_response(user_input)
            print(f"Bot: {bot_response}")

        except KeyboardInterrupt:
            print("\nBot: Goodbye!")
            break
        except Exception as e:
            print(f"Bot: Oops! {e}")

if __name__ == "__main__":
    chat()