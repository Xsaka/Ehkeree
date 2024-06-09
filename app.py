from flask import Flask, request, jsonify
from llama_cpp import Llama

app = Flask(__name__)
llm = Llama.from_pretrained(
    repo_id="Qwen/Qwen1.5-0.5B-Chat-GGUF",
    filename="*q8_0.gguf",
    verbose=False
)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    messages = data.get('messages', [])
    
    response = llm.create_chat_completion(messages=messages)
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
