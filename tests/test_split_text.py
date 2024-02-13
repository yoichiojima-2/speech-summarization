from pathlib import Path
from speech_summarization.split_text import split_text


def test_split_text():
    split_text(input_path = "./tests/data/split_text/test.txt", max_chunk_size = 1)
    output_dir = Path("./data/split_text")

    output1 = output_dir / "test_1.txt"
    output2 = output_dir / "test_2.txt"
    output3 = output_dir / "test_3.txt"
    output4 = output_dir / "test_4.txt"
    output5 = output_dir / "test_5.txt"

    assert output1.read_text() == "h"
    assert output2.read_text() == "e"
    assert output3.read_text() == "l"
    assert output4.read_text() == "l"
    assert output5.read_text() == "o"