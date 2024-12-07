FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y \
    python3-tk \
    libtk8.6 \
    libx11-dev \
    libxrender-dev \
    libxext-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

ENV DISPLAY=:0

CMD ["python", "todo-app.py"]

