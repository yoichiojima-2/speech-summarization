from pathlib import Path
from audio_summarization import summarize_text


def test_summarize_text():
    output = Path("./data/summarized_text.txt")
    if output.exists():
        output.unlink()
    summarize_text.main("./tests/data/test.txt")
    text = output.read_text()
    assert text
