# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy the app files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 8501 (default Streamlit port)
EXPOSE 8501

# Command to run Streamlit app
CMD ["streamlit", "run", "space_iss_app.py"]
