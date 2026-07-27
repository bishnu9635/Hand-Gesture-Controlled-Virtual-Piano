import cv2

from hand_tracker import HandTracker
from piano import Piano



camera=cv2.VideoCapture(0)


tracker=HandTracker()

piano=Piano()



while True:


    success,frame=camera.read()


    if not success:
        break


    frame=cv2.flip(
        frame,
        1
    )


    landmarks=tracker.detect(frame)



    piano.draw(frame)



    if len(landmarks)>8:


        # Index finger tip
        x,y=landmarks[8]


        cv2.circle(
            frame,
            (x,y),
            10,
            (0,0,255),
            -1
        )


        if y<170:


            width=frame.shape[1]

            key_width=width//14


            key_index=x//key_width


            note=piano.play(
                key_index
            )


            if note:

                cv2.putText(
                    frame,
                    "Playing: "+note,
                    (20,50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,255,0),
                    3
                )



    cv2.imshow(
        "Hand Gesture Virtual Piano",
        frame
    )



    if cv2.waitKey(1)&0xff==ord('q'):
        break



camera.release()

cv2.destroyAllWindows()