import pyowm
 
owm = pyowm.OWM('eb13269a381263cba0085390f7bd8917')
observation = owm.weather_at_place('London,uk')
w = observation.get_weather()
 
w.get_wind()
w.get_humidity()
