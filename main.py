import customtkinter
import time


class Clock(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.container = customtkinter.CTkFrame(self)
        self.container.pack(anchor="w", padx=10, pady=10)

        self.markers = customtkinter.CTkLabel(
            self.container, text="00:00:00", width=2, height=2, font=("Arial", 60)
        )
        self.markers.pack(side="left", padx=(0, 70))

        self.button_frame = customtkinter.CTkFrame(self.container)
        self.button_frame.pack(side="left")

        self.start_button = customtkinter.CTkButton(
            self.button_frame, width=50, height=50, text="Start", command=self.start_clock
        )
        self.start_button.pack(pady=5)

        self.stop_button = customtkinter.CTkButton(
            self.button_frame, width=50, height=50, text="Stop", command=self.stop_clock
        )
        
        self.stop_button.pack(pady=5)

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
            self.markers.configure(text=formatted)
        self.after(1000, self.update_label)


class Journal(customtkinter.CTkFrame):
    def __init__(self, master, clock: Clock, **kwargs):
        super().__init__(master, **kwargs)

        self.container_1 = customtkinter.CTkFrame(self)
        self.container_1.pack(anchor="w", expand="true", fill="x")
        self.container_2 = customtkinter.CTkFrame(self)
        self.container_2.pack(anchor="w", expand="true", fill="x")

        self.clock = clock
        self.logs = []
        self.team_entry = customtkinter.CTkEntry(
            self.container_1, placeholder_text="team", width=125
        )
        self.team_entry.pack(side="left", fill="x", padx=5)

        self.project_entry = customtkinter.CTkEntry(
            self.container_1, placeholder_text="project", width=125
        )
        self.project_entry.pack(side="left", fill="x", padx=5)

        self.issue_entry = customtkinter.CTkEntry(
            self.container_1, placeholder_text="issue", width=125
        )
        self.issue_entry.pack(side="left", fill="x", padx=5)

        self.notes_entry = customtkinter.CTkEntry(
            self.container_2, placeholder_text="notes" 
        )
        self.notes_entry.pack(side="top", fill="both", expand="true", padx=5, pady=5) 

        self.write_button = customtkinter.CTkButton(
            self.container_2, text="Write", command=self.log_activity
        )
        self.write_button.pack(side="bottom", fill="x", expand="true", padx=5, pady=5)

    def log_activity(self):
        activity_log = [
            self.clock.markers.cget("text"),
            self.team_entry.get(),
            self.project_entry.get(),
            self.issue_entry.get(),
            self.notes_entry.get(),
        ]
        self.logs.append(activity_log)
        print(self.logs)
        self.team_entry.delete(0),
        self.project_entry.delete(0),
        self.issue_entry.delete(0),
        self.notes_entry.delete(0),


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.main_container = customtkinter.CTkFrame(self)
        self.main_container.pack(fill="both", expand=True)
        self.title("Keepr")
        self.geometry("425x275")
        
        self.clock_frame = Clock(master=self.main_container)
        self.journal_frame = Journal(master=self.main_container, clock=self.clock_frame)
        self.clock_frame.pack(fill="x", padx=10, pady=5)
        self.journal_frame.pack(fill="x", padx=10, pady=5)


app = App()
app.mainloop()
