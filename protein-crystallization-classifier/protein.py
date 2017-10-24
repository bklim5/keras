import numpy as np
import os
from vgg16 import Vgg16
from matplotlib import pyplot as plt
from keras import backend as K
from PIL import Image


K.set_image_dim_ordering('th')

if __name__ == '__main__':
    print 'Creating new vgg instance...'
    vgg = Vgg16()
    print 'Loading trained weights...'
    vgg.model.load_weights('protein.h5')
    classes = ['gotcrystal', 'nocrystal']

    plt.ion()
    while True:
        print 'Enter image path: '
        path = raw_input()
        try:
            img = Image.open(path)
            resized_img = img.resize((224, 224))
            test_data = np.asarray(resized_img)
            test_data = np.rollaxis(test_data, 2, 0)  # change to 3x224x224 format
            test_data = np.reshape(test_data, (-1, test_data.shape[0], test_data.shape[1], test_data.shape[2]))
            
            print 'Predicting image...'
            prediction = vgg.model.predict(test_data)
            index = np.argmax(prediction, axis=1)
            predicted_class = classes[index[0]]
            probability = prediction[0, index][0]
            print 'Predicted label: {} with probability {}'.format(predicted_class, probability)
            plt.imshow(img)
        except IOError:
            print 'No such file or directory, type in another file path'
    