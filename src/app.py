from flask import request
from flask import Flask
from transformers import pipeline

app = Flask(__name__)

def analyze_text(input: str):
    pipe = pipeline("text-classification", model="mshenoda/roberta-spam")
    x = pipe(input)[0]

    if x["label"] == "LABEL_0":
        return {"type":"Not Spam", "score":x["score"]}
    else:
        return {"type":"Spam", "score":x["score"]}

@app.route('/')
def hello_world():
    return {}

@app.route('/analyze', methods=['POST'])
def analyze():
    error = None

    if request.method == 'POST':
        content = request.json
        text = content['payload']
    else:
        return {}

    return analyze_text(text)


if __name__ == '__main__':
    app.run(debug=True)