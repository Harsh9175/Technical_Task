FROM python:3.8-slim

# Install dependencies
RUN pip install --no-cache-dir boto3

# Set the working directory
WORKDIR /app

# Copy the Python code into the container
COPY lambda_function.py .

# Command to run the Lambda function
CMD ["lambda_function.lambda_handler"]
