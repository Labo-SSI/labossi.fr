# Use an official Python runtime as a parent image
FROM python:3.13-slim-bookworm

# Set the working directory in the container
WORKDIR /app

# Install necessary build dependencies (if needed for any libraries)
RUN apt-get update && apt-get install -y build-essential

# Create a non-root user and group to run the application
RUN groupadd -r flask && useradd -r -g flask flask

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn for WSGI server
RUN pip install gunicorn

# Copy the entire application code to the container
COPY . /app

# Change ownership of the /app directory to the non-root user
RUN chown -R flask:flask /app

# Switch to the non-root user to ensure the application doesn't run as root
USER flask

# Expose the port that the app will run on
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_ENV=production
ENV FLASK_APP=src/app

# Run the Gunicorn server (with 4 worker processes, adjustable based on CPU)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.app:app", "--workers", "2"]
