# Intended to create a separated file so it doesn't bloat scripts.
from displayer import console


def help():
    print('---------------------------------------')
    print(console.head('-- Help --'))
    print('---------------------------------------')
    print(console.head('** Features **'))
    print('echo - Prints the argument in the main console.')
    print('clean - Deletes python cache from the folders.')
    print(console.head('** Other Features **'))
    print('ArtASCII [art_ascii] - Converts a video/image into ASCII! Made by Chion82.')
    print('Binary Converter [binary_conv] - Converts your text into Binary.')
    print('Base64 Converter [dec_base64 | enc_base64] - Decodes/Encodes your text into Base64.')
    print('Base32 Converter [dec_base32 | enc_base32] - Decodes/Encodes your text into Base32.')
    print('Hex Converter [dec_hex | enc_dex] - Decodes/Encodes your text into hex.')
    print('Jadx [jadx] - Improved & updated version of Dex2Jar, Made by skylot.')
    print('YouTubeDL [yt_dl] - Open source download manager for video and audio from YouTube.')
    print('---------------------------------------')
    print('If you found a bug/error, please send the report to borcillofg2020@gmail.com')