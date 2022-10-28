# Hash all the images in the folder and copy the hash and filename to csv file
import hashlib
from PIL import Image
import glob
import numpy as np

#test md5 hash
"""
md5hash = hashlib.md5(Image.open('watermarkingimage\Capture.png').tobytes())
md5hash2 = hashlib.md5(Image.open('watermarkingimage\capture2.jpg').tobytes())
print(md5hash.hexdigest())
print(md5hash2.hexdigest())
"""

### hash images in folder and store in CSV
image_list = []
list_rows = []
file_name = []

for filename in glob.glob('watermarkingimage\*'):
    im = Image.open(filename).tobytes()
    image_list.append(im)
    file_name = filename
    img_hash = hashlib.md5(im)
    img_hash = img_hash.hexdigest(), filename
    list_rows.append(img_hash)
    #rows = zip(filename)
    print(img_hash, filename)

    np.savetxt("numpy_test.csv", list_rows, delimiter=",", fmt='% s')
    #np.savetxt("numpy_test.csv", (list_rows,filename),delimiter=",", fmt='% s')

    # test array
    """
    dtype = [('Hash', (np.str_, 20)), ('Filename', (np.str_, 100))]
    structuredArr = np.array(img_hash, file_name)
    np.savetxt('numpy_test2.csv', structuredArr, delimiter=',', fmt=['%s' , '%f', '%d'], header='Hash,Filename', comments='')
    """