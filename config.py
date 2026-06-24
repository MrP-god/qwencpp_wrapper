import os

# Root directory of the package folder (koboldcpp_wrapper_server)
PACKAGE_DIR = os.path.abspath(os.path.dirname(__file__))

# QwenTTS server executable path inside the package
QWEN_EXE = os.path.join(PACKAGE_DIR, "qwen-tts-server.exe")

# Server Config
PORT = 50020
BASE_URL = f"http://127.0.0.1:{PORT}"
TTS_URL = f"{BASE_URL}/v1/audio/speech"

# Logging Config
DEBUG = False

def log(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
