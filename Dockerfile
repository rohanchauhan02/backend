# ==========================
# Stage 1: Build Dependencies
# ==========================
FROM python:3.10.2-bullseye AS builder

WORKDIR /app

# Install system dependencies required for mysqlclient
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ==========================
# Stage 2: Production Image
# ==========================
FROM python:3.10.2-bullseye

WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    libssl-dev \
    libffi-dev \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy installed Python packages from the builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

# Copy project files into the container
COPY . /app

# Expose the application port
EXPOSE 11001

# Set environment variables for production
ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=app.settings \
    DEBUG=False

# Run Django server using Gunicorn
CMD ["python", "manage.py", "runserver", "127.0.0.1:11001"]

