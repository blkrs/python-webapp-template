FROM python
MAINTAINER Krzysztof Balka
RUN pip install flask requests
WORKDIR /app
CMD ["python", "server.py"]
ADD templates/* /app/templates/
ADD js/* /app/js/
ADD *.py /app/ 
