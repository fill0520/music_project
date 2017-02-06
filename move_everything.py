import os, re

path = os.path.dirname(os.path.abspath(__file__)) + '/'
mp3regex = re.compile('.*mp3')

onlymusic = [f for f in os.listdir(path) if mp3regex.match(f)]
for song in onlymusic:
	folder = path + song[:-4]
	os.mkdir(folder)
	os.rename(path+song, folder+'/'+song)

musicdirs = [f[0] for f in os.walk(path)]
musicdirs = musicdirs[1:]
for d in musicdirs:
	file = d + "/README.md"
	if not os.path.isfile(file):
		with open(file, 'w') as f:
			f.write('#Топовые моменты и тайминг:')

