# Use official Python image as base
FROM python:3.10.2-bullseye

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Expose port
EXPOSE 11001

# Run Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:11001"]
