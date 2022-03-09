#Needs xprintidle package

import subprocess

while True:
    idle = subprocess.check_output("xprintidle")
    if int(idle) >= 1200000: #Current time is 20 minutes measured in milliseconds
        subprocess.run(["shutdown", "-P", "now"])
