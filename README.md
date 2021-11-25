# Object-Detection
DataSet
---
**The Street View House Numbers** (SVHN) dataset link : http://ufldl.stanford.edu/housenumbers/  
Data in goole drive link (Class) : [Here](https://drive.google.com/drive/folders/1aRWnNvirWHXXXpPPfcWlHQuzGJdXagoc)  
You can download the dataset in this link : [Here(Myself)](https://drive.google.com/file/d/15ViQnv9pAEoA7fDN_OlkXPxO_UB5arTr/view?usp=sharing)


Requirement
---
```requirement.txt``` in yolov5 folder 

Folder Structure  
---
Please doenload the dataset yourself and excute the ```Split_Validation.py``` code to generate the below structure 


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


Check the time on colab
---
1. Click link : https://colab.research.google.com/drive/1cBg_bWOZtJvKgoZCzF1LKwSM5VhnOEFo?usp=sharing
2. Switch mode to GPU 
3. mount your drive  
4. Ensure to create the folder DL by yourself under Colab Notebooks (eg. /Colab Notebooks/DL)
5. Then click the bottom run all the blocks and waiting result 

| model time        | per image (sec) |
| ------------- |:-------------:|
| excluded loading image | 0.04887 |
| Including loading image | 0.04951|


Generate the answer in json file
---
為了使 inference.py 呈現在首頁，執行前須要先調整如下敘述。  
Before execute the following code, please open the inference.py and uncomment 8-th row code.(Insurance your code path is coreect).
```
python inference.py
```
Repository
---
yolo v5  
[ultralytics/yolov5](https://github.com/ultralytics/yolov5)

Reference
---
yolov5 github : https://github.com/ultralytics/yolov5  
yolov1 paper : https://arxiv.org/pdf/1506.02640.pdf  
yolov1 paper : https://arxiv.org/pdf/1804.02767.pdf  
