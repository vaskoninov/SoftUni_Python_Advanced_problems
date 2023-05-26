import tkinter as tk

import openai

openai.api_key = ''


def get_image_url():
    response = openai.Image.create(
        prompt=input_field.get(),
        n=1,
        size="256x256"
    )

    image_url = response['data'][0]['url']
    print(image_url)


def render_image():
    image_url = get_image_url()


window = tk.Tk()
window.title("Image creator")
window.geometry("500x500")

input_field = tk.Entry(window)
input_field.place(x=125, y=120)
generate_button = tk.Button(window, text="Create", height=1, command=render_image())
generate_button.place(x=300, y=120)

window.mainloop()
