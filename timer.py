import time

my_time = int(input("Enter the Time in Seconds : "))

for x in range(my_time, -1, -1):
    
    hr = int(x / 3600)
    
    min = int((x % 3600) / 60)
   
    sec = x % 60
    
    print(f"{hr:02d} : {min:02d} : {sec:02d}")
    time.sleep(1)

print("TIME'S UP!!!")
