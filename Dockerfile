# Stage 1: Base build stage
FROM python:3.13-slim AS builder

# Create the app directory
RUN mkdir /app

# Set the working directory
WORKDIR /app

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Upgrade pip and install dependencies
RUN pip install --upgrade pip

# Copy the requirements file first (better caching)
COPY requirements-server.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements-server.txt

# Stage 2: Production stage
FROM python:3.13-slim
LABEL authors="tuesd4y,eva-fitzinger"
LABEL org.opencontainers.image.source=https://github.com/tuesd4y/AnkiLeaderboard
LABEL org.opencontainers.image.description="Anki Leaderboard server"
LABEL org.opencontainers.image.licenses=MIT

RUN useradd -m -r appuser && \
   mkdir /app && \
   chown -R appuser /app

# Copy the Python dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Set the working directory
WORKDIR /app

# Copy application code
COPY --chown=appuser:appuser server ./server
COPY --chown=appuser:appuser api ./api

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Switch to non-root user
USER appuser

# Expose the application port
EXPOSE 8000

# Start the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "server.wsgi:application"]