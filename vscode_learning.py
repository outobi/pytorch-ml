print("hello world!")


import torch

# 检查是否能用 Apple Silicon 的 GPU 加速 (MPS)
device = "mps" if torch.backends.mps.is_available() else "cpu"
print(f"当前设备: {device}")

# 创建一个简单的张量进行测试
x = torch.rand(5, 4).to(device)
print(x)



# new code line 1
