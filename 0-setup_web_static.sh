#!/usr/bin/env bash
# A scrip that sets up your web servers for the deployment of web_static

# Install Nginx if it is not already installed
sudo apt-get update
sudo apt-get install -y nginx

# Create the necessary directories if they do not exist
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link, remove if it exists
sudo rm -f /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Configure Nginx to serve the content of /data/web_static/current/ under hbnb_static
if ! grep -q "hbnb_static" /etc/nginx/sites-available/default; then
    sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
fi

# Restart Nginx to apply the changes
sudo service nginx restart

# Exit successfully
exit 0

# # Check and install nginx if not installed
# if ! dpkg -s nginx >/dev/null 2>&1; then
#     sudo apt-get update
#     sudo apt-get install -y nginx
# fi

# # Create directories if not available
# sudo mkdir -p /data/web_static/releases/test/
# sudo mkdir -p /data/web_static/shared/

# # Creating a test HTML
# cat <<E0F | sudo tee /data/web_static/releases/test/index.html > /dev/null
# <html>
# <head></head>
# <body>Holberton School</body>
# </html>
# E0F

# # Create symbolic link
# sudo rm -rf /data/web_static/current
# sudo lm -sf /data/web_static/releases/test/ /data/web_static/current


# # Grant ownership
# sudo chown -R ubuntu:ubuntu /data/

# nginx_config="/etc/nginx/sites-available/default"
# sudo sed -i '38i \\\tlocation /hbnb_static/ {\n\t\talias /data_web_static/current/;\n\t}\n' "$nginx_config"

# sudo service nginx restart

# exit 0