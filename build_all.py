import os

for folder in ['play', 'clash']:
	os.system(f'cd {folder} && docker build . -t qbtradepub/{folder}')
	os.system(f'docker push qbtradepub/{folder}')
