# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install the necessary dependencies directly
RUN pip install --no-cache-dir fastapi pydantic uvicorn

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application
CMD ["python", "app.py"]