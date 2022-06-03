# SPDX-License-Identifier: AGPL-3.0-or-later

FROM fedora:36 AS core
RUN dnf install -y libpq openssl python3 sqlite tini tzdata
RUN ln -sf /usr/share/zoneinfo/UTC /etc/localtime
ENTRYPOINT ["/usr/bin/tini", "--"]

FROM core AS build
RUN dnf install -y gcc git libpq-devel patchelf python3-devel python3-pip python3-wheel
RUN pip install git+https://github.com/python-poetry/poetry@51824fc
COPY . /opt/snagem
RUN python3 -m venv /opt/snagem/.venv
ENV PATH="/opt/snagem/.venv/bin:$PATH"
WORKDIR /opt/snagem
RUN poetry install --only main

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
