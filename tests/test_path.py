from pathlib import Path

from speech_summarization import get_path


def test_app_root():
    assert get_path.app_root() == Path().cwd()


def test_speech2text():
    target = Path().cwd() / "tests/data/test.mp3"
    assert get_path.speech2text(target) == Path().cwd() / f"data/speech2text/{target.stem}.txt"


def test_split_text():
    target = Path().cwd() / "tests/data/test.mp3"
    assert get_path.split_text(target) == Path().cwd() / f"data/split_text/{target.stem}"

def test_summarize_text():
    target = Path().cwd() / "tests/data/split_text/test"
    assert get_path.summarize_text(target) == Path().cwd() / f"data/summarize_text/{target.stem}"