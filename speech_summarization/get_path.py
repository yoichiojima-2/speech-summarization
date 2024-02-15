from pathlib import Path


def app_root() -> Path:
    return Path().cwd()


def speech2text(target: Path) -> Path:
    return app_root() / f"data/speech2text/{Path(target).stem}.txt"


def split_text(target: Path) -> Path:
    return app_root() / f"data/split_text/{Path(target).stem}"


def summarize_text(target: Path) -> Path:
    return app_root() / f"data/summarize_text/{Path(target).stem}"
