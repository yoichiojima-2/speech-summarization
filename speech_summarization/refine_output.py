import os
from argparse import ArgumentParser
from pathlib import Path

from openai import OpenAI


def refine_outputs(input_dir: str):
    for f in Path(input_dir).rglob("*"):
        if f.is_file():
            refine_output(f)


def refine_output(input_path: str):
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    input_path = Path(input_path)
    input_text = input_path.read_text()

    prompt = (
        "You will be provided with a document processed from audio recordings. This document comes from converting spoken content into text, "
        "segmenting this content, summarizing those segments, and merging them into a single file. Given the process, you may notice inconsistencies in formatting, "
        "style, and clarity. Your task is to make a markdown format text by refining this document with a focus on detail and comprehensiveness. "
        "Start by reading the document to understand the overall themes, messages, and key information. "
        "Ensure each section is summarized with ample detail, particularly focusing on areas that connect different sections and "
        "the overarching narrative. When cleaning the text, besides correcting errors and standardizing terminology, ensure the style and tone are consistent throughout the document. "
        "Enhance clarity and coherence not just by reordering for logical progression but by elaborating on complex points to make them more accessible. "
        "Finally, while summarizing, aim for a detailed yet integrated narrative that captures the essence and specifics of the original content, "
        "avoiding overly concise summaries that may omit crucial information. The summary should reflect the depth of the original audio recordings, "
        "making it accessible and informative for the reader. Note that the output should be in Japanese, focusing on clarity and detail without the need for polite language."
    )

    response = (
        client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt},
                {"role": "user", "content": input_text},
            ],
            model="gpt-4-0125-preview",
        )
        .choices[0]
        .message.content
    )

    print(f"response: {response}")

    target_dir = Path("./data/refine_output")
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / input_path.name).write_text(response)


def parse_args() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("--target", "-t", type=str)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    refine_outputs(args.target)
