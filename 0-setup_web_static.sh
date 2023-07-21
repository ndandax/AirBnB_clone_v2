#!/usr/bin/env bash
#A Bash script that sets up your web servers for the deployment of web_static

if [ ! -x "$(command -v nginx)" ]; then
sudo apt-get update
sudo apt-get -y install nginx
fi

sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

echo "
<html>
  <head>
  </head>
  <body>
    ALX School
  </body>
</html>

" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf '/data/web_static/releases/test/' '/data/web_static/current'


sudo sed -i 's#server_name _;#server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n#g' /etc/nginx/sites-available/default

sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'

sudo service nginx restart
