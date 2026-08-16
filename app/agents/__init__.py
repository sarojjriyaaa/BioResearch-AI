class ReviewAgent:

    def __init__(self):

        self.client = configure_gemini(
            os.getenv("GEMINI_API_KEY")
        )