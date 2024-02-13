from pathlib import Path

from speech_summarization.summarize_text import summarize_text


def test_summarize_text():
    output = Path("./data/summarize_text/test.txt")
    if output.exists():
        output.unlink()
    summarize_text("./tests/data/summarize_text/test.txt")
    text = output.read_text()
    assert text
