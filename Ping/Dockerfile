# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application
COPY server.py .

# Expose the WebSocket port
EXPOSE 8765

# Run the WebSocket server
CMD ["python","-u", "server.py"]