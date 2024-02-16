from comfy_serverless import ComfyConnector
comfy_connector = ComfyConnector()
import json
import random

def genimg(mensaje):
    prompt = json.load(open('workflow_api.json'))  # loads the workflow_api.json file as exported by ComfyUI dev mode
    semilla = random.randint(0, 10000)
    prompt["8"]["inputs"]["seed"] = semilla
    prompt["7"]["inputs"]["text"] = mensaje # If this doesn't work, you have to verify your workflow_api.json
    images = comfy_connector.generate_images(prompt) # sends the json file and receives back the generated images
    return images[0]
