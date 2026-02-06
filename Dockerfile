FROM python:3.14-slim

WORKDIR /app

COPY pyproject.toml ./
RUN pip install --upgrade pip pytest

COPY . .

CMD ["pytest"]
