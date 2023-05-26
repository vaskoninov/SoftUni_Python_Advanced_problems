import tkinter as tk
import urllib.request
from io import BytesIO

import openai
from PIL import Image, ImageTk

openai.api_key = ''


def display_image(image_url):
    with urllib.request.urlopen(image_url) as url:
        image_data = url.read()

    image_stream = BytesIO(image_data)
    image = ImageTk.PhotoImage(Image.open(image_stream))
    image_label.configure(image=image)
    image_label.image = image


def get_image_url():
    response = openai.Image.create(
        prompt=input_field.get(),
        n=1,
        size="256x256"
    )

    image_url = response['data'][0]['url']
    return image_url


def render_image():
    try:
        image_url = get_image_url()
        input_field.delete(0, tk.END)
    except openai.error.InvalidRequestError:
        error_label = tk.Label(text="Prompt cannot be empty")
        error_label.place(x=100, y=100)
    else:
        display_image(image_url)


window = tk.Tk()
window.title("Image creator")
window.geometry("500x500")

image_label = tk.Label(window)
image_label.place(x=125, y=100)

input_field = tk.Entry(window)
input_field.place(x=125, y=120)
generate_button = tk.Button(window, text="Create", height=1, command=render_image())
generate_button.place(x=300, y=120)

window.mainloop()
