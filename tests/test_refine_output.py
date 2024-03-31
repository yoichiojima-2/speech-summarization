from pathlib import Path

from speech_summarization.refine_output import refine_outputs


def test_refine_output():
    output = Path("./data/refine_output")
    if output.exists():
        for file in output.iterdir():
            file.unlink()
        output.rmdir()
    refine_outputs("./tests/data/refine_output")
    text_1 = (output / "test_1.txt").read_text()
    text_2 = (output / "test_2.txt").read_text()
    assert text_1
    assert text_2
