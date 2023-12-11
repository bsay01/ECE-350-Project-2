# syntax=docker/dockerfile:1

# Pick a base image to serve as the foundation for the other build stages in this file.
FROM ece350project2_base:latest as base

# Create a stage for building/compiling the application.
FROM base as build

# copy all files for project into image
COPY ./start_433.sh /src

# configure libraries
RUN ldconfig

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser
USER appuser

# What the container should run when it is started.
#ENTRYPOINT [ "/src/start_433.sh" ]
CMD bash /src/start_433.sh
