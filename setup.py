import setuptools

setuptools.setup(
    name="NestsRecognition",
    version="0.0.1",
    author="Pierre Gaillard",
    author_email="pierre.gaillard@imt-atlantique.net",
    url="https://github.com/Blu3s1one/NestsRecognition",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "scikit-image",
        "sklearn",
        "importlib_metadata",
        "napari[all]==0.4.9",
        "jupyterlab==3.0.13",
        "ipywidgets==7.6.3",
        "albumentations==0.5.2",
        "pytorch-lightning==1.3.5",
        "magicgui==0.2.9",
        "torch==1.8.1",
        "torchvision==0.9.1",
        "torchsummary==1.5.1",
        "torchmetrics==0.2.0",
        "mlflow",
    ],
)
