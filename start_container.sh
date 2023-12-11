# this starts the container that runs the docker container

docker run -d --privileged --mount source=rtl_433_output,target=/src/data ece350project2:latest

# docker system prune -a -f --volumes
