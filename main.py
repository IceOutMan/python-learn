# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import openai

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    openai.organization = "org-SXSsrHgcU9Yiywr18wPVvxFi"
    openai.api_key = "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"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "你好,你会说中文么"}
        ]
    )

    data = completion.choices[0].message
    print(data['content'])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
