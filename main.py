import customtkinter as ctk
from tkinter import ttk
import time, datetime, csv, os

filename = ""
filecount = 0
date_str = datetime.datetime.today().strftime("%Y-%m-%d")

while True:
    filename = f"{date_str} notes {filecount if filecount != 0 else ""}.csv"
    if not os.path.exists(filename):
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Timestamp", "Team", "Project", "Issue", "Notes"])
        break

    filecount += 1

class Clock(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.container = ctk.CTkFrame(self, fg_color="#1E1E1E")
        self.container.pack(anchor="w", padx=10, pady=5)

        self.markers = ctk.CTkLabel(
            self.container, text="00:00:00", width=2, height=2, font=("Arial", 50)
        )
        self.markers.pack(side="left", padx=(10, 50))

        self.start_stop_frame = ctk.CTkFrame(self.container, fg_color="#1E1E1E")
        self.start_stop_frame.pack(side="left")

        self.start_button = ctk.CTkButton(
            self.start_stop_frame,
            width=50,
            height=50,
            fg_color="#C1C0C0",
            text_color="#1E1E1E",
            text="Start",
            command=self.start_clock,
        )
        self.start_button.pack(pady=5)

        self.stop_button = ctk.CTkButton(
            self.start_stop_frame,
            width=50,
            height=50,
            fg_color="#C1C0C0",
            text_color="#1E1E1E",
            text="Stop",
            command=self.stop_clock,
        )

        self.stop_button.pack(pady=5)

        self.reset_frame = ctk.CTkFrame(self.container, fg_color="#1E1E1E")
        self.reset_frame.pack(side="left", padx=(10, 0), pady=10)
        self.reset_button = ctk.CTkButton(
            self.reset_frame,
            width=50,
            height=110,
            fg_color="#C1C0C0",
            text_color="#1E1E1E",
            text="Reset",
            command=self.reset_clock,
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


class Journal(ctk.CTkFrame):
    def __init__(self, master, clock: Clock, **kwargs):
        super().__init__(master, **kwargs)
        self.container_1 = ctk.CTkFrame(self, fg_color="#1E1E1E")
        self.container_1.pack(anchor="w", expand="true", fill="x")
        self.container_2 = ctk.CTkFrame(self, fg_color="#1E1E1E")
        self.container_2.pack(anchor="w", expand="true", fill="x")

        self.clock = clock
        self.logs = []
        self.team_entry = ctk.CTkEntry(
            self.container_1, placeholder_text="team", width=125
        )
        self.team_entry.pack(side="left", fill="x", padx=5)

        self.project_entry = ctk.CTkEntry(
            self.container_1, placeholder_text="project", width=125
        )
        self.project_entry.pack(side="left", fill="x", padx=5)

        self.issue_entry = ctk.CTkEntry(
            self.container_1, placeholder_text="issue", width=125
        )
        self.issue_entry.pack(side="left", fill="x", padx=(5, 0))

        self.notes_entry = ctk.CTkEntry(self.container_2, placeholder_text="notes")
        self.notes_entry.pack(side="top", fill="both", expand="true", padx=5, pady=5)

        self.write_button = ctk.CTkButton(
            self.container_2,
            fg_color="#C1C0C0",
            text_color="#1E1E1E",
            text="Write",
            command=self.log_activity,
        )
        self.write_button.pack(fill="x", expand="true", padx=5, pady=5)

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

        with open(filename, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(activity_log)

class NotesView(ctk.CTkToplevel):
    def __init__(self, master, csv_file):
        super().__init__(master)
        self.title("CSV Table Viewer")
        self.csv_file = csv_file

        frame = ctk.CTkFrame(self)
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.tree = ttk.Treeview(frame)
        self.tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.load_csv(self.csv_file) 
        self.after(2000, self.auto_refresh_csv)

    def load_csv(self, file_path):
        try:
            with open(file_path, newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                headers = next(reader)
                self.tree["columns"] = headers
                self.tree["show"] = "headings"
                for i, header in enumerate(headers):
                    self.tree.heading(header, text=header)
                    if i == len(headers) - 1:
                        self.tree.column(header, anchor="w", width=250)
                    else:
                        self.tree.column(header, anchor="w", width=100)
                for row in reader:
                    self.tree.insert("", "end", values=row)
        except Exception as e:
            self.tree.insert("", "end", values=[f"Error: {e}"])

    def auto_refresh_csv(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.load_csv(self.csv_file)
        self.after(2000, self.auto_refresh_csv)


class Keepr(ctk.CTk):
    def __init__(self):
        super().__init__()
        window_width = 415
        window_height = 315
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = screen_width - window_width - 10  
        y = screen_height - window_height - 80 
        
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.title("Keepr")
        self.main_container = ctk.CTkFrame(self, fg_color="#1E1E1E")
        self.main_container.pack(fill="both", expand=True)
        self.options = ctk.CTkFrame(self.main_container, fg_color="#1E1E1E")
        self.options.pack(fill="both", side="top")
        
        self.notes_button = ctk.CTkButton(
            self.options, fg_color="#C1C0C0", text_color="#1E1E1E", text="Notes", width=30, height=10, command=self.open_notes
        )
        self.notes_button.pack(side="left", padx=5, pady=5)
        self.clock_frame = Clock(master=self.main_container, fg_color="#1E1E1E")
        self.journal_frame = Journal(
            master=self.main_container, clock=self.clock_frame, fg_color="#1E1E1E"
        )
        self.clock_frame.pack(fill="x", padx=5, pady=5)
        self.journal_frame.pack(fill="x", padx=5, pady=5)

    def open_notes(self):
        viewer = NotesView(self, filename)
        self.update_idletasks() 
        app_x = self.winfo_x()
        app_y = self.winfo_y()
        viewer_width = 615
        viewer_height = 300
        new_x = max(0, app_x - viewer_width - 10)  
        new_y = app_y
        viewer.geometry(f"{viewer_width}x{viewer_height}+{new_x}+{new_y}")

app = Keepr()
app.mainloop()

