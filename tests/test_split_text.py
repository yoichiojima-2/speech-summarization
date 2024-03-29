from pathlib import Path

from speech_summarization.split_text import split_text


def test_split_text():
    split_text(input_path="./tests/data/split_text/test.txt", max_chunk_size=1)
    output_dir = Path("./data/split_text/test")

    assert (output_dir / "splitted_1.txt").read_text() == "h"
    assert (output_dir / "splitted_2.txt").read_text() == "e"
    assert (output_dir / "splitted_3.txt").read_text() == "l"
    assert (output_dir / "splitted_4.txt").read_text() == "l"
    assert (output_dir / "splitted_5.txt").read_text() == "o"
