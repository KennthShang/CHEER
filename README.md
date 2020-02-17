# CHEER
CHEER is a novel hierarchical model, which can learn the species masking feature via deep learning classifier, for new RNA virus taxonomy classification

To use CHEER, you need to have two types of data. (1) reads set, such as viral metagenomic data containing reads from viruses. (2) pkl file, which are parameters for the model. For the parameters, you can download the pre-trained parameters in 'pkl' folder. 

Also, you can re-train CHEER on your own dataset. There are two types of parametrs need to be trained: (1) embedding layer. (2) CNN classifier. You need to train your embedding layer first following the paper, then use this embedding layer in CNN classifier. We provide the training environment for you to simplify the training procedure. 

## Required Dependencies
1. Python 3.x
2. numpy
3. Pytorch
4. cuda 10.1


## Use the pre-trained model
If you want to use the pre-trained model, please download the 'pkl' folder and make sure the pre-trained pkl files are in the folder. Then you can run CHEER follow the precedure shown bellow, make sure that at the every begining, you need to run `bash clean_all_script.sh` to clean the folder:

1. Put your reads set into validation folder in 'Classifier'
2. Run `bash code/pre_train_script.sh`. The script will run the pre-processing code one by one. If there is no error shown on your screen, you can move on.
3. Run `python show_result.py --gpus gpu_id --n num_of_class --kmers list_of_kmers --t threshold --embed embed_params --classifier classifier_params` in 'Classifier' folder. Then it will output two files named: **early_stop.txt** and **result.txt**. The format of these two files are **reads_id->label**. You can find the label in "pkl/corresponding id.xlsx" for each classifier.
4. Run `python split_data.py --input raw_reads_path` in 'Classifier' folder. Then it will output fasta files containing reads with same class in **prediction** folder.
5. If you want to continue the next taxa level, please use the output from step 4 and re-run step 1-3.

Detailed information of 'show_result.py'
There are six input parameters for 'show_result.py':
1. gpus: the id of gpu on your computer. Default is 1.
2. n: number of class of this classifier. This depending on which classifier you are using. You can check the supplymentary file in the paper for the n. Default is 5.
3. kmers: a list for the size of different kmers used in the classifier. In the pre-trained model, the default is [3, 7, 11, 15].
4. t: threshold for the SoftMax layer. Default is 0.6
5. embed: the pkl file for embedding layer
6. classifier: the pkl file for the classifier


## Train a new classifier
If you want to train a new classifier on your own training set, you can remove the pkl files in 'pkl' folder. Then you can train CHEER follow the precedure shown bellow:

1. Put your training set into train folder and validation set into validation folder in 'Classifier'. 
2. Run `bash code/re_train_script.sh`. The script will run the pre-processing code one by one. If there is no error shown on your screen, you can move on.
3. Run `python train.py --gpus gpu_id --n num_of_class --kmers list_of_kmers --weight weight_for_each_class --embed embed_params --classifier classifier_params` in 'Classifier' folder. Then it will output a 'result.txt' file shows the taxa of each read.

Detailed information of 'train.py'
There are six input parameters for 'show_result.py':
1. gpus: the id of gpu on your computer. Default is 1.
2. n: number of class of this classifier. This depending on which classifier you are using. You can check the supplymentary file in the paper for the n. Default is 5.
3. kmers: a list for the size of different kmers used in the classifier. In the pre-trained model, the default is [3, 7, 11, 15].
4. lr: threshold for the SoftMax layer. Default is 0.6
5. epoch: number of epoch for training. Default is 5
6. embed: the pkl file for embedding layer.
7. weight: if your dataset are unbalanced, you can use this params to train the model. 'Weight' stands for the coefficient of each class, so the size of the weight list should be equal to the number of class. Default: '1, 1, 1, 1, 1'



