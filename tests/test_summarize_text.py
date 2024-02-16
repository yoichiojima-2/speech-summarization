from pathlib import Path

from speech_summarization.summarize_text import summarize_text, summarize_texts


def test_summarize_text():
    output = Path("./data/summarize_text/test/summarized_1.txt")
    if output.exists():
        output.unlink()
    summarize_text("./tests/data/summarize_text/cleansed_text/test/cleansed_1.txt")
    text = output.read_text()
    assert text


def test_summarize_texts():
    output = Path("./data/summarize_text/test/")
    if output.exists():
        for file in output.iterdir():
            file.unlink()
        output.rmdir()
    summarize_texts("./tests/data/summarize_text/cleansed_text/test")
    text = (output / "summarized_2.txt").read_text()
    assert text
