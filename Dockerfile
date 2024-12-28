FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
CMD ["streamlit", "run", ".\chatbot_frontend.py", "--server.port=5000", "--server.address=0.0.0.0"]
