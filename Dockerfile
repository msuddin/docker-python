FROM python

COPY . ./sample-python/.

WORKDIR sample-python

RUN python3 -m unittest test/suite_smoke.py