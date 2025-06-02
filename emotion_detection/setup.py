from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="0.1.0",
    description="Watson-powered emotion detection utility",
    packages=find_packages(),
    install_requires=["requests"],
    python_requires=">=3.8",
)