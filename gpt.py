import openai, os

SYSTEM = ""
FORMAT = ""
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "gpt_assets", "system.txt"), "r", encoding="utf-8") as f:
    SYSTEM = f.read()

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "gpt_assets", "format.txt"), "r", encoding="utf-8") as f:
    FORMAT = f.read()

MODEL = "gpt-3.5-turbo-16k-0613"
TEMPERATURE = 0.45
MAX_TOKENS = 5000

def init(api_key):
    openai.api_key = api_key

    gpt = {}

    def complete(text):
        prompt = "Rozbor:\n" + text + "\n\n" + "Formát:\n" + FORMAT
        
        messages = [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": prompt}
        ]

        response = openai.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS
        )

        try:
            response_text = response.choices[0].message.content

            return response_text
        except:
            print("Error while saving answers. Will print to console instead.")

            print(response)
        
    gpt["complete"] = complete

    return gpt

if __name__ == "__main__":
    print("This file is not meant to be run directly.")
    print("Please run main.py instead.")
    exit(1)