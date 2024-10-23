import tkinter as tk
from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

HEIGHT = 350
WIDTH = 450

owm = OWM(API_KEY)
mgr = owm.weather_manager()

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


def get_weather(city):
    observation = mgr.weather_at_place(city)
    weather = observation.weather
    label[
        "text"] = (f"weather: {weather.status}\nwind speed: {weather.wind()['speed']}\nhumidity: {weather.humidity}\n"
                   f"temperature: {weather.temperature('celsius')['temp']}\nclouds: {weather.clouds}")


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14), justify='left', anchor='nw')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
