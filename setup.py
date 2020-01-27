from setuptools import find_packages, setup

extras = {
    "testing": [
        "pytest>=4.4.0",
        "pytest-xdist==1.31.0",
        "pytest-cov==2.8.1",
        "codecov==2.0.15",
    ]
}

setup(
    name="datasets",
    version="0.0.1",
    author="Fabio Beranizo Lopes",
    author_email="fabio.beranizo@gmail.com",
    description="Manages datasets.",
    license="Apache",
    url="https://github.com/platiagro/datasets",
    packages=[],
    install_requires=[
        # WSGI server
        "Flask==1.1.1",
        "Flask-Cors==3.0.8",
        # Access object storage server
        "minio==5.0.6",
        # Helps with structured data operations
        "pandas==0.25.3",
    ],
    extras_require=extras,
    python_requires=">=3.5.0",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)