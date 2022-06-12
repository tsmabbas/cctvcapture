import cv2
import time


def minimizeWindow():
    #importing modules to add minimize features in app
    import win32gui
    import win32con
    window = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(window,win32con.SW_MINIMIZE)


def cctv():
    video = cv2.VideoCapture(0)
    video.set(3, 640)
    video.set(4, 480)
    width = video.get(3)
    height = video.get(4)
    print("Video resolution is set to  ", width,  ' x ', height)
    print("Help-- \n1.Press Esc Key to exit. \n2.press m to minimize")
    fourcc = cv2.videoWriter_fourcc(*'XVID')
    date_time = time.strftime("recording %H-%M-%d -%m -%y")
    output = cv2.videoWriter('footage/' + datetime + ' .mp4')
    while video.isOpened():