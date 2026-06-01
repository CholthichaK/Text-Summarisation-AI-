from transformers import pipeline
from app.preprocessing import preprocess_text


class TextSummarizer:

    def __init__(self, model_name: str = "facebook/bart-large-cnn"):
        """
        Load the Hugging Face summarization pipeline.
        """
        self.model_name = model_name
        self.summarizer = pipeline("summarization", model=model_name)

    def summarize(
        self,
        text: str,
        max_input_words: int = 500,
        max_summary_length: int = 130,
        min_summary_length: int = 30
    ) -> str:
        """
        Generate a summary from input text.
        """
        processed_text = preprocess_text(text, max_words=max_input_words)

        result = self.summarizer(
            processed_text,
            max_length=max_summary_length,
            min_length=min_summary_length,
            do_sample=False
        )

        return result[0]["summary_text"]


if __name__ == "__main__":
    summarizer = TextSummarizer()

    text = """
Efficiency: Instantly reduce reading time and extract main ideas.Customization: Many tools allow adjusting summary length and choosing between paragraph or bulleted formats.Versatility: Useful for academic research, business meetings, and simplifying complex text.Accessibility: Most AI tools are free to use, requiring no sign-up to produce quick, accurate results.
    """

    summary = summarizer.summarize(text)

    print("Generated Summary:")
    print(summary)