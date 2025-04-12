import kivy

kivy.require("2.3.1")
import time
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.config import Config


class RunScreen(Widget):
    pass


class KeeprApp(App):
    Config.set("graphics", "width", "400")
    Config.set("graphics", "height", "150")

    def build(self):
        return RunScreen()

    def log_activity(time):
        team = input("Team?: ")
        project = input("Project?: ")
        ticket = input("Issue/Ticket?: ")
        notes = input("Notes?:  ")
        activity_log = {
            "Timestamp": time,
            "Team": team,
            "Project": project,
            "Issue/Ticket": ticket,
            "Notes": notes,
        }
        return activity_log

    def clock():
        active = True
        logs = []
        start_time = time.perf_counter()
        end_time, elapsed = 0, 0
        while active:
            i2 = input("Enter note or end?:")
            if button_press_off:
                end_time = time.perf_counter()
                elapsed = end_time - start_time
                # print(time.strftime("%H:%M:%S", time.gmtime(elapsed)), "Log: ", logs)
                active = False
            else:
                end_time = time.perf_counter()
                elapsed = end_time - start_time
                log = log_activity(time.strftime("%H:%M:%S", time.gmtime(elapsed)))
                logs.append(log)
                # print(time.strftime("%H:%M:%S", time.gmtime(elapsed)), "Last Log: ", log)


if __name__ == "__main__":
    KeeprApp().run()
