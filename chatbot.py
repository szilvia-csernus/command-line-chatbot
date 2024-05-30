import openai
from dotenv import dotenv_values
import argparse

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]


def main():
  parser = argparse.ArgumentParser(description="Chat with the AI")

  parser.add_argument("--personality", type=str, default="friendly and helpful", help="The personality of the AI")
  args = parser.parse_args()

  messages = [
    {
      "role": "system",
      "content": f"You are a conversational chatbot. Your personality is {args.personality}."
    }
  ]
  
  while True:
    try:
      user_input = input("You: ")
      messages.append({
        "role": "user",
        "content": user_input
      })
      response = openai.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=messages,
          max_tokens=50
      )
      print("AI: ", response.choices[0].message.content)

    except KeyboardInterrupt:
      print("Exiting...")
      break

if __name__ == "__main__":
  main()