import json

import flask


from flask import Flask, request
import openai

app = Flask(__name__)


def do_chat(question):
    openai.organization = "org-SXSsrHgcU9Yiywr18wPVvxFi"
    openai.api_key = "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"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    data = completion.choices[0].message
    return data['content']


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.data
    question = json.loads(data)['question']
    print(question)
    return do_chat(question)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9527)