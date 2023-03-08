from pynq import Overlay

overlay = Overlay('/home/xilinx/jupyter_notebooks/LPR/overlay/cnn.bit')
overlay?

import time
import numpy as np
import cv2
from pynq import allocate
import os

def RunConv(conv,Kx,Ky,Sx,Sy,mode,relu_en,feature_in,W,bias,feature_out):
    conv.write(0x10,feature_in.shape[2])
    conv.write(0x18,feature_in.shape[0])
    conv.write(0x20,feature_in.shape[1])
    conv.write(0x28,feature_out.shape[2])
    conv.write(0x30,Kx)
    conv.write(0x38,Ky)
    conv.write(0x40,Sx)
    conv.write(0x48,Sy)
    conv.write(0x50,mode)
    conv.write(0x58,relu_en)
    conv.write(0x60,feature_in.physical_address)
    conv.write(0x68,W.physical_address)
    conv.write(0x70,bias.physical_address)
    conv.write(0x78,feature_out.physical_address)
    conv.write(0, (conv.read(0)&0x80)|0x01 )
    tp=conv.read(0)
    while not ((tp>>1)&0x1):
        tp=conv.read(0)
    #print(tp);

def RunPool(pool, Kx, Ky, Sc, Sx, Sy, mode, feature_in, feature_out):
    pool.write(0x10, feature_in.shape[2])
    pool.write(0x18, feature_in.shape[0])
    pool.write(0x20, feature_in.shape[1])
    pool.write(0x28, Kx)
    pool.write(0x30, Ky)
    pool.write(0x38, Sc)
    pool.write(0x40, Sx)
    pool.write(0x48, Sy)
    pool.write(0x50, mode)
    pool.write(0x58, feature_in.physical_address)
    pool.write(0x60, feature_out.physical_address)
    pool.write(0, (pool.read(0) & 0x80) | 0x01)
    while not ((pool.read(0) >> 1) & 0x1):
        pass;
# Conv1
IN_WIDTH1 = 28
IN_HEIGHT1 = 28
IN_CH1 = 1

KERNEL_WIDTH1 = 5
KERNEL_HEIGHT1 = 5
X_STRIDE1 = 1
Y_STRIDE1 = 1

RELU_EN1 = 1
MODE1 = 1    # 0:VALID, 1:SAME
X_PADDING1 = 2
Y_PADDING1 = 2

OUT_CH1 = 6
OUT_WIDTH1 = int((IN_WIDTH1+2*X_PADDING1-KERNEL_WIDTH1)/X_STRIDE1+1)
OUT_HEIGHT1 = int((IN_HEIGHT1+2*Y_PADDING1-KERNEL_HEIGHT1)/Y_STRIDE1+1)

# Avgpool1
MODE_p1 = 0  # mode: 0:MEAN, 1:MAX
IN_WIDTH_p1 = OUT_WIDTH1
IN_HEIGHT_p1 = OUT_HEIGHT1
IN_CH_p1 = OUT_CH1

KERNEL_WIDTH_p1 = 2
KERNEL_HEIGHT_p1 = 2
C_STRIDE_p1 = 1
X_STRIDE_p1 = 2
Y_STRIDE_p1 = 2

OUT_CH_p1 = IN_CH_p1
OUT_WIDTH_p1 = int(IN_WIDTH_p1 / KERNEL_WIDTH_p1)
OUT_HEIGHT_p1 = int(IN_HEIGHT_p1 / KERNEL_HEIGHT_p1)

# Conv2
IN_WIDTH2 = OUT_WIDTH_p1
IN_HEIGHT2 = OUT_HEIGHT_p1
IN_CH2 = OUT_CH_p1

KERNEL_WIDTH2 = 5
KERNEL_HEIGHT2 = 5
X_STRIDE2 = 1
Y_STRIDE2 = 1

RELU_EN2 = 1
MODE2 = 0  # 0:VALID, 1:SAME
X_PADDING2 = 0
Y_PADDING2 = 0

OUT_CH2 = 16
OUT_WIDTH2 = int((IN_WIDTH2 + 2 * X_PADDING2 - KERNEL_WIDTH2) / X_STRIDE2 + 1)
OUT_HEIGHT2 = int((IN_HEIGHT2 + 2 * Y_PADDING2 - KERNEL_HEIGHT2) / Y_STRIDE2 + 1)

