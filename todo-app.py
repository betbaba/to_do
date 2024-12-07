import tkinter as tk
from tkinter import messagebox
import json
import os

class TodoApp:
    def __init__(self, root, filename='todolist.json'):
        self.root = root
        self.filename = filename
        self.tasks = []
        self.load_tasks()
        self.create_ui()

    def create_ui(self):
        self.root.title("To-Do List")
        self.root.geometry("400x400")

        self.task_listbox = tk.Listbox(self.root, height=10, width=40)
        self.task_listbox.pack(pady=20)

        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", width=15, command=self.add_task)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", width=15, command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(self.root, text="Complete Task", width=15, command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.refresh_listbox()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)

    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)

        for task in self.tasks:
            status = "Done" if task['completed'] else "Pending"
            task_text = f"{task['task']} - {status}"

            # Add color coding for task status
            if task['completed']:
                self.task_listbox.insert(tk.END, task_text)
                self.task_listbox.itemconfig(tk.END, {'bg': 'lightgreen'})
            else:
                self.task_listbox.insert(tk.END, task_text)
                self.task_listbox.itemconfig(tk.END, {'bg': 'lightcoral'})

    def add_task(self):
        task_text = self.entry.get()
        if task_text:
            self.tasks.append({'task': task_text, 'completed': False})
            self.save_tasks()
            self.refresh_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        selected_task_idx = self.task_listbox.curselection()
        if selected_task_idx:
            task_idx = selected_task_idx[0]
            del self.tasks[task_idx]
            self.save_tasks()
            self.refresh_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def complete_task(self):
        selected_task_idx = self.task_listbox.curselection()
        if selected_task_idx:
            task_idx = selected_task_idx[0]
            self.tasks[task_idx]['completed'] = True
            self.save_tasks()
            self.refresh_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
