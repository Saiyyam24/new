import tkinter as tk
from tkinter import filedialog

def add_task():
    task = task_entry.get()
    task_entry.delete(0, tk.END)
    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(tk.END, task)

def open_task_file():
    global task_list
    try:
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task != '\n':
                task_list.append(task.strip())
                listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        with open('tasklist.txt', 'w') as taskfile:
            pass

def delete_task():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
        task_list.pop(task_index)
        with open("tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(f"{task}\n")
    except IndexError:
        pass

root = tk.Tk()
root.title("TO-DO List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

# Icon
Image_icon = tk.PhotoImage(file="images/task.png")
root.iconphoto(False, Image_icon)

# Top bar
TopImage = tk.PhotoImage(file="images/topbar.png")
tk.Label(root, image=TopImage).pack()

dockImage = tk.PhotoImage(file="images/dock.png")
tk.Label(root, image=dockImage, bg="#32405b").place(x=30, y=25)
noteImage = tk.PhotoImage(file="images/task.png")
tk.Label(root, image=noteImage, bg="#32405b").place(x=340, y=25)

heading = tk.Label(root, text="ALL TASK", font="ariel 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

# Main
frame = tk.Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task = tk.StringVar()
task_entry = tk.Entry(frame, width=18, font="Arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

button = tk.Button(frame, text="ADD", font="ariel 20 bold", width=6, bg="#5a59ff", fg="#fff", bd=0, command=add_task)
button.place(x=300, y=0)

# Listbox
frame1 = tk.Frame(root, bd=3, width=700, height=200, bg="#32405b")
frame1.pack(pady=(160, 0))

listbox = tk.Listbox(frame1, font=('arial', 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a59ff")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=2)

scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

open_task_file()

# Delete
Delete_icon = tk.PhotoImage(file="images/delete.png")
delete_button = tk.Button(root, image=Delete_icon, bd=0).pack(side=BOTTOM,pady=13)
root.mainlool()