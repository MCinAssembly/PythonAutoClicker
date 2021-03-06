# PythonAutoClicker
An Auto Clicker made in python, can achieve 10CPS per thread, but it mostly depends on the speed of your computer.
I recommend having around 2 threads (20CPS in AutoClickerFast) to minimize CPU usage.

AutoClickerHooks listens for keystrokes in the background to start/stop/close by using keyboard hooks, I recommend against using it unless you really have to.

INFO: AutoClickerFast currently has a band-aid fix to delaying the start for 3s, as to prevent the start button from being spammed, I am currently working on a more elegant solution to this.

# Features

- 10 CPS Per Threads (AutoClickerFast Only)
- Unlimited Threads *
- Custom Keybinds (AutoClickerFull & AutoClickerHooks only)
- Simple Tkinter GUI
- Precompiled .exe (AutoClickerFast & AutoClickerHooks only)
- Hidden Console


*The more threads you make the less stable it becomes depending on your computer's performance. Multi-threading will be removed from AutoClickerHooks in the future in favour of a high performance single thread system*

# Dependencies

- Release EXE has no dependencies
- pygame (AutoClickerFull only) ```pip install pygame```
- keyboard (AutoClickerHooks only) ```pip install keyboard```
- Threading.py https://github.com/python/cpython/blob/3.8/Lib/threading.py
- pyautogui ```pip install pyautogui```

# Known Issues

AutoClickerFull Only:
- Will only register keypresses if the pygame window is in the foreground

AutoClickerHooks & AutoClickerFull:
- Suffers From reduced CPS, roughly 7.5 as opposed to 10 in AutoClickerFast

All:
- CPU usage can become very high wth many threads, 10+ usually. Doesn't seem like something which could be fixed.

