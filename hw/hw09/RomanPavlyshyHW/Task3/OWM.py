from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details


def call_the_weather(place: str):
    observation = mgr.weather_at_place(place)
    w = observation.weather
    return w.detailed_status, w.wind(), w.humidity, w.temperature('celsius'), w.rain, w.heat_index, w.clouds




