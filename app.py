import gradio as gr
import guidance
import torch
from server.model import load_model_main
from server.tools import load_tools
from server.agent import CustomAgentGuidance

import os
os.environ["SERPER_API_KEY"] = 'YOUR_API_KEY'

MODEL_PATH = '/home/quang/working/LLMs/oobabooga_linux/text-generation-webui/models/TheBloke_wizard-mega-13B-GPTQ'
CHECKPOINT_PATH = '/home/quang/working/LLMs/oobabooga_linux/text-generation-webui/models/TheBloke_wizard-mega-13B-GPTQ/wizard-mega-13B-GPTQ-4bit-128g.no-act.order.safetensors'
DEVICE = torch.device('cuda:0')

examples = [
    ["How much is the salary of number 8 of Manchester United?"],
    ["What is the population of Congo?"],
    ["Where was the first president of South Korean born?"],
    ["What is the population of the country that won World Cup 2022?"]    
]

def greet(name):
    final_answer = custom_agent(name)
    return final_answer, final_answer['fn']

model, tokenizer = load_model_main(MODEL_PATH, CHECKPOINT_PATH, DEVICE)
llama = guidance.llms.Transformers(model=model, tokenizer=tokenizer, device=0)
guidance.llm = llama

dict_tools = load_tools()

custom_agent = CustomAgentGuidance(guidance, dict_tools)

list_outputs = [gr.Textbox(lines=5, label="Reasoning"), gr.Textbox(label="Final Answer")]
demo = gr.Interface(fn=greet, inputs=gr.Textbox(lines=1, label="Input Text", placeholder="Enter a question here..."), 
                    outputs=list_outputs,
                    title="Demo ReAct agent with Guidance",
                    description="The source code can be found at: https://github.com/QuangBK/localLLM_guidance/",
                   examples=examples)
demo.launch(server_name="0.0.0.0", server_port=7860)
