FROM continuumio/miniconda3:4.9.2-alpine
RUN /opt/conda/bin/conda install -c conda-forge --yes pygithub pyyaml
COPY main.py /opt/main.py
ENTRYPOINT ["/opt/conda/bin/python", "/opt/main.py"]