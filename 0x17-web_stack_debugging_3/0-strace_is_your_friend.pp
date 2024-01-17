# Fixing apache configuration
exec { 'fix_apache_config_issue':
  command  => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  provider => shell,
}
