import glob, os.path, os, datetime
from picamera import PiCamera
from os import system
from time import sleep

class cameraClass():
    camera = PiCamera()
    camera.resolution = (1024, 768)

    picdir = "/home/pi/Pictures/"
    filelist = [ f for f in os.listdir(picdir) if f.endswith(".jpg") ]
    
    def takePhoto(self, pictureAmount, waitTime):
        sleep(2)   
        print('\nTaking photos...')
        for i in range(pictureAmount):
            sleep(waitTime)
            self.camera.capture('/home/pi/Pictures/image{0:04d}.jpg'.format(i))

        print('Photo capturing complete!\n\nCreating Gifraffe...')
        system('convert -delay 15 -loop 0 /home/pi/Pictures/image*.jpg gifraffe.gif')
        print('Gifraffe successfully created!\nAmount of pictures taken: %d' %pictureAmount)
        
    def emptyFolder(self):
        print('\nEmptying folder...')
        for the_file in os.listdir(self.picdir):
            file_path = os.path.join(self.picdir, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                #elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e) 
            
        print('Folder successfully emptied.\n\nCongratulations, your Gifraffe has been posted!')
        
