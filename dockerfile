# Use Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy your files into the container
COPY . .

# Install required Python packages
RUN pip install --no-cache-dir psutil requests streamlit pandas

# Run the main monitoring script
CMD ["python", "main.py"]
