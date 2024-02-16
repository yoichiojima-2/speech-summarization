from pathlib import Path

from speech_summarization.cleanse_text import cleanse_text, cleanse_texts


def test_cleanse_text():
    output = Path("./data/cleanse_text/test/cleansed_1.txt")
    if output.exists():
        output.unlink()
    cleanse_text("./tests/data/cleanse_text/split_text/test/splitted_1.txt")
    text = output.read_text()
    assert text


def test_cleanse_texts():
    output = Path("./data/cleanse_text/test/")
    if output.exists():
        for file in output.iterdir():
            file.unlink()
        output.rmdir()
    cleanse_texts("./tests/data/cleanse_text/split_text/test")
    text = (output / "cleansed_2.txt").read_text()
    assert text
