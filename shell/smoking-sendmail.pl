#!/usr/bin/perl
use Mail::Sender;
use Log::Minimal;
use File::Stamped;
use encoding 'utf-8';
$vAlert=$ARGV[0];
$vTarget=$ARGV[1];
$vPktLoss=$ARGV[2];
$vRTT=$ARGV[3];
$vHostName=$ARGV[4];
$vEdgeTrigger=$ARGV[5];

## LOGing Function
my $fh = File::Stamped->new(pattern => '/usr/local/smokeping/log/sendmail.log_%Y%m%d');
local $Log::Minimal::PRINT = sub {
        my ( $time, $type, $message, $trace) = @_;
            print {$fh} "$time [$type] $message at $trace\n";
        };

=pod
## debug test
#$log="/usr/local/smokeping/log/sendmail.log";
#open(FH,">>$log"); 
#print FH "$vAlert,$vTarget,$vPktLoss,$vRTT,$vHostName,$vEdgeTrigger\n";
#close FH;
## 

#For debug assist
$vAlert="SomeAlert";
$vTarget="SomeTarget";
$vPktLoss="20%";
$vRTT="3000";
$vHostName="BogusHost";
$vEdgeTrigger="1";
=cut

# If you leave any fields blank [most are required] leave them as empty strings [i.e. ""].
# Optional fields are CC/BCC/MessageBodyPrefix and Postfix.
# I've tailored this to attempt to fit in a 160 char SMS.
# Leave MessageBodyPrefix/MessageBodyProstfix blank if you try to fit
#in SMS's 160 chars
# Keeping everything short is a must! Short email addy's etc.
# I've stripped the message body as much as possible too.
# You're welcome to tinker if you like, just don't blame me if you break something! :)
# You can modify most all of the following variables - leave the code
#be, unless you know what you're doing. [I don't, and look what
#happened to me!]

$vSMTPHost="smtp.bb.net";
$vHelloHost="bb.net";
$vDestPort="25";
$vFrom='samonitor@bb.net';
$vSMTPAuthUser='samonitor@bb.net';
$vSMTPAuthPass='Sa';

#$vTo='abc@abc.com,13999999999@aa.com';
$vTo='aaag@cc.com,123456789@aa.com,bbb@cc.com';
#Multi-Address is like this: $vTo='alerts at somenet.local, some.other.addy at somewhere.local';
$vCC='';
$vBCC='';
$vReplyTo='';
$vPriority="3"; #Priority in Mail::Sender: 1-5, 1=high, 5=low
$vHeaderSubject="Subject: Smokeping alert: $vTarget";
$vMessageBodyPrefix="";
$vMessageBodyPostfix="";

eval {
        $smtp = new Mail::Sender {
                smtp => "$vSMTPHost",
                auth=>'LOGIN',
                from => "$vFrom",
                port => "$vDestPort",
                client => "$vHelloHost",
                authid => "$vSMTPAuthUser",
                authpwd => "$vSMTPAuthPass",
                charset=>"utf-8",
                on_errors => 'die',
        };
        $smtp->Open({
                to => "$vTo",
                cc => "$vCC",
                bcc => "$vBCC",
                replyto => "$vReplyTo",
                subject => "$vHeaderSubject",
                priority => "$vPriority"
        });

        if ($vMessageBodyPrefix ne "")
                {$smtp->datasend("$vMessageBodyPrefix");}

        $smtp->SendLineEnc("Alert:$vAlert");
        $smtp->SendLineEnc("$vTarget");
        $smtp->SendLineEnc("$vPktLoss");
        $smtp->SendLineEnc("$vRTT");
        $smtp->SendLineEnc("$vHostName");
        $smtp->SendLineEnc("ETSt: $vEdgeTrigger");

        if ($vMessageBodyPostfix ne "")
                {$smtp->SendLineEnc("$vMessageBodyPostfix");}

        $smtp->Close();
};
if ($@) {
        #die "Failed to send the message: $@\n";
        infof("Failed to send the message: $@");
}
else {
       infof("OK to send the message: $vTo") 
}
infof("$vAlert,$vTarget,$vPktLoss,$vRTT,$vHostName,$vEdgeTrigger");
