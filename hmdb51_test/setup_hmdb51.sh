wget http://serre-lab.clps.brown.edu/wp-content/uploads/2013/10/hmdb51_org.rar
wget http://serre-lab.clps.brown.edu/wp-content/uploads/2013/10/test_train_splits.rar

mkdir -p hmdb51_dataset hmdb51_splits
~/bin/unrar e hmdb51_org.rar hmdb51_dataset
rm hmdb51_org.rar
~/bin/unrar e test_train_splits.rar hmdb51_splits
rm test_train_splits.rar

cd hmdb51_dataset
for f in *.rar; do
    ~/bin/unrar x "$f"
    rm "$f"
done