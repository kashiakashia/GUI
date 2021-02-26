# from tkinter import *

# API key ac7b21e57fedf3d7fbc127b77c3f59bb
# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image
import requests
5
HEIGHT = 500
WIDTH = 600


def test_function(entry):
    print('This is entry:', entry)


def format_response(weather):

    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        country = weather['sys']['country']
        final_str = 'Miasto: %s, %s \nWarunki: %s \nTemperatura: %s °C' % (
            name, country, desc, temp)
    except:
        final_str = 'Nie mamy takiego miasta z bazie, \npy spróbuj podać inne.'

    return final_str


def get_weather(city):

    weather_key = 'ac7b21e57fedf3d7fbc127b77c3f59bb'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric', 'lang': 'pl'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)


def open_image(icon):
    size = int(frame_label.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open(
        './img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0, 0, anchor='nw', image=img)
    weather_icon.image = img


root = tk.Tk()
root.title('Weather App')

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

background_image = ImageTk.PhotoImage(Image.open('landscape2.png'))
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#96ceb4', bd=5)
frame.place(relheight=0.1, relwidth=0.8, relx=0.5, rely=0.1, anchor='n')

entry = tk.Entry(frame, font=('Calibri', 18))
entry.place(relheight=1, relwidth=0.65)

button = tk.Button(frame, text='Get Weather',
                   activebackground='#ff6f69', font=('Calibri', 16), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.30)

frame_label = tk.Frame(root, bg='#96ceb4', bd=5)
frame_label.place(relheight=0.6, relwidth=0.8, relx=0.5, rely=0.25, anchor='n')

bg_color = 'white'
label = tk.Label(frame_label, font=('Calibri', 18),
                 anchor='nw', justify='left', bd=4, bg=bg_color)
label.place(relwidth=1, relheight=1)

results = tk.Label(label, anchor='nw', justify='left', bd=4)
results.config(font=40, bg=bg_color)
results.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(results, bg=bg_color, bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)
# print(tk.font.families())

root.mainloop()
