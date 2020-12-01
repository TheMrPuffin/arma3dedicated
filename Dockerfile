FROM cm2network/steamcmd:root

LABEL maintainer="TheMrPuffin"

ENV STEAM_USER annoymous 
ENV PASSWORD annoymous


RUN set -x \ 
    && apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
        python3 \
    && apt-get remove --purge -y \
    && apt-get clean autoclean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*
USER ${USER}

RUN mkdir -p /home/${USER}/arma3-dedicated/configs/profiles 
 
COPY serverLaunch.py /home/${USER}/arma3-dedicated

WORKDIR  /home/${USER}/arma3-dedicated

USER ${USER} 

VOLUME ["/home/${USER}/arma3-dedicated"]

EXPOSE 2302/udp 2303/udp 2304/udp 2305/udp 2306/udp 