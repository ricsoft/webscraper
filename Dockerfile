# Setup the Python dev environment using Dockerfile
# docker build -t webscraper:latest .

# Run the image and mount the current project dir using CMD
# docker run -it -v %cd%:/usr/src --shm-size=2g --name webscraper webscraper:latest

FROM python:3.8-alpine3.12
	
RUN apk update
RUN apk add chromium chromium-chromedriver

RUN pip install --upgrade pip

RUN pip install pytz
RUN pip install selenium
RUN pip install boto3