# Avgpool2
MODE_p2 = 0  # mode: 0:MEAN, 1:MAX
IN_WIDTH_p2 = OUT_WIDTH2
IN_HEIGHT_p2 = OUT_HEIGHT2
IN_CH_p2 = OUT_CH2

KERNEL_WIDTH_p2 = 2
KERNEL_HEIGHT_p2 = 2
C_STRIDE_p2 = 1
X_STRIDE_p2 = 2
Y_STRIDE_p2 = 2

OUT_CH_p2 = IN_CH_p2
OUT_WIDTH_p2 = int(IN_WIDTH_p1 / KERNEL_WIDTH_p1)
OUT_HEIGHT_p2 = int(IN_HEIGHT_p1 / KERNEL_HEIGHT_p1)

# Conv3
IN_WIDTH3 = OUT_WIDTH_p2
IN_HEIGHT3 = OUT_HEIGHT_p2
IN_CH3 = OUT_CH_p2

KERNEL_WIDTH3 = 5
KERNEL_HEIGHT3 = 5
X_STRIDE3 = 1
Y_STRIDE3 = 1

RELU_EN3 = 0
MODE3 = 0  # 0:VALID, 1:SAME
X_PADDING3 = 0
Y_PADDING3 = 0

OUT_CH3 = 120
OUT_WIDTH3 = int((IN_WIDTH3 + 2 * X_PADDING3 - KERNEL_WIDTH3) / X_STRIDE3 + 1)
OUT_HEIGHT3 = int((IN_HEIGHT3 + 2 * Y_PADDING3 - KERNEL_HEIGHT3) / Y_STRIDE3 + 1)

# dense
IN_WIDTH4 = OUT_WIDTH3
IN_HEIGHT4 = OUT_HEIGHT3
IN_CH4 = OUT_CH3

KERNEL_WIDTH4 = 1
KERNEL_HEIGHT4 = 1
X_STRIDE4 = 1
Y_STRIDE4 = 1

RELU_EN4 = 0
MODE4 = 0  # 0:VALID, 1:SAME
X_PADDING4 = 0
Y_PADDING4 = 0

OUT_CH4 = 84
OUT_WIDTH4 = int((IN_WIDTH4 + 2 * X_PADDING4 - KERNEL_WIDTH4) / X_STRIDE4 + 1)
OUT_HEIGHT4 = int((IN_HEIGHT4 + 2 * Y_PADDING4 - KERNEL_HEIGHT4) / Y_STRIDE4 + 1)

# output
IN_WIDTH5 = OUT_WIDTH4
IN_HEIGHT5 = OUT_HEIGHT4
IN_CH5 = OUT_CH4

KERNEL_WIDTH5 = 1
KERNEL_HEIGHT5 = 1
X_STRIDE5 = 1
Y_STRIDE5 = 1

RELU_EN5 = 0
MODE5 = 0  # 0:VALID, 1:SAME
X_PADDING5 = 0
Y_PADDING5 = 0

OUT_CH5 = 65
OUT_WIDTH5 = int((IN_WIDTH5 + 2 * X_PADDING5 - KERNEL_WIDTH5) / X_STRIDE5 + 1)
OUT_HEIGHT5 = int((IN_HEIGHT5 + 2 * Y_PADDING5 - KERNEL_HEIGHT5) / Y_STRIDE5 + 1)

overlay.ip_dict
overlay.download()
overlay?

conv = overlay.Conv_0
pool = overlay.pooling_0
print("Overlay download finish!")

# input image
image = allocate(shape=(IN_HEIGHT1, IN_WIDTH1, IN_CH1), cacheable=0, dtype=np.float32)

# conv1
W_conv1 = allocate(shape=(KERNEL_HEIGHT1, KERNEL_WIDTH1, IN_CH1, OUT_CH1), cacheable=0, dtype=np.float32)
B_conv1 = allocate(shape=(OUT_CH1), cacheable=0, dtype=np.float32)
h_conv1 = allocate(shape=(OUT_HEIGHT1, OUT_WIDTH1, OUT_CH1), cacheable=0, dtype=np.float32)

# pool1
h_pool1 = allocate(shape=(OUT_HEIGHT_p1, OUT_WIDTH_p1, OUT_CH_p1), cacheable=0, dtype=np.float32)

# Conv2
W_conv2 = allocate(shape=(KERNEL_HEIGHT2, KERNEL_WIDTH2, IN_CH2, OUT_CH2), cacheable=0, dtype=np.float32)
B_conv2 = allocate(shape=(OUT_CH2), cacheable=0, dtype=np.float32)
h_conv2 = allocate(shape=(OUT_HEIGHT2, OUT_WIDTH2, OUT_CH2), cacheable=0, dtype=np.float32)

