import tkinter as tk
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.api_key = "b330ba9274582c195c94173ad084cc2a"  # Replace with your OpenWeatherMap API key

        self.city_label = tk.Label(root, text="Enter City:",font=('Arial', 25))
        self.city_label.pack()

        self.city_entry = tk.Entry(root,bg="white", fg="black",font=('Arial', 25))
        self.city_entry.pack()

        self.weather_label = tk.Label(root, text="")
        self.weather_label.pack()

        self.get_weather_button = tk.Button(root, text="Get Weather",font=('Arial', 12) , command=self.get_weather)
        self.get_weather_button.pack()

    def get_weather(self):
        city = self.city_entry.get()
        if city:
            try:
                url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
                response = requests.get(url)
                data = response.json()

                weather = data['weather'][0]['description']
                temperature = data['main']['temp']

                weather_text = f"Weather: {weather}\nTemperature: {temperature}°C"
                self.weather_label.config(text=weather_text,font=('Arial', 20))
            except Exception as e:
                self.weather_label.config(text="City not found!",font=('Arial', 20))

if __name__ == "__main__":
  root = tk.Tk()
  weather_app = WeatherApp(root)
  root.mainloop()
