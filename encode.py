# -*- coding: utf-8 -*-

#####################################################################
#   Creator: Lucas Avelino
#   Description: The main porpuse of this code is to learn about encripting
#   messages inside Images.
#
#####################################################################
import os
from PIL import Image as img

bitsPorCor = 4

for filename in os.listdir(os.getcwd()):
    if ".png" in filename:
        picture = img.open(filename)
        w = picture.size[0];
        h = picture.size[1];
        msgPosition = 0;
        picture.show()
        msgUtf = open("msg/a.txt","r",encoding = "utf8").read() # get Text
        msg = list(map(bin,bytearray(ascii(msgUtf),encoding = "utf8"))) # convert to array of binaries
        msg1 = []
        for bin in msg: # convert to array of binaries
            aux = bin.replace('0b','')
            bin = bin.replace('0b','0'*(8-len(aux)))
            msg1 += ([int(bin[i:i+bitsPorCor],2) for i in range(0, len(bin), bitsPorCor)])
        msg = msg1
        msg.append(bitsPorCor*bitsPorCor)
        for x in range(0,w):
            for y in range(0,h):
                pixel = picture.getpixel((x,y))
                r,g,b = pixel
                if y == 0 and x == 0:
                    print(pixel)
                #-----red-----
                if pixel[0] <= bitsPorCor*bitsPorCor and (msgPosition) < len(msg):
                    r = pixel[0] + msg[msgPosition]
                else:
                    if (msgPosition) < len(msg):
                        r = pixel[0] - msg[msgPosition]
                #-----green-----
                if pixel[1] <=bitsPorCor*bitsPorCor and (msgPosition + 1) < len(msg):
                    g = pixel[1] + msg[msgPosition + 1]
                else:
                    if (msgPosition + 1) < len(msg):
                        g = pixel[1] - msg[msgPosition+1]
                #-----blue-----
                if pixel[2] <=bitsPorCor*bitsPorCor and (msgPosition + 2) < len(msg):
                    b = pixel[2] + msg[msgPosition + 2]
                else:
                    if (msgPosition + 2) < len(msg):
                        b = pixel[2] - msg[msgPosition + 2]
                picture.putpixel( (x,y), (r,g,b))
                msgPosition += 3
        picture.show();
        picture.save("enc/"+filename,quality=150)
