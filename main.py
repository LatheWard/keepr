import customtkinter
import time, csv

class Clock(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.container = customtkinter.CTkFrame(self, fg_color="#1E1E1E")
        self.container.pack(anchor="w", padx=10, pady=5)

        self.markers = customtkinter.CTkLabel(
            self.container, text="00:00:00", width=2, height=2, font=("Arial", 50)
        )
        self.markers.pack(side="left", padx=(10, 50))

        self.start_stop_frame = customtkinter.CTkFrame(self.container, fg_color="#1E1E1E")
        self.start_stop_frame.pack(side="left")

        self.start_button = customtkinter.CTkButton(
            self.start_stop_frame, width=50, height=50, text="Start", command=self.start_clock
        )
        self.start_button.pack(pady=5)

        self.stop_button = customtkinter.CTkButton(
            self.start_stop_frame, width=50, height=50, text="Stop", command=self.stop_clock
        )
        
        self.stop_button.pack(pady=5)
        
        self.reset_frame = customtkinter.CTkFrame(self.container, fg_color="#1E1E1E")
        self.reset_frame.pack(side="left", padx=(10, 0), pady=10)
        self.reset_button = customtkinter.CTkButton(
            self.reset_frame, width=50, height=110, text="Reset", command=self.reset_clock
        )

        self.reset_button.pack(pady=5)
        self.active = False
        self.start_time = 0
        self.elapsed_time = 0
        
    def start_clock(self):
        if not self.active:
            self.start_time = time.perf_counter()
            self.active = True
        self.update_label()

    def stop_clock(self):
        if self.active:
            self.active = False
            self.elapsed_time += time.perf_counter() - self.start_time
        self.update_label()

    def reset_clock(self):
        self.active = False
        self.elapsed_time = 0
        self.start_time = None
        self.markers.configure(text="00:00:00")

    def update_label(self):
        if self.active:
            elapsed = (time.perf_counter() - self.start_time) + self.elapsed_time
        else:
            elapsed = self.elapsed_time
        formatted = time.strftime("%H:%M:%S", time.gmtime(elapsed))
        self.markers.configure(text=formatted)
        self.after(1000, self.update_label)


class Journal(customtkinter.CTkFrame):
    def __init__(self, master, clock: Clock, **kwargs):
        super().__init__(master, **kwargs)

        self.container_1 = customtkinter.CTkFrame(self, fg_color="#1E1E1E")
        self.container_1.pack(anchor="w", expand="true", fill="x")
        self.container_2 = customtkinter.CTkFrame(self, fg_color="#1E1E1E")
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
        self.issue_entry.pack(side="left", fill="x", padx=(5, 0))

        self.notes_entry = customtkinter.CTkEntry(
            self.container_2, placeholder_text="notes" 
        )
        self.notes_entry.pack(side="top", fill="both", expand="true", padx=5, pady=5) 

        self.write_button = customtkinter.CTkButton(
            self.container_2, text="Write", command=self.log_activity
        )
        self.write_button.pack(fill="x", expand="true", padx=5, pady=5)

        self.export_button = customtkinter.CTkButton(
            self.container_2, text="Export to file", command=self.export_to_file
        )
        self.export_button.pack(side="bottom", fill="x", expand="true", padx=5, pady=5)
    def log_activity(self):
        activity_log = [
            self.clock.markers.cget("text"),
            self.team_entry.get(),
            self.project_entry.get(),
            self.issue_entry.get(),
            self.notes_entry.get(),
        ]
        self.logs.append(activity_log)
        self.team_entry.delete(0, "end"),
        self.project_entry.delete(0, "end"),
        self.issue_entry.delete(0, "end"),
        self.notes_entry.delete(0, "end"),

    def export_to_file(self):
        with open('notes.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Timestamp","Team","Project","Issue","Notes"])
            writer.writerows(self.logs)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.main_container = customtkinter.CTkFrame(self, fg_color="#1E1E1E")
        self.main_container.pack(fill="both", expand=True)
        self.title("Keepr")
        self.geometry("415x315")
        
        self.clock_frame = Clock(master=self.main_container, fg_color="#1E1E1E")
        self.journal_frame = Journal(master=self.main_container, clock=self.clock_frame, fg_color="#1E1E1E")
        self.clock_frame.pack(fill="x", padx=5, pady=5)
        self.journal_frame.pack(fill="x", padx=5, pady=5)


app = App()
app.mainloop()
