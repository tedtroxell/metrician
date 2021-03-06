import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="metrician",
    version="0.0.3",
    author="Ted Troxell",
    author_email="ted@tedtroxell.com",
    description="Automatic metric logging for Pytorch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tedtroxell/metrician",
    project_urls={
        "Bug Tracker": "https://github.com/tedtroxell/metrician/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['metrician','metrician.dataset', 'metrician.recorders', 'metrician.writers', 'metrician.configs', 'metrician.signals', 'metrician.monitors', 'metrician.explainations'],#setuptools.find_packages(),
    python_requires='>=3.6',
)
