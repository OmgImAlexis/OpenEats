FROM jfloff/alpine-python:2.7
MAINTAINER Alexis Tyler <xo@wvvw.me>

# Add community back in so we can install tini
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" > /etc/apk/repositories \
 && echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories

RUN apk --no-cache add py-mysqldb \
    && apk --no-cache add --virtual devs tar curl

# Allow Let's Encrypt's cert to work with caddyserver.com
RUN apk --update upgrade && \
    apk add curl ca-certificates && \
    update-ca-certificates && \
    rm -rf /var/cache/apk/*

# Install Caddy Server, and All Middleware
RUN curl "https://caddyserver.com/download/build?os=linux&arch=amd64&features=cors%2Crealip" \
    | tar --no-same-owner -C /usr/bin/ -xz caddy

# Remove build devs
RUN apk del devs

RUN pip install supervisor==3.3.0

WORKDIR /src

COPY Caddyfile /etc/Caddyfile
COPY supervisord.conf /etc/supervisord.conf
COPY requirements.txt /tmp/requirements.txt
COPY entrypoint.sh /

RUN chmod +x /entrypoint.sh && /entrypoint.sh -r /tmp/requirements.txt

ADD . .

EXPOSE 80

CMD ["supervisord", "--nodaemon", "--configuration", "/etc/supervisord.conf"]
