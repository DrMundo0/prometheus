# 尝试启用 Google Drive，并挂载到 /content/drive 目录
# from google.colab import drive
# drive.mount("/content/drive")

# 将 ChilloutMix 模型保存到 Google Drive
# !curl -Lo /content/drive/MyDrive/models/Chilloutmix-Ni-pruned-fp32-fix.safetensors https://civitai.com/api/download/models/11745

!pip install --upgrade fastapi==0.90.1

!git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui /content/stable-diffusion-webui
!git clone https://github.com/yfszzx/stable-diffusion-webui-images-browser /content/stable-diffusion-webui/extensions/stable-diffusion-webui-images-browser
!git clone https://github.com/DominikDoom/a1111-sd-webui-tagcomplete /content/stable-diffusion-webui/extensions/a1111-sd-webui-tagcomplete

# 创建 Stable-diffusion 模型目录
!mkdir -p /content/stable-diffusion-webui/models/Stable-diffusion

# 下载 ChilloutMix 模型并保存到 Stable-diffusion 模型目录
!curl -Lo /content/stable-diffusion-webui/models/Stable-diffusion/Chilloutmix-Ni-pruned-fp32-fix.safetensors https://civitai.com/api/download/models/11745

import shutil
shutil.rmtree('/content/stable-diffusion-webui/embeddings')

%cd /content/stable-diffusion-webui
%pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchtext==0.14.1 torchaudio==0.13.1 torchdata==0.5.1 --extra-index-url https://download.pytorch.org/whl/cu117
%pip install torchmetrics==0.11.4

!git checkout 3715ece
!git clone https://huggingface.co/nolanaatama/embeddings
!COMMANDLINE_ARGS="--share --disable-safe-unpickle --no-half-vae --xformers --reinstall-xformers --enable-insecure-extension-access --skip-torch-cuda-test" REQS_FILE="requirements.txt" python launch.py
