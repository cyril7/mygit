<?php /* Smarty version Smarty-3.1.11, created on 2012-10-09 02:35:59
         compiled from "smarty2.html" */ ?>
<?php /*%%SmartyHeaderCode:1456332995507313457c1110-95298903%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    '8643f815eeb6eb1d129a157139a2328f005e2d82' => 
    array (
      0 => 'smarty2.html',
      1 => 1349721353,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '1456332995507313457c1110-95298903',
  'function' => 
  array (
  ),
  'version' => 'Smarty-3.1.11',
  'unifunc' => 'content_50731345b92876_04809584',
  'variables' => 
  array (
    'db_count' => 0,
    'db_coltitle' => 0,
    'col' => 0,
    'db_rows' => 0,
    'dbrow' => 0,
    'val' => 0,
  ),
  'has_nocache_code' => false,
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_50731345b92876_04809584')) {function content_50731345b92876_04809584($_smarty_tpl) {?><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<link href="smarty2.css" rel="stylesheet" type="text/css" media="all" />
<script type="text/javascript" src="../jquery-1.3.2.js"></script>
<script type="text/javascript" src="smarty2.js"></script>
<title><?php echo @DB_TABLENAME;?>
</title>
</head>
<body>
<h1>表中有<?php echo $_smarty_tpl->tpl_vars['db_count']->value;?>
条记录</h1>
<table border="1" align="center" cellpadding="10" cellspacing="2" bordercolor="#ffaaoo">
<?php  $_smarty_tpl->tpl_vars['col'] = new Smarty_Variable; $_smarty_tpl->tpl_vars['col']->_loop = false;
 $_from = $_smarty_tpl->tpl_vars['db_coltitle']->value; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array');}
foreach ($_from as $_smarty_tpl->tpl_vars['col']->key => $_smarty_tpl->tpl_vars['col']->value){
$_smarty_tpl->tpl_vars['col']->_loop = true;
?>
    <th><?php echo $_smarty_tpl->tpl_vars['col']->value;?>
</th>
<?php } ?>
<?php  $_smarty_tpl->tpl_vars['dbrow'] = new Smarty_Variable; $_smarty_tpl->tpl_vars['dbrow']->_loop = false;
 $_from = $_smarty_tpl->tpl_vars['db_rows']->value; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array');}
foreach ($_from as $_smarty_tpl->tpl_vars['dbrow']->key => $_smarty_tpl->tpl_vars['dbrow']->value){
$_smarty_tpl->tpl_vars['dbrow']->_loop = true;
?>
    <tr>
    <?php  $_smarty_tpl->tpl_vars['val'] = new Smarty_Variable; $_smarty_tpl->tpl_vars['val']->_loop = false;
 $_smarty_tpl->tpl_vars['k'] = new Smarty_Variable;
 $_from = $_smarty_tpl->tpl_vars['dbrow']->value; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array');}
foreach ($_from as $_smarty_tpl->tpl_vars['val']->key => $_smarty_tpl->tpl_vars['val']->value){
$_smarty_tpl->tpl_vars['val']->_loop = true;
 $_smarty_tpl->tpl_vars['k']->value = $_smarty_tpl->tpl_vars['val']->key;
?>
        <td><?php echo $_smarty_tpl->tpl_vars['val']->value;?>
</td>
    <?php } ?>
    </tr>
<?php } ?>
</table>
</body>
</html>
<?php }} ?>