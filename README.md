# Using the Win Predictor
Run CardDetector.py to start the script.
- A window will open displaying the webcam image
- The terminal will prompt you to use "p" to take a picture of the community cards
    - Position the 5 community cards in frame and make sure the live card classification is correct before capturing the photo
    - The capture will register as successful as long as 5 cards were detected
    - The terminal window will relay the cards captured
- The Terminal will then prompt to similarly take picture of the hands
    - Position each 2 card hand in the frame and capture the picture of each hand separately
    - Similarly, the capture will register as successful as long as 2 cards were detected
    - The terminal window will relay the cards captured
    - Repeat this process as desired up to 10 times
    - The option to run the win prediction will become available after two hands have been captured
- After using "r" to run the win prediction, the winning hand will be returned via the terminal and the script and image window will close.

# Information from the Source Code Readme

## OpenCV-Playing-Card-Detector
This is a Python program that uses OpenCV to detect and identify playing cards from a PiCamera video feed on a Raspberry Pi. Check out the YouTube video that describes what it does and how it works:

https://www.youtube.com/watch?v=m-QPjO-2IkA

## Usage
Download this repository to a directory and run CardDetector.py from that directory. Cards need to be placed on a dark background for the detector to work. Press 'q' to end the program.

The program was originally designed to run on a Raspberry Pi with a Linux OS, but it can also be run on Windows 7/8/10. To run on Windows, download and install Anaconda (https://www.anaconda.com/download/, Python 3.6 version), launch Anaconda Prompt, and execute the program by launching IDLE (type "idle" and press ENTER in the prompt) and opening/running the CardDetector.py file in IDLE. The Anaconda environment comes with the opencv and numpy packages installed, so you don't need to install those yourself. If you are running this on Windows, you will also need to change the program to use a USB camera, as described below.

The program allows you to use either a PiCamera or a USB camera. If using a USB camera, change line 38 in CardDetector.py to:
```
videostream = VideoStream.VideoStream((IM_WIDTH,IM_HEIGHT),FRAME_RATE,2,0).start()
```

The card detector will work best if you use isolated rank and suit images generated from your own cards. To do this, run Rank_Suit_Isolator.py to take pictures of your cards. It will ask you to take a picture of an Ace, then a Two, and so on. Then, it will ask you to take a picture of one card from each of the suits (Spades, Diamonds, Clubs, Hearts). As you take pictures of the cards, the script will automatically isolate the rank or suit and save them in the Card_Imgs directory (overwriting the existing images).


## Files
CardDetector.py contains the main script

Cards.py has classes and functions that are used by CardDetector.py

PiVideoStream.py creates a video stream from the PiCamera, and is used by CardDetector.py

Rank_Suit_Isolator.py is a standalone script that can be used to isolate the rank and suit from a set of cards to create train images

Card_Imgs contains all the train images of the card ranks and suits

## Dependencies
Python 3.6

OpenCV-Python 3.2.0 and numpy 1.8.2:
See https://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/
for how to build and install OpenCV-Python on the Raspberry Pi

picamera library:
```
sudo apt-get update
sudo apt-get install python-picamera python3-picamera
```


