from tkinter import *;
from dotenv import load_dotenv
import os
import openai


load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def send():
    send = e.get()
    ask = txt.insert(END, "\n" + send)
    print(e.get())
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=e.get(),
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    text = response['choices'][0]['text']
    txt.insert(END, "\n" + text)

root = Tk()
root.title("Chatbot Using CHATGPT")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
 
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
    row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=send).grid(row=2, column=1)


root.mainloop()