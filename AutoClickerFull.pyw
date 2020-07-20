import threading
import pyautogui
import pygame
import tkinter

threads = []
start_key = 'z'
stop_key = 'x'
exit_key = 'm'
thread_count = 10
stop_threads = False

pyautogui.FAILSAFE = True

def processInputs(start_key, stop_key, exit_key, thread_count, threads):
    pygame.init()
    display_surface = pygame.display.set_mode((200, 200))
    while True:
        #stop_threads = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == ord(start_key):
                    startThreads(thread_count, threads)
                if event.key == ord(stop_key):
                    killThreads()
                    resetThreads(thread_count, threads)
                if event.key == ord(exit_key):
                    killThreads()
                    exit()


def readEntries():
    start_key = start_entry.get()
    stop_key = stop_entry.get()
    exit_key = exit_entry.get()
    thread_count = int(threads_entry.get())
    return start_key, stop_key, exit_key, thread_count


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
    start_key, stop_key, exit_key, thread_count = readEntries()    
    root.destroy()
    inputs_thread = threading.Thread(target=processInputs, args=(start_key, stop_key, exit_key, thread_count, threads))
    createThreads(thread_count, threads)   
    inputs_thread.start()
    
                    

root = tkinter.Tk()
threads_label = tkinter.Label(root, text="Thread Count (7.5CPS)")
threads_label.grid(row=0, column=0)

threads_entry = tkinter.Entry(root)
threads_entry.grid(row=1, column=0)

start_label = tkinter.Label(root, text="Enter Start Key")
start_label.grid(row=0,column=1)
start_entry = tkinter.Entry(root)
start_entry.grid(row=1, column=1)

stop_label = tkinter.Label(root, text="Enter Stop Key")
stop_label.grid(row=0,column=2)
stop_entry = tkinter.Entry(root)
stop_entry.grid(row=1, column=2)

exit_label = tkinter.Label(root, text="Enter Exit Key")
exit_label.grid(row=0,column=3)
exit_entry = tkinter.Entry(root)
exit_entry.grid(row=1, column=3)

info_label = tkinter.Label(root, text="NO CHARACTER CAN BE THE SAME", fg="red")
info_label.grid(row=2, column=4)

start_button = tkinter.Button(root, text="Start program", command=mainProgram)
start_button.grid(row=1, column=4)

root.mainloop()
        
    
    

        
