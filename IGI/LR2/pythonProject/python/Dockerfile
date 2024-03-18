FROM python:3
COPY . /python
WORKDIR /python
EXPOSE 80
RUN apt-get update && apt-get install -y python3
CMD ["python", "main.py"]