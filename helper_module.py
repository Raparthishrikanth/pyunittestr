import shutil
import os
import glob

def move_png(dir_name):

    source_dir = 'C:/Users/91630/PycharmProjects/screensht' #Path where your files are at the moment

    try:
        dst = 'C:/Users/91630/PycharmProjects/screensht/row_' + str(dir_name)
        os.makedirs(dst)
    except:
        pass

    #dst = '/home/danw32/PyCharmProjects/TestProjectVEnv/Screenshots/' + str(dir_name) #Path you want to move your files to

    files = glob.iglob(os.path.join(source_dir, "*.png"))
    for file in files:
        if os.path.isfile(file):
            shutil.move(file, dst)