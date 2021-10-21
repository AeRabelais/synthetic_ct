import os
import pandas as pd
import csv

from zipfile import ZipFile

padchest_zips = 'path where the padchest zip folders are held'
tb_image_ids = pd.read_csv('path of the tb image_ids')
nontb_image_ids = pd.read_csv('path of the non-tb image_ids')

for file_name in os.listdir(padchest_zips):
  if(file_name.endswith('.zip'):
     zip_file = padchest_zips + '/' + filename
     with ZipFile(zip_file, 'r') as zipObject:
        listOfFileNames = zipObject.namelist()
        for img in listOfFileNames:
           if img in tb_image_ids:
              zipObject.extract(img, path='tuberculosis_set')
              continue;
           elif img in nontb_image_ids:
              zipObject.extract(img, path='nontuberculosis_set')
              continue;
           else:
              continue;
            
     
     
     
     
     
