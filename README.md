# ModelAPI
Demo project for deployment of ML models using FastAPI.

## Prerequisites
1. Python 3.x
2. pip (Python package manager)

## Install FastAPI
1. Create a Python virtual environment.
   ```
   python3 -m venv model_api_env
2. Activate newly created venv.
   ```
   source model_api_env/bin/activate
3. Install FastAPI.
   ```
   pip install fastapi

## Configure cloud environment 
1. Edit Inbound rules in cloud environment and enable a port for ModelAPI deployment.
2. Allow inbound traffic in the OS firewall.
   ```
   sudo ufw allow <PORT>
   ```
   
## Configure and Run ModelAPI
1. Clone ModelAPI.
   ```
   git clone https://github.com/pramit-d/ModelAPI
2. Install all the required Python packages.
   ```
   cd ModelAPI
   pip install -r requirements.txt
   
3. Run ModelAPI.
   ```
   uvicorn main:app --host 0.0.0.0 --port <PORT>

## Access and Use ModelAPI
1. Access ModelAPI:
   ```
   <VM_IP_ADDRESS>:<PORT>
2. Interactive API docs:
   ```
   <VM_IP_ADDRESS>:<PORT>/docs
   ```
   You will see the automatic interactive API documentation (provided by Swagger UI).
3. Use ModelAPI to predict images.

   ![predict_image](docs/ModelAPI_result.gif)

   It will predict an image from the mentioned list.
   `[airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck]`

## Customization
* Model: You can replace the pre-trained model (image.h5) with your own trained model by placing it in the project directory and updating the model = models.load_model("image.h5") line in main.py.

* Input Data: By default, the API is configured to accept image files for prediction. However, if you want to accept different types of input data, such as text, you can modify the predict_image function in main.py to handle the new data format appropriately. For example, if you want to support text input, you can update the function to accept text input instead of an image file. You'll also need to modify the model input accordingly and update the logic to preprocess the text data before making predictions.

* Class Names: Update the class_names list in main.py with your own class names.

## Acknowledgement
The model utilized in this project has been obtained from [Hugging Face](https://huggingface.co/).
