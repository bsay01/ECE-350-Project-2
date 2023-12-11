# this builds the images for the project

echo ""
read -r -p "Build base image? [Y/n]: " response

if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]
then
    echo ""
    echo "-------------------------------------------------------"
    echo "|                                                     |"
    echo "|               building base image...                |"
    echo "|                                                     |"
    echo "-------------------------------------------------------"
    echo ""
    docker build --no-cache -t ece350project2_base ./base_docker_image
fi

echo ""
echo "-------------------------------------------------------"
echo "|                                                     |"
echo "|         building regular image from base...         |"
echo "|                                                     |"
echo "-------------------------------------------------------"
echo ""

docker build --no-cache -t ece350project2 ./docker_image
