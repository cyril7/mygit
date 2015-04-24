<?php
$data[]=array('name'=>'万','sex'=>'男','age'=>12);
$data[]=array('name'=>'陈','sex'=>'女','age'=>10);
$data[]=array('name'=>$_REQUEST['name'],'sex'=>$_REQUEST['sex'],'age'=>$_REQUEST['age']);
//echo json_encode($data);
echo json_encode ( gbk2utf8($data) );
function gbk2utf8($data){
    if(is_array($data)){
        return array_map('gbk2utf8', $data);
    }
    return iconv('gbk','utf-8',$data);
}
?>

