# SPDX-License-Identifier: AGPL-3.0-or-later

FROM fedora:35 AS core
ENV PYTHONDONTWRITEBYTECODE="true" \
    PYTHONPYCACHEPREFIX="/tmp" \
    PYTHONUNBUFFERED="true"
RUN dnf --refresh -y upgrade && \
    dnf -y install openssl libpq sqlite && \
    dnf -y autoremove && \
    dnf clean all
RUN ln -sf /usr/share/zoneinfo/UTC /etc/localtime
CMD ["/bin/sh"]


FROM core AS build
RUN dnf --refresh -y install \
    automake cargo cmake gcc-c++ git meson ninja-build patchelf rust \
    libpq-devel openssl-devel python3-devel python3-wheel sqlite-devel
COPY . /opt/snagem
WORKDIR /opt/snagem
RUN python3 -m venv --upgrade-deps /opt/snagem/.venv
ENV PATH="/opt/snagem/.venv/bin:$PATH"
RUN pip --disable-pip-version-check --no-cache-dir --use-feature=in-tree-build install poetry
RUN poetry install --no-dev


# podman build . --tag jcmdln/snagem:release --target release
FROM core AS release
COPY --from=build --chown=root:root /opt/snagem/.venv /opt/snagem/.venv
ENV PATH="/opt/snagem/.venv/bin:$PATH"
CMD ["snagd"]


# podman build . --tag jcmdln/snagem:devel --target devel
FROM build as build-devel
RUN poetry install

FROM core as devel
COPY --from=build-devel --chown=root:root /opt/snagem /opt/snagem
ENV PATH="/opt/snagem/.venv/bin:$PATH"
WORKDIR /opt/snagem
CMD ["tox"]
