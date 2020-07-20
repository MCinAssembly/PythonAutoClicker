# PythonAutoClicker
An Auto Clicker made in python, can achieve 10CPS per thread, but it mostly depends on the speed of your computer.
I recommend having around 2 threads (20CPS in AutoClickerFast) to minimize CPU usage.

# Dependencies

- pygame (AutoClickerFull only) ```pip install pygame```
- Threading.py https://github.com/python/cpython/blob/3.8/Lib/threading.py
- pyautogui ```pip install pyautogui```

# Known Issues

AutoClickerFull Only:
- Will only register keypresses if the pygame window is in the foreground
- Suffers From reduced CPS, roughly 7.5 as opposed to 10 in AutoClickerFast

Both:
- CPU usage can become very high wth many threads, 10+ usually. Doesn't seem like something which could be fixed.

