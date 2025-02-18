import json
import os
import tkinter as tk
from tkinter import messagebox


class nLoader:
    def __init__(self):
        self.mods = []

    def load_mod(self, mod_path):
        try:
            with open(os.path.join(mod_path, "info.json"), "r", encoding="utf-8") as f:
                mod_info = json.load(f)
                print(f"load.mod: {mod_info['name']} v{mod_info['version']}")

            with open(os.path.join(mod_path, "script.py"), "r", encoding="utf-8") as f:
                script = f.read()
                exec(script, globals())

            self.mods.append(mod_path)
            print(f"Mod {mod_path} is loaded sucsessfully!")
            return f"Mod {mod_info['name']} is loaded!"
        except Exception as e:
            print(f"load.mod Exception: {e}")
            return f"Mod load error: {e}"


class Launcher:
    def __init__(self, root):
        self.root = root
        self.root.title("Retro Future Launcher - Processing nLoader")
        self.root.geometry("400x300")

        self.loader = nLoader()

        self.label = tk.Label(root, text="Retro Future Launcher", font=("Arial", 16))
        self.label.pack(pady=10)

        self.load_button = tk.Button(root, text="Load mod", command=self.load_mod)
        self.load_button.pack(pady=10)

        self.status_label = tk.Label(root, text="Click the button to load the mod.", wraplength=350)
        self.status_label.pack(pady=10)

    def load_mod(self):
        result = self.loader.load_mod("mods/example_mod")
        self.status_label.config(text=result)
        messagebox.showinfo("Result:", result)


if __name__ == "__main__":
    root = tk.Tk()
    app = Launcher(root)
    root.mainloop()