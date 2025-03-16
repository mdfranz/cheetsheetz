# Variables

- `OLLAMA_KEEP_ALIVE`
- `OLLAMA_NUM_PARALLEL`
- `OLLAMA_MAX_QUEUE`

# Runner Arguments

```
Runner usage
  -batch-size int
    	Batch size (default 512)
  -ctx-size int
    	Context (or KV cache) size (default 2048)
  -flash-attn
    	Enable flash attention
  -kv-cache-type string
    	quantization type for KV cache (default: f16)
  -lora value
    	Path to lora layer file (can be specified multiple times)
  -main-gpu int
    	Main GPU
  -mlock
    	force system to keep model in RAM rather than swapping or compressing
  -mmproj string
    	Path to projector binary file
  -model string
    	Path to model binary file
  -multiuser-cache
    	optimize input cache algorithm for multiple users
  -n-gpu-layers int
    	Number of layers to offload to GPU
  -no-mmap
    	do not memory-map model (slower load but may reduce pageouts if not using mlock)
  -parallel int
    	Number of sequences to handle simultaneously (default 1)
  -port int
    	Port to expose the server on (default 8080)
  -tensor-split string
    	fraction of the model to offload to each GPU, comma-separated list of proportions
  -threads int
    	Number of threads to use during generation (default 10)
```




