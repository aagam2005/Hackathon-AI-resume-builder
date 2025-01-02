from transformers import AutoModelForCausalLM, AutoTokenizer
import os

# Set your Hugging Face token in the environment (if you want to do this in code)
os.environ['HF_HOME'] = r'the location of hugging face here'
os.environ['HF_HUB_TOKEN'] = 'your hugging face api here'

# Load the model and tokenizer
model_name = "EleutherAI/gpt-neo-1.3B"
model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=os.getenv('HF_HUB_TOKEN'))
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Set the pad_token to eos_token
tokenizer.pad_token = tokenizer.eos_token

def suggest_improvements(section, content):
    if not content.strip():
        return "No content provided to improve."
    
    try:
        # Use a more specific prompt
        prompt = f"Improve and rewrite the following {section} section of a resume. Focus on concise, impactful, and professional phrasing, avoiding redundancy and repetition.\n\n{content}"
        
        # Tokenize the input and generate attention_mask manually
        inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True, padding=True)

        # Manually create the attention mask if it isn't set
        attention_mask = inputs["attention_mask"] if "attention_mask" in inputs else None

        # Generate improved content
        outputs = model.generate(
            inputs["input_ids"],
            attention_mask=attention_mask,  # Use the attention mask
            max_length=250,
            num_return_sequences=1,
            no_repeat_ngram_size=2,  # Prevents repetition
            pad_token_id=tokenizer.eos_token_id  # Set padding token explicitly
        )

        # Decode the output
        improved_content = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        return improved_content.strip()
    
    except Exception as e:
        return f"Error generating suggestions: {e}"