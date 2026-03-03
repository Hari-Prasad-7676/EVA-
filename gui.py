import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import json
import requests


def load_memory():
    with open("memory.json", "r") as file:
        return json.load(file)

memory = load_memory()


def ask_eva(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma:2b",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]


def send_message(event=None):
    user_input = user_entry.get()
    if not user_input.strip():
        return

    chat_area.insert(tk.END, f"> USER: {user_input}\n", "user")
    user_entry.delete(0, tk.END)

    level = memory["relationship_level"]
    mood = memory["mood"]
    personality = memory.get("personality", "calm")

    prompt = f"""
You are EVA, a futuristic AI assistant.
Personality: {personality}
User name: {memory['user_name']}
Relationship level: {level}
Current mood: {mood}

Be intelligent, calm, slightly futuristic but still human.

User says: {user_input}
"""

    reply = ask_eva(prompt)

    chat_area.insert(tk.END, f"> EVA: {reply}\n\n", "eva")
    chat_area.yview(tk.END)


window = tk.Tk()
window.title("EVA // HOLOGRAM INTERFACE")
window.geometry("800x800")
window.configure(bg="#050510")

header = tk.Label(
    window,
    text="EVA AI CORE",
    font=("Orbitron", 24, "bold"),
    fg="#00f7ff",
    bg="#050510"
)
header.pack(pady=20)

sub_header = tk.Label(
    window,
    text="Neural Companion System Online",
    font=("Consolas", 10),
    fg="#00aaff",
    bg="#050510"
)
sub_header.pack()


status_frame = tk.Frame(window, bg="#0b0b1a", highlightbackground="#00f7ff", highlightthickness=1)
status_frame.pack(padx=40, pady=20, fill=tk.X)

rel_label = tk.Label(
    status_frame,
    text="RELATIONSHIP LINK STRENGTH",
    fg="#00f7ff",
    bg="#0b0b1a",
    font=("Consolas", 10)
)
rel_label.pack(anchor="w", padx=10, pady=(10,0))

progress = ttk.Progressbar(
    status_frame,
    length=600,
    maximum=4,
    value=memory["relationship_level"]
)
progress.pack(padx=10, pady=5)

mood_label = tk.Label(
    status_frame,
    text=f"EMOTIONAL STATE: {memory['mood'].upper()}",
    fg="#00ffaa",
    bg="#0b0b1a",
    font=("Consolas", 10)
)
mood_label.pack(pady=(0,10))


chat_area = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,
    bg="#0b0b1a",
    fg="#00f7ff",
    font=("Consolas", 12),
    insertbackground="#00f7ff",
    highlightbackground="#00f7ff",
    highlightthickness=1
)
chat_area.pack(padx=40, pady=20, fill=tk.BOTH, expand=True)

chat_area.tag_config("user", foreground="#00f7ff")
chat_area.tag_config("eva", foreground="#00ffaa")


input_frame = tk.Frame(window, bg="#050510")
input_frame.pack(padx=40, pady=20, fill=tk.X)

user_entry = tk.Entry(
    input_frame,
    bg="#0b0b1a",
    fg="#00f7ff",
    font=("Consolas", 12),
    insertbackground="#00f7ff",
    highlightbackground="#00f7ff",
    highlightthickness=1
)
user_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

send_button = tk.Button(
    input_frame,
    text="EXECUTE",
    command=send_message,
    bg="#00f7ff",
    fg="black",
    font=("Consolas", 11, "bold"),
    relief=tk.FLAT
)
send_button.pack(side=tk.RIGHT)

window.bind("<Return>", send_message)

window.mainloop()