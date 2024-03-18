# from apex.Ml import LLM
#
#
# def chat(model_name, system_message="You are Jarvis"):  # system prompt
#     AI = LLM(model_name, system_message)
#     AI.chat()
#
#
# if __name__ == "__main__":
#     model_name = "mistralai/Mistral-7B-Instruct-v0.1"
#     chat(model_name)

# from apex.Ml import LLM
#
# def chat(model_name,system_message="You are Jarvis an helping ai "):
#     AI = LLM(model_name, system_message)
#     AI.chat()
#
#
# if __name__  == "__main__":
#     model_name = "mistralai/Mistral-7B-Instruct-v0.1"
#     chat(model_name)

from apex.Ai import PIC

prompt = "A beautiful girl"

PIC.gen(prompt)