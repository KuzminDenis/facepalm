from __future__ import unicode_literals

from django.db import models
import cv2
import os
from django.conf import settings
#from .. import settings

def scale_image(img, size):
    rows, cols, _ = img.shape
    print cols, rows
    if cols > rows:
        dim = (size*cols/rows, size)
    else:
        dim = (size, size*rows/cols)
        
    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
class Palmer(models.Model):
    raw_image = models.ImageField(upload_to='photos')
    #processed_image = models.ImageField(upload_to='photos/processed', blank=True)
    
    def result_relative_url(self):
        return self.raw_image.url[1:-4] + '_processed.jpg'
    
    def result_absolute_url(self):
        return self.raw_image.url[:-4] + '_processed.jpg'
    
    def process(self):
        path = os.path.join(settings.BASE_DIR, self.raw_image.url[1:]) 
        print path
        img = cv2.imread(path)
        #img = cv2.imread(self.raw_image.url)
        
        #cv2.rectangle(img, (20,20), (100, 100), (0, 255, 0), 5)
        
        result_url = self.result_relative_url()

        face_cascade = cv2.CascadeClassifier('face_cascade.xml')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2) 
        scaled = scale_image(img, 500)
        cv2.imwrite(result_url, scaled)
        #processed_image = img
        return #img       
    
# Create your models here.
