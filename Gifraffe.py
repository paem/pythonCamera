import camera_class, db_class

camera = camera_class.cameraClass()
firebase = db_class.fireClass()

correctPictureInput = False
correctTimeInput = False
gifraffeName = input("What does thy wish to calleth thy Gifraffe? ")

while correctPictureInput == False:
    try:
        pictureAmount = int(input("How many photographies do thy wish to taketh? "))
        correctPictureInput = True
    except Exception as e:
        print("Please enter a valid number.\n")
        
while correctTimeInput == False:
    try:
        waitTime = int(input("How long shall thy timeth pass between each photograph? "))
        correctTimeInput = True
    except Exception as e:
        print("Please enter a valid number.\n")  

camera.takePhoto(pictureAmount, waitTime)
firebase.uploadGif(pictureAmount, gifraffeName)
camera.emptyFolder()
