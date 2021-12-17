FROM python:3.8-slim-buster
ADD script/* /usr/local/bin/
RUN python -m pip install --upgrade pip \
    && pip install requests \
    && pip install pyyaml \
    && pip install validators
ENTRYPOINT ["python"]
CMD ["/usr/local/bin/publish.py"]