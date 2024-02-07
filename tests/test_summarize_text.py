import sys
from pathlib import Path

app_root = Path("./audio_summarization")
sys.path.append(str(app_root))

import summarize_text

def test_summarize_text():
    res = summarize_text.main(
        "hey chat gpt. this is a test prompt just to check "
        "if this code works fine. if you receive something, "
        "just say 'yay"
    )
    assert res
    assert isinstance(res, str)
