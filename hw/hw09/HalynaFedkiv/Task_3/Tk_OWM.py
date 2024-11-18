import tkinter as tk
from tkinter import font
from OWM import weather_results


HEIGHT = 350
WIDTH = 450


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)


def get_weather(detailed_status, wind, humidity, temperature, rain, heat_index, clouds):
    # print(detailed_status, wind, humidity, temperature, rain, heat_index, clouds)
    result = f'detailed_status: {detailed_status}\n' \
             f'wind_speed: {wind['speed']}\n' \
             f'wind_deg: {wind['deg']}\n' \
             f'wind_gust: {wind['gust']}\n' \
             f'humidity: {humidity}\n' \
             f'temperature: {temperature['temp']}\n' \
             f'max_temperature: {temperature['temp_max']}\n' \
             f'min_temperature: {temperature['temp_min']}\n' \
             f'feels like: {temperature['feels_like']}\n' \
             f'temperature_kf: {temperature['temp_kf']}\n' \
             f'rain: {rain}\n' \
             f'heat_index: {heat_index}\n' \
             f'clouds: {clouds}'

    label['text'] = result


button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather(*weather_results(entry_field.get())))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()
