# SPDX-License-Identifier: AGPL-3.0-or-later

FROM fedora:36 AS core
RUN dnf install -y libpq python3 sqlite tini tzdata && \
    dnf autoremove -y && \
    dnf clean all
RUN ln -sf /usr/share/zoneinfo/UTC /etc/localtime
ENTRYPOINT ["/usr/bin/tini", "--"]

FROM core AS build
RUN dnf install -y gcc gcc-c++ git libpq-devel patchelf python3-devel python3-pip python3-wheel
COPY . /opt/snagem
WORKDIR /opt/snagem
RUN python3 -m venv /opt/snagem/.venv
ENV PATH="/opt/snagem/.venv/bin:$PATH"
RUN pip install .

FROM core AS release
RUN useradd --system snagem
COPY --from=build --chown=snagem:snagem /opt/snagem /opt/snagem
ENV PATH="/opt/snagem/.venv/bin:$PATH"
WORKDIR /opt/snagem
USER snagem
CMD ["snagd"]
