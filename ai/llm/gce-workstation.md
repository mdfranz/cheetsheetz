# Create Instance 

30GB RAM and 24GB GPU is probably the minimum for running OpenLLM so do an `n1-standard-8`

# OS Prerequisites

## Install Nvidia Drivers (via Ollama) 

```
curl -fsSL https://ollama.com/install.sh | sh
```

## Confirm NVIDIA

```
$ nvidia-detect
Detected NVIDIA GPUs:
00:04.0 3D controller [0302]: NVIDIA Corporation TU104GL [Tesla T4] [10de:1eb8] (rev a1)

Checking card:  NVIDIA Corporation TU104GL [Tesla T4] (rev a1)
Your card is supported by all driver versions.
Your card is also supported by the Tesla drivers series.
Your card is also supported by the Tesla 470 drivers series.
It is recommended to install the
    nvidia-driver
package.
```

## Install Python Virtual Environment for OpenLLM

```
sudo apt -y install python3-virtualenv python3.11-venv mosh tmux
mkdir openllm
cd openllm/
python3 -m venv .venv
source .venv/bin/activate
pip install "openllm[vllm]"
```

# Test OpenLLM

## Start PHI with PyTorch Backend 

```
$ TRUST_REMOTE_CODE=True openllm start microsoft/phi-2  --backend pt 
```

# Run Mistral

I'm still experimenting with `max_model_len` 

```
TRUST_REMOTE_CODE=True .venv/bin/openllm start mistralai/Mistral-7B-Instruct-v0.1 --backend vllm --max_model_len=16384
```

but if it starts you should see something like this:

```
🚀Tip: run 'openllm build mistralai/Mistral-7B-Instruct-v0.1 --backend vllm --serialization safetensors' to create a BentoLLM for 'mistralai/Mistral-7B-Instruct-v0.1'
2024-03-20T21:31:00+0000 [INFO] [cli] Prometheus metrics for HTTP BentoServer from "_service:svc" can be accessed at http://localhost:3000/metrics.
2024-03-20T21:31:00+0000 [INFO] [cli] Starting production HTTP BentoServer from "_service:svc" listening on http://0.0.0.0:3000 (Press CTRL+C to quit)
INFO 03-20 21:31:06 llm_engine.py:70] Initializing an LLM engine with config: model='/home/mdfranz/bentoml/models/vllm-mistralai--mistral-7b-instruct-v0.1/73068f3702d050a2fd5aa2ca1e612e5036429398', tokenizer='/home/mdfranz/bentoml/models/vllm-mistralai--mistral-7b-instruct-v0.1/73068f3702d050a2fd5aa2ca1e612e5036429398', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=15120, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, enforce_eager=False, seed=0)
INFO 03-20 21:31:16 llm_engine.py:275] # GPU blocks: 2043, # CPU blocks: 2048
INFO 03-20 21:31:17 model_runner.py:501] Capturing the model for CUDA graphs. This may lead to unexpected consequences if the model is not static. To run the model in eager mode, set 'enforce_eager=True' or use '--enforce-eager' in the CLI.
INFO 03-20 21:31:17 model_runner.py:505] CUDA graphs can take additional 1~3 GiB memory per GPU. If you are running out of memory, consider decreasing `gpu_memory_utilization` or enforcing eager mode.
INFO 03-20 21:31:23 model_runner.py:547] Graph capturing finished in 6 secs.
2024-03-20T21:42:25+0000 [INFO] [api_server:llm-mistral-service:1] 127.0.0.1:52012 (scheme=http,method=POST,path=/v1/metadata,type=application/json,length=2) (status=200,type=application/json,length=879) 1.603ms (trace=ff2f0c294ebf420d95e5a44f467a0161,span=cb7b5afeaed03eaa,sampled=1,service.name=llm-mistral-service)
INFO 03-20 21:42:25 async_llm_engine.py:383] Received request openllm-aec7ac3874b94367a201caf8310b0050: prompt: None, sampling params: SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.75, top_p=0.78, top_k=15, min_p=0.0, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=['</s>'], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=128, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True), prompt token ids: [1, 1824, 349, 22377, 5244, 2059, 28804].
INFO 03-20 21:42:25 llm_engine.py:706] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%
INFO 03-20 21:42:30 llm_engine.py:706] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 17.4 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.3%, CPU KV cache usage: 0.0%
```

and `gpu_memory_utilization` (this is from 0 to 1 and is the percentage of the GPU to use)

See [nvidia](../../nvidia.md) for how to monitor GPU memory and metrics

```
TRUST_REMOTE_CODE=True .venv/bin/openllm start mistralai/Mistral-7B-Instruct-v0.1 --gpu_memory_utilization=.9 --max_model_len=15120 --backend vllm

```

