import os
import time

import pygame

pygame.mixer.init()
print(os.getcwd())
os.chdir(os.getcwd())


def play_song(song, channel):

    if channel == 1:
        print('Stopping Channel 2, playing channel 1')
        pygame.mixer.Channel(2).fadeout(5000)
        pygame.mixer.Channel(channel).play(song, -1, fade_ms=5000)
    elif channel == 2:
        print('Stopping Channel 1, playing channel 2')
        # pygame.mixer.Channel(2).stop
        pygame.mixer.Channel(1).fadeout(5000)
        pygame.mixer.Channel(channel).play(song, -1, fade_ms=5000)



s1 = pygame.mixer.Sound('./Music/Holy Orders III - Guilty Gear Xrd-SIGN-OST.wav')
s2 = pygame.mixer.Sound("./Music/Turnabout Jazz Soul - Track 8 - Godot - The Fragrance of Dark Coffee - Turnabout Jazz Soul.wav")

while True:
    # play_song(s1)
    wait = input('Wait and shit')
    if wait == '1':
        play_song(s1, 1)
        # pygame.mixer.Channel(1).play(s1, -1)
    elif wait == '2':
        # pygame.mixer.Channel(1).play(s2, -1)
        play_song(s2, 2)
    elif wait == '0':
        pygame.mixer.Channel(1).stop()




