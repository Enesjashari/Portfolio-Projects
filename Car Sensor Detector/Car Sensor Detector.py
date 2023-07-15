#Importing nessesary modules
import time
import winsound
import colorama


while True:
    #Real Time Distance
    sensor_input = int(input('Distance: '))

    #Beep Distance : 1m - 80cm
    if sensor_input <= 100 and sensor_input >= 80:
        y = 0
        while y < 8:
            time.sleep(0.9)
            winsound.Beep(1000 , 100)
            print(colorama.Fore.LIGHTGREEN_EX+'Parking Alert!!!')
            y += 1
    #Beep Distance : 80cm - 60cm
    elif sensor_input <= 79 and sensor_input >= 60:
        y = 0
        while y < 8:
            time.sleep(0.5)
            winsound.Beep(1000 , 50)
            print(colorama.Fore.YELLOW+'Parking Alert!!!')
            y += 1
    #Beep Distance : 60cm - 50cm
    elif sensor_input <= 59 and sensor_input >= 50:
        y = 0
        while y < 8:
            time.sleep(0.3)
            winsound.Beep(1000 , 50)
            print(colorama.Fore.RED+'Parking Alert!!!')
            y += 1
    #Beep Distance : Below 50cm
    elif sensor_input <= 49:
        y = 0
        while y < 3:
            winsound.Beep(1000 , 3000)
            print(colorama.Fore.LIGHTRED_EX+'Parking Alert!!!')
            y += 1
        break
    else:
        pass