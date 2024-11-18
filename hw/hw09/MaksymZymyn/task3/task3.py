# Task 3.
# You need combine two programs OWM.py and Tk_OWM.py
# into one working program.
# Files OWM.py and Tk_OWM.py are in this directory

import tkinter as tk
from tkinter import messagebox
from pyowm import OWM

# Weather API configuration
API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

# Tkinter window setup
HEIGHT = 360
WIDTH = 450

root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# Use Text widget for colorful output
output_text = tk.Text(lower_frame, font=('Courier', 10), bg='white', wrap='word')
output_text.place(relx=0, rely=0, relwidth=1, relheight=1)

# Configure tags for colors
output_text.tag_configure("header", foreground="blue", font=('Courier', 10, 'bold'))
output_text.tag_configure("condition", foreground="green", font=('Courier', 10))
output_text.tag_configure("wind", foreground="purple", font=('Courier', 10))
output_text.tag_configure("humidity", foreground="orange", font=('Courier', 10))
output_text.tag_configure("temperature", foreground="red", font=('Courier', 10))
output_text.tag_configure("rain", foreground="brown", font=('Courier', 10))
output_text.tag_configure("heat_index", foreground="cyan", font=('Courier', 10))
output_text.tag_configure("clouds", foreground="magenta", font=('Courier', 10))


def get_weather():
    location = entry_field.get()  # Get the location from the entry field
    output_text.delete(1.0, tk.END)  # Clear previous output
    try:
        observation = mgr.weather_at_place(location)
        weather = observation.weather

        # Prepare weather details
        detailed_status = weather.detailed_status
        wind_info = weather.wind()
        humidity = weather.humidity
        temperature = weather.temperature('celsius')
        rain = weather.rain
        heat_index = weather.heat_index
        clouds = weather.clouds

        # Extract temperature details
        temp = temperature.get('temp')
        temp_max = temperature.get('temp_max')
        temp_min = temperature.get('temp_min')
        feels_like = temperature.get('feels_like')
        temp_kf = temperature.get('temp_kf')

        # Insert weather details with different colors
        output_text.insert(tk.END, "Weather Condition: ", "header")
        output_text.insert(tk.END, f"{detailed_status}\n", "condition")

        output_text.insert(tk.END, "Wind Info: ", "header")
        output_text.insert(tk.END, f"{wind_info}\n", "wind")

        output_text.insert(tk.END, "Humidity: ", "header")
        output_text.insert(tk.END, f"{humidity}%\n", "humidity")

        output_text.insert(tk.END, "Temperature: \n", "header")
        output_text.insert(tk.END, f"  Current: {temp}°C\n", "temperature")
        output_text.insert(tk.END, f"  Max: {temp_max}°C\n", "temperature")
        output_text.insert(tk.END, f"  Min: {temp_min}°C\n", "temperature")
        output_text.insert(tk.END, f"  Feels Like: {feels_like}°C\n", "temperature")
        output_text.insert(tk.END, f"  Temp KF: {temp_kf}\n", "temperature")

        output_text.insert(tk.END, "Rain: ", "header")
        output_text.insert(tk.END, f"{rain}\n", "rain")

        output_text.insert(tk.END, "Heat Index: ", "header")
        output_text.insert(tk.END, f"{heat_index}\n", "heat_index")

        output_text.insert(tk.END, "Cloud Coverage: ", "header")
        output_text.insert(tk.END, f"{clouds}%", "clouds")

    except Exception as e:
        messagebox.showerror("Error", f"Could not retrieve weather data for '{location}'.\n{str(e)}")


root.mainloop()
