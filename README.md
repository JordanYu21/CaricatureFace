# CaricatureFace
This repository includes source code, pretrained model and a 3D dataset of paper "Landmark Detection and 3D Face Reconstruction for Caricature using a Nonlinear Parametric Model", *Graphical Models* (2021), [http://arxiv.org/abs/2004.09190](http://arxiv.org/abs/2004.09190).

Authors: [Hongrui Cai](https://rainbowrui.github.io/), [Yudong Guo](https://yudongguo.github.io/), Zhuang Peng and [Juyong Zhang](http://staff.ustc.edu.cn/~juyong/).

Note that all of the code is protected under patent. It can be only used for research purposes. If you are interested in business purposes/for-profit use, please contact Juyong Zhang (the corresponding author, email: juyong@ustc.edu.cn).

## Prerequisites and Installation
- Python 3.7
- Pytorch
- opencv-python 3.4.2

### Getting Started
**Clone this repository:**
```bash
git clone git@github.com:Juyong/CaricatureFace.git
cd CaricatureFace
```
**Install dependencies using Anaconda:**
 ```bash
conda create -n cariface python=3.7
source activate cariface
pip install -r requirements.txt
```

## Advanced Work
**Prepare related data:**
- You can download related data for alogorithm here [Google Drive](https://drive.google.com/open?id=11m9dC6j-SUyjhtSiXsUqiBdZOQ3S8phD), or [Baidu Drive](https://pan.baidu.com/s/1v4V-7rYszDhyhzhCH2aYeA) with password: tjps.
- Unzip downloaded files and move files into ```./data``` directory.

**Prepare pretrained model:**
- You can download pretrained model here [Google Drive](https://drive.google.com/open?id=1If_rjQp5mDZMbK1-STGYOPyw_cTG66jO), or [Baidu Drive](https://pan.baidu.com/s/113QFM-zhSUIZfzjFhQfTTA) with password: fukf.
- Unzip downloaded files and move files into ```./model``` directory.

**Prepare some examples:**
- You can download some examples here [Google Drive](https://drive.google.com/open?id=1X8TpVpGzRrQuSS93_Hb32ERU-P4q6SSG), or [Baidu Drive](https://pan.baidu.com/s/1fn6Ll3ogF5LrYByBe-T5Ew) with password: sq06.
- Unzip downloaded files and move files into ```./exp``` directory.

  ** THESE MUST BE PLACED INTO THE EXACT PATH DIRECTORY **



## Test with Pretrained Model
Within ```./CaricatureFace``` directory, run following command:
 ```bash
    bash test.sh
```

***alternatively ***

Within ```./CaricatureFace``` directory, run following command:
```
python train.py --no_train --landmark_num 68 --vertex_num 6144 --device_num 0 --data_path "data/" --test_image_path "exp/test_images.txt" --test_landmark_path "exp/test_landmarks.txt" --test_lrecord_path "exp/test_lrecord.txt" --test_vrecord_path "exp/test_vrecord.txt" --resnet34_lr 1e-4 --mynet1_lr 1e-5 --mynet2_lr 1e-8 --model1_path "model/resnet34_adam.pth" --model2_path "model/mynet_adam.pth" --premodel
```

Note: Input images must be preprocessed - crop the whole face roughly and resize to size (224, 224).

## Recover 3D faces
Within ```./CaricatureFace``` directory, run command:
```
python vertex_to_mesh2.py
```
The 3D meshes will be generated as .obj files in the vertex_results folder additionally the caricatures w/ landmarked labels will be generated as .jpg files in the landmark_results folder. 

## Calculate error
Within ```./CaricatureFace``` directory, run command:
'''
python cal_error.py
'''

## Citation

```
@article{cai2021landmark,
  title={Landmark detection and 3D face reconstruction for caricature using a nonlinear parametric model},
  author={Cai, Hongrui and Guo, Yudong and Peng, Zhuang and Zhang, Juyong},
  journal={Graphical Models},
  volume={115},
  pages={101103},
  year={2021},
  publisher={Elsevier}
}
``` 
