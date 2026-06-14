import torch
tensor=torch.arange(0,50,5)
print(tensor)

print(tensor.min())
print(tensor.max())
print(tensor.sum())
print(tensor.median())
# print(tensor.mean())   int tensor.float()  # convert to float

print(tensor.float().mean())

#argmax and argmin

print(tensor.argmax())
print(tensor.argmin())

#manipulating tensor; reshaping, stacking, squeezing and unsqueezing

x=torch.arange(1,10,1)
print(x)
print(x.shape)

#reshaping
y=x.reshape(3,3)
print(y)


#view is similar to reshape but it returns a view of the original tensor, which means that if you modify the view, the original tensor will also be modified. Reshape, on the other hand, returns a new tensor with the same data but a different shape.
z=y.view(9,1)
z[0]=100
print(z)
#view just working on contiguous tensors, if the tensor is not contiguous, you will get an error. Reshape can work on non-contiguous tensors.


#stacking
z=torch.stack([x,x,x],dim=0)  # stack along the first dimension
print(z)

stacked=torch.stack([x,z])
print(stacked)


#squeezing and unsqueezing
print(stacked.shape)    
print(stacked.unsqueeze(0).shape)  # add a dimension at the beginning
print(stacked.unsqueeze(1).shape)  # add a dimension in the middle
print(stacked.unsqueeze(2).shape)  # add a dimension at the end
print(stacked.squeeze().shape)  # remove all dimensions of size 1






