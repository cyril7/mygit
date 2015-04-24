<?php
$data['#title#'] = 'Page title';
$data['#textcontent#'] = ' Yadda yadda yadda';
//Grab a seperate bit of text that is the HTML with placeholders in it:

$html = '<html>
<head>
<title>#title#</title>
</head>
<body><p>#textcontent#</p>
</body>
</html>'; // etc
//Then merge the two with a simple command:

$html = str_replace(array_keys($data),array_values($data),$html);
//The print or store in cache.

echo $html;
?>
