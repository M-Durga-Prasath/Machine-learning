Installing PyTorch with CUDA Support (Windows + NVIDIA GPU)
1. Verify NVIDIA Driver

Open PowerShell or Command Prompt:

nvidia-smi

Expected output should show something like:

NVIDIA-SMI xxx.xx
Driver Version: xxx.xx
CUDA Version: xx.x

If nvidia-smi is not found, install/update your NVIDIA driver first.

2. Create a Virtual Environment

Navigate to your project folder:

cd path\to\project

Create a virtual environment:

python -m venv .venv

Activate it:

.venv\Scripts\activate

Verify:

python --version
3. Remove Existing CPU Version of PyTorch (if installed)
pip uninstall torch torchvision torchaudio -y

Optional:

pip cache purge
4. Install CUDA-Enabled PyTorch

Install the CUDA 12.8 build:

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
5. Verify Installation

Run Python:

python

Then:

import torch

print(torch.__version__)
print(torch.version.cuda)
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))

Expected output:

2.x.x+cu128
12.8
True
NVIDIA GeForce RTX 3050 Ti

Exit Python:

exit()
6. Verify from Terminal Directly
python -c "import torch; print(torch.__version__); print(torch.version.cuda); print(torch.cuda.is_available())"

Expected:

2.x.x+cu128
12.8
True
7. Configure VS Code / Jupyter Notebook

If PyTorch works in the terminal but not in notebooks:

Open notebook and run:

import sys
print(sys.executable)

Ensure the path points to:

...\project\.venv\Scripts\python.exe

If not:

Open notebook.
Click the Kernel selector (top-right).
Select the .venv interpreter.
Restart the notebook kernel.