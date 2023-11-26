#!/usr/bin/env bash
# configuration by puppet

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "
    host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
  "
}

