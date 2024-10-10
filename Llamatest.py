import ollama
 
# Use the locally installed LLaMA 2 model via Ollama
model_name = "llama2"  # The model name as listed in Ollama
 
# Define the prompt
prompt = "Tell me a joke."
 
# Use Ollama to interact with the model
response = ollama.chat(model=model_name, messages=[{"role": "system", "content": prompt}])
 
# Print the model's response content
print(response['message']['content'])
