FROM python:3.10

#RUN pip install --no-cache-dir poetry==1.5.1 pytest

WORKDIR /simulation-integration
COPY tests/requirements.txt ./
RUN pip install -r requirements.txt

COPY scenarios scenarios/
COPY tests tests/

CMD [ "bash", "tests/run_tests.sh" ]
