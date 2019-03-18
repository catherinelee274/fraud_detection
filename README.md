# AdTracking Fraud Detection

## Summary

Fraudulent mobile ad clicks have become an increasingly difficult problem for advertisers as the word experiences a proliferation of smart mobile devices. Advertisers pay affiliate website when their users click on one of their mobile ads.

This compensation model has incentivized bad actors to generate fraudulent clicks on mobile ads in the hope of conning advertisers into paying them a commission. Advertisers must compensate affiliates even when these clicks do not result in a download of the advertised application.

In response to this problem, we've developed a machine learning model that can predict whether a user will download an app after clicking a mobile advertisement. Training our model on a dataset of over 100,000 mobile advertisement clicks spanning three days, we were able to achieve 83% accuracy using XGBoost.

This model can be used by advertisers to segregate fraudulent clicks from genuine ones. This distinction saves advertisers significant money and thwarts bad actors.

## Team
- [Catherine Lee ](https://www.linkedin.com/in/catherinelee274/)
- [Amit Saxena](https://www.linkedin.com/in/amitsa1/)
- [Kyle O'Brien](https://www.linkedin.com/in/kyle1668/)

## Project Structure

### Source Code

- **main.ipynb**: The Jupyter Notebook where the source code for the model is written and executed.
- **equalizer.py**: The script that parses the original 183 million training CSV file and returns an equalized CSV of around 100 thousand records.
- **Dockerfile**: Configures and configuration and setup of the container that the notebook will be running in.
- **Pipfile**: Configuration for the project Pipenv virtual environment. Used to install specific project dependencies and version of Python.
- **Pipfile.lock**: Contains meta-data for the Pipenv virtual environment.
- **__init__.py**: Make the project root a Python module.

### Data

- **data/equalized_train.csv**: The downsized training data for our model.
- **data/train.csv**: The full unequalized CSV file.

### Utilities

- **.gitignore**: Includes file patterns not to be included in Git.
- **.dockerignore**: Includes file patterns not to be added to the Docker image.
- **README.md**: Project description and direction on how to run the model.

## Running this Model

### Option 1 (Recommended): Running the Jupyter Notebook via Docker

This project has multiple dependencies and only supports Python 3.6+. Since each of us work on different operation systems, we decided to run the project inside a Docker container along with Pipenv. This allows our project to run the same and automate installation regardless of the host OS. [An up to date installation of Docker is required to complete the following steps](https://www.docker.com/get-started).

Step 1: Build the Docker Image:

`docker build -t fraud_detection .`

Step 2: Run the Docker Container:

`docker run -p 8080:8888 -v $(pwd):/fraud_detection fraud_detection`

Step 3: Open the Jupyter Notebook in Your Browser

Once the Docker container is running, you can go to `http://localhost:8080` to view the notebook. When prompted, enter the password/token found in the output of your running Docker container.

![alt text](./assets\token-readme-image.png "The Notebook Token")

### Option 2: Running the Jupyter Notebook Directly

You can run the project notebook directly by running `jupyter notebook main.ipynb`. This is **not recommended** since you might not have the correct version of the project's dependencies.

## Links

[Google Drive](https://drive.google.com/drive/u/0/folders/0AFnlAysa3MTEUk9PVA)\
[Kaggle Challenge](https://www.kaggle.com/c/talkingdata-adtracking-fraud-detection)

