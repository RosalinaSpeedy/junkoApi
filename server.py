
from transformers import AutoModel
model = AutoModel.from_pretrained("RosalinaS/Junko")

#pipe = pipeline(task="text-generation", model=model_id, tokenizer=tokenizer, max_length=200)
messages = [
    {"role": "user", "content": "Addiction name: Pornography Triggers: - late night - horny - lonliness Addiction Severity: 0.7 Warning Signs: -"},
]

outputs = model(
    messages,
    max_new_tokens=128
)
print(model)
print("OUTPUT:")
print(outputs[0]["generated_text"][-1])
# app = Flask(__name__) 

# @app.route('/') 
# def root(): 
#     return render_template("index.html")

# @app.route('/predict', methods=['POST']) 
# def predictions_endpoint(): 
   
#     if request.method == 'POST': 
        
#         file = request.data

#         predicted_class = make_predictions(file)
    
#     return jsonify(predicted_class.item()) 


# if __name__ == "__main__": 

#     host = "127.0.0.1"
#     port_number = 8080 

#     app.run(host, port_number)