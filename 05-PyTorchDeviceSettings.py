import torch
print(torch.cuda.is_available()) # check if GPU is available
print(torch.backends.mps.is_available()) # check if Apple Silicon GPU is available



device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
print(f"Using device: {device}")

#manual way to set device
if torch.cuda.is_available():
    device = "cuda"
elif torch.backends.mps.is_available():
    device = "mps"
else:
    device = "cpu"
print(f"Using device: {device}")

#tensor manual set device
tensor=torch.tensor([1,2,3])
print(tensor)

tensor_on_gpu=tensor.to(device)
print(tensor_on_gpu)

#context manager to set device
with torch.device(device):
    tensor2=torch.tensor([1,2,3])
    layer=torch.nn.Linear(20,30)

print(tensor2.device)
print(layer.weight.device)


#torch.set_default_device() to set default device for tensors and modules
torch.set_default_device(device)
tensor3=torch.tensor([1,2,3])
layer2=torch.nn.Linear(10,20)
print(tensor3.device)
print(layer2.weight.device)

