import tkinter as tk
from tkinter import font
from OWM import call_for_weather

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

def get_weather(detailed_status: str, wind: dict, humidity: int, temperature: dict, rain: dict, heat_index: str, clouds: int):
    weather = (
        f"Detailed Status: {detailed_status}\n"
        f"Wind Speed: {wind['speed']} m/s\n"
        f"Wind Direction: {wind['deg']} degrees\n"
        f"Wind Gust: {wind['gust']} m/s\n"
        f"Humidity: {humidity}%\n"
        f"Temperature: {temperature}\n"
        f"Rain: {rain}\n"
        f"Heat Index: {heat_index}\n"
        f"Clouds: {clouds}%"
    )

    label['text'] = weather
    

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray",
                   font=('Courier', 8), 
                   command=lambda: get_weather(*call_for_weather(entry_field.get())))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14), wraplength=310, justify='left', anchor='nw')
label.pack(expand=True, fill='both')



root.mainloop()

