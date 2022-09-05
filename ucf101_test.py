import torch, torchvision, time

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

ucf101 = torchvision.datasets.UCF101('./ucf101/', './ucfTrainTestlist/', 5, 5)

ucf101_loader = torch.utils.data.DataLoader(ucf101, batch_size=256, shuffle=True, num_workers=1)

start = time.time()
print(start)

for i, (data, target) in enumerate(ucf101_loader):
    data = data.to(device)
    target = target.to(device)
    print(i)

end = time.time()
print(end - start)