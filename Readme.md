# ABOUT
This is a large language model with great japanese support : \
	Llama-3-neoAI-8B-Chat-v0.1.Q8_0

# PREREQUISITES
	python
	pip
	langchain_community extension
	ollama
	llm model

# HOW TO USE

## INSTALL PYTHON EXTENSION
`pip3 install langchain_community`


## DOWNLOAD MODEL
Wesite : https://huggingface.co/mradermacher/Llama-3-neoAI-8B-Chat-v0.1-GGUF

Download the following model with the command below: \
GGUF	Q8_0	8.6 :	fast, best quality.
```
wget https://huggingface.co/mradermacher/Llama-3-neoAI-8B-Chat-v0.1-GGUF/resolve/main/Llama-3-neoAI-8B-Chat-v0.1.Q8_0.gguf
```

## CREATE MODEL FROM MODELFILE
```
ollama create neoai-8b-chat -f Modelfile
ollama ps
```
## RUN MODEL
`python run run.py` \
for linux, \
`python3 run run.py`

run in terminal with the command below : \
`ollama run neoai-8b-chat:latest`
