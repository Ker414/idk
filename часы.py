import time 
import os

while 1 < 2:
    t = time.localtime(time.time())
    localtime = time.asctime(t)
    str = time.asctime(t)
 
    print(str)
    
    time.sleep(1)
    
    os.system('cls' if os.name == 'nt' else 'clear')