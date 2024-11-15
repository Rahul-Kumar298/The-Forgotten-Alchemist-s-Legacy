import time
def countdown_timer(seconds):
    total_seconds = seconds
    while total_seconds > 0:
        # Calculate minutes and seconds
        mins, secs = divmod(total_seconds, 60)
        
        # Format the time as MM:SS
        timer = f"{mins:02}:{secs:02}"
        
        # Print the timer (overwrite previous line)
        print(timer, end='\r')
        
        # Wait for 1 second
        time.sleep(1)
        
        # Decrease the total seconds by 1
        total_seconds -= 1
    
    # Print final message
    print("00:00")

def sleep(sec):
    time.sleep(sec)