## To install - pip install apex
##  usage of image generator from apex.Ai
### 5. `PIC` - make image using prodia
```python
from apex.Ai import PIC

# Define a prompt for the image generation
prompt = "A beautiful sunset over the ocean"


PIC.gen(prompt)
```
## usage of special .LLM file from apex (apex.Ml)

### `LLM`
```python
from apex.Ml import LLM

def chat(model_name, system_message="You are Jarvis"):# system prompt
    AI = LLM(model_name, system_message)
    AI.chat()

if __name__ == "__main__":
    model_name = "mistralai/Mistral-7B-Instruct-v0.1" # name of the model you wish to use It supports ALL text generation models on deepinfra.com.
    chat(model_name)
```
