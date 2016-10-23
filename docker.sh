
#!/bin/bash

### It dockerizes automatically ###
cd /home/TolaTables
git stash
git pull origin docker

docker-compose build 
docker-compose up
