<?php
/**
oauth mc test
 */

$mc = new Memcache;
$memOauthServers = array (array ('host' => $_ENV['WAP_OAUTH_MEMCACHED_HOST'], 'port' => $_ENV['WAP_OAUTH_MEMCACHED_PORT']),array ('host' => $_ENV['WAP_OAUTH_MEMCACHED_HOST2'], 'port' => $_ENV['WAP_OAUTH_MEMCACHED_PORT2']),array ('host' => $_ENV['WAP_OAUTH_MEMCACHED_HOST3'], 'port' => $_ENV['WAP_OAUTH_MEMCACHED_PORT3']));
foreach ($memOauthServers as $mem) echo "{$mem['host']} connect ". ($mc->connect($mem['host'], $mem['port']) ? 'success' : 'fail').'<hr/>';

