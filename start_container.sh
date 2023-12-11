# this starts the container that runs the docker container

# to use a volume: (docker managed)
#docker run -d --privileged --mount source=rtl_433_output,target=/src/data ece350project2:latest

# to use a mind mount: (a directory in the file system)
docker run -d --privileged --mount type=bind,source=/home/bsay/Documents/data,target=/src/data ece350project2:latest

# sometimes best to remove stuff after
# docker system prune -a -f --volumes
