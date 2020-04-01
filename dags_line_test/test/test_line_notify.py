#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import requests

#create message
def lineNotify(message):
    payload = {'message':message}
    return _lineNotify(payload)

#create image file
def notifyFile(filename):
    file = {'imageFile':open(filename,'rb')}
    #payload = message
    payload = {'message': 'test'}
    return _lineNotify(payload,file)

#get picture url
def notifyPicture(url):
    payload = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
    return _lineNotify(payload)

#create sticker
def notifySticker(stickerID,stickerPackageID):
    payload = {'message':" ",'stickerPackageId':stickerPackageID,'stickerId':stickerID}
    return _lineNotify(payload)

#post data
def _lineNotify(payload,file=None):
    url = 'https://notify-api.line.me/api/notify'
    print(url)
    token = 'CqY5EbG4DNoRVNhpt08DtVZ6naINlfvqWGemv0aT7S1'
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers , data=payload, files=file)

# notifyFile('./logo.png')
# lineNotify('ทดสอบภาษาไทย hello')
# notifySticker(40,2)
# notifyPicture("https://www.honey.co.th/wp-content/uploads/2017/03/cropped-logo_resize.png")