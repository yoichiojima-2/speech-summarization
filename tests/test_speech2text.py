import warnings
from pathlib import Path

from speech_summarization.speech2text import speech2text


def test_speech2text():
    warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")
    output = Path("./data/speech2text/test.txt")
    if output.exists():
        output.unlink()
    speech2text("./tests/data/input/test.aif")
    text = output.read_text()
    assert text
