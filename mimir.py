#Needs xprintidle package

import subprocess

while True:
    idle = subprocess.check_output("xprintidle")
    if int(idle) >= 660000: #Current time needs to be measured
        subprocess.run(["shutdown", "-P", "now"])
