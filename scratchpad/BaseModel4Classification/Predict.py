# =========================================================================
# requerments: 
#   pytorch  version > 1.6.0  -- https://pytorch.org/get-started/locally/
# =========================================================================

import torch
from ResNet import ResNet

from PIL import Image
import torchvision.transforms as transforms


# if GPU is available, use GPU; otherwise use CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


# functions for loading image
image_transformer = transforms.Compose([
                        transforms.Grayscale(),
                        transforms.ToTensor(),
                        transforms.Normalize(0.5,0.5)
                    ])
def load_img(path):
    with open(path,'rb') as f:
        img = Image.open(f)
        img = image_transformer(img)
    # remove the margin of the img. 
    # If the img is not the corpus img, you mey need to re consider the following parameter
    img = transforms.functional.crop(img, 8,87,301,385)

    # if you want to print the croped image, you can uncommentt the following lines.
    # import torchvision.utils as vutils
    # vutils.save_image(img.add(1).div(2), f'test.jpg', nrow=1, padding=4)
    return img


model = ResNet(label_size=2)
model.load_state_dict(torch.load(f'resnet18.tch', map_location=torch.device('cpu')))
model.eval()
model = model.to(device)


# example of prediction
img = load_img('example_imgs/554_1.jpg')
prediction = model(img).argmax().item()

if prediction==0:
    print('Benign')
elif prediction==1:
    print('Malignant')
