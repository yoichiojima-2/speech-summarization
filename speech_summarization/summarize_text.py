import os
from pathlib import Path

from openai import OpenAI


def summarize_texts(input_dir: str):
    for f in Path(input_dir).rglob("*"):
        if f.is_file():
            summarize_text(f)


def summarize_text(input_path: str):
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    input_path = Path(input_path)
    input_text = input_path.read_text()
    print(f"input_text:  {input_text}")

    response = (
        client.chat.completions.create(
            messages=[
                {"role": "user", "content": "summarize this text in Japanese."},
                {"role": "user", "content": input_text},
            ],
            model="gpt-4",
        )
        .choices[0]
        .message.content
    )

    print(f"response: {response}")

    target_dir = Path("./data/summarize_text") / input_path.parts[-2]
    target_dir.mkdir(parents=True, exist_ok=True)
    output_filename = input_path.name.replace("split", "summarize")
    (target_dir / output_filename).write_text(response)
