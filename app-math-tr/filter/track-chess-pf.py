import sys
import cv
from numpy import *
from K import *
from PF import *

def proj_board(im, xl, yl, z):
    color = cv.CV_RGB(0, 255, 0)
    image_size = (im.width, im.height)
    for x in arange(xl-9, xl+9, 0.5):
        for y in arange(yl-9, yl+9, 0.5):
            X = array([x, y, z])
            q = dot(K, X)
            q = [int(q[0]/q[2]), int(q[1]/q[2])]
            cv.Set2D(im, im.height-q[1], q[0], color)

def detect(image):
    image_size = cv.GetSize(image)
 
    # create grayscale version
    grayscale = cv.CreateImage(image_size, 8, 1)
    cv.CvtColor(image, grayscale, cv.CV_BGR2GRAY)
    storage = cv.CreateMemStorage(0)
    
    im = cv.CreateImage (image_size, 8, 3)    
    
    status, corners = cv.FindChessboardCorners( grayscale, (dim,dim)) 
    if status: 
        cv.DrawChessboardCorners( image, (dim,dim), corners, status)
        is_x = [p[0] for p in corners]
        is_y = [p[1] for p in corners]
        return is_x, is_y
    return [], []

def show_data(image, mu_x):
    line_type = cv.CV_AA
    pt1 =  (30, 400)
    font = cv.InitFont (cv.CV_FONT_HERSHEY_SIMPLEX, 
                        0.8, 0.1, 0, 1, cv.CV_AA)
    cv.PutText (image, "Particle Filter " + str(mu_x), pt1
                , font, cv.CV_RGB(255,255,0))


if __name__ == "__main__":

    snap_no = 0
    frame_no = 0
    
    # create windows
    cv.NamedWindow('Camera')
 
    # create capture device
    device = 0 # assume we want first device

    capture = cv.CreateFileCapture (sys.argv[1])
    dim = 3
    forward_step = -2.

    pts = dim * dim
    mid = int(pts / 2)
    
    cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH, 640)
    cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT, 480)    
 
    # check if capture device is OK
    if not capture:
        print "Error opening capture device"
        sys.exit(1)
        
    pf = PF(K, 200)
    
    frame = cv.QueryFrame(capture)        
    proj_board(frame, 1, 1, 160)
    cv.ShowImage('Camera', frame)
        
    while 1:        
        frame_no += 1
        frame = cv.QueryFrame(capture)        
            
        image_size = cv.GetSize(frame)
        if frame is None:
            break
        
        is_x, is_y = detect(frame)
        
        if len(is_x) > 0: 
            pf.update(array([is_x[5], frame.height-is_y[5], 1.]))
            mu_x = pf.average()
            proj_board(frame, mu_x[0], mu_x[1], mu_x[2])
            show_data(frame, mu_x)
                
        # display webcam image
        cv.ShowImage('Camera', frame)
                
        if snap_no == 12: break
        if frame_no % 10 == 0:
            cv.SaveImage('cb-pf-' + str(snap_no) + '.jpg', frame)
            snap_no += 1
            
        # handle events        
        k = cv.WaitKey(40) 
        if k == 27: # ESC
            print 'ESC pressed. Exiting ...'
            break            
       
            
