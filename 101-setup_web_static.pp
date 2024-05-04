# Define a class to set up web servers for web_static deployment
class setup_web_static {
  
  # Install Nginx if not already installed
  package { 'nginx':
    ensure => installed,
  }
  
  # Create necessary directories
  file { '/data':
    ensure  => directory,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0755',
    recurse => true,
  }

  file { '/data/web_static':
    ensure  => directory,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0755',
    recurse => true,
  }

  file { '/data/web_static/releases':
    ensure  => directory,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0755',
    recurse => true,
  }

  file { '/data/web_static/shared':
    ensure  => directory,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0755',
    recurse => true,
  }

  file { '/data/web_static/releases/test':
    ensure  => directory,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0755',
    recurse => true,
  }
  
  # Create a fake HTML file
  file { '/data/web_static/releases/test/index.html':
    ensure  => present,
    content => "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n",
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0644',
  }
  
  # Create or recreate symbolic link
  file { '/data/web_static/current':
    ensure  => link,
    target  => '/data/web_static/releases/test',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    require => File['/data/web_static/releases/test/index.html'],
    before  => Service['nginx'],
  }
  
  # Update Nginx configuration
  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => "server {\n    listen 80;\n    server_name _;\n\n    location /hbnb_static {\n        alias /data/web_static/current/;\n    }\n}\n",
    notify  => Service['nginx'],
  }

  # Restart Nginx after updating the configuration
  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/sites-available/default'],
  }
}

# Apply the class to the node
include setup_web_static
