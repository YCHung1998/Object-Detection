# Object-Detection
DataSet
---
**The Street View House Numbers** (SVHN) dataset link : http://ufldl.stanford.edu/housenumbers/  
Data in goole drive link :　https://drive.google.com/drive/folders/1aRWnNvirWHXXXpPPfcWlHQuzGJdXagoc  

Folder Structure  
---
```
├──data/
    ├─ train/images
    │     ├─ 1.png      # pic 
    │     ├─ 2.png
    │     │     .
    │     │     .
    │     │     .
    │     ├─ 30000.png
    ├─ train/labels
    │     ├─ 1.txt      # pic bboxes with the labels
    │     ├─ 2.txt
    │     │     .
    │     │     .
    │     │     .
    │     └─ 30000.txt
    ├─ valid/images
    │     ├─ 30001.png
    │     ├─ 30002.png
    │     │     .
    │     │     .
    │     │     .
    │     └─ 33402.png
    ├─ valid/labels
    │     ├─ 30001.txt
    │     ├─ 30002.txt
    │     │     .
    │     │     .
    │     │     .
    └─    └─ 33402.txt
```

Training
---
```
python train.py --img 640 --batch 16 --epochs 20 --data SVHN.yaml --weights yolov5m.pt
```

detection
---
```
python detect.py --source  --weights runs/train/exp/weights/best.pt 
```

generate the answer in json file
---
```
python inference.py
```

reference
---
yolov5 github : https://github.com/ultralytics/yolov5
yolov1 paper : https://arxiv.org/pdf/1506.02640.pdf
yolov1 paper : https://arxiv.org/pdf/1804.02767.pdf
