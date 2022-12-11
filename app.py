import time
from SmartWatchSimulator import Smartwatch
import numpy as np

def predict_activity(accelerometer, gyroscope):
    # Use the accelerometer and gyroscope data to predict the human activity
    # The actual implementation of this will depend on the specific machine learning model used
    # For this example, we will simply use a simple heuristic to predict the activity
    
    # If the accelerometer data shows large movement, we will predict the activity as "walking" or "running"
    if max(accelerometer) > 0.5:
        return "walking" if np.mean(accelerometer) < 0 else "running"
    
    # If the gyroscope data shows large rotation, we will predict the activity as "turning"
    if max(gyroscope) > 1:
        return "turning"
    
    # Otherwise, we will predict the activity as "sitting"
    return "sitting"

watch = Smartwatch()
while True:
    watch.generate_data()
    print(f'Generated data: \n{watch.accelerometer}\n {watch.gyroscope}')
    activity = predict_activity(watch.accelerometer, watch.gyroscope)
    print(f'Activity: {activity}')
    time.sleep(1)
