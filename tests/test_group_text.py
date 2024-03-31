from pathlib import Path

from speech_summarization.group_text import group_text


def test_group_text():
    output_grouped = Path("./data/group_text/test.txt")
    output_not_grouped = Path("./data/group_text/test_not_to_split.txt")

    if output_grouped.exists():
        output_grouped.unlink()
    if output_not_grouped.exists():
        output_not_grouped.unlink()

    group_text("./tests/data/group_text")
    group_text("./tests/data/group_text")

    assert output_grouped.read_text()
    assert output_not_grouped.read_text()
