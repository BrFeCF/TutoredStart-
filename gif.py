#CREDIT TO : https://www.codedex.io/projects/create-a-gif-with-python
#Run in terminal: pip3 install imageio                 
import imageio.v3 as iio
filenames = ['slide1.jpg', 'slide2.jpg']   #inside [''] will be the names of the files that will be in your gif
images = [ ]              
for filename in filenames:
  images.append(iio.imread(filename))  
  iio.imwrite('first.gif', images, duration = 500, loop = 0)
