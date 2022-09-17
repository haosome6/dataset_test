import torch, torchvision
from torchvision import transforms
import os

torch.manual_seed(0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

if os.path.exists('./ucf101_cache'):
    print('Loading from cache...')
    ucf101 = torch.load('./ucf101_cache')
else:
    print('Loading from disk...')
    ucf101 = torchvision.datasets.UCF101('./ucf101/', './ucfTrainTestlist/', frames_per_clip=16, step_between_clips=2, fold=1, train=True)
    torch.save(ucf101, './ucf101_cache')


ucf101_loader = torch.utils.data.DataLoader(ucf101, batch_size=1, shuffle=True)

cat_result = None
row_result = None

for i, (data,_, target) in enumerate(ucf101_loader):
    assert data.shape == (1, 16, 240, 320, 3)

    data = torch.squeeze(data, 0) # (16, 240, 320, 3)
    if row_result is None:
        row_result = data
    else:
        row_result = torch.cat((row_result, data), 2)
    
    if (i + 1) % 10 == 0:
        if cat_result is None:
            cat_result = row_result
        else:
            cat_result = torch.cat((cat_result, row_result), 1)
        row_result = None
    
    if (i + 1) % 100 == 0:
        break

torchvision.io.write_video('ucf101_video_test.mp4', cat_result, fps=4)
