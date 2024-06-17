# Use official Python runtime as a parent image
FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Run flask when the container launches
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
