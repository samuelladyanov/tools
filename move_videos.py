import sys
import os
import shutil
import mimetypes


def copy_video(video_dir, video_output):
    '''This function copies video files from a one directory into another.'''

    output_path = os.path.join(sys.argv[2], 'copied_videos')

    os.makedirs(output_path, exist_ok=True)

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
                shutil.copy(os.path.join(dirs, file), output_path)



if __name__=='__main__':

    if '-h' in sys.argv:
        print('''                 Enter a FULL path to your video folder and output folder. Example:( python move_videos.py "your/video/folder" "your/output/folder" ). A folder will be created within your output path with the copied videos inside. \n 
                 Missing Argument: Provide two paths or this error will occur. \n
                 Invalid folder path: This error occurs when the directory you passed does not exist or the path was not a full path.\n''')
   
    elif len(sys.argv) == 1:
        print('Missing Argument: Video folder path not passed (reference -h for help)')
        exit()
    elif len(sys.argv) == 2:
        print('Missing Argument: Output folder path not passed (reference -h for help)')
        exit()
        
    else:
        if not os.path.exists(sys.argv[1]):
            print('Invalid video folder path. (reference -h for help)')
            exit()
        if not os.path.exists(sys.argv[2]):
            print('Invalid output folder path. (reference -h for help)')
            exit()
        if sys.argv[1] == sys.argv[2]:
            print('DOOFUS DETECTED: BRO JUST PUT IT IN THE SAME FOLDER :skull: WHY ARE YOU EVEN USING THIS?')
            exit()

        copy_video(sys.argv[1], sys.argv[2])