FROM python:3.10.14-slim-bullseye

WORKDIR /usr/src/app

RUN pip install playwright==1.45.1 && \
    playwright install --with-deps

COPY . .

RUN pip install -r requirements.txt

CMD ["pytest", "--alluredir=allure-results"]
