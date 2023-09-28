FROM python:3.10

WORKDIR /
RUN pip install --no-cache-dir poetry==1.5.1 pytest

COPY . /tests

CMD [ "/tests/run_tests.sh" ]
