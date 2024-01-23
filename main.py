import tkinter as tk
from datetime import datetime
import platform

class TypingSpeedTestApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed Test")

        self.text_to_type = "A gem cannot be polished without friction, nor a man perfected without trials. 'Seneca'"
        self.current_input = tk.StringVar()
        self.start_time = None

        self.setup_ui()

    def setup_ui(self):
        self.info_label = tk.Label(self.master, text="Type the following text as quickly as possible, then hit enter "
                                                     "<return>:")
        self.info_label.pack(pady=10)

        self.text_label = tk.Label(self.master, text=self.text_to_type)
        self.text_label.pack()

        self.entry = tk.Entry(self.master, width=65, textvariable=self.current_input)
        self.entry.pack(pady=10)

        self.start_button = tk.Button(self.master, text="Start Typing Test", command=self.start_typing_test)
        self.start_button.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack(pady=10)

        if platform.system() == 'Windows':
            self.entry.bind('<Control-c>', self.disable_copy_paste)
            self.entry.bind('<Control-v>', self.disable_copy_paste)
        elif platform.system() == 'Darwin':
            self.entry.bind('<Command-c>', self.disable_copy_paste)
            self.entry.bind('<Command-v>', self.disable_copy_paste)

    def start_typing_test(self):
        self.start_time = datetime.now()
        self.start_button["state"] = tk.DISABLED
        self.entry.bind("<Return>", self.check_typing)

    def check_typing(self, event):
        end_time = datetime.now()
        typed_text = self.current_input.get()

        if typed_text == self.text_to_type:
            time_taken = end_time - self.start_time
            typing_speed = len(self.text_to_type) / (time_taken.total_seconds() / 60)
            self.result_label.config(text=f"Typing speed: {typing_speed:.2f} words per minute")
        else:
            self.result_label.config(text="Incorrect! Please try again.")

        self.start_button["state"] = tk.NORMAL
        self.entry.unbind("<Return>")
        self.current_input.set("")

    def disable_copy_paste(self, event):
        return 'break'


def main():
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
