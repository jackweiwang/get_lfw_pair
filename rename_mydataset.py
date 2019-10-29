import os

# import re
imgs_path = '/home/ww/myGit/Probabilistic-Face-Embeddings/my_data/my_mtcnncaffe_aligned/'

if os.path.isdir(imgs_path):
    for s in os.listdir(imgs_path):
        newdir = os.path.join(imgs_path, s)
        # print(newdir)
        filenames = os.listdir(newdir)
        filenames.sort()
        for name in filenames:
            newname = newdir.split('/')[-1]
            os.rename(newdir + '/' + name,
            os.path.join(newdir, newname + '_' + '%04d' % int(filenames.index(name) + 1)) + '.jpg')
