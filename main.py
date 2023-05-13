import cv2
import mediapipe as mp
import time

#Deklarasi Variabel
    #mpdraw = solusi mediapipe untuk mengoutput pose estimator
    #mppose = untuk mediapipe agar menghitung pose tubuh

mpdraw = mp.solutions.drawing_utils
mppose = mp.solutions.pose

pose = mppose.Pose()                        # | pose = variabel mppose yang akan dirangkap dengan Pose class di variabel 'pose'

camera = cv2.VideoCapture(0)                # | variabel camera dengan package cv2 beserta class VideoCapture untuk memulai kamera

ptime = 0                                   # | ptime = Variabel untuk frame per Second

#jika berhasil, maka ...
while True:
    success, frame = camera.read()
    #menentukan warna dan mendeteksi pose
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hasil = pose.process(frameRGB)
    #print(hasil.pose_landmarks)

    if hasil.pose_landmarks:

        #titik landmarks ( dot )
        mpdraw.draw_landmarks(frame, hasil.pose_landmarks, mppose.POSE_CONNECTIONS)
        for id, lm in enumerate(hasil.pose_landmarks.landmark):
            h, w, c = frame.shape
            #print(id, lm)
            cx, cy = (int(lm.x*w)), (int(lm.y*h))
            #print(cx, cy)



    ctime = time.time()                 # | Package time dengan Class time
    fps = 1/(ctime-ptime)               # | menghitung FPS
    ptime = ctime                       #

    if cv2.waitKey(1) == ord('q'):
        break

    cv2.putText(frame, str(int(fps)), (30, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,21), 2)       # | Untuk FPS dan warna pose Estimator

    cv2.imshow("Motion Estimation", frame)
    cv2.waitKey(1)                              # | Untuk menjalankan Video atau men Skip Frame, semakin besar angkanya maka semakin banyak frame yang di skip

