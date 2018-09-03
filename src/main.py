import  os
import argparse
import torch

def GenerateDataSetWithGAN():
    pass

def TrainCNN():
    pass

def TrainDEM():
    pass

def ParseArgs():
    parser = argparse.ArgumentParser()

    parser.add_argument('--gpu_id', default=0, help='GPU ID to use, e.g. \'0\'', type=int)
    parser.add_argument('--workPath', default=None, help='Give me the path your project located', type=str)


    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()

    gpuId, workPath = arg.gpu_id, arg.workPath

    os.chdir(workPath)
    if gpuId == 0:
        print('train process begin on cpu')
        torch.device('cpu')
    else:
        print(f'train process begin on GPU{gpuId}')
        torch.device(f'cuda:{gpuId}')

    GenerateDataSetWithGAN()

    model = TrainCNN()

    DEM = TrainDEM()

    DSE.predict()