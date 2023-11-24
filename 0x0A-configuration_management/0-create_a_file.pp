# Creating a file with the provided path
file { '/tmp/school':
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
}
