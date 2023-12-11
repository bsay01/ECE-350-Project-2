# this starts the container that runs the docker container

docker run -d --mount source=rtl_433_output,target=/src/data

# docker system prune -a -f --volumes
