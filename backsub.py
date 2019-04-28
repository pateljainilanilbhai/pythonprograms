# import numpy as np
# import cv2
#
# cap = cv2.VideoCapture(0)
#
# rett,first=cap.read()
#
# while(True):
#     ret, frame = cap.read()
#     s = 255-cv2.absdiff(first, frame)
#
#
#
#
#
#     print(s)
#     cv2.imshow('frame',s)
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()





# # #
# # #
# # # import numpy as np
# # # import cv2
# # #
# # # cap = cv2.VideoCapture(0)
# # # fgbg = cv2.createBackgroundSubtractorMOG2()
# # #
# # # while (1):
# # #     ret, frame = cap.read()
# # #
# # #     fgmask = fgbg.apply(frame)
# # #
# # #     cv2.imshow('fgmask', frame)
# # #     cv2.imshow('frame', fgmask)
# # #     s=cv2.bitwise_and(frame,fgmask)
# # #     cv2.imshow('frames', s)
# # #
# # #     k = cv2.waitKey(30) & 0xff
# # #     if k == 27:
# # #         break
# # #
# # # cap.release()
# # # cv2.destroyAllWindows()
# #
# #
# # from __future__ import print_function
# # import cv2 as cv
# # import argparse
# #
# # parser = argparse.ArgumentParser(description='This program shows how to use background subtraction methods provided by \
# #                                               OpenCV. You can process both videos and images.')
# # parser.add_argument('--input', type=str, help='Path to a video or a sequence of image.', default=0)
# # parser.add_argument('--algo', type=str, help='Background subtraction method (KNN, MOG2).', default='MOG2')
# # args = parser.parse_args()
# # if args.algo == 'MOG2':
# #     backSub = cv.createBackgroundSubtractorMOG2()
# # else:
# #     backSub = cv.createBackgroundSubtractorKNN()
# # capture = cv.VideoCapture(0)
# # if not capture.isOpened:
# #     print('Unable to open: ' + args.input)
# #     exit(0)
# # while True:
# #     ret, frame = capture.read()
# #     if frame is None:
# #         break
# #
# #     fgMask = backSub.apply(frame)
# #
# #     cv.rectangle(frame, (10, 2), (100, 20), (255, 255, 255), -1)
# #     cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
# #                cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
# #
# #     cv.imshow('Frame', frame)
# #     cv.imshow('FG Mask', fgMask)
# #
# #
# #     keyboard = cv.waitKey(30)
# #     if keyboard == 'q' or keyboard == 27:
# #         break
#
#
# import cv2
# import numpy as np
#
# cap = cv2.VideoCapture(0)
#
# panel = np.zeros([100, 700], np.uint8)
# cv2.namedWindow('panel')
#
#
# def nothing(x):
#     pass
#
#
# cv2.createTrackbar('L - h', 'panel', 0, 179, nothing)
# cv2.createTrackbar('U - h', 'panel', 179, 179, nothing)
#
# cv2.createTrackbar('L - s', 'panel', 0, 255, nothing)
# cv2.createTrackbar('U - s', 'panel', 255, 255, nothing)
#
# cv2.createTrackbar('L - v', 'panel', 0, 255, nothing)
# cv2.createTrackbar('U - v', 'panel', 255, 255, nothing)
#
# cv2.createTrackbar('S ROWS', 'panel', 0, 480, nothing)
# cv2.createTrackbar('E ROWS', 'panel', 480, 480, nothing)
# cv2.createTrackbar('S COL', 'panel', 0, 640, nothing)
# cv2.createTrackbar('E COL', 'panel', 640, 640, nothing)
#
# while True:
#     _, frame = cap.read()
#
#     s_r = cv2.getTrackbarPos('S ROWS', 'panel')
#     e_r = cv2.getTrackbarPos('E ROWS', 'panel')
#     s_c = cv2.getTrackbarPos('S COL', 'panel')
#     e_c = cv2.getTrackbarPos('E COL', 'panel')
#
#     roi = frame[s_r: e_r, s_c: e_c]
#
#     hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
#
#     l_h = cv2.getTrackbarPos('L - h', 'panel')
#     u_h = cv2.getTrackbarPos('U - h', 'panel')
#     l_s = cv2.getTrackbarPos('L - s', 'panel')
#     u_s = cv2.getTrackbarPos('U - s', 'panel')
#     l_v = cv2.getTrackbarPos('L - v', 'panel')
#     u_v = cv2.getTrackbarPos('U - v', 'panel')
#
#     lower_green = np.array([l_h, l_s, l_v])
#     upper_green = np.array([u_h, u_s, u_v])
#
#     mask = cv2.inRange(hsv, lower_green, upper_green)
#     mask_inv = cv2.bitwise_not(mask)
#
#     bg = cv2.bitwise_and(roi, roi, mask=mask)
#     fg = cv2.bitwise_and(roi, roi, mask=mask_inv)
#
#     cv2.imshow('bg', bg)
#     cv2.imshow('fg', fg)
#
#     cv2.imshow('panel', panel)
#
#     k = cv2.waitKey(30) & 0xFF
#     if k == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()



# import numpy as np
# import cv2
#
# cap = cv2.VideoCapture(0)
# rett,first=cap.read()
#
# while(True):
#     ret, frame = cap.read()
#     diff_frame = 255-cv2.absdiff(first, frame)
#
#     # If change in between static background and
#     # current frame is greater than 30 it will show white color(255)
#     cv2.imshow('frame3', diff_frame)
#     thresh_frame = cv2.threshold(diff_frame, 1, 255, cv2.THRESH_MASK)[1]
#
#
#
#
#
#
#     cv2.imshow('frame',thresh_frame)
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()





#
#
#
#
#
# import cv2
# import numpy as np
#
#
# cap = cv2.VideoCapture(0)
# rett,first=cap.read()
# while(True):
#     ret, frame = cap.read()
#     diff_frame = cv2.absdiff(first, frame)
#
#
#
#
#     gray=cv2.cvtColor(diff_frame,cv2.COLOR_BGR2GRAY)
#     ret,mask=cv2.threshold(diff_frame,1,255,cv2.THRESH_BINARY)
#     kk=cv2.bitwise_and(frame,mask)
#     cv2.imshow('f',kk)
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()






import numpy as np
import cv2

cap = cv2.VideoCapture(0)
rett,first=cap.read()

while(True):
    ret, frame = cap.read()
    diff_frame = cv2.absdiff(first, frame)

    # If change in between static background and
    # current frame is greater than 30 it will show white color(255)

    img_gray = cv2.cvtColor(diff_frame, cv2.COLOR_BGR2GRAY)
    th,thres= cv2.threshold(img_gray,10,254,cv2.THRESH_BINARY)

    img2_fg = cv2.bitwise_and(frame,diff_frame, mask=thres)

    cv2.imshow('frame', diff_frame)
    cv2.imshow('frame1', thres)

    cv2.imshow('output', img2_fg)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

