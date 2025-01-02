from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the model and tokenizer
model_name = "EleutherAI/gpt-neo-125M"
try:
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
except Exception as e:
    print(f"Error loading model or tokenizer: {e}")
    model = None
    tokenizer = None

def suggest_improvements(section, content):
    if not content.strip():
        return "No content provided to improve."
    
    if model is None or tokenizer is None:
        return "Model or Tokenizer not loaded correctly."

    try:
        # Format the prompt
        prompt = f"Improve the following {section} section of a resume:\n{content}"
        
        # Tokenize and generate
        inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
        outputs = model.generate(inputs["input_ids"], max_length=150, num_return_sequences=1)

        # Decode the output and clean it
        improved_content = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Return the cleaned suggestions
        return improved_content.strip()
    
    except Exception as e:
        return f"Error generating suggestions: {e}"