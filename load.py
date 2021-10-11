from tensorflow import keras
import numpy as np
import cv2
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot as plt
model = keras.models.load_model('chest_xray_covid_unprocessed.h5')
model.compile(loss='categorical_crossentropy',

              optimizer='adam',

              metrics=['accuracy'])
test_datagen = ImageDataGenerator(rescale = 1./255)
test_set = test_datagen.flow_from_directory('2/test',
                                            target_size = (224, 224),
                                            batch_size = 8,
                                            class_mode = 'categorical')

model.evaluate(test_set)

img = cv2.imread('test.jpg')
cv2.imshow('img',img)
cv2.waitKey(0)


img = cv2.resize(img,(224,224))

img = np.reshape(img,[1,224,224,3])


classes = model.predict(img)

print (classes)

