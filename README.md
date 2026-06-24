# KoboldCPP Server Wrapper

A self-contained, lightweight Python wrapper package for [KoboldCPP](https://github.com/LostRuins/koboldcpp). This package provides clean, programmatic APIs and an interactive Web UI dashboard to manage the KoboldCPP server lifecycle and generate TTS audio using zero-shot voice cloning and voice design.

---

## Features
- **Lifecycle Management**: Programmatically start and stop the KoboldCPP Vulkan GPU-accelerated server.
- **Detached Asset Storage**: Keep GGUF models, tokenizers, and reference voice files fully inside your projects.
- **Performance Settings Accordion**: Customize your GPU acceleration (Vulkan, CUDA, or CPU), threads, and GPU layer offloading directly from the UI to optimize generation speed on 4GB VRAM cards or dedicated AMD GPUs.
- **Voice Cloning**: Generate audio by referencing a `.wav` file template and a matching transcript file.
- **Voice Design**: Generate designed voices by specifying audio traits (e.g., gender, age, clarity, speed).
- **Web UI Access**: Easily launch the server persistently to access the built-in KoboldCPP Web UI in your browser.

---

## Directory Structure
To use the wrapper, copy the `koboldcpp_wrapper_server/` directory into your project:

> [!NOTE]
> The `koboldcpp.exe` binary is excluded from this repository due to file size limits. To use this package, you must download the compiled `koboldcpp.exe` binary from the official [KoboldCPP Releases Page](https://github.com/LostRuins/koboldcpp/releases) and place it inside the root of the package.

```text
your_project/
  pyproject.toml
  koboldcpp.exe                 # Add the downloaded koboldcpp.exe here
  Voices/                       # Your reference voice templates (.wav and .txt files)
  your_base_model.gguf          # GGUF Base Model
  your_design_model.gguf        # GGUF VoiceDesign Model
  your_tokenizer.gguf           # GGUF Tokenizer
  main.py                       # CLI Launcher
```

---

## Installation

To make the package globally accessible inside your Python environment, run the following command in the package root:
```bash
pip install .
```
Or for development / editable mode:
```bash
pip install -e .
```

---

## Testing via the Web UI Dashboard

The easiest way to test everything is to start the built-in Web UI.

1. **Launch the UI**:
   If installed via `pip`:
   ```bash
   kobold-tts-studio --ui
   ```
   Or run the CLI script directly:
   ```bash
   python main.py --ui
   ```

2. **Run Tests Inside the UI**:
   - In the **Server Controls** sidebar, select your mode (Voice Cloning or Voice Design).
   - Enter your GGUF model and tokenizer paths.
   - Adjust performance settings under **🔌 Performance & Debug Settings** (select Vulkan for AMD cards/iGPUs or CUDA for Nvidia, adjust threads, and VRAM offload).
   - Click **Start Server**.
   - Go to the operations panel, choose a template or enter trait descriptions, and click **Generate** to verify audio output directly inside your browser!

---

## Programmatic Quick Start Example

Here is how you can use the wrapper package in your python scripts:

```python
import os
from koboldcpp_wrapper_server import start_server, shutdown_server, clone_voice

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_BASE = os.path.join(BASE_DIR, "Qwen3-TTS-12Hz-1.7B-Base-q8_0.gguf")
TOKENIZER = os.path.join(BASE_DIR, "qwen3-tts-tokenizer-q8_0.gguf")
VOICES_DIR = os.path.join(BASE_DIR, "Voices")
OUTPUT_CLONE = os.path.join(BASE_DIR, "output_cloned.wav")

try:
    # 1. Start the server programmatically (silenced logs by default)
    start_server(
        action_type="base",
        model_path=MODEL_BASE,
        tokenizer_path=TOKENIZER,
        voices_dir=VOICES_DIR,
        gpu_backend="vulkan",
        debug=False
    )
    
    # 2. Generate cloned voice
    clone_voice(
        text="Hello, this is a voice cloning test.",
        voice_ref="alice.wav",
        output_path=OUTPUT_CLONE,
        reference_text="Hello, this is a voice cloning test."
    )
finally:
    # Always shutdown when finished
    shutdown_server()
```

---

## License & Credits

- **Credits**: This package wraps **KoboldCPP** developed by [LostRuins](https://github.com/LostRuins/koboldcpp).
- **License**: Distributed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.
