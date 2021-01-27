import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = r'C:\Users\izzak\Desktop\opencv_tutorial\Resources\Faces\train'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

#p = []
#for i in os.listdir(r'C:\Users\izzak\Desktop\opencv_tutorial\Resources\Faces\train')
#    p.append(i)

#print(p)

features= []
labels = []

#train function
def create_train():
    #read through file with each person
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        #read image throu each person path
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            #read img and convert to grayscale
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            #recognize img
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            #append roi and label each img
            for (x, y, w, h) in faces_rect:
                #region of interest
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training done !')

features = np.array(features, dtype='object')
labels = np.array(labels)

#check features and labels
#print(f'Length of the features = {len (features)}')
#print(f'Length of the labels = {len (labels)}')

face_recognizer = cv.face.LBPHFaceRecognizer_create()

#Train the recognizer on the features list and the labels list
face_recognizer.train(features, labels)

#save as yml
face_recognizer.save('face_trained.yml')

#save to npy file
np.save('features.npy', features)
np.save('labels.npy', labels)