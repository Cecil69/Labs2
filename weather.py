from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('f6e8d5bd4a37e8432cbd31254e32b050')
mgr = owm.weather_manager()
place = input("Enter Country Name  ")

# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(f'{place},GB')
w = observation.weather

w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
HongKong = w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
rain = w.rain                    # {}
w.heat_index              # None
cloud = w.clouds                  # 75
print(cloud, rain)
