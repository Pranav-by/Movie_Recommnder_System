# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy everything else
COPY . .

# Expose default Streamlit port
EXPOSE 8501

# Run streamlit properly
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
