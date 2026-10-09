import os
import json
import argparse
from call_function import available_functions
from prompts import system_prompt
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key == None:
    raise RuntimeError("Runtime Error, please check your API key!")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [
    {"role": "user", "content": system_prompt},
    {"role": "user", "content": args.user_prompt}
]

response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages,
    temperature=0,
    tools=available_functions
)

message = response.choices[0].message

def main():
    print("Hello from python-ai-agent, here's your answer:")
    print("-----------------------------------------------")
    for tool_call in message.tool_calls:
        function_args = json.loads(tool_call.function.arguments or "{}")
        print(f"Calling function: {tool_call.function.name}({function_args})")
    
    if response.usage == None:
        raise RuntimeError("Failed API request, please try again later!")
    elif args.verbose == True:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
        print(f"Response:\n{response.choices[0].message.content}")
    elif args.verbose == False:
        print(f"Response:\n{response.choices[0].message.content}")

if __name__ == "__main__":
    main()
