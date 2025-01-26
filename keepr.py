import time

## Timestamp, Team, Project, Issue/Ticket Number, Notes
def main():
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
            if i2 == "":
                end_time = time.perf_counter()
                elapsed = end_time - start_time
                print(time.strftime("%H:%M:%S", time.gmtime(elapsed)), "Log: ", logs)
                active = False
            else:
                end_time = time.perf_counter()
                elapsed = end_time - start_time
                log = log_activity(time.strftime("%H:%M:%S", time.gmtime(elapsed)))
                logs.append(log)
                print(time.strftime("%H:%M:%S", time.gmtime(elapsed)), "Last Log: ", log)
    clock()        

if __name__ == "__main__":
    main()