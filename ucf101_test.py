import torch, torchvision, time
from datetime import timedelta
from torchvision import transforms
from torch import nn

torch.manual_seed(0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

ucf101 = torchvision.datasets.UCF101('./ucf101/', './ucfTrainTestlist/', frames_per_clip=16, step_between_clips=2, fold=1, train=True)

ucf101_loader = torch.utils.data.DataLoader(ucf101, batch_size=16, shuffle=True)

start_time = time.monotonic()

for i, (data,_, target) in enumerate(ucf101_loader):
    data = data.to(device)
    target = target.to(device)
    print(i)

end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))