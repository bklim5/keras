# Convolutional Neural Network for Crystallization Image Classification

protein-classifier.ipynb contains steps and comments on the classification of protein crystallization using CNN. A simple CNN and pre-trained model (Vgg16) has been used to demonstrate the effectiveness of CNN in this task.

You might need to download Vgg16 weights from public source for the script to run. One source is here: http://files.fast.ai/models/ vgg16.h5 file.

One step in the notebook is saving the weights after training with protein crystals image. With that, you can run protein.py with the saved weights to predict new images.

To predict new images, just 
```
python protein.py
```
and follow the instruction on screen (basically just entering the image file path)
