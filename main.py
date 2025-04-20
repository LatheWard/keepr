import customtkinter
import time


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.active = False
        self.logs = []
        self.title("Keepr")
        self.geometry("400x150")
        self.button = customtkinter.CTkButton(self, text="testing123")
        self.button.grid(row=0, column=0, padx=20, pady=20)
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

        def clock():
            active = not active
            start_time = time.perf_counter()
            end_time, elapsed = 0, 0
            while active:
                if button_press_off:
                    end_time = time.perf_counter()
                    elapsed = end_time - start_time
                    # print(time.strftime("%H:%M:%S", time.gmtime(elapsed)), "Log: ", logs)
                else:
                    end_time = time.perf_counter()
                    elapsed = end_time - start_time
                    log_activity()
                    # print(time.strftime("%H:%M:%S", time.gmtime(elapsed)), "Last Log: ", log)
    

app = App()
app.mainloop
