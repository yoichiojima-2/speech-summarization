import sys
from pathlib import Path

import luigi

app_root = Path().cwd()
sys.path.append(str(app_root))

from speech_summarization import get_path
from speech_summarization.speech2text import speech2text
from speech_summarization.split_text import split_text


class Speech2Text(luigi.Task):
    target = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(str(get_path.speech2text(self.target)))

    def run(self):
        speech2text(input_path=str(self.target))


class SplitText(luigi.Task):
    target = luigi.Parameter()

    def requires(self):
        return Speech2Text(target=self.target)

    def output(self):
        return luigi.LocalTarget(str(get_path.split_text(self.target)))

    def run(self):
        print(str(self.target))
        split_text(input_path=str(get_path.speech2text(self.target)), max_chunk_size=4096)


if __name__ == "__main__":
    luigi.run()
