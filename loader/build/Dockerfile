FROM python:3

WORKDIR /usr/src/loader

COPY ./loader/build/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./loader/app .

CMD [ "python", "./app/start_loader.py" ]