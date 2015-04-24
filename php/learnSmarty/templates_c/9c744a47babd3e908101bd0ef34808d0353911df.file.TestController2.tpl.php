<?php /* Smarty version Smarty-3.1.11, created on 2012-08-17 23:43:57
         compiled from "./templates/TestController2.tpl" */ ?>
<?php /*%%SmartyHeaderCode:1979967134502e579971fc74-59267008%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    '9c744a47babd3e908101bd0ef34808d0353911df' => 
    array (
      0 => './templates/TestController2.tpl',
      1 => 1345218232,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '1979967134502e579971fc74-59267008',
  'function' => 
  array (
  ),
  'version' => 'Smarty-3.1.11',
  'unifunc' => 'content_502e5799888042_77433014',
  'variables' => 
  array (
    'arr1' => 0,
    'k' => 0,
    'temp' => 0,
    'arr2' => 0,
    'arr3' => 0,
    'k2' => 0,
    'val' => 0,
    'arr4' => 0,
  ),
  'has_nocache_code' => false,
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_502e5799888042_77433014')) {function content_502e5799888042_77433014($_smarty_tpl) {?><html>
	<h1>one vec index array for USER LIST</h1>
	<?php  $_smarty_tpl->tpl_vars['temp'] = new Smarty_Variable; $_smarty_tpl->tpl_vars['temp']->_loop = false;
 $_smarty_tpl->tpl_vars['k'] = new Smarty_Variable;
 $_from = $_smarty_tpl->tpl_vars['arr1']->value; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array');}
foreach ($_from as $_smarty_tpl->tpl_vars['temp']->key => $_smarty_tpl->tpl_vars['temp']->value){
$_smarty_tpl->tpl_vars['temp']->_loop = true;
 $_smarty_tpl->tpl_vars['k']->value = $_smarty_tpl->tpl_vars['temp']->key;
?>
		<?php echo $_smarty_tpl->tpl_vars['k']->value;?>
=<?php echo $_smarty_tpl->tpl_vars['temp']->value;?>

	<?php } ?>
	<p>===================</p>
	<h1>one vec assoc array for  USER LIST</h1>
	<?php  $_smarty_tpl->tpl_vars['temp'] = new Smarty_Variable; $_smarty_tpl->tpl_vars['temp']->_loop = false;
 $_smarty_tpl->tpl_vars['k'] = new Smarty_Variable;
 $_from = $_smarty_tpl->tpl_vars['arr2']->value; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array');}
foreach ($_from as $_smarty_tpl->tpl_vars['temp']->key => $_smarty_tpl->tpl_vars['temp']->value){
$_smarty_tpl->tpl_vars['temp']->_loop = true;
 $_smarty_tpl->tpl_vars['k']->value = $_smarty_tpl->tpl_vars['temp']->key;
?>
		<?php echo $_smarty_tpl->tpl_vars['k']->value;?>
=<?php echo $_smarty_tpl->tpl_vars['temp']->value;?>

	<?php } ?>

	<p>===================</p>
	<h1>two vec index array for  USER LIST</h1>
	<?php  $_smarty_tpl->tpl_vars['temp'] = new Smarty_Variable; $_smarty_tpl->tpl_vars['temp']->_loop = false;
 $_smarty_tpl->tpl_vars['k1'] = new Smarty_Variable;
 $_from = $_smarty_tpl->tpl_vars['arr3']->value; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array');}
foreach ($_from as $_smarty_tpl->tpl_vars['temp']->key => $_smarty_tpl->tpl_vars['temp']->value){
$_smarty_tpl->tpl_vars['temp']->_loop = true;
 $_smarty_tpl->tpl_vars['k1']->value = $_smarty_tpl->tpl_vars['temp']->key;
?>
		<?php  $_smarty_tpl->tpl_vars['val'] = new Smarty_Variable; $_smarty_tpl->tpl_vars['val']->_loop = false;
 $_smarty_tpl->tpl_vars['k2'] = new Smarty_Variable;
 $_from = $_smarty_tpl->tpl_vars['temp']->value; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array');}
foreach ($_from as $_smarty_tpl->tpl_vars['val']->key => $_smarty_tpl->tpl_vars['val']->value){
$_smarty_tpl->tpl_vars['val']->_loop = true;
 $_smarty_tpl->tpl_vars['k2']->value = $_smarty_tpl->tpl_vars['val']->key;
?>
			<?php echo $_smarty_tpl->tpl_vars['k2']->value;?>
=<?php echo $_smarty_tpl->tpl_vars['val']->value;?>

		<?php } ?>
	<br/>
	<?php } ?>

	<p>===================</p>
	<h1>two vec assoc array for  USER LIST</h1>
	<?php  $_smarty_tpl->tpl_vars['temp'] = new Smarty_Variable; $_smarty_tpl->tpl_vars['temp']->_loop = false;
 $_smarty_tpl->tpl_vars['k1'] = new Smarty_Variable;
 $_from = $_smarty_tpl->tpl_vars['arr4']->value; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array');}
foreach ($_from as $_smarty_tpl->tpl_vars['temp']->key => $_smarty_tpl->tpl_vars['temp']->value){
$_smarty_tpl->tpl_vars['temp']->_loop = true;
 $_smarty_tpl->tpl_vars['k1']->value = $_smarty_tpl->tpl_vars['temp']->key;
?>
		<?php  $_smarty_tpl->tpl_vars['val'] = new Smarty_Variable; $_smarty_tpl->tpl_vars['val']->_loop = false;
 $_smarty_tpl->tpl_vars['k2'] = new Smarty_Variable;
 $_from = $_smarty_tpl->tpl_vars['temp']->value; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array');}
foreach ($_from as $_smarty_tpl->tpl_vars['val']->key => $_smarty_tpl->tpl_vars['val']->value){
$_smarty_tpl->tpl_vars['val']->_loop = true;
 $_smarty_tpl->tpl_vars['k2']->value = $_smarty_tpl->tpl_vars['val']->key;
?>
			<?php echo $_smarty_tpl->tpl_vars['k2']->value;?>
=<?php echo $_smarty_tpl->tpl_vars['val']->value;?>

		<?php } ?>
	<br/>
	<?php } ?>

	<p>===================</p>
	<h1>two vec assoc array for  USER LIST "if"</h1>
	<?php  $_smarty_tpl->tpl_vars['temp'] = new Smarty_Variable; $_smarty_tpl->tpl_vars['temp']->_loop = false;
 $_smarty_tpl->tpl_vars['k1'] = new Smarty_Variable;
 $_from = $_smarty_tpl->tpl_vars['arr4']->value; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array');}
foreach ($_from as $_smarty_tpl->tpl_vars['temp']->key => $_smarty_tpl->tpl_vars['temp']->value){
$_smarty_tpl->tpl_vars['temp']->_loop = true;
 $_smarty_tpl->tpl_vars['k1']->value = $_smarty_tpl->tpl_vars['temp']->key;
?>
		<?php  $_smarty_tpl->tpl_vars['val'] = new Smarty_Variable; $_smarty_tpl->tpl_vars['val']->_loop = false;
 $_smarty_tpl->tpl_vars['k2'] = new Smarty_Variable;
 $_from = $_smarty_tpl->tpl_vars['temp']->value; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array');}
foreach ($_from as $_smarty_tpl->tpl_vars['val']->key => $_smarty_tpl->tpl_vars['val']->value){
$_smarty_tpl->tpl_vars['val']->_loop = true;
 $_smarty_tpl->tpl_vars['k2']->value = $_smarty_tpl->tpl_vars['val']->key;
?>
			<?php if ($_smarty_tpl->tpl_vars['k2']->value!='age'){?>
				<?php echo $_smarty_tpl->tpl_vars['k2']->value;?>
=<?php echo $_smarty_tpl->tpl_vars['val']->value;?>

			<?php }?>
		<?php } ?>
	<br/>
	<?php } ?>

	<p>===================</p>
	<h1>two vec assoc array for  USER LIST "if else elseif"</h1>
	<?php  $_smarty_tpl->tpl_vars['temp'] = new Smarty_Variable; $_smarty_tpl->tpl_vars['temp']->_loop = false;
 $_smarty_tpl->tpl_vars['k1'] = new Smarty_Variable;
 $_from = $_smarty_tpl->tpl_vars['arr4']->value; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array');}
foreach ($_from as $_smarty_tpl->tpl_vars['temp']->key => $_smarty_tpl->tpl_vars['temp']->value){
$_smarty_tpl->tpl_vars['temp']->_loop = true;
 $_smarty_tpl->tpl_vars['k1']->value = $_smarty_tpl->tpl_vars['temp']->key;
?>
		<?php if ($_smarty_tpl->tpl_vars['temp']->value['age']>40){?>
			older
		<?php }else{ ?>
			<h2>younger</h2>
		<?php }?>
	<br/>
	<?php } ?>
	

</html>
<?php }} ?>