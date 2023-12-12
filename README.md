# ECE-350-Project-2

provides a way to create and start a docker image for ECE 350 project 2.

meant for a raspberry pi running Raspbian 11 Bullseye.

for a new system, run configure_docker_raspbian.sh before anything else.

then run build_image.sh to build the project image. the base image needs to be built if it's not there already.

if you're unsure, build it.

afterwards, run start_container.sh to run the container.

find the docker volume that was created (automatically) during startup to export the data. it will persist between containers.

run analysis using python 2.7.18 or any version that acts the same as it. a new combined data file will be created from all csv's of data in the data directory.
