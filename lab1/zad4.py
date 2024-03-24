from datetime import datetime


data = datetime.strptime("15-03-2024", "%d-%m-%Y")
data_now=datetime.now()

delta_time=data-data_now
print(delta_time)