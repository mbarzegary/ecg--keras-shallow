# ECG  Signals Classification with Federated-Learning and Differential Privacy in Keras, Shallow Implementation

This repository contains a lightweight version of the [previously developed code](https://github.com/mbarzegary/ecg-classification) for classification of ECG signals, reimplemented using Keras instead of scikit-learn, which also includes a basic implementation of federated learning and differential privacy techniques for privacy-preserving machine learning. The [TensorFlow Federated](https://github.com/tensorflow/federated) and [TensorFlow Privacy](https://github.com/tensorflow/privacy) libraries were used to accomplish this. It can be a good learning resource to see how to employ privacy-preserving machine learning in a practical case.

## Getting started

The code depends on Keras and TensorFlow, but as the implemented model is a shallow neural network model, it's not necessary to have TensorFlow-GPU installed. After installing these components (which will accordingly install the required dependencies), the code can be executed by running `run_train.py`. The normal, differential privacy, and federated learning training routines are implemented in different functions, so the proper method should be uncommented in `run_train.py`.
