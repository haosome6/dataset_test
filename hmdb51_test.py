import torch, torchvision, time
from datetime import timedelta
from torchvision import transforms
from torch import nn

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

transform = transforms.Compose([transforms.Lambda(lambda x: x / 255.),
                                transforms.Resize((240, 320))])

hmdb51 = torchvision.datasets.HMDB51('./hmdb51/', './testTrainMulti_7030_splits/', 16, 5, transform=transform)

hmdb51_loader = torch.utils.data.DataLoader(hmdb51, batch_size=1, shuffle=True)

for i, (data,_, target) in enumerate(hmdb51_loader):
    data = data.to(device)
    target = target.to(device)
    print(data.shape)
    print(i)



