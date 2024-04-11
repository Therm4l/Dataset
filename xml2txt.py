import xml.etree.ElementTree as ET
import cv2
import os
from tqdm import tqdm
dir = r'D:\DATASOURCE\DOLOAD\dataset(txt)\broke'

p1 = r'\JPEGImages'

x1 = r'\Annotations'


def t(n: str):
    if n == 'broke':
        return 0
    if n == 'circle':
        return 1
    if n == 'good':
        return 2
    if n == 'lose':
        return 3
    if n == 'uncovered':
        return 4


imgdir = r'D:\outsourcing\Well-cover-from-Henan-province\10000_dataset\JPEGImages'
xmldir = r'D:\outsourcing\Well-cover-from-Henan-province\10000_dataset\Annotations'
txtdir = r'D:\outsourcing\Well-cover-from-Henan-province\10000_dataset\10000_dataset_anno_txt'
fl = os.listdir(imgdir)
for f in tqdm(fl):
    img = cv2.imread(imgdir + '\\' + f)
    h, w, _ = img.shape
    n, _ = os.path.splitext(f)
    tree = ET.parse(xmldir + '\\' + n + '.xml')
    root = tree.getroot()
    obj = root.findall('object')
    for o in obj:
        name = o.find('name').text
        name = t(name)
        bndbox = o.find('.//bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)
        rmx = ((xmin + xmax) / 2) / w
        rmy = ((ymin + ymax) / 2) / h
        rx = (xmax - xmin) / w
        ry = (ymax - ymin) / h
        with open(txtdir + '\\' + n + '.txt', 'w') as fi:
            # print(name,rmx,rmy,rx,ry)
            print(name, rmx, rmy, rx, ry, file=fi)
