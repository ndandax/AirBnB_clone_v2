#!/usr/bin/env bash
<<<<<<< HEAD
#A Bash script that sets up your web servers for the deployment of web_static

if [ ! -x "$(command -v nginx)" ]; then
sudo apt-get update
sudo apt-get -y install nginx
fi

sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

echo "
=======
# Setup a web servers for the deployment of web_static.
apt update -y
apt install -y nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<!DOCTYPE html>
>>>>>>> b7bd53f53b3d33e16d6c38c4ef24682b48d1f8c9
<html>
  <head>
  </head>
  <body>
<<<<<<< HEAD
    ALX School
  </body>
</html>

" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf '/data/web_static/releases/test/' '/data/web_static/current'


sudo sed -i 's#server_name _;#server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n#g' /etc/nginx/sites-available/default

sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'

=======
    <p>Nginx server test</p>
  </body>
</html>" | tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
sudo sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default
>>>>>>> b7bd53f53b3d33e16d6c38c4ef24682b48d1f8c9
sudo service nginx restart
