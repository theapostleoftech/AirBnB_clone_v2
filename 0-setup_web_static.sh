#!/usr/bin/env bash
# A scrip that sets up your web servers for the deployment of web_static

# Check and install nginx if not installed
if ! dpkg -s nginx > /dev/null 2>&1; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create directories if not available
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Creating a test HTML
echo "<html>
<head></head>
<body>Holberton School</body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
sudo rm -rf /data/web_static/current
sudo lm -sf /data/web_static/releases/test/ /data/web_static/current


# Grant ownership
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '38i \\\tlocation /hbnb_static/ {\n\t\talias /data_web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart

exit 0