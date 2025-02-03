# Use the official Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./src /app

# Install any dependencies (if you have a requirements.txt file, uncomment the next line)
# RUN pip install --no-cache-dir -r requirements.txt

# Install the required Python packages
RUN pip install sqlite3 tk

# Expose the port your app will run on (optional for this case as it's a desktop app)
# EXPOSE 8080

# Run the application
CMD ["python", "task_manager_main.py"]
