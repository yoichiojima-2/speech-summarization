import sys
from pathlib import Path

app_root = Path("./audio_summarization")
sys.path.append(str(app_root))

import summarize_text

def test_summarize_text():
    res = summarize_text.main(input_path = "./tests/data/test.txt")
    output = Path("./data/summarized_text.txt")
    text = output.read_text()
    assert text
