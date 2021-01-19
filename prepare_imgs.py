
from os import listdir
from skimage import io
from skimage.transform import resize

trainImages = 'images/fruits/trainprep'
trainImagesPrepared = 'images/fruits/trainprep2'

# # image = io.imread(trainImages+'apples/'+'rotated_by_15_Screen Shot 2018-06-08 at 4.59.36 PM.png')
# img = io.imread(trainImages+'/'+'apples'+'/'+'rotated_by_15_Screen Shot 2018-06-08 at 4.59.36 PM.png')
# img = resize(img, (256,256))
# io.imsave('img.png',img)

def prepimg(path,save_path):
    img = io.imread(trainImages+'/'+subdir+'/'+file)
    img = resize(img, (100,100))
    io.imsave(save_path, img)
i = 0
for subdir in listdir(trainImages):
    for file in listdir(trainImages+'/'+subdir):
        img_path = trainImages+'/'+subdir+'/'+file
        im_save_path = f'{trainImagesPrepared}/{subdir}/{file}100.png'
        prepimg(img_path, im_save_path)
        i+=1
        print(i)
        

