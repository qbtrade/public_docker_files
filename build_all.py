import os

for folder in ['play', 'clash', 'ss-server']:
	os.system(f'cd {folder} && docker build . -t qbtradepub/{folder}')
	os.system(f'docker push qbtradepub/{folder}')
