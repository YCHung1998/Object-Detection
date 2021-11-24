import os
import sys
import json

import torch
from PIL import Image

# sys.path.insert(0, 'yolov5')
from utils.datasets import LoadImages
from utils.general import non_max_suppression, scale_coords
from models.common import DetectMultiBackend

if torch.cuda.is_available():
    device = torch.device('cuda:0')
else:
    device = "cpu"

weight_dir = os.path.join('yolov5',
                          'runs',
                          'train',
                          'exp',
                          'weights',
                          'best.pt')
model = DetectMultiBackend(weight_dir, device=device)

dataset = LoadImages(os.path.join('datasets', 'Testing', 'images'))

JSON = []
ctr = 0
for path, img, im0, vid_cap, s in dataset:
    # get image id
    img_id = path.split('/')[-1]  # '100000.png'
    img_id = int(img_id.split('.')[0])  # 100000

    # predict
    img = torch.from_numpy(img).float().to(device)
    img /= 255
    img = img.unsqueeze(0)

    pred = model(img, augment=False)
    pred = non_max_suppression(pred)

    for det in pred:
        # for prediction in mini-batch size

        if len(det):
            # (x, y, x, y, score, cls_id)
            det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape)

            for *xyxy, conf, cls in det:
                '''
                {'image_id': 100000, 'category_id': cls_id, 'score': score,
                 'bbox': [x, y, w, h]}
                '''
                xyxy = [float(c) for c in xyxy]
                conf = float(conf)
                cls = int(cls)

                x1, y1, x2, y2 = xyxy
                w = x2 - x1
                h = y2 - y1

                bbox = {'image_id': img_id,
                        'category_id': cls,
                        'score': conf,
                        'bbox': [x1, y1, w, h]}

                JSON.append(bbox)

    ctr += 1
    if ctr % 100 == 0:
        print(ctr)

JSON = json.dumps(JSON, indent=4)
with open(os.path.join('datasets', 'Testing', 'answer.json'), 'w') as f:
    f.write(JSON)