# Conv3
W_conv3 = allocate(shape=(KERNEL_HEIGHT3, KERNEL_WIDTH3, IN_CH3, OUT_CH3), cacheable=0, dtype=np.float32)
B_conv3 = allocate(shape=(OUT_CH3), cacheable=0, dtype=np.float32)
h_conv3 = allocate(shape=(OUT_HEIGHT3, OUT_WIDTH3, OUT_CH3), cacheable=0, dtype=np.float32)

# pool2
h_pool2 = allocate(shape=(OUT_HEIGHT_p2, OUT_WIDTH_p2, OUT_CH_p2), cacheable=0, dtype=np.float32)

# dense
W_conv4 = allocate(shape=(IN_CH4, OUT_CH4), cacheable=0, dtype=np.float32)
B_conv4 = allocate(shape=(OUT_CH4), cacheable=0, dtype=np.float32)
h_conv4 = allocate(shape=(OUT_HEIGHT4, OUT_WIDTH4, OUT_CH4), cacheable=0, dtype=np.float32)

# output
W_conv5 = allocate(shape=(IN_CH5, OUT_CH5), cacheable=0, dtype=np.float32)
B_conv5 = allocate(shape=(OUT_CH5), cacheable=0, dtype=np.float32)
h_conv5 = allocate(shape=(OUT_HEIGHT5, OUT_WIDTH5, OUT_CH5), cacheable=0, dtype=np.float32)

w_conv1 = np.load('/home/xilinx/jupyter_notebooks/LPR/weights/conv1_weight.npy')
for i in range(5):
    for j in range(5):
        for k in range(1):
            for l in range(6):
                W_conv1[i][j][k][l] = w_conv1[l][k][j][i]

b_conv1 = np.load('/home/xilinx/jupyter_notebooks/LPR/weights/conv1_bias.npy')
B_conv1[i] = b_conv1[i]

w_conv2 = np.load('/home/xilinx/jupyter_notebooks/LPR/weights/conv2_weight.npy')
for i in range(5):
    for j in range(5):
        for k in range(6):
            for l in range(16):
                W_conv2[i][j][k][l] = w_conv2[l][k][j][i]

b_conv2 = np.load('/home/xilinx/jupyter_notebooks/LPR/weights/conv2_bias.npy')
B_conv2[i] = b_conv2[i]

w_conv3 = np.load('/home/xilinx/jupyter_notebooks/LPR/weights/conv3_weight.npy')
for i in range(5):
    for j in range(5):
        for k in range(16):
            for l in range(120):
                W_conv3[i][j][k][l] = w_conv3[l][k][j][i]

b_conv3 = np.load('/home/xilinx/jupyter_notebooks/LPR/weights/conv3_bias.npy')
B_conv3 = b_conv3

w_conv4 = np.load('/home/xilinx/jupyter_notebooks/LPR/weights/dense_weight.npy')
for i in range(120):
    for j in range(84):
        W_conv4[i][j] = w_conv4[j][i]

b_conv4 = np.load('/home/xilinx/jupyter_notebooks/LPR/weights/dense_bias.npy')
B_conv4 = b_conv4

w_conv5 = np.load('/home/xilinx/jupyter_notebooks/LPR/weights/output_weight.npy')
for i in range(84):
    for j in range(65):
        W_conv5[i][j] = w_conv5[j][i]

print("weights and bias are loaded")

classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           '川', '鄂', '赣', '甘', '贵', '桂', '黑', '沪', '冀', '津', '京', '吉', '辽', '鲁', '蒙',
           '闽', '宁', '青', '琼', '陕', '苏', '晋', '皖', '湘', '新', '豫', '渝', '粤', '云', '藏', '浙']

