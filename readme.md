# Cerebellar fissure segmentation with convolutional neural networks.

### Here we use U-Net for performing cerebellar fissure segmentation from magnetic resonance imaging.

### Folder images/ contains the 24 original MRIs we used for the dataset creation.
### Folder src/ conrains the code for the dataset creation. Code is beeing actually pruned.


### Requirements (easy install from jupyter notebook):

!pip install deepbrain

!pip install pydicom==2.0.0
!pip install elasticdeform
!pip install bezier

!pip uninstall -y keras-nightly
!pip uninstall -y keras
!pip uninstall -y tensorflow
!pip install h5py==2.9.0

!pip install tensorflow-gpu==2.0.0 --no-cache
!pip install Keras==2.3.1 --no-cache

!pip uninstall SimpleITK
!pip install --upgrade --pre SimpleITK --find-links https://github.com/SimpleITK/SimpleITK/releases/tag/latest

!pip uninstall -y nibabel
!pip install nibabel==3.1.1

!pip install nilearn
!pip install git+https://www.github.com/keras-team/keras-contrib.git

!pip install descartes==1.1.0