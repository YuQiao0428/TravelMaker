from flask import Flask
app = Flask(__name__)
import openai
import os
openai.api_key = os.getenv("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")
@app.route("/")
def index():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="靜宜大學資管系教學特色？",
        max_tokens=128,
        temperature=0.5,
    )
    msg = response.choices[0].text
    return msg
if __name__ == "__main__":
    app.run()
