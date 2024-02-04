# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY Password.py /app/

# Run the Python script when the container launches
CMD ["python", "/app/Password.py"]
