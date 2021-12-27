FROM python:alpine3.7 AS build
COPY requirements.txt /
RUN pip3 install -r requirements.txt

FROM gcr.io/distroless/python3
COPY weather-frontend.py /
COPY --from=build /usr/local/lib/python3.7/site-packages /usr/local/lib/python3.7/site-packages
ENV PYTHONPATH=/usr/local/lib/python3.7/site-packages
EXPOSE 5002
ENTRYPOINT ["python", "weather-frontend.py"]