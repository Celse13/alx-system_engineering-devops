# Stoping the process
exec { 'killmenow':
  command   => '/usr/bin/pkill -TERM killmenow',
}
