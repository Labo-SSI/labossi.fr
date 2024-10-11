# Use the official Python image from the DockerHub
FROM python:3.13-slim-bookworm

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y build-essential

# Copy the requirements file to install dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install additional tools needed for development
RUN pip install flask[dotenv] watchdog

# Copy the application source code
COPY . /app

# Expose the port that Flask will run on
EXPOSE 5000

# Define environment variables for Flask
ENV FLASK_ENV=development
ENV FLASK_APP=src/app
ENV FLASK_RUN_HOST=0.0.0.0

# Enable live reload using the flask run command with the --reload flag
CMD ["flask", "run", "--host=0.0.0.0", "--reload"]
