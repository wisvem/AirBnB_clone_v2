#!/usr/bin/env bash
# 0. Prepare your web servers
mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >/data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
my_string="        location /hbnb_static {
                alias /home/vagrant/AirBnB_clone_v2/data/web_static/current/
        }"
FILE=/etc/nginx/sites-available/default
result=$(grep "$my_string" "$FILE")
if [ -z "$result" ]; then
    sed -i "48 a $my_string" "$FILE"
fi
service nginx restart
