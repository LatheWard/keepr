import customtkinter
import time

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Keepr")
        self.geometry("400x150")
        self.active = False
        self.logs = []
        self.start_time = None

        self.text = customtkinter.CTkLabel(self, text="00:00:00", width=30, height=30, font=("Arial", 80))
        self.text.pack()

        self.start_button = customtkinter.CTkButton(self, text="Start", command=self.start_clock)
        self.start_button.pack(side="left", expand=1)

        self.stop_button = customtkinter.CTkButton(self, text="Stop", command=self.stop_clock)
        self.stop_button.pack(side="left", expand=1)

        self.update_label()  

    def start_clock(self):
        self.active = True
        self.start_time = time.perf_counter()

    def stop_clock(self):
        self.active = False
        elapsed = time.perf_counter() - self.start_time

    def log_activity():
        team = input("Team?: ")
        project = input("Project?: ")
        ticket = input("Issue/Ticket?: ")
        notes = input("Notes?:  ")
        activity_log = {
            "Timestamp": time.strftime("%H:%M:%S", time.gmtime(elapsed)),
            "Team": team,
            "Project": project,
            "Issue/Ticket": ticket,
            "Notes": notes,
        }
        self.logs.append(activity_log)
    
    def update_label(self):
        if self.active and self.start_time is not None:
            elapsed = time.perf_counter() - self.start_time
            formatted = time.strftime("%H:%M:%S", time.gmtime(elapsed))
            self.text.configure(text=formatted)
        self.after(1000, self.update_label)  

app = App()
app.mainloop()

