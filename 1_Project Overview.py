
import streamlit as st
import os
from PIL import Image
import torch
from torchvision import transforms
import torch.nn as nn
import  torch.optim as optim

# Load your model (make sure to adjust the path and loading mechanism as necessary)
#  # Ensure you instantiate the model class
#model.load_state_dict(torch.load('model.cpkt'))
class Colornet(nn.Module):
    def __init__(self):
        super(Colornet,self).__init__()
        self.conv1=nn.Conv2d(1,64,kernel_size=5,stride=1,padding=4,dilation=2)
        self.conv2=nn.Conv2d(64,64,kernel_size=5,stride=1,padding=4,dilation=2)
        self.conv3=nn.Conv2d(64,128,kernel_size=5,stride=1,padding=4,dilation=2)
        self.conv4=nn.Conv2d(128,3,kernel_size=5,stride=1,padding=4,dilation=2)

    def forward(self,x):
        x=nn.functional.relu(self.conv1(x))
        x=nn.functional.relu(self.conv2(x))
        x=nn.functional.relu(self.conv3(x))
        x=torch.sigmoid(self.conv4(x))
        return x
model = torch.load('model.cpkt')
model.eval()

# Define the transformation
transform = transforms.Compose([
    transforms.Resize((256, 256)),  # Adjust size as needed
    transforms.ToTensor(),
])

# Create directories for input and output images
input_dir = 'input_images'
output_dir = 'output_images'
os.makedirs(input_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

# Streamlit UI
st.title("Image Colorization")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Save the uploaded image
   # uploaded_file = uploaded_file.resize((256,256))
    image_path = os.path.join(input_dir, uploaded_file.name)
    #image = Image.open(uploaded_file)
    #new_image = image.resize((256, 256))
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.image(image_path, caption='Uploaded Image', use_column_width=True,width=256)

    if st.button("Colorize"):
        # Open the saved image
        img = Image.open(image_path)
        gray_img = img.convert("L")
        
        # Save the grayscale image (optional)
        gray_img.save(os.path.join(output_dir, uploaded_file.name))

        # Prepare the image for the model
        img_tensor = transform(gray_img).unsqueeze(0)
        img_tensor = img_tensor.to('cuda' if torch.cuda.is_available() else 'cpu')

        with torch.no_grad():
            colorized_tensor = model(img_tensor)

        # Convert the output tensor to a PIL image and save it
        colorized_img = transforms.ToPILImage()(colorized_tensor.squeeze(0).cpu())
        colorized_img.save(os.path.join(output_dir, uploaded_file.name))
        st.image(colorized_img, caption='Colorized Image', use_column_width=True,width=256)