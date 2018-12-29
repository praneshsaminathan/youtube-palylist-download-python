import threading
from pytube import Playlist

threads = []
#####your playlist links
play_lists = ['https://www.youtube.com/playlist?list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj', 'https://www.youtube.com/playlist?list=PLQVvvaa0QuDeA05ZouE4OzDYLHY-XH-Nd', 'https://www.youtube.com/playlist?list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW',
'https://www.youtube.com/playlist?list=PL1WVjBsN-_NIdlnACz0Mxuq8VcuxER-is', 'https://www.youtube.com/watch?v=YOTZ_5zW6mk&list=PLbpAWbHbi5rN9hp7KaJnGOFYc0vxtTAh4']
def downld(name, n):
    pl = Playlist(name)
    #####location to store
    pl.download_all(('/home/user/Desktop/{0}').format(n))
direct = 2
for play_ in play_lists:
    t = threading.Thread(target=downld,name=play_, args =(play_, direct) )
    #threads.append(t)
    direct += 1
    t.start()
    print('{} has started \n'.format(t.name))
