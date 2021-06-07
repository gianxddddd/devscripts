basevideofile: str = 'None'
code = f"""import time, os

if __name__ == '__main__':
	f = open('converted.txt', 'r')
	frame_raw = f.read()
	frame_raw = frame_raw.replace('.', ' ')
	f.close()
	frames = frame_raw.split('SPLIT')
	os.system('mplayer -vo null -vc null {basevideofile} &')
	#os.system('mplayer test.mp4 &')
	init_time = time.time()
	while time.time() <= init_time + 218:
		os.system('clear')
		print(frames[int((time.time()-init_time)*10)])
		time.sleep(0.05)"""