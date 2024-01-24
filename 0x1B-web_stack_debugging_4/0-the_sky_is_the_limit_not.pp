# Increasing the request limit for nginx web-server
file_line { 'fix--for-nginx':
  path  => '/etc/default/nginx',
  line  => '4096',
  match => '15',
}

# After changes, restart the nginx
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File_line['fix--for-nginx'],
}
