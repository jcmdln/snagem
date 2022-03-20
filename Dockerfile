# SPDX-License-Identifier: AGPL-3.0-or-later

FROM fedora:35 AS core
ENV PYTHONDONTWRITEBYTECODE="true" \
    PYTHONPYCACHEPREFIX="/tmp" \
    PYTHONUNBUFFERED="true"
RUN dnf --refresh -y upgrade && \
    dnf -y install libpq openssl python3-pip sqlite && \
    dnf -y autoremove && \
    dnf clean all
RUN ln -sf /usr/share/zoneinfo/UTC /etc/localtime
# FIXME: poetry>=1.2,<2 once released
RUN pip install poetry==1.2.0b1


FROM core AS build
RUN dnf --refresh -y install cargo gcc-c++ git libpq-devel openssl-devel patchelf python3-devel \
    rust sqlite-devel
COPY . /opt/snagem
RUN python3 -m venv /opt/snagem/.venv
ENV PATH="/opt/snagem/.venv/bin:$PATH"
WORKDIR /opt/snagem


FROM build as build-release
RUN poetry install --only default

FROM core AS release
COPY --from=build-release --chown=root:root /opt/snagem/.venv /opt/snagem/.venv
ENV PATH="/opt/snagem/.venv/bin:$PATH"
CMD ["snagd"]


FROM build-release as build-devel
RUN poetry install --without lsp

FROM core as devel
COPY --from=build-devel --chown=root:root /opt/snagem /opt/snagem
ENV PATH="/opt/snagem/.venv/bin:$PATH"
WORKDIR /opt/snagem
CMD ["tox"]
