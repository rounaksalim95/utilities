import os 
path = '/home/icewolf/Documents/git/ccnn/data/day_val_imgs/images/'
files = os.listdir(path)

f = open(path + 'test.txt', 'w+')

for i in range(len(files)):
    name = str(i) + '.jpg'
    os.rename(os.path.join(path, files[i]), os.path.join(path, name))
    f.write(name + '\n')

f.close()