FROM python:3

WORKDIR /usr/src/loader

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ../app .

CMD [ "python", "start_loader.py" ]