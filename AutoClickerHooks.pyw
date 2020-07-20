import threading
import pyautogui
import tkinter
import keyboard
import time

threads = []
start_key = 'z'
stop_key = 'x'
exit_key = 'm'
thread_count = 10
stop_threads = True
inputs_thread = 0
threads_started = False


def processInputs(start_key, exit_key, thread_count):
    global threads, stop_threads, threads_started
    while not keyboard.is_pressed(exit_key):
        if keyboard.is_pressed(start_key):
            stop_threads = not stop_threads
            if threads_started == False:
                startThreads(thread_count)
                time.sleep(1)
            elif stop_threads == False:
                time.sleep(1)
                pass
            else:
                killThreads()
                time.sleep(1)               
    exit()

    

def readEntries():
    start_key = start_entry.get()
    exit_key = exit_entry.get()
    thread_count = int(threads_entry.get())
    return start_key, exit_key, thread_count


def killThreads():
    global stop_threads
    stop_threads = True


def clicker():
    global stop_threads
    while True:
        if not stop_threads:
            pyautogui.click()
        else:
            pass


def createThreads(thread_count):
    global threads
    for i in range(thread_count):
        threads.append(threading.Thread(target=clicker))
        
def startThreads(thread_count):
    global threads, threads_started
    for i in range(thread_count):
        threads[i].start()
    threads_started = True


def mainProgram():
    global start_key, exit_key, thread_count, threads, inputs_thread
    start_key, exit_key, thread_count = readEntries()       
    createThreads(thread_count)
    if inputs_thread == 0:
        inputs_thread = threading.Thread(target=processInputs, args=(start_key, exit_key, thread_count))
    try:
        inputs_thread.start()
    except:
        pass
                        

root = tkinter.Tk()
threads_label = tkinter.Label(root, text="Thread Count (7.5CPS)")
threads_label.grid(row=0, column=0)

threads_entry = tkinter.Entry(root)
threads_entry.grid(row=1, column=0)

start_label = tkinter.Label(root, text="Start / Stop Key")
start_label.grid(row=0,column=1)
start_entry = tkinter.Entry(root)
start_entry.grid(row=1, column=1)

exit_label = tkinter.Label(root, text="Enter Exit Key")
exit_label.grid(row=0,column=3)
exit_entry = tkinter.Entry(root)
exit_entry.grid(row=1, column=3)

start_button = tkinter.Button(root, text="Start program", command=mainProgram)
start_button.grid(row=1, column=4)


root.mainloop()
        
    
    

        
