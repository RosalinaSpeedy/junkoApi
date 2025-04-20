from flask import Flask, render_template, request
from ngrok_flask_cart import run_with_ngrok
from pyngrok import ngrok

import torch
import base64
from io import BytesIO

import transformers

from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from transformers import pipeline

#!huggingface_cli.login

pipe =  pipeline(
    "text-generation",
    model="RosalinaS/Junko",
    device_map="cuda",
)

#pipe.to("cuda")

app = Flask(__name__)
print(app)
run_with_ngrok(app, domain='--domain=trusting-multiply-rattler.ngrok-free.app')

@app.route("/submit-prompt", methods=["GET"])
def generate_plan():
    prompt = request.args.get("prompt")
    messages = [{"role": "user", "content": prompt}]

    outputs = pipe(
        messages,
        max_new_tokens=128
    )
    return outputs[0]["generated_text"][-1]

#ngrok_tunnel = ngrok.connect(80)
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port=80)