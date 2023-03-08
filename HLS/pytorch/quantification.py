# float32 --> int8
import torch
import numpy as np


def quantification(data):
    pretic = data * 2 ** 7
    flag = 0
    if(abs(pretic) >= 1):
        pretic = int(pretic)
    else:
        pretic = 0

    if pretic < 0:
        flag = 1

    if flag == 1:
        data_out = hex(abs(pretic) + 2 ** 7)
    else:
        data_out = hex(pretic)
    return data_out

# a = -0.588888
# print(a)
# a = quantification(a)
# b =eval(a)
# print(b)
# a = 0.588888
# print(a)
# a = quantification(a)
# b =eval(a)
# print(b)
# a = int(a[2:])
# print(a)

model_dict = torch.load(r'D:\personal_srcs\IcDesignandDebug\lpr_model\lpr_model.pth', map_location=torch.device('cpu'))

# for key, value in model_dict.items():
#     # name_l = list(key)
#     # j = 0
#     # for i in name_l:
#     #     if i == '.':
#     #         name_l[j] = '_'
#     #     j = j + 1
#     # key = "".join(name_l)
#     if key == "conv1.weight":
#         print(value)
#         print(value.size())
#         for i, j, k, l in value.size():
#             print(i, j, k, l)
#     # value = quantification(value)
#     # print(value)
#     # np.save('./qWeights/' + str(key) + '.npy', value)

# a = np.load('./weights/conv1_weight.npy')
# print(a)

def weightToQweights(a, index_list):
    ch_out = index_list[0]
    ch_in = index_list[1]
    kx = index_list[2]
    ky = index_list[3]

    for i in range(ch_out):
        for j in range(ch_in):
            for k in range(kx):
                for l in range(ky):
                    # print(a[i][j][k][l])
                    # a[i][j][k][l] = quantification(a[i][j][k][l])
                    # print(a[i][j][k][l])
                    inter_a = quantification(a[i][j][k][l])
                    a[i][j][k][l] = eval(inter_a)
                    # print(a[i][j][k][l])

    return a

def biasToQbias(a, index_list):
    for i in range(index_list):

                    # print(a[i][j][k][l])
                    # a[i][j][k][l] = quantification(a[i][j][k][l])
                    # print(a[i][j][k][l])
        inter_a = quantification(a[i])
        a[i] = eval(inter_a)
                    # print(a[i][j][k][l])

    return a

def weight2ToQweights2(a, index_list):
    ch_out = index_list[0]
    ch_in = index_list[1]
    for i in range(ch_out):
        for j in range(ch_in):

                    # print(a[i][j][k][l])
                    # a[i][j][k][l] = quantification(a[i][j][k][l])
                    # print(a[i][j][k][l])
            inter_a = quantification(a[i][j])
            a[i][j] = eval(inter_a)
                    # print(a[i][j][k][l])
    return a


# conv1_weight = np.load('./weights/conv1_weight.npy')
# conv1_weight = weightToQweights(conv1_weight, [6, 1, 5, 5])
# np.save('./qWeights/conv1_qweight.npy', conv1_weight)

# conv1_bias = np.load('./weights/conv1_bias.npy')
# conv1_bias = biasToQbias(conv1_bias, 6)
# # print(conv1_bias)
# # conv1_bias = weightToQweights(conv1_bias, [6, 1, 1, 1])
# np.save('./qWeights/conv1_qbias.npy', conv1_bias)

# conv2_weight = np.load('./weights/conv2_weight.npy')
# conv2_weight = weightToQweights(conv2_weight, [16, 6, 5, 5])
# np.save('./qWeights/conv2_qweight.npy', conv2_weight)
#
# conv2_bias = np.load('./weights/conv2_bias.npy')
# conv2_bias = biasToQbias(conv2_bias, 16)
# np.save('./qWeights/conv2_qbias.npy', conv2_bias)
#
# conv3_weight = np.load('./weights/conv3_weight.npy')
# conv3_weight = weightToQweights(conv3_weight, [120, 16, 5, 5])
# np.save('./qWeights/conv3_qweight.npy', conv3_weight)
#
# conv3_bias = np.load('./weights/conv3_bias.npy')
# conv3_bias = biasToQbias(conv3_bias, 120)
# np.save('./qWeights/conv3_qbias.npy', conv3_bias)

dense_weight = np.load('./weights/dense_weight.npy')
dense_weight = weight2ToQweights2(dense_weight, [84, 120])
np.save('./qWeights/dense_qweight.npy', dense_weight)

dense_bias = np.load('./weights/dense_bias.npy')
dense_bias = biasToQbias(dense_bias, 84)
np.save('./qWeights/dense_qbias.npy', dense_bias)



output_weight = np.load('./weights/output_weight.npy')
output_weight = weight2ToQweights2(output_weight, [65, 84])
np.save('./qWeights/output_qweight.npy', output_weight)

output_bias = np.load('./weights/output_bias.npy')
output_bias = biasToQbias(output_bias, 65)
np.save('./qWeights/output_qbias.npy', output_bias)


# print(dense_weight)

# print(model_dict.items())
# print(model_dict["output.weight"].size())
# print(dense_weight.size())
# dense_weight = weightToQweights(dense_weight, [84, 120, 1, 1])
# print(dense_weight)
# np.save('./qWeights/dense_qweight.npy', dense_weight)





print('Success')

# a = np.load('./qWeights/conv1_qweight.npy')
# print(a)
# print(a)