import threading
import pyautogui
import tkinter
import time

threads = []
thread_count = 10
stop_threads = False

pyautogui.FAILSAFE = True

def killThreads():
    global stop_threads
    stop_threads = True


def clicker():
    while True:
        pyautogui.click()
        if stop_threads:
            break


def createThreads(thread_count, threads):
    for i in range(thread_count):
        threads.append(threading.Thread(target=clicker))
        

def resetThreads(thread_count, threads):
    for i in range(thread_count):
            threads[i] = (threading.Thread(target=clicker))
            

def startThreads(thread_count, threads):
    global stop_threads
    stop_threads = False
    for i in range(thread_count):
        threads[i].start()


def mainProgram():
    global threads
    global thread_count
    thread_count = int(threads_entry.get())
    if (len(threads)) == 0:
        createThreads(thread_count, threads)        
    else:
        resetThreads(thread_count, threads)
    time.sleep(3) # will wait three seconds so it doesnt spam start
    startThreads(thread_count, threads)
                           

root = tkinter.Tk()
threads_label = tkinter.Label(root, text="Thread Count 10CPS/T")
threads_label.grid(row=0, column=0)

threads_entry = tkinter.Entry(root)
threads_entry.grid(row=1, column=0)

start_button = tkinter.Button(root, text="Start Clicking", command=mainProgram)
start_button.grid(row=1, column=1)

stop_button = tkinter.Button(root, text="Stop Clicking", command=killThreads, padx=1)
stop_button.grid(row=1, column=2)

root.mainloop()
