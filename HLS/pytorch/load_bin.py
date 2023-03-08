import torch
import pickle
import numpy as np
import struct
model_dict = torch.load(r'D:\personal_srcs\IcDesignandDebug\lpr_relu\lpr_relu.pth', map_location=torch.device('cpu'))
# # fp = open('model_parameter.bin', 'wb')
# weight_count = 0
# num = 1
# for k, v in model_dict.items():
#     print(k, num)
#     num = num + 1
#     if 'num_batches_tracked' in k:
#         continue
#     v = v.cpu().numpy().flatten()
#     print(v)
#
#     name_l = list(k)
#     j = 0
#     for i in name_l:
#         if i == '.':
#             name_l[j] = '_'
#         j = j + 1
#     k = "".join(name_l)
#
#     for d in v:
#         fp = open('./weights/' + str(k)+'.txt', 'wb')
#         fp.write(d)
#         weight_count += 1
# print('model_weight has Convert Completely!', weight_count)
# # print(model_dict)

# stu_dict = {"Chinese": 58,
#             "Math": 99,
#             "English": 60,
#             "Python": 100}
#
#
# s = pickle.dumps(stu_dict)
# print(s)
# s = pickle.dumps(stu_dict["Chinese"])
# print(s)
# i = pickle.dumps(stu_dict["Math"])
# print(i)
# with open("D:\personal_srcs\IcDesignandDebug\model_dict.bin", "wb") as f:
#     f.write(s)
#     f.close()
#
# with open("D:\personal_srcs\IcDesignandDebug\model_dict.bin", "rb") as f:
#     a_dict = f.read()
#     f.close()
# a_dict = pickle.loads(a_dict)
#
# print(a_dict)

# 需求：分开保存，且只保存值，键作为文件名
# for key, value in stu_dict.items():
#     # print(value)
#     with open('./weights' + str(key) + '.txt', "wb") as f:
# data = 64
#
# with open('./testStruct3.txt', 'wb') as f:
#     bin = struct.pack('d', data)
#     print(bin)
#     f.write(bin)



# for key, value in model_dict.items():
# #
#     if key == "conv1.weight":
#         print(value)
#         np.save('./testNumpy.npy', value)
#     #     print(key)
#     #     v = value.cpu().numpy().flatten()
#     #     a = np.array(v)
#     #     # print(v)
#     #     print(value)
#     #     print(value.size()) # torch.Size([6, 1, 5, 5]) -->([out, in, kern_x, kern_y])
#     #
#     #     a = a.reshape((6, 1, 5, 5))
#     #     print(a)
#     #     print(a[0][0][0][0])
#     # with open('./weights/' + str(key) + '.txt', "wb") as f:
#     # if key == "conv1.weight":
#     #     v = value.cpu().numpy().flatten()
#     #     print(v)
#     #     for d in v:
#     #         print(d)
#     if key == "conv1.weight":
#         l = pickle.dumps(value)
#         print(l)
# a = np.load('./testNumpy.npy')
# print(a)
# print(a[5][0][0][0])

# main
# for key, value in model_dict.items():
#     name_l = list(key)
#     j = 0
#     for i in name_l:
#         if i == '.':
#             name_l[j] = '_'
#         j = j + 1
#     key = "".join(name_l)
#     np.save('./relu_weights/' + str(key) + '.npy', value)

a = np.load('./relu_weights/dense_weight.npy')
print(a)
print(a.ndim)

# check
# for key, value in model_dict.items():
#     name_l = list(key)
#     j = 0
#     for i in name_l:
#         if i == '.':
#             name_l[j] = '_'
#         j = j + 1
#     key = "".join(name_l)
#     a = np.load('./weights/' + str(key) + '.npy')
#     if a == value:
#         print(True)

# print(model_dict)
# for key, value in model_dict.items():
#     print(value)
#     name_l = list(key)
#     j = 0
#     for i in name_l:
#         if i == '.':
#             name_l[j] = '_'
#         j = j + 1
#     key = "".join(name_l)
#     a = np.load('./relu_weights/' + str(key) + '.npy')
#     print(a)

print("Completed!")


