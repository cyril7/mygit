<?php /*%%SmartyHeaderCode:162225012850308563ea6361-28314564%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    '64198ceaa90b1e0daa7b97f3800fd330b0ec1c48' => 
    array (
      0 => './templates/myindexUI.tpl',
      1 => 1345357244,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '162225012850308563ea6361-28314564',
  'version' => 'Smarty-3.1.11',
  'unifunc' => 'content_5030861b55f9b5_06142767',
  'has_nocache_code' => false,
  'cache_lifetime' => 20,
),true); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_5030861b55f9b5_06142767')) {function content_5030861b55f9b5_06142767($_smarty_tpl) {?><h1>Total of the visitors</h1>
<?php echo insert_getVisitTime(array (
),$_smarty_tpl);?>
<h2>User List</h2>
<?php }} ?>