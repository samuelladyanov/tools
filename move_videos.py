import sys
import os
import shutil
import mimetypes


def copy_video(video_dir, video_output):
    '''This function copies video files from a one directory into another.'''

    os.makedirs(sys.argv[2], exist_ok=True)

    def check_video(video):
        '''Checks if a file has a video extension'''
        mimestart = mimetypes.guess_type(video)[0]
        if mimestart != None:
            mimestart = mimestart.split('/')[0]
            if mimestart == 'video':
                return True
            else:
                return False
                

    # Search for video files and copy
    for dirs, subdirs, files in os.walk(video_dir):
        for file in files:
            if check_video(file) == True:
                shutil.copy(os.path.join(dirs, file), video_output)



if __name__=='__main__':

    if '-h' in sys.argv:
        print('''                 Enter a full path to your video folder. For output folder, you can have the folder created by specifying a name (ex:'output') and it will save in your working directory. To save to a different path, use the full path followed by "/name_of_new_folder" to generate folder. If name of new folder is not specified, video files will copy into existing directory. NOTE: if your output path isn't an existing path it will create a nested folder in your working directory in the format of the path you entered.  \n 
                 Missing Argument: Provide two paths or this error will occur. \n
                 Invalid folder path: This error occurs when the folder you passed does not exist or the path was not a full path.\n''')
   
    elif len(sys.argv) != 3:
        print('Missing Argument: 1 or 2 paths are missing (reference -h for help)')
        exit()
    
    else:
        if not os.path.exists(sys.argv[1]):
            print('Invalid video folder path. (reference -h for help)')
            exit()
        
            
        copy_video(sys.argv[1], sys.argv[2])