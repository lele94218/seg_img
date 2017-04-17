#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 13:55:00 2017

@author: taoranxue
"""
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy
from scipy import ndimage
from scipy import misc

from PIL import Image


def fun():
    # Segnet:
    # Sky = 0,
    # Building = 1,
    # Pole = 2,
    # Road = 3,
    # Pavement 4,
    # Tree = 5,
    # SignSymbol = 6,
    # Fence = 7,
    # Car = 8,
    # Pedestrian = 9,
    # Bicyclist = 10,
    # Unlabelled = 11

    # Our:
    # road(background) = 11,
    # sky = 1 -> 0,
    # building = 2 -> 1,
    # people = 3 -> 9,
    # tree = 4 -> 5,
    # bikes = 5 -> 10,
    # cars = 6 -> 8,
    path = "data/annotations/"
    for filename in os.listdir(path):
        if filename.endswith(".png"): 
            my_train = Image.open(path + filename)
            my_train_r = my_train.split()[0]

            tmp = my_train_r
            img_r = my_train_r.load()

            for i in range(0, my_train_r.size[0]):
                for j in range(0, my_train_r.size[1]):
                    if img_r[i, j] == 0:
                        img_r[i, j] = 11
                    elif img_r[i, j] == 1:
                        img_r[i, j] = 0
                    elif img_r[i, j] == 2:
                        img_r[i, j] = 1
                    elif img_r[i, j] == 3:
                        img_r[i, j] = 9
                    elif img_r[i, j] == 5:
                        img_r[i, j] = 10
                    elif img_r[i, j] == 4:
                        img_r[i, j] = 5
                    elif img_r[i, j] == 6:
                        img_r[i, j] = 8

            my_train_r.save("data/segannot/train_" + filename, "PNG")
            print("data/segannot/train_" + filename)


if __name__ == "__main__":
    fun()
