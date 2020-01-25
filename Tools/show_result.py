import numpy as np
import torch
import torch.utils.data as Data
from torch import nn
from model import Wcnn

"""
===========================================================
                Load Trained Model
===========================================================
"""
torch.cuda.set_device(1)
cnn = Wcnn.WCNN(num_token=100,num_class=2,kernel_sizes=[3, 7, 11, 15], kernel_nums=[256, 256, 256, 256])
#cnn = Wcnn.WCNN(num_token=100,num_class=20,kernel_sizes=[3, 7, 11, 15], kernel_nums=[256, 256, 256, 256], seq_len=244)
pretrained_dict=torch.load("Reject_params.pkl", map_location='cpu')
cnn.load_state_dict(pretrained_dict)

# Evaluation mode
cnn = cnn.eval()
cnn = cnn.cuda()

# Load embedding
torch_embeds = nn.Embedding(64, 100)
torch_embeds.load_state_dict(torch.load('embed.pkl', map_location='cpu'))
torch_embeds.weight.requires_grad=False


"""
===========================================================
                Load Validation Dataset
===========================================================
"""

val = np.genfromtxt('dataset/val.csv', delimiter=',')
#val = np.genfromtxt('dataset/family_validation.csv', delimiter=',')
val_label = val[:, -1]
val_feature = val[:, :-1]

val_feature = torch.from_numpy(val_feature).long()
val_label = torch.from_numpy(val_label).float()
val_feature = torch_embeds(val_feature)
val_feature = val_feature.reshape(len(val_feature), 1, 248, 100)


"""
===========================================================
                Record Confusion Matrix
===========================================================
"""
record = np.zeros((7, 7))
with torch.no_grad():
    for (feature, label) in zip(val_feature, val_label):
        pred = cnn(torch.unsqueeze(feature.cuda(), 0))
        pred = pred.cpu().detach().numpy()[0]
        y = int(np.argmax(pred))
        x = int(label)
        record[x, y] += 1


np.set_printoptions(suppress=True)
record
sum(record.diagonal())/sum(sum(record))



def softmax(x):
    return np.exp(x)/sum(np.exp(x))

record = np.zeros((7, 7))
with torch.no_grad():
    for (feature, label) in zip(val_feature, val_label):
        pred = cnn(torch.unsqueeze(feature.cuda(), 0))
        pred = pred.cpu().detach().numpy()[0]
        pred = softmax(pred)
        if max(pred) > 0.8:
            y = int(np.argmax(pred))
            x = int(label)
            record[x, y] += 1


np.set_printoptions(suppress=True)
record
sum(record.diagonal())/sum(sum(record))
