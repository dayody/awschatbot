# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install streamlit
RUN pip install langchain
RUN pip install langchain_aws

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=chat_backend.py
ENV FLASK_APP=chat_frontend.py

# Run chatbot_frontend.py when the container launches
CMD ["streamlit", "run", ".\chatbot_frontend.py", "--server.port=5000", "--server.address=0.0.0.0"]
