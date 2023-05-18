# Make a simple agent with Guidance and local LLMs
The [Guidance](https://github.com/microsoft/guidance) is a tool for controlling LLM. It provides a good concept to build prompt templates. This repository shows you how to make a agent with Guidance. You can combine it with various LLMs in Huggingface.

# Install
Python packages:
- [guidance](https://github.com/microsoft/guidance)
- [GPTQ-for-LLaMa](https://github.com/oobabooga/GPTQ-for-LLaMa.git)
- [langchain](https://github.com/hwchase17/langchain)

Note: we only use langchain for build the `GoogleSerper` tool. The agent itself is built only by Guidance. Feel free to change/add/modify the tools with your goal.
The GPTQ-for-LLaMa I used is the oobabooga's fork. You can install it with [this command](https://github.com/oobabooga/text-generation-webui/blob/main/docs/GPTQ-models-(4-bit-mode).md#step-1-install-gptq-for-llama).

# Run
Please check the notebook file. You should have a free SERPER API KEY and a LLM model to run this.
I use the [wizard-mega-13B-GPTQ](https://huggingface.co/TheBloke/wizard-mega-13B-GPTQ) model. Feel free to try others.
