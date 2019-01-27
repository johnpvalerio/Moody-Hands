from subprocess import call
import os
import random

# 0 = most intense, 3 = chilliest
import pygame

Playlists = {'Moody-Room-0': 'https://www.youtube.com/playlist?list=PLiU3RtKBcY8KvVxCrsNel4Rl8VCjCAWQS',
             'Moody-Room-3': 'https://www.youtube.com/watch?v=HMnrl0tmd3k&list=PLiU3RtKBcY8JHo-acuAvhKZmQIfknGGpR'}
Downloaded = {}
MAX_ANALOG_VALUE = 1024
switch_flag = 1


def Download_Playlists():
    global Playlists
    print(os.getcwd())
    for playlist in Playlists.keys():
        file = open(playlist + ".txt", "w")
        command = "youtube-dl --download-archive downloaded.txt --no-post-overwrites -ciwx --audio-format wav -o %(playlist)s/%(playlist_index)s-%(title)s.%(ext)s " + \
                  Playlists[playlist]
        call(command.split(), shell=False)
        for filename in os.listdir(os.getcwd() + "/" + playlist + "/"):
            file.write(os.getcwd() + "/" + playlist + "/" + filename + "\n")


def Populate_Downloaded_List():
    global Downloaded
    global Playlists
    Downloaded.clear()
    for playlist in Playlists.keys():
        # Downloaded.append(playlist)
        Downloaded[playlist] = open(playlist + ".txt").read().splitlines()


##TEST AREA

# input: mood value
# return: string absolute .wav file path
def Pick_Song(value):
    global Downloaded
    if value >= MAX_ANALOG_VALUE * 4 / 5:
        return random.choice(Downloaded['Moody-Room-0'])
    elif value >= MAX_ANALOG_VALUE * 3 / 5:
        return random.choice(Downloaded['Moody-Room-1'])
    elif value >= MAX_ANALOG_VALUE * 2 / 5:
        return random.choice(Downloaded['Moody-Room-2'])
    else:
        return random.choice(Downloaded['Moody-Room-3'])


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


def play_next(path):
    global switch_flag
    song = pygame.mixer.Sound(path)
    if switch_flag == 1:
        play_song(song, 1)
        switch_flag = 2
    else:
        play_song(song, 2)
        switch_flag = 1


Download_Playlists()
Populate_Downloaded_List()
print(Pick_Song(1200))

# for l in Downloaded:
#    print(Downloaded[l])
