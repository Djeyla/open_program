import os
import subprocess

jpeg_files = os.listdir('C:/Users/lenovo/PycharmProjects/open_programm/external-programs/Source')

#os.mkdir('C:/Users/lenovo/PycharmProjects/open_programm/external-programs/Result') #говорит, что папка уже создана
try:
  os.mkdir("Result")
except FileExistsError:
  None

def convert(file):
    subprocess.call(['C:/Users/lenovo/PycharmProjects/open_programm/external-programs/convert.exe', os.path.join('C:/Users/lenovo/PycharmProjects/open_programm/external-programs/Source', file),
                     "-resize", "200", os.path.join('C:/Users/lenovo/PycharmProjects/open_programm/external-programs/Result', file)])

for f in jpeg_files:
    convert(f)




import subprocess
import os

