import os

from PIL import Image
import scipy.io as sio

if __name__ == '__main__':
    image_dir = os.path.join('datasets', 'Training', 'images')
    label_dir = os.path.join('datasets', 'Training', 'labels')
    digitStruct_dir = os.path.join('datasets', 'digitStruct.mat')

    dS = sio.loadmat(digitStruct_dir)['digitStruct'][0]

    for i, Name_and_Boxes in enumerate(dS):
        name, bboxes = Name_and_Boxes
        name, bboxes = name[0], bboxes[0]

        img = Image.open(os.path.join(image_dir, name))
        WIDTH, HEIGHT = img.size

        fp = open(os.path.join(label_dir, name.replace('png', 'txt')), 'w')
        for bbox in bboxes:
            bbox = [elt.squeeze().tolist() for elt in bbox]
            
            height, left, top, width, label = bbox
            label %= 10

            x_center = (left + width / 2) / WIDTH
            y_center = (top + height / 2) / HEIGHT
            width /= WIDTH
            height /= HEIGHT

            bbox = f"{label} {x_center} {y_center} {width} {height}\n"
            fp.write(bbox)
        fp.close()

        if i % 1000 == 0:
            print(i)

        
