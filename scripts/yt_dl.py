import main
import os
import platform
import re
import random

from displayer import console

try:
    from mutagen.mp4 import MP4
    from youtube_dl import YoutubeDL
    from youtube_dl import DownloadError
except ModuleNotFoundError:
    print(console.err('Failed to get external packages, make sure you have installed them using "pip install -r '
                      'install.txt, exiting script...'))
    os.system(main.pythonExec + ' scripts/main.py')
    exit(0)

inputsec: str = 'None'
regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
videodlopts = {
    'format': random.choice(['bestvideo+bestaudio/best',
                             'worstvideo+worstaudio/worst']),
    'outtmpl': 'youtube_dl/downloads/%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}
audiodlopts = {
    'format': '140',
    'outtmpl': 'youtube_dl/downloads/%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}


def getvidsource():
    if inputsec == 'exit':
        print('Ending script process..')

        if platform.system() == 'Linux':
            os.system('clear')
        elif platform.system() == 'Windows':
            os.system('cls')

        os.system(main.pythonExec + ' scripts/main.py')
        exit(0)
        return
    if len(inputsec) == 0:
        print(console.err('ERROR: No URL argument given.'))
        createinput()
        return
    if re.match(regex, inputsec) is None:
        print(console.err('ERROR: Url is malformed, or not a valid url.'))
        createinput()
        return
    if not os.path.exists('youtube_dl/downloads'):
        os.makedirs('youtube_dl/downloads')

    # Ask for output type
    print('---------------------------------------')
    print('-- Output Type --')
    print('-srcOnly = Outputs the source url only.')
    print('-video = Downloads the video to local storage.')
    print('-audio = Downloads the audio to local storage.')
    print('---------------------------------------')
    print('Enter output type: ')
    outputsec = input()
    console.rmline_by_count(2)

    if outputsec == '-srcOnly':
        with YoutubeDL(audiodlopts) as ytdl:
            info = ytdl.extract_info(inputsec, download=False)
            print('Source: ' + info.get('url'))
            ytdl.download([inputsec])
    elif outputsec == '-video':
        # Ask for video quality
        print('-- Video Quality --')
        print('---------------------------------------')
        print('-better = Suitable for good connections & consumes more data.')
        print('-worst = Consumes less data & friendly to weak connections.')
        print('---------------------------------------')
        print('Manual selection:')
        print('-1080p60 = Higher resolution, huge file size, 60fps')
        print('-720p60 = High resolution, higher file size, 60fps')
        print('-1080p = Higher resolution, higher file size, 30fps')
        print('-720p = High resolution, high file size, 30fps')
        print('-480p = Normal resolution, normal file size, 30fps')
        print('-360p = Low resolution, low file size, 28fps')
        print('---------------------------------------')
        print('Enter video quality: ')
        qualitysec = input()
        console.rmline_by_count(2)

        if qualitysec == '-better':
            videodlopts['format'] = 'bestvideo+bestaudio/best'
        elif qualitysec == '-worst':
            videodlopts['format'] = 'worstvideo+worstaudio/worst'
        elif qualitysec == '-1080p60':
            videodlopts['format'] = '299+bestaudio'
        elif qualitysec == '-720p60':
            videodlopts['format'] = '298+bestaudio'
        elif qualitysec == '-1080p':
            videodlopts['format'] = '137+bestaudio'
        elif qualitysec == '-720p':
            videodlopts['format'] = '136+bestaudio'
        elif qualitysec == '-480p':
            videodlopts['format'] = '135+worstaudio'
        elif qualitysec == '-360p':
            videodlopts['format'] = '134+worstaudio'
        else:
            print(console.err('ERROR: Video quality not specified.'))
            return
        try:
            with YoutubeDL(videodlopts) as ytdl:
                print(console.success('Output: ' + outputsec))
                print(console.success('Video quality: ' + qualitysec))
                print(console.success('Download path: /youtube_dl/downloads'))
                print(console.success('YouTubeDL: Downloading...'))
                ytdl.download([inputsec])
        except DownloadError:
            print(console.err('ERROR: Cannot download video.'))
            return
        print('---------------------------------------')
        print(console.success('FINISH: Download successful!'
                              ' Located at "youtube_dl/downloads".'))
    elif outputsec == '-audio':
        with YoutubeDL(audiodlopts) as infodl:
            info = infodl.extract_info(inputsec, download=False)
            audiodlopts['outtmpl'] = 'youtube_dl/downloads/' + info['title'] + '.' + info['ext']
        try:
            with YoutubeDL(audiodlopts) as ytdl:
                print(console.success('Output: ' + outputsec))
                print(console.success('Download path: /youtube_dl/downloads'))
                print(console.success('YouTubeDL: Downloading...'))
                ytdl.download([inputsec])
        except DownloadError:
            print(console.err('ERROR: Cannot download audio.'))
            return
        meta = MP4('youtube_dl/downloads/' + info['title'] + '.' + info['ext']).tags
        meta['\xa9nam'] = info['title']
        meta['\xa9ART'] = info['uploader']
        meta.save('youtube_dl/downloads/' + info['title'] + '.' + info['ext'])
        print(console.success('FINISH: Download successful!'
                              ' Located at "youtube_dl/downloads".'))
    else:
        print(console.err('ERROR: Output type not specified.'))
    createinput()


def createinput():
    global inputsec
    print('---------------------------------------')
    print('Enter video URL: ')
    inputsec = input()
    console.rmline_by_count(2)
    print('URL: ' + inputsec)
    getvidsource()


print(console.head('DevScripts yt_dl.py'))
print('YouTubeDL - version 2021.5.16')
createinput()