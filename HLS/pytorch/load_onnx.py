import torch
import torchvision

dummy_input = torch.randn(1, 3, 224, 224, device="cpu")
model = torch.load("D:/personal_srcs/IcDesignandDebug/lpr_allModel/lpr_allModel.pth", map_location="cpu")
model.eval()

# 给输入输出取个名字
input_names = ["input_1"]
output_names = ["output_1"]

torch.onnx.export(model, dummy_input, "Lenet.onnx", verbose=True, input_names=input_names, output_names=output_names)