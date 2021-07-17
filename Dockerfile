FROM python:3.6.5
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app
EXPOSE 5000
CMD ["python","app.py"]