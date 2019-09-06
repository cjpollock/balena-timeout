import sys
import time
import os
sys.path.append("...")
import keyboard

print('timer started...')
timeoutTimer = 60 # Sets the initial timer. 60 = 60 minutes.
print('Starting session with %d minutes.'%timeoutTimer)

def on_press_reaction(e):
    global timeoutTimer
    timeoutTimer = 3 # Resets the timer for 3 minutes for every keyboard input.
    print('Keyboard input detected; session reset to %d minutes.'%timeoutTimer)

while timeoutTimer>0:
    global timeoutTimer
    keyboard.hook(on_press_reaction)
    time.sleep(60) # this is what sets the time in seconds. 60 = 1 minute.
    timeoutTimer -= 1 #subtracts 1 minute from the timer.
    print('Minutes remaining in session: %d'%timeoutTimer)
else:
    print("Restarting browser")
    os.system('curl --header "Content-Type:application/json" "$BALENA_SUPERVISOR_ADDRESS/v2/applications/$BALENA_APP_ID/restart-service?apikey=$BALENA_SUPERVISOR_API_KEY" -d \'{"serviceName": "chromium-kiosk"}\'')
    # In the previous line of code, change {"serviceName": "chromium-kiosk"} to the name of the container you want to restart.
    # Example: {"serviceName": "my-awesome-container"}