while(1):
    while(1):
        g = input("input enter to continue")
        break
    image1 = cv2.imread('/home/xilinx/jupyter_notebooks/LPR/images/2-6.jpg', cv2.IMREAD_GRAYSCALE).astype(np.float32)
    image1 = cv2.resize(image1, (28, 28))
    print("read image")
    for i in range(IN_HEIGHT1):
        for j in range(IN_WIDTH1):
            for k in range(IN_CH1):
                image[i][j][k] = (255-image1[i][j])/255
    print("image is loaded")
    RunConv(conv, KERNEL_WIDTH1, KERNEL_HEIGHT1, X_STRIDE1, Y_STRIDE1, MODE1, RELU_EN1, image, W_conv1, B_conv1, h_conv1)
    RunPool(pool, KERNEL_WIDTH_p1, KERNEL_HEIGHT_p1, C_STRIDE_p1, X_STRIDE_p1, Y_STRIDE_p1, MODE_p1, h_conv1, h_pool1)
    RunConv(conv, KERNEL_WIDTH2, KERNEL_HEIGHT2, X_STRIDE2, Y_STRIDE2, MODE2, RELU_EN2, h_pool1, W_conv2, B_conv2, h_conv2)
    RunPool(pool, KERNEL_WIDTH_p2, KERNEL_HEIGHT_p2, C_STRIDE_p2, X_STRIDE_p2, Y_STRIDE_p2, MODE_p2, h_conv2, h_pool2)
    RunConv(conv, KERNEL_WIDTH3, KERNEL_HEIGHT3, X_STRIDE3, Y_STRIDE3, MODE3, RELU_EN3, h_pool2, W_conv3, B_conv3,
            h_conv3)
    RunConv(conv, KERNEL_WIDTH4, KERNEL_HEIGHT4, X_STRIDE4, Y_STRIDE4, MODE4, RELU_EN4, h_conv3, W_conv4, B_conv4,
            h_conv4)
    RunConv(conv, KERNEL_WIDTH5, KERNEL_HEIGHT5, X_STRIDE5, Y_STRIDE5, MODE5, RELU_EN5, h_conv4, W_conv5, B_conv5,
            h_conv5)
    print("hardware run complete")
    MAX = h_conv5[0][0][0]
    for i in range(1, OUT_CH5):
        if h_conv5[0][0][i] > MAX:
            MAX = h_conv5[0][0][i]
            index = i
    print("the result is " + classes[i])

print("helloworld")


lprResult = []
def Lpr(imagePath):
    image1 = cv2.imread('/home/xilinx/jupyter_notebooks/LPR/images/2-6.jpg', cv2.IMREAD_GRAYSCALE).astype(np.float32)
    image1 = cv2.resize(image1, (28, 28))
    print("read image")
    for i in range(IN_HEIGHT1):
        for j in range(IN_WIDTH1):
            for k in range(IN_CH1):
                image[i][j][k] = (255 - image1[i][j]) / 255
    print("image is loaded")
    RunConv(conv, KERNEL_WIDTH1, KERNEL_HEIGHT1, X_STRIDE1, Y_STRIDE1, MODE1, RELU_EN1, image, W_conv1, B_conv1,
            h_conv1)
    RunPool(pool, KERNEL_WIDTH_p1, KERNEL_HEIGHT_p1, C_STRIDE_p1, X_STRIDE_p1, Y_STRIDE_p1, MODE_p1, h_conv1, h_pool1)
    RunConv(conv, KERNEL_WIDTH2, KERNEL_HEIGHT2, X_STRIDE2, Y_STRIDE2, MODE2, RELU_EN2, h_pool1, W_conv2, B_conv2,
            h_conv2)
    RunPool(pool, KERNEL_WIDTH_p2, KERNEL_HEIGHT_p2, C_STRIDE_p2, X_STRIDE_p2, Y_STRIDE_p2, MODE_p2, h_conv2, h_pool2)
    RunConv(conv, KERNEL_WIDTH3, KERNEL_HEIGHT3, X_STRIDE3, Y_STRIDE3, MODE3, RELU_EN3, h_pool2, W_conv3, B_conv3,
            h_conv3)
    RunConv(conv, KERNEL_WIDTH4, KERNEL_HEIGHT4, X_STRIDE4, Y_STRIDE4, MODE4, RELU_EN4, h_conv3, W_conv4, B_conv4,
            h_conv4)
    RunConv(conv, KERNEL_WIDTH5, KERNEL_HEIGHT5, X_STRIDE5, Y_STRIDE5, MODE5, RELU_EN5, h_conv4, W_conv5, B_conv5,
            h_conv5)
    print("hardware run complete")
    MAX = h_conv5[0][0][0]
    for i in range(1, OUT_CH5):
        if h_conv5[0][0][i] > MAX:
            MAX = h_conv5[0][0][i]
            index = i
    lprResult.append(classes[index])





file = r'D:\personal_srcs\IcDesignandDebug\lpr_data\0'

for root, dirs, files in os.walk(file):
    for file in files:
        path = os.path.join(root, file)
        Lpr(path)

print("".join(a))