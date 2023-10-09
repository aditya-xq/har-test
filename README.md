# SmartWatch Activity Simulator 🕰️

Hello and welcome to the **SmartWatch Activity Simulator**! This fun little test project simulates the data generation of a smartwatch's accelerometer and gyroscope. But that's not all; it also predicts human activity based on this data! 

Ever wondered how your smartwatch knows if you're walking, running, or just chilling? Let's dive into the magical world of smartwatch data, and find out! 🏃‍♀️🚶‍♂️🪑

## How it works:
1. **SmartWatchSimulator.py:** This file contains a class `Smartwatch` which can generate random accelerometer and gyroscope data, simulating the kind of data a real smartwatch might capture.

2. **App.py:** This is where the action happens! It uses the `Smartwatch` class to generate data and then predicts the activity using a simple heuristic. The results are printed out for you to see.

## How to use:
1. Run the `App.py` script.
2. Watch the console! You'll see generated data from the smartwatch's sensors and then a prediction of the human activity based on that data.
3. It will keep running, generating a new prediction every second. If you want to stop, simply press `CTRL + C` or close the console.

## Future Directions:
🚀 **Machine Learning Integration:** Instead of using simple heuristics, we can integrate a machine learning model to predict activities based on the data for even more accurate predictions!

🎨 **GUI Implementation:** A simple graphical user interface could be added to visualize the data and predictions in a more user-friendly manner.

🌍 **Additional Sensors:** We can simulate other sensors such as heart rate monitors or GPS to generate even richer datasets.

🕵️ **Anomaly Detection:** Beyond just predicting activities, we can detect unusual patterns in the data, potentially useful for health monitoring or fall detection.

## Conclusion:
This project is ideal for anyone new to programming and wanting a sneak peek into how smartwatch data works or for those wanting to experiment with their own activity prediction algorithms.

**Happy Coding!** 🚀👩‍💻👨‍💻🎉
