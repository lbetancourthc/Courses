import numpy as np
import onnxruntime
import torch


from flask import Flask, jsonify, request
from transformers import RobertaTokenizer

app = Flask(__name__)
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
session = onnxruntime.InferenceSession("roberta-squence-classification-9.onnx")

def to_numpy(tensor):
    return (tensor.detach().cpu().numpy() if tensor.required_grad else tensor.cpu().numpy())

@app.route("/")
def home():
    return "<h2>RoBERTa Sentiment Analysis</h2>"

@app.route("/predict", methods=["POST"])
def predict():
    input_ids = torch.tensor(tokenizer.encode(request.json[0], add_special_tokens=True).unsqueeze(0))
    inputs = {
        session.get_inputs()[0].name: to_numpy(input_ids)
        }
    out = session.run(None, inputs)
    result = np.argmax(out)

    return jsonify({"positive": bool(result)})

if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")