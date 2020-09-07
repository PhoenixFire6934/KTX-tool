import os
import platform

def _(*args):
    print('[Tool] ', end='')
    for arg in args:
        print(arg, end=' ')
    print()

if not os.path.isdir('ktx/'):
    os.mkdir('ktx')
if not os.path.isdir('png/'):
    os.mkdir('png/')

path = './ktx'
system = platform.system()
for file in os.listdir(path):
    
    if file.endswith(".ktx"):
        filepath = 'ktx/' + file
        no_extension = file.split('\\')[-1].split('.')[0]
        opath = 'png/' +  no_extension +'.png'
        
        if system == 'Windows':
            os.system("PVRTexToolCLI.exe -i " + filepath + " -d " + opath + " -f r8g8b8a8 ")
        elif system == 'Linux':
            os.system("chmod +x ./PVRTexToolCLI")
            os.system("./PVRTexToolCLI -i " + filepath + " -d " + opath + " -f r8g8b8a8")
        else:
            _("Unsupported OS system")
