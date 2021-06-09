import main
import os
import platform
import re
import random

from youtube_dl import YoutubeDL
from youtube_dl import DownloadError

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
        print('---------------------------------------')
        print('Command: exit')
        print('Ending script process..')

        if platform.system() == 'Linux':
            os.system('clear')
        elif platform.system() == 'Windows':
            os.system('cls')

        os.system(main.pythonExec + ' scripts/main.py')
        exit(0)
        return
    if len(inputsec) == 0:
        print('---------------------------------------')
        print('ERROR: No URL argument given.')
        createinput()
        return
    if re.match(regex, inputsec) is None:
        print('---------------------------------------')
        print('ERROR: Url is malformed, or not a valid url.')
        createinput()
        return

    # Ask for output type
    print('---------------------------------------')
    print('Output type:')
    print('-srcOnly = Outputs the source url only.')
    print('-video = Downloads the video to local storage.')
    print('-audio = Downloads the audio to local storage.')
    print('---------------------------------------')
    outputsec = input().lower()

    if not os.path.exists('youtube_dl/downloads'):
        os.makedirs('youtube_dl/downloads')

    print('---------------------------------------')
    print('URL: ' + inputsec)
    if outputsec == '-srcOnly':
        with YoutubeDL(audiodlopts) as ytdl:
            info = ytdl.extract_info(inputsec, download=False)
            print('Source: ' + info.get('url'))
            ytdl.download([inputsec])
    elif outputsec == '-video':
        # Ask for video quality
        print('Video quality:')
        print('---------------------------------------')
        print('Better = Suitable for good connections & consumes more data.')
        print('Worst = Consumes less data & friendly to weak connections.')
        print('---------------------------------------')
        print('Manual selection:')
        print('1920x1080 resolution (with 60fps if applicable)')
        print('1280x720 resolution (with 60fps if applicable)')
        print('854x480 resolution')
        print('640x360 resolution')
        print('256x144 resolution')
        print('---------------------------------------')
        qualitysec = input()
        print('---------------------------------------')

        if qualitysec == 'Better':
            videodlopts['format'] = 'bestvideo+bestaudio/best'
        elif qualitysec == 'Worst':
            videodlopts['format'] = 'worstvideo+worstaudio/worst'
        elif qualitysec == '1920x1080 resolution':
            videodlopts['format'] = '299+bestaudio'
        elif qualitysec == '1280x720 resolution':
            videodlopts['format'] = '298+bestaudio'
        elif qualitysec == '854x480 resolution':
            videodlopts['format'] = '135+worstaudio'
        elif qualitysec == '640x360 resolution':
            videodlopts['format'] = '134+worstaudio'
        elif qualitysec == '256x144 resolution':
            videodlopts['format'] = '160+worstaudio'
        else:
            print('ERROR: Video quality not specified.')
            return
        try:
            with YoutubeDL(videodlopts) as ytdl:
                ytdl.download([inputsec])
        except DownloadError:
            print('ERROR: Cannot download video.')
            return
        print('Download successful! Located at "youtube_dl/downloads".')
    elif outputsec == '-audio':
        try:
            with YoutubeDL(audiodlopts) as ytdl:
                ytdl.download([inputsec])
        except DownloadError:
            print('ERROR: Cannot download audio.')
            return
        print('Download successful! Located at "youtube_dl/downloads".')
    else:
        print('ERROR: Output type not specified.')
    createinput()


def createinput():
    global inputsec
    print('---------------------------------------')
    inputsec = input('Enter YouTube URL: ')
    getvidsource()


print('DevScripts yt_dl.py')
print('YouTubeDL - version 2021.5.16')
createinput()