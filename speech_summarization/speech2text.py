from pathlib import Path

import whisper


def speech2text(input_path: str) -> str:
    model = whisper.load_model("medium")
    res = model.transcribe(input_path, language="ja")

    output_dir = Path("./data/speech2text")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / f"{Path(input_path).stem}.txt").write_text(res["text"])