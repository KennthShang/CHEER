import torch
from torch import nn
import torch.nn.functional as F
from torch.autograd import Variable
from torch.nn.parallel.data_parallel import data_parallel

class WCNN(nn.Module):
    def __init__(self, num_class=20, num_token=4, seq_len=250, kernel_nums=[256, 256, 256, 256],
                 kernel_sizes=[3, 7, 11, 15], dropout=0.5, num_fc1=1024, num_fc2=512):
        super(WCNN, self).__init__()

        self.num_token = num_token
        self.seq_len = seq_len
        self.num_class = num_class
        self.channel_in = 1
        self.kernel_nums = kernel_nums
        self.kernel_sizes = kernel_sizes
        self.dropout_rate = dropout

        self.convs1 = nn.ModuleList(
            [nn.Conv2d(self.channel_in, self.kernel_nums[i], (kernel_size, self.num_token)) for i, kernel_size in
             enumerate(self.kernel_sizes)])
        self.convs2 = nn.ModuleList(
            [nn.Conv2d(self.channel_in, self.kernel_nums[i], (kernel_size, self.num_token)) for i, kernel_size in
             enumerate(self.kernel_sizes)])
        self.convs3 = nn.ModuleList(
            [nn.Conv2d(self.channel_in, self.kernel_nums[i], (kernel_size, self.num_token)) for i, kernel_size in
             enumerate(self.kernel_sizes)])
        self.convs4 = nn.ModuleList(
            [nn.Conv2d(self.channel_in, self.kernel_nums[i], (kernel_size, self.num_token)) for i, kernel_size in
             enumerate(self.kernel_sizes)])
        self.convs5 = nn.ModuleList(
            [nn.Conv2d(self.channel_in, self.kernel_nums[i], (kernel_size, self.num_token)) for i, kernel_size in
             enumerate(self.kernel_sizes)])
        self.convs6 = nn.ModuleList(
            [nn.Conv2d(self.channel_in, self.kernel_nums[i], (kernel_size, self.num_token)) for i, kernel_size in
             enumerate(self.kernel_sizes)])
        
        self.dropout = nn.Dropout(self.dropout_rate)
        self.fc1 = nn.Linear(sum(self.kernel_nums)*6, num_fc1)
        self.fc2 = nn.Linear(num_fc1, num_fc2)
        self.out = nn.Linear(num_fc2, self.num_class)

    def forward(self, x):
        x1 = x[:,0,:,:].reshape(len(x), 1, -1, 100)
        x2 = x[:,1,:,:].reshape(len(x), 1, -1, 100)
        x3 = x[:,2,:,:].reshape(len(x), 1, -1, 100)
        x4 = x[:,3,:,:].reshape(len(x), 1, -1, 100)
        x5 = x[:,4,:,:].reshape(len(x), 1, -1, 100)
        x6 = x[:,5,:,:].reshape(len(x), 1, -1, 100)
        
        
        
        x1 = [F.relu(conv(x1)).squeeze(3) for conv in self.convs1]
        x2 = [F.relu(conv(x2)).squeeze(3) for conv in self.convs2]
        x3 = [F.relu(conv(x3)).squeeze(3) for conv in self.convs3]
        x4 = [F.relu(conv(x4)).squeeze(3) for conv in self.convs4]
        x5 = [F.relu(conv(x5)).squeeze(3) for conv in self.convs5]
        x6 = [F.relu(conv(x6)).squeeze(3) for conv in self.convs6]
        
        
        
        x1 = [F.max_pool1d(i, i.size(2)).squeeze(2) for i in x1]
        x2 = [F.max_pool1d(i, i.size(2)).squeeze(2) for i in x2]
        x3 = [F.max_pool1d(i, i.size(2)).squeeze(2) for i in x3]
        x4 = [F.max_pool1d(i, i.size(2)).squeeze(2) for i in x4]
        x5 = [F.max_pool1d(i, i.size(2)).squeeze(2) for i in x5]
        x6 = [F.max_pool1d(i, i.size(2)).squeeze(2) for i in x6]
        
        x1 = torch.cat(x1, 1)
        x2 = torch.cat(x2, 1)
        x3 = torch.cat(x3, 1)
        x4 = torch.cat(x4, 1)
        x5 = torch.cat(x5, 1)
        x6 = torch.cat(x6, 1)
        
        x = torch.cat((x1, x2, x3, x4, x5, x6), 1)

        x = self.dropout(x)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        output = self.out(x)
        return output  
