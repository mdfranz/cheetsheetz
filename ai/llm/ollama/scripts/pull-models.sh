!/bin/bash

# Models to pull
ollama_models=("phi4:14b" "olmo2:13b" "command-r7b:7b")

# Pull ollama models
echo "Pulling Ollama models..."
for model in "${ollama_models[@]}"; do
  echo "Pulling $model..."
  ollama pull "$model"
  if [ $? -ne 0 ]; then
    echo "Error pulling $model. Skipping."
  fi
done
