# 5. Puppet for setup

package { 'nginx':
  ensure   => present,
  provider => 'apt'
}
->
# create direcotries /data/web_static/shared/
file { '/data/web_static/shared':
  ensure => directory
}
->
# create direcotries /data/web_static/shared/
file { '/data/web_static/releases/test':
  ensure => directory
}
->
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => 'Holberton School',
  owner   => 'ubuntu',
  group   => 'ubuntu'
}
->
exec { 'symbolik link':
  command  => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
  user     => 'root',
  provider => 'shell'
}
->
file { '/data':
  ensure  => directory,
  user    => 'ubuntu',
  group   => 'ubuntu',
  recurse => true
}
->
exec { 'Added location':
  command   => 'sed -i "48i \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default',
  user      => 'root',
  provider  => 'shell'
}
->
exec { 'Start nginx':
  command  => 'service nginx restart',
  user     => 'root',
  provider => 'shell'
}
