import math
from pathlib import Path


def split_text(input_path: str, max_chunk_size: int):
    text = Path(input_path).read_text()

    chunk_num = math.ceil(len(text) / max_chunk_size)

    output_dir = Path(f"./data/split_text/{Path(input_path).stem}")
    if output_dir.exists():
        for item in output_dir.iterdir():
            item.unlink()

    output_dir.mkdir(parents=True, exist_ok=True)

    for i in range(chunk_num):
        chunk_path = output_dir / f"split_{i + 1}.txt"
        chunk_path.write_text(text[i * max_chunk_size : (i + 1) * max_chunk_size])
