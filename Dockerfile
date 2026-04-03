# Use a specific Python version
FROM python:3.11.9-slim

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of your app
COPY . .

# Expose port if your app has a web server
EXPOSE 8080

# Set the default command to run your bot
CMD ["python", "-m", "ShivamNox.__main__"]
