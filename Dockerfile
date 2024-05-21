# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install Python dependencies
RUN pip3 install --upgrade pip
RUN pip3 install basicsr  --use-pep517
RUN pip3 install gfpgan --use-pep517
RUN pip3 install -r requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the Flask app
CMD ["python3", "app.py"]

