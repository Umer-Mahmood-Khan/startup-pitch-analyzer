import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Local model path
model_path = os.getenv("LLM_MODEL_PATH", "default/path/to/your/model")

# Load tokenizer and model once
tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16,
    device_map="auto",
    local_files_only=True
)

def generate_prompt(startup_idea: str):
    return f"""
You are a startup business analyst. For the startup idea below, provide:

**Market Summary**: (1–2 sentence summary)
**SWOT Analysis**:
- Strengths:
- Weaknesses:
- Opportunities:
- Threats:

**Business Type**: (B2B or B2C)
**Business Model**: (e.g., subscription, marketplace, SaaS, etc.)

Startup Idea: {startup_idea}
"""




# HyDE generator function
def generate_analysis(idea: str) -> str:
    prompt = generate_prompt(idea)
    temperature = 0.7

    try:
        device = model.device if hasattr(model, "device") else "cuda"
        inputs = tokenizer(prompt, return_tensors="pt").to(device)

        prompt_len = inputs["input_ids"].shape[1]

        with torch.no_grad():
            output = model.generate(
                **inputs,
                max_new_tokens=250,       # 🔹 reasonable cap
                do_sample=False,          # 🔹 deterministic, faster
                 pad_token_id=tokenizer.eos_token_id,
                eos_token_id=tokenizer.eos_token_id
            )

        decoded = tokenizer.decode(output[0][prompt_len:], skip_special_tokens=True)
        response = decoded.split("\n")[0].strip()  # Trim any follow-ups
        return response
    except Exception as e:
        print(f"Generation error: {e}")
        return "Could not generate analysis."
