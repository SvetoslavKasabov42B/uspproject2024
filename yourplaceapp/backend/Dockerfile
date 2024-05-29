# Use Python 3.8 image as base
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy and install requirements
COPY ./backend/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the backend code
COPY ./backend /app

# Command to run the application
CMD ["python", "app.py"]
