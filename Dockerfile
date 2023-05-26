# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Copy the requirements file into the working directory
COPY requirements.txt /app/requirements.txt

# Install the required packages using pip
RUN pip3 install -r /app/requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run main.py when the container launches
CMD ["python3", "/app/src/main.py", "--host=0.0.0.0"]