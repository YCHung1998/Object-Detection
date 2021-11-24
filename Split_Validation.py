import os
import random

if __name__ == '__main__':
    ValidNum = 3402
    
    Train_Dir = os.path.join('datasets', 'Training')
    Valid_Dir = os.path.join('datasets', 'Validation')

    # collect dataset
    FileList = []
    for Dir in [Train_Dir, Valid_Dir]:
        FileList += os.listdir(os.path.join(Dir, 'images'))
    FileList = [filename.split('.')[0] for filename in FileList]

    # shuffle and split
    random.shuffle(FileList)
    TrainList = FileList[:-ValidNum]
    ValidList = FileList[-ValidNum:]
                         
    # move file
    for i, TrName in enumerate(TrainList):
        try:
            os.rename(os.path.join(Train_Dir, 'images', TrName+'.png'),
                      os.path.join(Train_Dir, 'images', TrName+'.png'))
            
            os.rename(os.path.join(Train_Dir, 'labels', TrName+'.txt'),
                      os.path.join(Train_Dir, 'labels', TrName+'.txt'))
            
        except:
            os.rename(os.path.join(Valid_Dir, 'images', TrName+'.png'),
                      os.path.join(Train_Dir, 'images', TrName+'.png'))

            os.rename(os.path.join(Valid_Dir, 'labels', TrName+'.txt'),
                      os.path.join(Train_Dir, 'labels', TrName+'.txt'))
        if i % 1000 == 0:
            print(i)

    for i, ValName in enumerate(ValidList):
        try:
            os.rename(os.path.join(Train_Dir, 'images', ValName+'.png'),
                      os.path.join(Valid_Dir, 'images', ValName+'.png'))
            
            os.rename(os.path.join(Train_Dir, 'labels', ValName+'.txt'),
                      os.path.join(Valid_Dir, 'labels', ValName+'.txt'))
            
        except:
            os.rename(os.path.join(Valid_Dir, 'images', ValName+'.png'),
                      os.path.join(Valid_Dir, 'images', ValName+'.png'))

            os.rename(os.path.join(Valid_Dir, 'labels', ValName+'.txt'),
                      os.path.join(Valid_Dir, 'labels', ValName+'.txt'))
        if i % 1000 == 0:
            print(i)
