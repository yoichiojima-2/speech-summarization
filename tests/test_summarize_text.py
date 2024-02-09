from pathlib import Path
from audio_summarization import summarize_text


def test_summarize_text():
    output = Path("./data/summarize_text/test.txt")
    if output.exists():
        output.unlink()
    summarize_text.main("./tests/data/input/test.txt")
    text = output.read_text()
    assert text
