## KERAS FRCNN
Keras implementation of Faster R-CNN for style Classification (Machine Printed VS Handwritten Text)

## STYLE CLASSIFICATION
This is keras FRCNN implementation to train a model for detecting text from scene_images/documents and classify them either as machine machine and Handwritten text. Model is trained using COCO dataset.

### REQUIREMENTS:
h5py
numpy
opencv-python
sklearn
Keras==2.0.3 (Both theano and tensorflow backends are supported. However tensorflow is recommended)

### TRAINED MODEL
Trained model can be downloaded from: https://drive.google.com/open?id=0B2VodxaPfDISUFVoclg1MHpvNlk

### HOW TO RUN TRAINING:
-  Copy pretrained weights for resnet50 (resnet50_weights_tf_dim_ordering_tf_kernels.h5) in Style_Classification directory.

- `train_frcnn.py` can be used to train a model. To train the data must be in PASCAL VOC format. To train simply do: 
     `python train_frcnn.py -p /path/to/train_data/`. 

- Running `train_frcnn.py` will write weights to disk to an hdf5 file, as well as all the setting of the training run to a `pickle` file. These
settings can then be loaded by `test_frcnn.py` for any testing.


### HOW TO RUN TESTING:
-  Copy trained model(model_frcnn.hd5) and config.pickle file in Style_Classification diectory.


- `test_frcnn.py` can be used to perform inference, given pretrained weights and a config file. Specify a path to the folder containing
images:
 `python test_frcnn.py -p /path/to/test_data/`


### CREDITS
This code is inspired from https://github.com/yhenon/keras-frcnn
