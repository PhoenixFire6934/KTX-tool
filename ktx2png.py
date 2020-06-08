import os


if not os.path.isdir('ktx/'):
    os.mkdir('ktx')

if not os.path.isdir('png/'):
    os.mkdir('png/')

path = './ktx'
for file in os.listdir(path):
    if file.endswith(".ktx"):
        filepath = 'ktx/' + file
        no_extension = file.split('\\')[-1].split('.')[0]
        opath = 'png/' +  no_extension +'.png'
        os.system("PVRTexToolCLI.exe -i " + filepath + " -d " + opath + " -f r8g8b8a8 ")
