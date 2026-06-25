```python
from setuptools import setup, find_packages

setup(
    name="Unsloth-PhiSage",
    version="1.0.0",
    author="Manoj",
    description="Fine-Tuning Phi-3.5-Mini-Instruct for Medical Question Answering using Unsloth",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "torch",
        "unsloth",
        "transformers",
        "trl",
        "peft",
        "accelerate",
        "bitsandbytes",
        "datasets",
        "evaluate",
        "numpy",
        "pandas",
        "scikit-learn",
        "sentencepiece",
        "protobuf",
        "huggingface_hub",
        "safetensors",
        "tqdm",
    ],
)
```
