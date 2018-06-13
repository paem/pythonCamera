import pyrebase, datetime

class fireClass():
    config = {
        "apiKey": "",
        "authDomain": "",
        "databaseURL": "",
        "storageBucket": ""
        }

    firebase = pyrebase.initialize_app(config)
    times = datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
    storage = firebase.storage()
    db = firebase.database()
    
    def uploadGif(self, pictureAmount, gifraffeName):
        print('\nUploading Gifraffe to database...')
        gifPath = "gifs/timelapse-"+self.times
        self.storage.child(gifPath).put("gifraffe.gif")
        print('Upload was completed!\n\nUploading Gifraffe URL...')

        gifUrl = self.storage.child(gifPath).get_url(None)
        data = {"gifName": gifraffeName, "gifUrl": gifUrl, "pictureAmount": pictureAmount}
        self.db.child("gifs").push(data)

        print('URL: ' + gifUrl)
