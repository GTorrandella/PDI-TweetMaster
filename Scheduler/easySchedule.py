import time
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from Manager.manager import Manager

while True:
	print("Llamada a Manager")
	Manager().fetchCampaings()
	#schedule.run_all(delay_seconds=5)
	time.sleep(120) #Cada 2 minutos llama al manager.
