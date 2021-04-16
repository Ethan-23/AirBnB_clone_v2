#!/usr/bin/env bash
#comment
if ! which nginx > /dev/null 2>&1; then
    apt-get update
    apt-get install nginx
fi

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

rm -f /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "/listen \[::\]:80 default_server/a location /hbnb_static {\n\talias /data/web_static/current/;\n}" /etc/nginx/sites-available/default
