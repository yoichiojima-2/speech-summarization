import argparse
import math
from pathlib import Path


def main(input_path: str, max_chunk_size: int):
    text = Path(input_path).read_text()

    chunk_num = math.ceil(len(text) / max_chunk_size)

    output_dir = Path("./data/split_text")
    if output_dir.exists():
        for item in output_dir.iterdir():
            item.unlink()

    output_dir.mkdir(parents=True, exist_ok=True)

    for i in range(chunk_num):
        chunk_path = output_dir / f"chunk_{i + 1}.txt"
        chunk_path.write_text(text[i * max_chunk_size: (i + 1) * max_chunk_size])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-path", type=str, required=True)
    parser.add_argument("--max-chunk-size", type=int, required=True)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(input_path=args.input_path, max_chunk_size=args.max_chunk_size)
