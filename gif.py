import imageio.v3 as iio
filenames = ['slide1.jpg', 'slide2.jpg']
images = [ ]
for filename in filenames:
  images.append(iio.imread(filename))
  iio.imwrite('sayang2.gif', images, duration = 500, loop = 0)