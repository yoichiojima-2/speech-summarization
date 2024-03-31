from pathlib import Path


def app_root() -> Path:
    return Path().cwd()


def speech2text(target: str) -> Path:
    return app_root() / f"data/speech2text/{Path(target).stem}.txt"


def split_text(target: str) -> Path:
    return app_root() / f"data/split_text/{Path(target).stem}"


def cleanse_text(target: str) -> Path:
    return app_root() / f"data/cleanse_text/{Path(target).stem}"


def summarize_text(target: str) -> Path:
    return app_root() / f"data/summarize_text/{Path(target).stem}"


def merge_text(target: str) -> Path:
    return app_root() / f"data/merge_text/{Path(target).stem}"


def group_text() -> Path:
    return app_root() / f"data/group_text"


def refine_output() -> Path:
    return app_root() / f"data/refine_output"
