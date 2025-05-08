# setup.py
from setuptools import setup, find_packages

setup(
    name="langchain-GLM_agent",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    extras_require={
        'dev': [
            'sphinx',
            'sphinx-rtd-theme',
            'myst-parser',
            'snowballstemmer>=2.0.0'
            # 其他文档相关的依赖
        ]
    }
)
