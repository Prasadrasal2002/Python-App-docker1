# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./src /app
COPY ./templates /app/templates
# Copy the requirements.txt file into the container
COPY ./requirements.txt /app/requirements.txt

# Install dependencies for Tkinter and X11 support
RUN apt-get update && \
    apt-get install -y \
    python3-tk \
    x11-apps \
    sqlite3 \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install the Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN python /app/task_manager_db.py
# Expose port 5000 to the outside world
EXPOSE 5000

# Run the application when the container starts
CMD ["python", "task_manager_main.py"]
