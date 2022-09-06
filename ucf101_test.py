import torch, torchvision, time
from datetime import timedelta
from torchvision import transforms
from torch import nn

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

tfs = transforms.Compose([
            # TODO: this should be done by a video-level transfrom when PyTorch provides transforms.ToTensor() for video
            # scale in [0, 1] of type float
            transforms.Lambda(lambda x: x / 255.),
            # reshape into (T, C, H, W) for easier convolutions
            transforms.Lambda(lambda x: x.permute(0, 3, 1, 2)),
            # rescale to the most common size
            transforms.Lambda(lambda x: nn.functional.interpolate(x, (240, 320)))])

ucf101 = torchvision.datasets.UCF101('./ucf101/', './ucfTrainTestlist/', frames_per_clip=16, step_between_clips=2, fold=1, train=True, transform=tfs)

def custom_collate(batch):
    filtered_batch = []
    for video, _, label in batch:
        filtered_batch.append((video, label))
    return torch.utils.data.dataloader.default_collate(filtered_batch)


ucf101_loader = torch.utils.data.DataLoader(ucf101, batch_size=16, shuffle=True, collate_fn=custom_collate)

start_time = time.monotonic()

for i, (data,_, target) in enumerate(ucf101_loader):
    data = data.to(device)
    target = target.to(device)
    print(i)

end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))