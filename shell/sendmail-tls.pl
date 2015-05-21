use strict;
use warnings;

use Net::SSLGlue::SMTP;
my $smtp = Net::SMTP->new( 'mail.aa.net', Debug => 1 ) or die $@;
# $smtp->starttls( SSL_ca_path => "/etc/ssl/certs" ) or die $@;

# 服务器不检查ca的话需要把 SSL_verify_mode => 0 
$smtp->starttls( SSL_verify_mode => 0) or die $@;

$smtp->auth( 'monitor@aa.net','xxx2');
$smtp->mail( 'monitor@aa.net' );
$smtp->to( 'xyz@aa.net' );
$smtp->data;
$smtp->datasend( <<EOD );
From: me
To: you
Subject: test test
lalaal
EOD
$smtp->dataend;
$smtp->quit;

