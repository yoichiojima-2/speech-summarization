import re
from pathlib import Path


def merge_text(input_dir: str) -> None:
    target_files = {}
    for i in sorted(Path(input_dir).rglob("*.txt")):
        if match := re.match(r".*_(\d+)\.txt", str(i)):
            target_files[int(match.group(1))] = i

    merged_text = ""
    for _, file in sorted(target_files.items()):
        merged_text += f"{file.read_text()}\n\n"

    output_dir = Path("./data/merge_text")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / f"{Path(input_dir.split(" / ")[-1]).stem}.txt").write_text(merged_text)
