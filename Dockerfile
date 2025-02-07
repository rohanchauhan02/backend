# ==========================
# Stage 1: Build Dependencies
# ==========================
FROM python:3.10 AS builder

WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# ==========================
# Stage 2: Production Image
# ==========================
FROM python:3.10-slim

WORKDIR /app

# Copy the installed packages from the builder stage to the production stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

# Copy the project files into the container
COPY . /app

# Expose port 8000
EXPOSE 8000

# Set environment variables for production
ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=myproject.settings \
    DEBUG=False

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
