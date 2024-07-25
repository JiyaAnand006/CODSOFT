import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning('Warning', 'Please enter a task.')

def delete_task():
    try:
        task_index = task_listbox.curselection()[0]
        task_listbox.delete(task_index)
    except IndexError:
        messagebox.showwarning('Warning', 'Please select a task to delete.')


root = tk.Tk()
root.title('To-Do List')

background_image = Image.open("download.jpeg")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



style = ttk.Style()
style.configure('Title.TLabel', foreground='purple', font=('Aptos Narrow', 20, 'bold')) 
title_frame = ttk.Frame(root, style='Title.TFrame')
title_frame.grid(row=0, column=0, sticky='w', padx=5, pady=5)
ttk.Label(root, text='To-Do List', style='Title.TLabel',).grid(row=0, column=0,  padx=5, pady=5)


task_entry = tk.Entry(root, width=50)
task_entry.grid(row=1, column=0, padx=10, pady=10)

add_button = tk.Button(root, text='Add Task', command=add_task)
add_button.grid(row=1, column=1, padx=10, pady=10)

task_listbox = tk.Listbox(root, width=60, height=10)
task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

delete_button = tk.Button(root, text='Delete Task', command=delete_task)
delete_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
root.mainloop()
