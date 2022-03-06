# SPDX-License-Identifier: AGPL-3.0-or-later

FROM alpine:3.15 AS core
ENV PYTHONDONTWRITEBYTECODE="true" \
    PYTHONPYCACHEPREFIX="/tmp" \
    PYTHONUNBUFFERED="true" \
    VIRTUALENV="/opt/.venv"
RUN apk --no-cache add openssl postgresql14-client python3 sqlite tzdata
RUN ln -sf /usr/share/zoneinfo/UTC /etc/localtime


FROM core AS build
RUN apk --no-cache add cargo g++ gcc git libffi libstdc++ lld musl-dev openssl-dev patchelf
    postgresql14-dev py3-virtualenv py3-wheel python3-dev rust sqlite-dev
RUN virtualenv --system-site-packages $VIRTUALENV
ENV PATH="$VIRTUALENV/bin:$PATH"
COPY . /opt/snagem
RUN pip --disable-pip-version-check --no-cache-dir install /opt/snagem


FROM core AS release
COPY --from=build --chown=root:root $VIRTUALENV $VIRTUALENV
ENV PATH="$VIRTUALENV/bin:$PATH"
CMD ["snagd"]
