#Needs xprintidle package

import subprocess
import time

# # # # # # # # # # 

def usrtimefn(): #Usr input for time
    global timetype
    time = input("Select (Seconds 's', Minutes 'm'): ")
    if time == "s":
        timetype = 1000
    elif time == "m":
        timetype = 60000
    else:
        print("Non valid type")
        usrtimefn()
    global usrtime
    usrtime = int(input("Time till shutdown: "))
    print("Shuting down in " + str(usrtime) + " " + str(time))
    mainloop()

# # # # # # # # # # # # # # # # # # # # # # # # # # # #

def mainloop(): #Main loop function
    while True:
        idle = subprocess.check_output("xprintidle")
        if int(idle) >= usrtime*timetype: #Time is defined here
            subprocess.run(["shutdown", "-P", "now"])
        time.sleep(3) #Precision

usrtimefn()
