FROM python:3.9.10

WORKDIR app/

RUN pip install gunicorn==20.1.0

COPY req.txt .

RUN pip install -r req.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Diplom.wsgi"]
