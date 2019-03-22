# Style Classification into Machine Printed and Handwritten Text

> Keras implementation of Faster R-CNN to classify text into Machine Printed and Handwritten Text

![](https://github.com/mohammaduzair9/Style-Classification/blob/master/result_images/4.png)

## Getting Started

### Prerequisites
*	numpy
```shell
$ pip install numpy
```
*	h5py
```shell
$ pip install h5py
```
*	opencv-python
```shell
$ pip install opencv-python
```
*	sklearn
```shell
$ pip install scikit-learn
```
*	Keras==2.0.3 (Both theano and tensorflow backends are supported. However tensorflow is recommended)
```shell
$ pip install Keras==2.0.3
```
*	Tensorflow 
```shell
$ pip install Tensorflow
```

### Trained Model
Trained model can be downloaded from: https://drive.google.com/drive/folders/1SmDLcv-8HRbJwqSecHZKL121PishXb1v?usp=sharing

### How to run Training:
-  Copy pretrained weights for resnet50 (resnet50_weights_tf_dim_ordering_tf_kernels.h5) in Style-Classification directory.

- `train_frcnn.py` can be used to train a model. To train the data, it must be in PASCAL VOC format. To train simply do: 
```shell
$ python train_frcnn.py -p /path/to/train_data/
```

- Running `train_frcnn.py` will write weights to disk to an hdf5 file, as well as all the setting of the training run to a `pickle` file. These settings can then be loaded by `test_frcnn.py` for any testing.


### How to run Testing:
-  Copy trained model(model_frcnn.hd5) and config.pickle file in Style-Classification diectory.

- `test_frcnn.py` can be used to perform inference, given pretrained weights and a config file. Specify a path to the folder containing images:
```shell
$ python test_frcnn.py -p /path/to/test_data/
```



## CREDITS
This code is inspired from https://github.com/yhenon/keras-frcnn
