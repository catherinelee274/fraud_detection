FROM ubuntu:18.04

LABEL maintainer="kdobrien@ucsc.edu"
LABEL course="UCSC CS 144: Applied Machine Learning"

# Copy local project files into the container.
# Files epecified in .dockerignore are not copied.
COPY . ./fraud_detection
WORKDIR /fraud_detection

# Make all file line endings Unix format.
RUN find ./ -exec sed -i 's/\r//' {} \;
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Installs Python 3.6 and Pip.
RUN apt-get update && apt-get install -y --no-install-recommends python3-pip

# Install python packages defined in the Pipefile.
RUN pip3 install pipenv
RUN pipenv install

# Allow us to access the contain's port 5000 via our own localhost:5000
EXPOSE 8888

# Start the notebook.
CMD [ "pipenv", "run", "jupyter", "notebook" , "main.ipynb", "--allow-root", "--ip=0.0.0.0"]

