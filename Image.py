def OpenImage(path,openWindow=False,thread=False,gray=False):
    import cv2 as cv
    img = cv.imread(path, 0 if gray else 1)
    if openWindow:
        if thread:
            pass
        else:
            cv.imshow("image",img)
            cv.waitKey(0)
            cv.destroyAllWindows()
    else:
        return img

def OpenVideo(camera=0):
    import cv2
    return cv2.VideoCapture(camera)

def OpenVideoWithLink(link, color = 0, rotate = None, resizeX = 1, resizeY = 1):
    import cv2
    cap = cv2.VideoCapture(0)
    #link sample = "https://192.168.43.1:8080/video"
    address = link
    cap.open(address)
    while True:
        try:
            ret, frame=cap.read()
            #color sample = cv2.COLOR_BGR2BGRA or 0
            frame = cv2.cvtColor(frame, color)
            #rotate sample = cv2.ROTATE_90_COUNTERCLOCKWISE
            frame = cv2.rotate(frame,rotate)
            frame = cv2.resize(frame,None,fx=resizeX,fy=resizeY)
        except:
            print("error")
            

        if ret:
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1)

            #escape key for quit()
            if key == 27:
                cv2.destroyAllWindows()
                break
    cap.release()
    cv2.destroyAllWindows()