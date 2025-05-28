import tkinter as tk
from tkinter import ttk, messagebox
import requests

URL = 'http://127.0.0.1:8000/avengers/'

# ------------------ API Functions ------------------ #

def get_avengers():
    response = requests.get(URL)
    if response.status_code == 200:
        avengers = response.json()
        for row in tree.get_children():
            tree.delete(row)
        for avenger in avengers:
            tree.insert('', tk.END, values=(avenger['id'], avenger['name'], avenger['heroic_name']))
    else:
        messagebox.showerror("Error", "Could not retrieve Avengers.")

def add_avenger():
    name = entry_name.get()
    heroic_name = entry_heroic.get()
    data = {'name': name, 'heroic_name': heroic_name}
    response = requests.post(URL, json=data)
    if response.status_code == 201:
        messagebox.showinfo("Success", "Avenger added successfully.")
        get_avengers()
    else:
        messagebox.showerror("Error", "Failed to add Avenger.")

def get_avenger_by_id():
    avenger_id = entry_id.get()
    response = requests.get(URL + avenger_id + '/')
    if response.status_code == 200:
        avenger = response.json()
        for row in tree.get_children():
            tree.delete(row)
        tree.insert('', tk.END, values=(avenger['id'], avenger['name'], avenger['heroic_name']))
    else:
        messagebox.showerror("Error", "Avenger not found.")

def update_avenger():
    avenger_id = entry_id.get()
    name = entry_name.get()
    heroic_name = entry_heroic.get()
    data = {'name': name, 'heroic_name': heroic_name}
    response = requests.put(URL + avenger_id + '/', json=data)
    if response.status_code == 200:
        messagebox.showinfo("Success", "Avenger updated successfully.")
        get_avengers()
    else:
        messagebox.showerror("Error", "Failed to update Avenger.")

def delete_avenger():
    avenger_id = entry_id.get()
    response = requests.delete(URL + avenger_id + '/')
    if response.status_code == 204:
        messagebox.showinfo("Success", "Avenger deleted.")
        get_avengers()
    else:
        messagebox.showerror("Error", "Failed to delete Avenger.")

# ------------------ Tkinter GUI ------------------ #

root = tk.Tk()
root.title("🌟 Avengers API Interface")
root.geometry("750x600")
root.configure(bg='#e0f7f9')

# Fonts and colors
FONT = ("Segoe UI", 11)
BG_COLOR = '#e0f7f9'
BTN_COLOR = '#007acc'
BTN_HOVER = '#005f99'
ENTRY_BG = '#ffffff'

# Input Frame
input_frame = tk.Frame(root, bg=BG_COLOR, pady=10)
input_frame.pack(fill='x')

tk.Label(input_frame, text="ID", font=FONT, bg=BG_COLOR).grid(row=0, column=0, padx=10, pady=5)
entry_id = tk.Entry(input_frame, font=FONT, bg=ENTRY_BG)
entry_id.grid(row=0, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Name", font=FONT, bg=BG_COLOR).grid(row=1, column=0, padx=10, pady=5)
entry_name = tk.Entry(input_frame, font=FONT, bg=ENTRY_BG)
entry_name.grid(row=1, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Heroic Name", font=FONT, bg=BG_COLOR).grid(row=2, column=0, padx=10, pady=5)
entry_heroic = tk.Entry(input_frame, font=FONT, bg=ENTRY_BG)
entry_heroic.grid(row=2, column=1, padx=10, pady=5)

# Button Frame
button_frame = tk.Frame(root, bg=BG_COLOR, pady=10)
button_frame.pack()

def style_button(btn):
    btn.config(font=FONT, bg=BTN_COLOR, fg='white', bd=0, padx=15, pady=5, cursor="hand2")
    btn.bind("<Enter>", lambda e: btn.config(bg=BTN_HOVER))
    btn.bind("<Leave>", lambda e: btn.config(bg=BTN_COLOR))

buttons = [
    ("Get All Avengers", get_avengers),
    ("Add Avenger", add_avenger),
    ("Get Avenger by ID", get_avenger_by_id),
    ("Update Avenger", update_avenger),
    ("Delete Avenger", delete_avenger),
]

for idx, (text, cmd) in enumerate(buttons):
    btn = tk.Button(button_frame, text=text, command=cmd)
    btn.grid(row=idx//2, column=idx%2, padx=10, pady=5)
    style_button(btn)

# Treeview Frame
table_frame = tk.Frame(root, bg=BG_COLOR, pady=10)
table_frame.pack(fill='both', expand=True)

columns = ('ID', 'Name', 'Heroic Name')
tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=12)
tree.heading('ID', text='ID')
tree.heading('Name', text='Name')
tree.heading('Heroic Name', text='Heroic Name')
tree.column('ID', anchor='center', width=60)
tree.column('Name', anchor='center', width=200)
tree.column('Heroic Name', anchor='center', width=200)
tree.pack(fill='both', expand=True, padx=20, pady=10)

# Styling the Treeview
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview",
                background="white",
                foreground="black",
                rowheight=28,
                fieldbackground="white",
                font=FONT)
style.configure("Treeview.Heading",
                font=('Segoe UI', 11, 'bold'),
                background='#007acc',
                foreground='white')

root.mainloop()
