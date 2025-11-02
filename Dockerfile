# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Prevents Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential libpq-dev netcat-traditional && apt-get clean

# Copy dependency list
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Add a non-root user
RUN useradd -ms /bin/bash django
USER django

# Run the app
CMD ["gunicorn", "PHOTOGRAPHY_PORTFOLIO.wsgi:application", "--bind", "0.0.0.0:8000"]

