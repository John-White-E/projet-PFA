
import pandas as pd
import numpy as np 
import sklearn
from sklearn.cluster import KMeans
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import cv2
import webcolors

def get_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image
def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

def closet_colour(req):
  min_co={}
  for key,name in webcolors.CSS3_HEX_TO_NAMES.items():
    r_c,g_c,b_c=webcolors.hex_to_rgb(key)
    rd=(r_c - req[0])**2
    gd=(g_c - req[1])**2
    bd=(b_c - req[2])**2
    min_co[(rd+gd+bd)]=name
  return min_co[min(min_co.keys())]


def color_name(reqco):
  try:
    closet_name=actual_name=webcolors.rgb_to_name(reqco)
  except ValueError:
    closet_name=closet_colour(reqco)
    actual_name=None
  return closet_name



def get_color(img):
  image = get_image(img)
  number_of_colors = 10
  modified_image = image.reshape(image.shape[0]*image.shape[1], 3)
  clf = KMeans(n_clusters = 2)
  labels = clf.fit_predict(modified_image)
  counts = Counter(labels)
  center_colors = clf.cluster_centers_
  # We get ordered colors by iterating through the keys
  ordered_colors = [center_colors[i] for i in counts.keys()]
  hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
  rgb_colors = [ordered_colors[i] for i in counts.keys()]
  named_colors = [color_name((int(rgb_colors[i][0]),int(rgb_colors[i][1]),int(rgb_colors[i][2]))) for i in  counts.keys()]
  
  return named_colors

