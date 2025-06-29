import customtkinter
import time

class Clock(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.markers = customtkinter.CTkLabel(
            self, text="00:00:00", width=5, height=5, font=("Arial", 50)
        )
        self.markers.pack()

        self.start_button = customtkinter.CTkButton(
            self, text="Start", command=self.start_clock
        )
        self.start_button.pack(side="left")

        self.stop_button = customtkinter.CTkButton(
            self, text="Stop", command=self.stop_clock
        )
        self.stop_button.pack(side="left")

        self.timestamp_entry = customtkinter.CTkEntry(
            self, placeholder_text="timestamp"
        )
        self.timestamp_entry.pack(side="left")
        self.active = False
        self.start_time = None

        self.update_label()

    def start_clock(self):
        self.active = True
        self.start_time = time.perf_counter()

    def stop_clock(self):
        self.active = False
        elapsed = time.perf_counter() - self.start_time

    def update_label(self):
        if self.active and self.start_time is not None:
            elapsed = time.perf_counter() - self.start_time
            formatted = time.strftime("%H:%M:%S", time.gmtime(elapsed))
            self.text.configure(text=formatted)
        self.after(1000, self.update_label)


class Journal(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.logs = []
        self.team_entry = customtkinter.CTkEntry(self, placeholder_text="team")
        self.team_entry.pack(side="left")

        self.project_entry = customtkinter.CTkEntry(self, placeholder_text="project")
        self.project_entry.pack(side="left")

        self.issue_entry = customtkinter.CTkEntry(self, placeholder_text="issue")
        self.issue_entry.pack(side="left")

        self.notes_entry = customtkinter.CTkEntry(self, placeholder_text="notes")
        self.notes_entry.pack(side="left")

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


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Keepr")
        self.geometry("400x150")
        self.clock_frame = Clock(master=self)
        self.clock_frame.grid(row=0, column=0, padx=10, pady=20, sticky="nsew")
        self.journal_frame = Journal(master=self)
        self.journal_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")


app = App()
app.mainloop()
