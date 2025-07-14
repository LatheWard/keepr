# Keepr 
### A time-keeping-and-note-scribing display tool.
#### (Version 1 coming soon!)

Keepr is meant to be simple, free, and dedicated to 
these 2 purposes: acting as a display clock for working hours
and writing organized notes paired accordingly with time stamps.

I plan on continually updating this to be as available as possible across operating systems.

This probably could have been written in C.

## Using the UI

### The clock
Keepr will run and display within a small window designated for one of the lower
corners of the screen. 3 options will be available upon startup: Start, Pause, and
Reset.

**Start** - Start the clock for the day.
**Pause** - Pause the clock. Note that if you're viewing the clock in *real mode*,
only the internal timer will pause. You should still be able to view the current time.
**Reset** - Restart the clock. **This action will also clear the stored notes available for export.**

### The notes
On the bottom row of the window, the notes are divided into 4 optional input fields:
Team, Project, Issue/Ticket, and Notes. The stored notes can be exported at any time 
with the *Export* option in the lowest right corner. This can be exported as a CSV file
with an additional timestamp field at the front of each row.

## Using the command line flags (Linux)
```
--help               Show this screen
--r, --realmode      Set clock for system time rather than expired time.
```


