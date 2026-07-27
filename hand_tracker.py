import cv2
import mediapipe as mp


class HandTracker:


    def __init__(self):

        self.hands = mp.solutions.hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.drawer = mp.solutions.drawing_utils



    def detect(self, frame):

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        result = self.hands.process(rgb)


        landmarks = []


        if result.multi_hand_landmarks:


            hand = result.multi_hand_landmarks[0]


            for lm in hand.landmark:

                h,w,_ = frame.shape

                x=int(lm.x*w)
                y=int(lm.y*h)

                landmarks.append(
                    (x,y)
                )


            self.drawer.draw_landmarks(
                frame,
                hand,
                mp.solutions.hands.HAND_CONNECTIONS
            )


        return landmarks