from setuptools import setup, find_packages

setup(
    name="ImageUI",
    version="0.9",
    description="A package for easily creating UIs in Python, mainly using OpenCV's drawing functions.",
    long_description=open("README.md").read(),
    author="Glas42",
    license="GPL-3.0",
    packages=["ImageUI"],
    python_requires=">=3.9",
    install_requires=[
        "mouse",
        "numpy",
        "pillow",
        "pywin32",
        "opencv-python",
        "deep-translator",
    ],
)