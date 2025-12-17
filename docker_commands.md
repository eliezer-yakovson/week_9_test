# Creates the volume
docker volume create fastapi-db

# Builds the server1 image
docker build -t shopping-server1:v1 ./server1

# Starting the server1 container and creating the file on the volume
docker run --rm -v fastapi-db:/app/db
docker run -d --name shopping-server1 -p 8000:8000 -v fastapi-db:/app/db shopping-server1:v1
docker exec -it shopping-server1 sh
echo '[]' > /app/db/shopping_list.json
cat /app/db/shopping_list.json

# Builds the server2 image
docker build -t shopping-server2:v1 ./server2

# Runs the server2 container with the same volume
docker run -d --name shopping-server2 -p 8001:8001 -v fastapi-db:/app/db shopping-server2:v1