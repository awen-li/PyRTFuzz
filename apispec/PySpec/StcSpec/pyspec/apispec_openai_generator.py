# pip3 install openai
import openai, os

class Prompter:
    # responsible for communicate with chatGPT
    def __init__(self):
        # remember to set up env var
        self.key = os.environ["OPENAI_API_KEY"]
        openai.api_key = self.key
        self.model_engine = "text-davinci-002"
    
    def ask(self, prompt: str) -> str:
        # Generate a response from the model
        response = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        print(response.choices[0].text)


if __name__ == '__main__':
    ptr = Prompter();
    ptr.ask("Please help me generate python3 example of calling `xml.sax.expatreader.ExpatParser.getProperty`")