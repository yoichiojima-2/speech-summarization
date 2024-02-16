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

    prompt = (
        "Summarize the text tailored for processing multiple Japanese transcripts. "
        "These transcripts have been converted from speech to text using Whisper, and subsequently enhanced "
        "for clarity and punctuation using GPT-4, ensuring high-quality input. Each transcript represents "
        "a segment of a broader narrative or discussion and requires individual summarization. The model should: "
        "1. Summarize each transcript accurately, focusing on capturing the core ideas and essential information. "
        "2. Merge these individual summaries into a coherent, consolidated summary that encapsulates the overarching "
        "themes, conclusions, and insights from all transcripts. "
        "3. Acknowledge and adapt to the nuances of the Japanese language and the improvements made by Whisper and GPT-4. "
        "This includes understanding the context, the conversation flow, and the significance of cultural or idiomatic "
        "expressions. "
        "4. Given the segmented nature of the transcripts, ensure the final merged summary integrates content from each "
        "segment smoothly, providing a comprehensive overview of the entire discussion or narrative. "
        "Consider the benefit of intermediate steps for review or adjustment between summarizing individual transcripts "
        "and creating the final merged summary to enhance overall accuracy and cohesion."
        "Make sure the model is written in Japanese"
        "Do not include the prompt above in the response."
    )

    response = (
        client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt},
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
    output_filename = input_path.name.replace("cleansed", "summarized")
    (target_dir / output_filename).write_text(response)
