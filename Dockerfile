############################
# STEP 1 build executable binary
############################
FROM python:3.8-slim-buster AS builder
ARG DOCKER_TAG=0.0.0
ARG DATA_URL=https://opendata.arcgis.com/datasets/273bf4ae7f6a460fbf3000d73f7b2f76_0.csv?outSR=%7B%22latestWkid%22%3A3857%2C%22wkid%22%3A102100%7D
# Install git.
# Git is required for fetching the dependencies.
RUN apt update && apt install -y curl
# checkout the project 
WORKDIR /builder
COPY . .
# download the location file 
RUN curl -L $DATA_URL -o /tmp/data.csv
# build the database
RUN pip install plzpy
RUN plzpy massage --input /tmp/data.csv --output /data.json --summary
############################
# STEP 2 build a small image
############################
FROM python:3.8-slim-buster
WORKDIR /
# Copy packages + data
COPY --from=builder /data.json /
RUN pip install plzpy
# Run the whole shebang.
ENTRYPOINT [ "plzpy" ]
CMD [ "serve"]
