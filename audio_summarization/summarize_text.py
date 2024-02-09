import os
import argparse
from pathlib import Path
from openai import OpenAI


def main(input_path: str):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    input_path = Path(input_path)
    input_text = input_path.read_text()

    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": "summarize this text"},
            {"role": "user", "content": input_text},
        ],
        model="gpt-4",
    ).choices[0].message.content

    print(f"response: {response}")

    target_dir = Path("./data/summarize_text")
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "test.txt").write_text(response)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-path")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(input_path=args.input_path)
