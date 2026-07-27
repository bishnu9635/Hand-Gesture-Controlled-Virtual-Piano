import pygame
import cv2


pygame.mixer.init()


class Piano:

    def __init__(self):

        self.keys = [
            "C","D","E","F",
            "G","A","B",
            "C2","D2",
            "E2","F2",
            "G2","A2","B2"
        ]

        self.sounds = {}

        for key in self.keys:
            self.sounds[key] = pygame.mixer.Sound(
                f"sounds/{key}.wav"
            )

        self.pressed = None


    def draw(self, frame):

        width = frame.shape[1]

        key_width = width // len(self.keys)

        piano_height = 150   # piano size

        start_y = 20         # TOP position


        for i,key in enumerate(self.keys):

            x1 = i * key_width
            x2 = x1 + key_width


            color = (255,255,255)


            # Highlight pressed key
            if self.pressed == key:
                color = (0,255,0)


            # Draw white key
            cv2.rectangle(
                frame,
                (x1,start_y),
                (x2,start_y+piano_height),
                color,
                -1
            )


            # Border

            cv2.rectangle(
                frame,
                (x1,start_y),
                (x2,start_y+piano_height),
                (0,0,0),
                2
            )


            # Note name

            cv2.putText(
                frame,
                key,
                (x1+10,start_y+90),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0,0,0),
                2
            )



    def play(self,index):

        if index < len(self.keys):

            key = self.keys[index]

            self.sounds[key].play()

            self.pressed = key

            return key

        return None