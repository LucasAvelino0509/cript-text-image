# -*- coding: utf-8 -*-

#####################################################################
#   Creator: Lucas Avelino
#   Description: The main porpuse of this code is to learn about encripting
#   messages inside Images.
#
#####################################################################

import os
from PIL import Image as img
import math
import unicodedata

bPColor = 1                         # bits per color (is the mount of bit each color of each pixel bring)
criptImg = img.open("enc/a.png");   #encripted Image
keyImg = img.open("a.png");         #key Image


criptImgWitdth = criptImg.size[0];
keyImgWitdth = keyImg.size[0];
criptImgHeigth = criptImg.size[1];
keyImgHeigth = keyImg.size[1];


if criptImgWitdth == keyImgWitdth and criptImgHeigth == keyImgHeigth: # when the size of images matchs we have a valid key
    print("Valid Key!");
    nums = []; # array of numbers that represents each color diference between images
    bins = []; # array of 8-bit binaries that represents each char in the mensage
    br = False; # break point
    i = 1; #
    n = "";
    text = "" # result

    for x in range(0,criptImgWitdth - math.trunc(criptImgWitdth*0)): # run all x pixels of image
        numss = "";
        if br:
            break;
        for y in range(0,criptImgHeigth - math.trunc(criptImgHeigth*0)):# run all y pixels of image
            # calculate the module of diference of each color of each pixel of the images
            num = int(math.copysign(criptImg.getpixel( (x,y) )[0] - keyImg.getpixel( (x,y) )[0],0.0))
            num1 = int(math.copysign(criptImg.getpixel( (x,y) )[1] - keyImg.getpixel( (x,y) )[1],0.0))
            num2 = int(math.copysign(criptImg.getpixel( (x,y) )[2] - keyImg.getpixel( (x,y) )[2],0.0))
            if num == bPColor*bPColor : # analize if it's the last piece of bit in mensage
                br = True;
                break;
            nums.append(num) # add red color diference in array
            if num1 == bPColor*bPColor : # analize if it's the last piece of bit in mensage
                br = True;
                break;
            nums.append(num1) # add green color diference in array
            if num2 == bPColor*bPColor : # analize if it's the last piece of bit in mensage
                br = True;
                break;
            nums.append(num2) # add blue color diference in array
        if br: # break if last pixel
            print("break")
            break;
    for num in nums: # run each piece of bit found
        if i%(8/bPColor)==0: # if is the last piece of binary of the 8-bit binary
            aux = "{0:b}".format(num)
            aux = (bPColor - len(aux))*"0" + aux
            n +=aux
            bins.append(n) # Append formatted bit with len = 8
            n = ""
        else:
            aux = "{0:b}".format(num)
            aux = (bPColor - len(aux))*"0" + aux
            n +=aux
        i+=1

    for bin in bins: # run each 8-bit binary
        text+=chr(int(bin,2)) #convert each 8-bit binary to char
    text = bytes(text, 'utf-8')
    text = repr(text.decode('unicode-escape'))
    print(text)
else:
    print("Invalid Key!")
