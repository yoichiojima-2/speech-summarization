import argparse
import whisper


def main(input_path: str) -> str:
    model = whisper.load_model("base")
    res = model.transcribe(input_path)
    return res["text"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-path")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(input_path=args.input_path)
