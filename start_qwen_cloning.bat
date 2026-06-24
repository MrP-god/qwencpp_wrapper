@echo off
cd /d "%~dp0"
echo Launching Qwen3-TTS Base Model on AMD iGPU via Vulkan (Voice Cloning)...
set GGML_BACKEND=vulkan
"qwen-tts-server.exe" --model "Qwen3-TTS-12Hz-1.7B-Base-Q8_0.gguf" --codec "qwen3-tts-tokenizer-q8_0.gguf" --ttsdir "Voices" --port 50020
pause
