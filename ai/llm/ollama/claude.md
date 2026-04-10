
# Using Claude Code with Gemma4

```
matthew@instance-20260403-220151:~/testing$ ollama show gemma4:latest
  Model
    architecture        gemma4    
    parameters          8.0B      
    context length      131072    
    embedding length    2560      
    quantization        Q4_K_M    
    requires            0.20.0    

  Capabilities
    completion    
    vision        
    audio         
    tools         
    thinking      

  Parameters
    temperature    1       
    top_k          64      
    top_p          0.95    

  License
    Apache License               
    Version 2.0, January 2004    
    ...                          
```


# Create a new Modelfile

New `Modelfile` is

```
FROM gemma4:latest
PARAMETER num_ctx 65536
```

and build it 

matthew@instance-20260403-220151:~/testing$ ollama create gemma4-coder -f Modelfile 
gathering model components 
using existing layer sha256:4c27e0f5b5adf02ac956c7322bd2ee7636fe3f45a8512c9aba5385242cb6e09a 
using existing layer sha256:7339fa418c9ad3e8e12e74ad0fd26a9cc4be8703f9c110728a992b193be85cb2 
using existing layer sha256:ae869ec57fe78755390d67943d3b8134884fac2f512254737320bd68e0d8d269 
writing manifest 
success 

```
matthew@instance-20260403-220151:~/testing$ ollama list
NAME                         ID              SIZE      MODIFIED          
gemma4-coder:latest          9a557ef1657b    9.6 GB    4 seconds ago
```
