import torch
from net import MyLeNet5
from torch.autograd import Variable
from torchvision import datasets, transforms
from torchvision.transforms import ToPILImage

# 数据转化为tensor格式
data_transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize(28),
    transforms.ToTensor()
]
)

# 加载训练数据集
train_dataset = datasets.ImageFolder(root='D:/personal_srcs/IcDesignandDebug/lpr_data', transform=data_transform)
train_dataloader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=16, shuffle=True)

# 加载测试数据集
test_dataset = datasets.ImageFolder(root='D:/personal_srcs/IcDesignandDebug/lpr_data', transform=data_transform)
test_dataloader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=16, shuffle=True)

device = "cuda" if torch.cuda.is_available() else "cpu"

# 调用网络模型
model = MyLeNet5().to(device)

model.load_state_dict(torch.load('D:/personal_srcs/IcDesignandDebug/lpr_model/lpr_model.pth'))

# 获取结果
classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           '川', '鄂', '赣', '甘', '贵', '桂', '黑', '沪', '冀', '津', '京', '吉', '辽', '鲁', '蒙',
           '闽', '宁', '青', '琼', '陕', '苏', '晋', '皖', '湘', '新', '豫', '渝', '粤', '云', '藏', '浙']

# tensor转化为图片
show = ToPILImage()


test_dataset = datasets.ImageFolder(root='D:/personal_srcs/IcDesignandDebug/infer_data', transform=data_transform)
test_dataloader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=16, shuffle=True)
# 进入验证
# for i in range(5):
#     X, y = test_dataset[i+10000][0], test_dataset[i+10000][1]
#     show(X).show()
#
#     X = Variable(torch.unsqueeze(X, dim=0).float(), requires_grad=False).to(device)
#     with torch.no_grad():
#         pred = model(X)
#         predicted, actual = classes[torch.argmax(pred[0])], classes[y]
#         print(f'predicted: f"{predicted}", actual:"{actual}"')

for i in range(10):
    X, y = test_dataset[i][0], test_dataset[i][1]
    show(X).show()

    X = Variable(torch.unsqueeze(X, dim=0).float(), requires_grad=False).to(device)
    with torch.no_grad():
        pred = model(X)
        predicted, actual = classes[torch.argmax(pred[0])], classes[y]
        print(f'predicted: f"{predicted}", actual:"{actual}"')
