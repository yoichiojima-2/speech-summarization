from pathlib import Path

from speech_summarization.group_text import group_text

def test_group_text():
    group_text("./data/merge_text")

    output = Path("./data/group_text/test.txt")
    if output.exists():
        output.unlink()
    group_text("./tests/data/group_text")
    text = output.read_text()
    assert text
