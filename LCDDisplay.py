#jackson Vaughn
#Program to display data on the LCD screen
#!/usr/bin/env python3

#Imports
import time 
import LCDDriver as LCD    
import GetPrice as Price
from datetime import datetime

LCD.setup()
#Clear screen 
LCD.clear()

try:
	while True:
		
		#the top of the screen should be scrolling stock prices
		
		#This is for testing, in the future we will use a list from db
		ticker = 'VOO'
		data = Price.GetCurrentPrice(ticker)
		
		Display = f'{ticker}: {data[0]} {data[1]}'
		
		LCD.write(Display,LCD.LINE_1)
		#Display date & time at the bottom of the screen
		now = datetime.now()
		Curdate = str(now.strftime("%m-%d %H:%M:%S"))
		
		LCD.write(Curdate,LCD.LINE_2)
		time.sleep(0.5)



		#LCD.clear()

except KeyboardInterrupt:
	LCD.clear()
	LCD.write("Good bye!",LCD.LINE_1)
	time.sleep(0.5)
	LCD.clear()
	print("exit")
