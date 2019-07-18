FROM python

COPY . ./sample-python/.

WORKDIR sample-python

RUN pip3 install pytest && pytest