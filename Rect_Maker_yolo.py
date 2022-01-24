import cv2
import numpy as np
import os
import argparse

# from  yolotococo_ak import bboxYoloToCoco


def bboxYoloToCoco(ls,imgshape):
    # print(ls)
    x1,y1,x2,y2=ls
    height,width=imgshape
    if height==-1:
        return -1,-1,-1,-1
    x1,y1,x2,y2=float(x1),float(y1),float(x2),float(y2)
    x2=x2*width
    y2=y2*height
    x1=(x1*width)-(x2/2)
    y1=(y1*height)-(y2/2)
    return int(x1),int(y1),int(x1+x2),int(y1+y2)




# ann_dir="./mudasir/ann"
# img_dir="./mudasir/images"
# result_dir="./mudasir/results"
def start (ann_dir,img_dir,result_dir):
	if not os.path.exists(result_dir):
		os.mkdir(result_dir)
	for i in os.listdir(ann_dir):
		if not i in ['classes.txt']:
			img_name=list(os.path.splitext(i))
			img_name[-1]='jpg'
			img_name='.'.join(img_name)
			ann_name=os.path.join(ann_dir,i)
			fimg_name=os.path.join(img_dir,img_name)


			img=cv2.imread(fimg_name)
			print(fimg_name)
			if img is None:
				continue
			# print(fimg_name)
			for j in open(ann_name,"r"):
				print(j.split())
				x1,y1,x2,y2=bboxYoloToCoco(list(map(float,j.split()))[1:],img.shape[:-1])
				cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),5)
			cv2.imwrite(os.path.join(result_dir,img_name),img)
	print('done')



parser = argparse.ArgumentParser()
parser.add_argument("-a", "--ann", type=str,
                    default="ann/", dest="ann")
parser.add_argument("-i", "--img", type=str, default="images", dest="images",
                    help='Use ":amazon" for amazon filer')
parser.add_argument("-r", "--result", type=str, default="results", dest="results")

args = vars(parser.parse_args())
ann_dir=args['ann']
img_dir=args['images']
result_dir=args['results']
start(ann_dir,img_dir,result_dir)