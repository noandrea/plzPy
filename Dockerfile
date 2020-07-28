############################
# STEP 1 build executable binary
############################
FROM python:3.8-buster AS builder
ARG DOCKER_TAG=0.0.0
ARG DATA_URL=https://opendata.arcgis.com/datasets/273bf4ae7f6a460fbf3000d73f7b2f76_0.csv?outSR=%7B%22latestWkid%22%3A3857%2C%22wkid%22%3A102100%7D
# Install git.
# Git is required for fetching the dependencies.
RUN apt update && apt install -y curl
# checkout the project 
WORKDIR /builder
COPY . .
# install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
RUN $HOME/.poetry/bin/poetry install
RUN $HOME/.poetry/bin/poetry build
# download the location file 
RUN curl -L $DATA_URL -o /tmp/data.csv
# build the database
RUN $HOME/.poetry/bin/poetry run plzpy massage --input /tmp/data.csv --output /data.json
############################
# STEP 2 build a small image
############################
FROM python:3.8-buster
WORKDIR /
# Copy packages + data
COPY --from=builder /data.json /
RUN pip install plzpy
# Run the whole shebang.
ENTRYPOINT [ "plzpy" ]
CMD [ "serve"]
