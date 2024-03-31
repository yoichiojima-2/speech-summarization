from pathlib import Path

from speech_summarization.merge_text import merge_text


def test_split_text():
    merge_text(input_dir="./tests/data/merge_text/merge_text/test")
    assert Path("./data/merge_text/test.txt").exists()
