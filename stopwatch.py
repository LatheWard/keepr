import time

## Expected Output
## Timestamp(?), Team, Project, Issue/Ticket Number, Notes


def main():
    counter = 0
    def startDay():
        global counter
        for i in range(10):
            # tt = datetime.fromtimestamp(counter)
            display_stamp = time.strftime("%H:%M:%S", time.gmtime(counter))
            display=display_stamp
            print(display)
            counter += 1
            time.sleep(1)
        return None 
    is_starting = input("Ready?")
    if is_starting == 'Y':
        print("Starting....")
        startDay()
    return None

main()