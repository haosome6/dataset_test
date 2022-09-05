import torch, torchvision

hmdb51 = torchvision.datasets.HMDB51('./hmdb51/', './testTrainMulti_7030_splits/', 5, 5)

print(hmdb51[0])