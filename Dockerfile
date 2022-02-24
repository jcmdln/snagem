# SPDX-License-Identifier: AGPL-3.0-or-later

FROM fedora:35 AS core
ENV PYTHONDONTWRITEBYTECODE="true" \
    PYTHONPYCACHEPREFIX="/tmp" \
    PYTHONUNBUFFERED="true" \
    VIRTUALENV="/opt/.venv"
RUN dnf --refresh upgrade -y && \
    dnf install -y openssl postgresql python3 tzdata && \
    dnf autoremove -y && \
    dnf clean all
RUN ln -sf /usr/share/zoneinfo/UTC /etc/localtime


FROM core AS build
RUN dnf install -y cargo gcc git rust openssl-devel patchelf \
    postgresql-server-devel python3-devel python3-wheel
RUN python3 -m venv --system-site-packages $VIRTUALENV
ENV PATH="$VIRTUALENV/bin:$PATH"
COPY . /opt/snagem
RUN pip --disable-pip-version-check --no-cache-dir install /opt/snagem


FROM core AS release
COPY --from=build --chown=root:root $VIRTUALENV $VIRTUALENV
ENV PATH="$VIRTUALENV/bin:$PATH"
CMD ["snagd"]
