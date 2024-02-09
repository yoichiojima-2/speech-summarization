from pathlib import Path
import argparse
import whisper


def main(input_path: str) -> str:
    model = whisper.load_model("large-v2")
    res = model.transcribe(input_path, language = "ja")

    output_dir = Path("./data/audio2text")
    output_dir.mkdir(parents = True, exist_ok = True)
    (output_dir / "test.txt").write_text(res["text"])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-path")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(input_path=args.input_path)
