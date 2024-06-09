from llama_cpp import Llama
llm = Llama.from_pretrained(
    repo_id="Qwen/Qwen1.5-0.5B-Chat-GGUF",
    filename="*q8_0.gguf",
    verbose=False
)

# llm = Llama(
#       model_path="./models/7B/llama-model.gguf",
#       # n_gpu_layers=-1, # Uncomment to use GPU acceleration
#       # seed=1337, # Uncomment to set a specific seed
#       # n_ctx=2048, # Uncomment to increase the context window
# )
a=llm.create_chat_completion(
      messages = [
         # {"role": "system", "content": "You are an assistant who perfectly describes images."},
          {
              "role": "user",
              "content": "123" 

          }
      ]
)
print(a)
