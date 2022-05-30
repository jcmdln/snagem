# SPDX-License-Identifier: AGPL-3.0-or-later

FROM alpine:3.15 AS core
RUN apk --no-cache add git libffi libpq openssl py3-pip python3 sqlite tini tzdata
RUN ln -sf /usr/share/zoneinfo/UTC /etc/localtime
ENTRYPOINT ["/sbin/tini", "--"]

FROM core AS build
RUN apk --no-cache add \
    cargo gcc g++ libffi-dev libpq-dev openssl-dev patchelf python3-dev rust sqlite-dev
RUN pip install git+https://github.com/python-poetry/poetry@b1b3ce9
COPY . /opt/snagem
RUN python3 -m venv /opt/snagem/.venv
ENV PATH="/opt/snagem/.venv/bin:$PATH"
WORKDIR /opt/snagem
RUN poetry install --only default

FROM core AS release
COPY --from=build --chown=root:root /opt/snagem /opt/snagem
ENV PATH="/opt/snagem/.venv/bin:$PATH"
WORKDIR /opt/snagem
CMD ["snagd"]

FROM build AS build-devel
RUN poetry install --with tox

FROM core AS devel
COPY --from=build-devel --chown=root:root /opt/snagem /opt/snagem
ENV PATH="/opt/snagem/.venv/bin:$PATH"
WORKDIR /opt/snagem
CMD ["tox"]
