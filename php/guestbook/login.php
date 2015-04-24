<?php
    session_start();
    if (isset($_POST['Submit'])){
        if (!get_magic_quotes_gpc()) {
            foreach ($_POST as $items) {
                $items = addslashes($items);
            }
        }
        if($_POST['username'] == 'admin' && $_POST['password'] == 'admin') {
            $_SESSION['login'] == true;
            echo "
                <script>
                    location.href='index.php';
                </script>";
            exit();
        }
        else {
            echo "
                <script>
                    alert('登录失败');
                </script>";
        }
    }
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>无标题文档</title>
    </head>
    <body>
                    <form action="login.php" method="POST" name="form1">
                        用户名：<input type="text" name="username" size="20"/>
                        密码：<input type="password" name="password" size="20">
                        <input type="submit" value="登录" name="Submit"/>
                        <input type="button" onclick="javascript:location.href='index.php'" value="放弃"/>
                    </form>
    </body>
</html>
