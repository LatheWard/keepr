import time

## Expected Output
## Timestamp(?), Team, Project, Issue/Ticket Number, Notes

def clock():
    print("Press enter to start")
    input()
    start_time = time.perf_counter()

    print("Press enter to end")
    input()
    end_time = time.perf_counter()
    elapsed = end_time - start_time
    print(time.strftime("%H:%M:%S", time.gmtime(elapsed)))
    return None

if __name__ == "__main__":
    clock()