import torch
import numpy as np

random_array= np.random.rand(3, 5)
print(random_array)
# Convert the numpy array to a PyTorch tensor

print(type(random_array))
print(random_array.dtype)
print(random_array.shape)

random_matrix=torch.rand(3, 5)
print(random_matrix)
print(random_matrix.dtype)
print(random_matrix.ndim())
print(random_matrix.shape)


# Create a random image tensor of shape (224, 224, 3)
random_image_tensor=torch.rand(size=(224, 224,3))
print(random_image_tensor)



#Zeros and Ones
zeros=torch.zeros(size=(3, 4))
print(zeros)
ones=torch.ones(size=(3, 4))
print(ones)


#arrange
arrange_tensor=torch.arange(start=0, end=10, step=2)
print(arrange_tensor)

#onelikes
like_ex=torch.ones_like(arrange_tensor)
print(like_ex)