# For more information, please refer to https://aka.ms/vscode-docker-python
FROM rayproject/ray:2.8.1
RUN pip install --upgrade pip

# Install pip requirements
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN export PYTHONPATH="${PYTHONPATH}:/app"
COPY ./src /app
