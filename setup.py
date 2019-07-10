import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PoseEstimator",
    version="0.0.1",                        # Update this for every new version
    author="Anupam Mundale",
    author_email="mundleanupam@gmail.com",
    description="Tricycle Model Pose Estimator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "numpy==1.16.4",
        "pytest==4.5.0",
        "allure-pytest==2.7.0"
    ],
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
