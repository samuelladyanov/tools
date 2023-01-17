import sys
import os
import shutil
import mimetypes


def copy_video(video_dir, video_output):
    '''This function copies video files from a one directory into another.'''

    os.makedirs(video_output, exist_ok=True)

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
        print('''                 Enter a full path with quotations to your video folder and output folder in the following format: "home/user/videos" "home/user/output". \n 
                 Missing Argument: Provide two paths or this error will occur. \n
                 Invalid folder input/output path: This error occurs when the folder you passed does not exist or the path was not a full path.\n''')
   
    elif len(sys.argv) == 1:
        print('Missing Argument: Enter a path to a video folder. (reference -h for help)')
        exit()
    elif len(sys.argv) == 2:
        print('Missing Argument: Enter a path to your output folder. (reference -h for help)')
        exit()
    
    else:
        if not os.path.exists(sys.argv[1]):
            print('Invalid video folder path. (reference -h for help)')
            exit()
        if not os.path.exists(sys.argv[2]):
            print('Invalid folder output path. (reference -h for help)')
            exit()    
        copy_video(sys.argv[1], sys.argv[2])