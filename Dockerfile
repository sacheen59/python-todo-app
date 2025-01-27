FROM python:3.10-slim

# install system dependencies 
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# copy the requirements files to the working directory
COPY requirements.txt .

# install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the application code

COPY . .

CMD [ "python" , "app/main.py" ]