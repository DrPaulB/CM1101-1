import winsound, sys
def beep(sound):
    winsound.PlaySound('%s.wav' % sound, winsound.menu)