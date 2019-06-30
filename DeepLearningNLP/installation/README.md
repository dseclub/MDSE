# Installation Deep Learning & NLP

## Table of Contents

  - [Anaconda](#anaconda)
    - [Conda](#conda)
    - [Jupyter notebook](http://jupyter.org/)
    - [Nbviewer](https://nbviewer.jupyter.org/)
  - [VirtualEnv](#virtualenv)
  - [Google Colab](#colab)
  - [Installing CUDA](#cuda)

  - [Installing NLTK](#nltk)
  - [Installing Spacy](#spacy)

##  Anaconda
Anaconda is a Python (and other languages including R) distribution that aims to provide everything needed for common scientific and machine learning situations out-of-the-box. We chose Anaconda for this tutorial as it significantly simplifies Python dependency management. Anaconda can be used to manage different environment and packages. This setup document will assume that you have Anaconda installed as your default Python distribution.
You can download Anaconda here: https://www.continuum.io/downloads

After installing Anaconda, you can access its command-line interface with the conda command.

## Conda
https://conda.io/docs/ https://www.anaconda.com/download/

https://conda.io/docs/user-guide/getting-started.html

https://conda.io/docs/user-guide/tasks/manage-environments.html


Windows / Linux
```
$ conda create -n dl_nlp36 python=3.6
$ conda (source) activate dl_nlp36
```

### Install packages from txt file with pip
```
$ pip install -r requirements.txt
```

## Other useful commands and links
```
$ conda install pandas  #install one package
$ deactivate (source deactivate)
```

### To check conda environments
```
$ conda info --envs
```

### Create install file
```
$ pip freeze > req.txt
```

### to export a yaml specification file, containing the detailed dependencies of your environment
```
$ conda env export > environment.yaml
$ more environment.yaml
```

### Install from yaml
```
$ conda env create -f environment.yaml
```

### Old instruction of installation. Ref
[installation tensorflow keras](installation_tensorflow_keras.txt)

## VirtualEnv

Python virtualenv Ubuntu
```
$ sudo pip install virtualenv myenv    # if error   sudo apt install python-pip
$ sudo apt-get update
$ virtualenv myenv
$ source myenv/bin/activate          # deactivate
```

http://docs.python-guide.org/en/latest/dev/virtualenvs/

https://virtualenv.pypa.io/en/stable/

https://packaging.python.org/guides/installing-using-pip-and-virtualenv/


Tensorflow GPU  https://www.tensorflow.org/install/gpu
```
tensorflow-gpu
```

## Colab
https://towardsdatascience.com/getting-started-with-google-colab-f2fff97f594c

https://medium.com/deep-learning-turkey/google-colab-free-gpu-tutorial-e113627b9f5d

https://www.kdnuggets.com/2018/02/google-colab-free-gpu-tutorial-tensorflow-keras-pytorch.html

Colab GPU

https://colab.research.google.com/notebooks/gpu.ipynb



## Kaggle GPU

https://www.kaggle.com/dansbecker/running-kaggle-kernels-with-a-gpu

## CUDA

Will be updated

Installing CUDA (optional)
NOTE: CUDA is currently not supported out of the conda package control manager


https://medium.com/@zhanwenchen/install-cuda-and-cudnn-for-tensorflow-gpu-on-ubuntu-79306e4ac04e

https://medium.com/@zhanwenchen/install-cuda-9-2-and-cudnn-7-1-for-tensorflow-pytorch-gpu-on-ubuntu-16-04-1822ab4b2421

Install NVIDIA Driver and CUDA.md
https://gist.github.com/wangruohui/df039f0dc434d6486f5d4d098aa52d07

https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html



## NLTK

https://www.nltk.org/install.html

## spaCy

https://spacy.io/usage/


### Install spaCy
```
$ conda install -c conda-forge spacy  
```
