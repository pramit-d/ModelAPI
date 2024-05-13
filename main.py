# 1. Library imports
import uvicorn
from fastapi import FastAPI, File, UploadFile
import numpy as np
from PIL import Image
import io
import tensorflow as tf
from tensorflow.keras import models

# 2. Create the app object
app = FastAPI()

# 3. Load the pre-trained model
model = models.load_model("image.h5")

# Define class names for CIFAR-10 dataset
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# 4. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'ML Model API'}

# 5. Expose the prediction functionality, make a prediction from the passed
#    image file and return the predicted output
@app.post('/predict')
async def predict_image(file: UploadFile = File(...)):
    # Read the contents of the uploaded file
    print("Trying to read file...")
    contents = await file.read()
    print("file reading successful..")
    # Open the image using PIL and convert to RGB mode
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    
    # Resize the image to match the input shape of the model
    image = image.resize((32, 32))
    
    # Convert the image to a NumPy array and normalize pixel values
    image_array = np.asarray(image) / 255.0
    
    # Add batch dimension to the image array
    image_array = np.expand_dims(image_array, axis=0)
    
    # Make prediction using the loaded model
    prediction = model.predict(image_array)
    
    # Get the predicted class name based on the highest probability
    predicted_class = class_names[np.argmax(prediction)]
    
    return {
        'prediction': predicted_class
    }

# 6. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    #uvicorn.run(app, host='0.0.0.0', port=8000)
    uvicorn.run(app)


