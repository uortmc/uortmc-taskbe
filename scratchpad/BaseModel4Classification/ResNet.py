import torch
import torch.nn as nn
import torchvision
from torch.nn import functional as F

class ResNet(nn.Module):
    def __init__(self, nf=32, label_size=7):
        super().__init__()
        self.main = torchvision.models.resnet18()
    def forward(self, imgs):
        imgs.unsqueeze_(0)
        imgs = F.interpolate(imgs,[224,224]).expand(-1,3,-1,-1)
        return self.main(imgs)[:,:2].squeeze()