import os
import argparse
from pathlib import Path
import openai
from openai import OpenAI


def main(input_path: str):
    input_path = Path(input_path)
    input_text = input_path.read_text()
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    response = client.chat.completions.create(
        messages = [
            {"role": "user", "content": "summarize this text"},
            {"role": "user", "content": input_text},
        ],
        model = "gpt-4"
    )
    return response.choices[0].message.content

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-path")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    print(main(input_path = args.input_path))
    
