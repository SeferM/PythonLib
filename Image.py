from os import error, truncate


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