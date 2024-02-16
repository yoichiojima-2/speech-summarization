import luigi

from speech_summarization import get_path
from speech_summarization.speech2text import speech2text
from speech_summarization.split_text import split_text
from speech_summarization.cleanse_text import cleanse_texts
from speech_summarization.summarize_text import summarize_texts


class Speech2Text(luigi.Task):
    target = luigi.Parameter()

    def run(self):
        speech2text(input_path=str(self.target))

    def output(self):
        return luigi.LocalTarget(str(get_path.speech2text(self.target)))


class SplitText(luigi.Task):
    target = luigi.Parameter()

    def requires(self):
        return Speech2Text(target=self.target)

    def run(self):
        split_text(input_path=str(get_path.speech2text(self.target)), max_chunk_size=2000)

    def output(self):
        return luigi.LocalTarget(str(get_path.split_text(self.target)))


class CleanseText(luigi.Task):
    target = luigi.Parameter()

    def requires(self):
        return SplitText(target=self.target)

    def run(self):
        cleanse_texts(input_dir=str(get_path.split_text(self.target)))

    def output(self):
        return luigi.LocalTarget(str(get_path.cleanse_text(self.target)))


class SummarizeText(luigi.Task):
    target = luigi.Parameter()

    def requires(self):
        return CleanseText(target=self.target)

    def run(self):
        summarize_texts(input_dir=str(get_path.cleanse_text(self.target)))

    def output(self):
        return luigi.LocalTarget(str(get_path.summarize_text(self.target)))


if __name__ == "__main__":
    luigi.run()
