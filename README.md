# Makea simple agent with Guidance and local LLMs
The [Guidance](https://github.com/microsoft/guidance) is a tool for controlling LLM. It provides a good concept to build prompt templates. This repository shows you how to make a agent with Guidance. You can combine it with various LLMs in Huggingface. My [medium article](https://medium.com/@gartist/a-simple-agent-with-guidance-and-local-llm-c0865c97eaa9) for more explanation.

UPDATE: Add gradio UI.

# Install
Python packages:
- [guidance](https://github.com/microsoft/guidance)
- [GPTQ-for-LLaMa](https://github.com/oobabooga/GPTQ-for-LLaMa.git)
- [langchain](https://github.com/hwchase17/langchain)
- [gradio](https://github.com/gradio-app/gradio) (Only for web UI)

Note: we only use langchain for build the `GoogleSerper` tool. The agent itself is built only by Guidance. Feel free to change/add/modify the tools with your goal.
The GPTQ-for-LLaMa I used is the oobabooga's fork. You can install it with [this command](https://github.com/oobabooga/text-generation-webui/blob/main/docs/GPTQ-models-(4-bit-mode).md#step-1-install-gptq-for-llama).

# Run
There are two options: run a Gradio server with UI and run the notebook file.

## Gradio server
Please modify the `SERPER_API_KEY`, `MODEL_PATH`, `CHECKPOINT_PATH` in the app.py and run:
```sh
gradio app.py
```

## Notebook
Please check the [notebook file]((https://github.com/QuangBK/localLLM_guidance/blob/main/demo_ReAct.ipynb)). You should have a free SERPER API KEY and a LLM model to run this.
I use the [wizard-mega-13B-GPTQ](https://huggingface.co/TheBloke/wizard-mega-13B-GPTQ) model. Feel free to try others.

# Example
![alt text](https://github.com/QuangBK/localLLM_guidance/blob/main/gradio.png?raw=true)
