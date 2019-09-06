import sys
import time
import os
sys.path.append("...")
import keyboard

print('timer started...')
timeoutTimer = 60
print('Starting session with %d minutes.'%timeoutTimer)

keyboard.write('num_lock')

def on_press_reaction(e):
    global timeoutTimer
    timeoutTimer = 3
    print('Keyboard input detected; session reset to %d minutes.'%timeoutTimer)

while timeoutTimer>0:
    global timeoutTimer
    keyboard.hook(on_press_reaction)
    time.sleep(60)
    timeoutTimer -= 1
    print('Minutes remaining in session: %d'%timeoutTimer)
else:
    print("Restarting browser")
    os.system('curl --header "Content-Type:application/json" "$BALENA_SUPERVISOR_ADDRESS/v2/applications/$BALENA_APP_ID/restart-service?apikey=$BALENA_SUPERVISOR_API_KEY" -d \'{"serviceName": "chromium-kiosk"}\'')
    timeoutError = 60
    #time.sleep(10)
    #print("Restarting keyboard")
    #os.system('curl --header "Content-Type:application/json" "$BALENA_SUPERVISOR_ADDRESS/v2/applications/$BALENA_APP_ID/restart-service?apikey=$BALENA_SUPERVISOR_API_KEY" -d \'{"serviceName": "keyboard"}\'')