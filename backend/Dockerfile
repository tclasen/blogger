FROM python:3
WORKDIR /opt/app
COPY *.whl ./
RUN pip install *.whl
USER nobody
CMD ["blogger", "runserver"]