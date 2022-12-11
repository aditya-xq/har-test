import time
import random

class Smartwatch:
    def __init__(self):
        self.accelerometer = [0, 0, 0]
        self.gyroscope = [0, 0, 0]
    
    def generate_data(self):
        # Generate random data for the accelerometer and gyroscope
        self.accelerometer = [random.uniform(-1, 1) for _ in range(3)]
        self.gyroscope = [random.uniform(-1, 1) for _ in range(3)]

# watch = Smartwatch()
# while True:
#     watch.generate_data()
#     print(f'Accelerometer: {watch.accelerometer}')
#     print(f'Gyroscope: {watch.gyroscope}')
#     time.sleep(1)
