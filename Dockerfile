FROM python:3.7

COPY . /LegendOfZeldaRemake

WORKDIR /LegendOfZeldaRemake

RUN pip install pygame

CMD ["python3", "main.py"]
