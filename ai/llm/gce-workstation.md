
# Create Instance 

30GB RAM is probably the minimum for running OpenLLM so do an `n1-standard-8`

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

## Install Python Virtual Environment

```
sudo apt -y install python3-virtualenv python3.11-venv mosh tmux
```
mdfranz@instance-20240317-151052:~/openllm$ python3 -m venv .venv

```
pip install "openllm[vllm]
```

# Test OpenLLM

## Start PHI with PyTorch Backend 

```
$ TRUST_REMOTE_CODE=True openllm start microsoft/phi-2  --backend pt 
```

Was unable to run Mistral 

```
ValueError: Bfloat16 is only supported on GPUs with compute capability of at least 8.0. Your Tesla T4 GPU has compute capability 7.5.
```

