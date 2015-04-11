<?php /* Smarty version Smarty-3.1.11, created on 2012-10-09 22:57:13
         compiled from "smarty2.html" */ ?>
<?php /*%%SmartyHeaderCode:182198323850731c7baca2f0-62910087%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    '8643f815eeb6eb1d129a157139a2328f005e2d82' => 
    array (
      0 => 'smarty2.html',
      1 => 1349794602,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '182198323850731c7baca2f0-62910087',
  'function' => 
  array (
  ),
  'version' => 'Smarty-3.1.11',
  'unifunc' => 'content_50731c7bc8c1a6_17117046',
  'variables' => 
  array (
    'db_tablename' => 0,
    'db_count' => 0,
    'db_coltitle' => 0,
    'col' => 0,
    'db_rows' => 0,
    'dbrow' => 0,
    'val' => 0,
  ),
  'has_nocache_code' => false,
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_50731c7bc8c1a6_17117046')) {function content_50731c7bc8c1a6_17117046($_smarty_tpl) {?><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<link href="smarty2.css" rel="stylesheet" type="text/css" media="all" />
<script type="text/javascript" src="../jquery-1.3.2.js"></script>
<script type="text/javascript" src="smarty2.js"></script>
<title><?php echo @DB_TABLENAME;?>
</title>
</head>
<body>
<h1>表名：<?php echo $_smarty_tpl->tpl_vars['db_tablename']->value;?>
</h1>
<table id="Table" border="1" align="center" cellpadding="10" cellspacing="2" bordercolor="#ffaaoo">
<caption style="font-size:15px">当前记录数：<label id="tableRowCount"><?php echo $_smarty_tpl->tpl_vars['db_count']->value;?>
</label>  &nbsp;&nbsp;&nbsp; <input type="button" value="Add" onclick="addFun()" /> </caption>
<?php  $_smarty_tpl->tpl_vars['col'] = new Smarty_Variable; $_smarty_tpl->tpl_vars['col']->_loop = false;
 $_from = $_smarty_tpl->tpl_vars['db_coltitle']->value; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array');}
foreach ($_from as $_smarty_tpl->tpl_vars['col']->key => $_smarty_tpl->tpl_vars['col']->value){
$_smarty_tpl->tpl_vars['col']->_loop = true;
?>
    <th><?php echo $_smarty_tpl->tpl_vars['col']->value;?>
</th>
<?php } ?>
<th>操作</th>
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
	<td>
		<input type="button" value="Edit" onclick="editFun('<?php echo $_smarty_tpl->tpl_vars['dbrow']->value['id'];?>
', '<?php echo $_smarty_tpl->tpl_vars['dbrow']->value['name'];?>
', '<?php echo $_smarty_tpl->tpl_vars['dbrow']->value['age'];?>
');" />
        <input type="button" value="Delete" onclick="deleteFun('<?php echo $_smarty_tpl->tpl_vars['dbrow']->value['id'];?>
')" />
	</td> 
    </tr>
<?php } ?>
</table>

<div id="editdiv" style="display:none;color:red;" align="center">
 <form>
 id:<input type=text id="editdiv_id" readonly="true" />
 name:<input type=text id="editdiv_name" />
 age:<input type=text id="editdiv_age" />
 <input type=button name="Updata" value="Updata" onclick="updataFun()" />
</form>
</div>
<div id="adddiv" style="display:none;color:green;" align="center">
 <form>
 name:<input type=text id="adddiv_name" />
 age:<input type=text id="adddiv_age" />
 <input type=button name="Insert" value="Insert" onclick="insertFun()" / >
</form>
</div>
</body>
</html>
<?php }} ?>