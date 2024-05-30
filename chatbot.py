import openai
from dotenv import dotenv_values
import argparse

config = dotenv_values(".env")

if "OPENAI_API_KEY" not in config:
  raise ValueError("OPENAI_API_KEY is missing from the .env file, please provide one.")
openai.api_key = config["OPENAI_API_KEY"]


def bold(text):
  return f'\033[1m{text}\033[0m'

def blue(text):
  return f'\033[94m{text}\033[0m'

def green(text):
  return f'\033[92m{text}\033[0m'


def main():

  print("\n", bold("Chat with the AI chatbot!") + "\n")

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
      user_input = input(bold(blue("You: ")))
      messages.append({
        "role": "user",
        "content": user_input
      })
      response = openai.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=messages,
          max_tokens=50
      )
      print("\n", bold(green("AI: ")), response.choices[0].message.content, "\n")

    except KeyboardInterrupt:
      print("Exiting...")
      break

if __name__ == "__main__":
  main()