wget --no-check-certificate https://www.crcv.ucf.edu/data/UCF101/UCF101.rar
wget --no-check-certificate https://www.crcv.ucf.edu/data/UCF101/UCF101TrainTestSplits-RecognitionTask.zip

unrar e UCF101.rar ucf101
rm UCF101.rar
unzip UCF101TrainTestSplits-RecognitionTask.zip 
rm UCF101TrainTestSplits-RecognitionTask.zip