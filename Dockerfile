# SPDX-License-Identifier: AGPL-3.0-or-later

FROM fedora:35 AS core
ENV PYTHONDONTWRITEBYTECODE="true" \
    PYTHONPYCACHEPREFIX="/tmp" \
    PYTHONUNBUFFERED="true"
RUN dnf --refresh -y upgrade && \
    dnf -y install libpq openssl sqlite && \
    dnf -y autoremove && \
    dnf clean all
RUN ln -sf /usr/share/zoneinfo/UTC /etc/localtime


FROM core AS build
RUN dnf --refresh -y install \
    automake cargo cmake gcc-c++ git meson ninja-build patchelf rust \
    libpq-devel openssl-devel python3-devel sqlite-devel
COPY . /opt/snagem
RUN python3 -m venv --upgrade-deps /opt/snagem/.venv
ENV PATH="/opt/snagem/.venv/bin:$PATH"
# FIXME: poetry>=1.2,<2 once released
RUN pip install poetry==1.2.0b1
WORKDIR /opt/snagem


FROM build as build-release
RUN poetry install --only default

FROM core AS release
COPY --from=build-release --chown=root:root /opt/snagem/.venv /opt/snagem/.venv
ENV PATH="/opt/snagem/.venv/bin:$PATH"
CMD ["snagd"]


FROM build as build-devel
RUN poetry install

FROM core as devel
COPY --from=build-devel --chown=root:root /opt/snagem /opt/snagem
ENV PATH="/opt/snagem/.venv/bin:$PATH"
WORKDIR /opt/snagem
CMD ["tox"]
