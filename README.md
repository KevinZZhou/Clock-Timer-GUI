# Clock-Timer-GUI

## Description
This project is a clock and timer GUI with 5 modes: 
1. Digital clock
2. Analog clock
3. Stopwatch
4. Timer
5. [Pomodoro](https://en.wikipedia.org/wiki/Pomodoro_Technique) timer

## Modes
#### Digital Clock
In this mode, you can check the time and date.  The clock defaults to your device's local timezone, but you can select any timezone: just select one from the dropdown box.
![Digital clock](/files/images/readme-images/digital-mode.png)

#### Analog Clock
In this mode, you can check the time and date with an analog clock.  Like the digital clock, many timezones can be selected.
![Analog clock](/files/images/readme-images/analog-mode.png)

#### Stopwatch
In this mode, you can measure how much time elapses in a given period.  Just click the Start button to start the stopwatch and click the Stop button to stop it.  Clicking the Reset button will set the stopwatch back to 0.
![Stopwatch](/files/images/readme-images/stopwatch-mode.png)

#### Timer
In this mode, you can measure a specific time interval.  To do so, input the desired number of hours, minutes, and seconds.
![Timer](/files/images/readme-images/timer-mode.png)

#### Pomodoro Timer
In this mode, you can use a Pomodoro timer, which will help you study with scheduled study and short/long break periods.
![Pomodoro timer](/files/images/readme-images/pomodoro-mode.png)

## Installation/Setup
First, make sure that you have Python installed on your device.  This project uses Python 3.9.1, but should work for Python 3.x.
To avoid conflicting dependencies, creating a virtual environment, either with [pip](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/) or [Anaconda](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/), is advised, but not strictly required.

Download the files onto your system, either by downloading it directly in the browser or entering the following into the command line:
```sh
$ git clone https://github.com/KevinZZhou/Clock-Timer-GUI.git
```

To download the required packages, activate the virtual environment (if you are using one), navigate to the project directory, and enter the following:

pip:
```sh
$ pip install -r requirements.txt
```
Anaconda:
```sh
$ conda install --file requirements.txt
```

After this, run MainApp.py within an IDE or navigate to the src folder and enter the following:
```sh
$ python MainApp.py
```

## Technologies Used
This GUI was coded in Python 3.9.1 using Tkinter.
Packages that were used in the project can be found in requirements.txt.