# Needs opencv-python
# pip3 install opencv-python
# Resolution Reference: 
# 4K = 3840x2160
# 1080 = 1920x1080
# My configuration
# Camera 0 = USB HDMI to USB Camera Adapter
# Camera 1 = WebCam

import cv2 as cv2


def get_devices():
    is_working = True
    dev_port = 0
    while is_working:
        cameratest = cv2.VideoCapture(dev_port)
        if not cameratest.isOpened():
            is_working = False
            print("Port %s is not working." %dev_port)
        else:
            is_reading, img = cameratest.read()
            w = cameratest.get(3)
            h = cameratest.get(4)
            if is_reading: 
                print("Port %s is working and read images (%s x %s)" %(dev_port,h,w))
            else:
                print("Port %s is present but does not read (%s x %s)" %(dev_port,h,w))
        dev_port +=1
    return

def show_webcam(mirror=False,camnumber=0,width=1920,height=1080,desktopxloc=0,desktopyloc=0,windowname="Camera Shadow"):
    cam = cv2.VideoCapture(camnumber)   
    cam.set(3,width)
    cam.set(4,height)
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
        cv2.namedWindow(windowname,cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty(windowname,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.moveWindow(windowname,desktopxloc,desktopyloc)  # Adjust this for WHICH Monitor you need it on
        cv2.imshow(windowname,img)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    #get_devices()
    show_webcam()


if __name__ == '__main__':
    main()