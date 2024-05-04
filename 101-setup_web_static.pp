# File: setup_web_servers.pp

# Update package repository
package { 'nginx':
  ensure => latest,
}

# Create necessary directories
file { ['/data/web_static/releases', '/data/web_static/shared']:
  ensure => directory,
}

# Create a fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
}

# Set ownership recursively
file { '/data':
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

# Configure Nginx
file_line { 'hbnb_static':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => '    location /hbnb_static/ {
        alias /data/web_static/current/;
    }',
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File_line['hbnb_static'],
}
