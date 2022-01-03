import os

os.system('cd play && docker build . -t qbtradepub/play')
os.system('docker push qbtradepub/play')
