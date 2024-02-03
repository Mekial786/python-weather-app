from dotenv import load_dotenv
import os
import requests
import tkinter as tk

load_dotenv()
api_key= os.getenv("API_KEY")
url = os.getenv("URL")

#get weather info 
def get_weather(city):

    params = {
        'q' : city,
        'appid' : api_key,
        'units' : 'metric',
    }

    try:
        res = requests.get(url, params=params)
        data = res.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']

        result_label.config(text=f"The temperature is {temp} degrees celcius and {description}")

    except requests.exceptions.Timeout:
        result_label.config(text="Error: The request timed out. Try again later.")

    except KeyError:
        result_label.config(text=f"{city} is not a valid city")


#tkinter gui
window = tk.Tk()
window.title('Weather App')

input_frame = tk.Frame(window, pady=10)
input_frame.pack()

name_label = tk.Label(input_frame, text='Enter city:')
name_label.grid(row=0, column=0, padx=5)

entry = tk.Entry(input_frame, bg="white", width=30)
entry.grid(row=0, column=1, padx=5)

get_weather_button = tk.Button(input_frame, text='Get Weather', fg='green', bg='white', command=lambda: get_weather(entry.get()))
get_weather_button.grid(row=0, column=2, padx=5)

result_frame = tk.Frame(window, pady=10)
result_frame.pack()

result_label = tk.Label(result_frame, text='', font=('Helvetica', 12), wraplength=400, justify='center')
result_label.pack()

window.mainloop()
