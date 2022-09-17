import torch, torchvision, time
from datetime import timedelta
from torchvision import transforms
from torch import nn
import pdb

torch.manual_seed(0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

hmdb51 = torchvision.datasets.HMDB51('/mnt/c/Users/zhz/course_code/dataset_test/hmdb51/', '/mnt/c/Users/zhz/course_code/dataset_test/testTrainMulti_7030_splits/', 16, 5)
torch.save(hmdb51, '/mnt/c/Users/zhz/course_code/dataset_test/hmdb51_cache.pth')

# hmdb51 = torch.load('/mnt/c/Users/zhz/course_code/dataset_test/hmdb51_cache.pth')

hmdb51_loader = torch.utils.data.DataLoader(hmdb51, batch_size=1, shuffle=True)

for i, (data,_, target) in enumerate(hmdb51_loader):
    # pdb.set_trace()
    data = data.to(device)
    target = target.to(device)
    print(data.shape)
    print(i)



