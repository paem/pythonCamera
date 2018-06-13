# pythonCamera
A simple gif creator made with a Raspberry Pi which uploads to a firebase database.

Gifraffe.py is the main class which uses the camera_class and the db_class.

The script does the following:

1. Takes multiple shots - This requirement refers to the camera module and refers to the images to be taken to form the gif image.
2. Converts images to gifs - Once a sequence of images has been taken, these are joined to a picture of the file format gif.
3. Clears the folder where the original images are saved - To save space on the Raspberry Pi, the images are continuously erased after the gif image has been created.
4. Upload gif image to database - The program will automatically upload the gif file to a database after it has been created.
5. Show GIF Images on External Website - The images stored in the database is retrieved for rendering on a external website.
