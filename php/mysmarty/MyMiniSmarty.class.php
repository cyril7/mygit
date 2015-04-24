<?php

	class MyMiniSmarty {
		//我们的模板文件,var 兼容 4.0 之前的 public
		var $template_dir = "./templates/"; 
		//指定一个模板文件被替换后的文件（编译之后） 格式dom_对应的tpl.php
		var $complie_dir = "./templates_c/";
		//存放变量值
		var $tpl_vars = array();
		
		//这里我们主要模拟两个方法
		function assign($tpl_var,$val = null) {
		
			if( $tpl_var != '') {
				$this->tpl_vars[$tpl_var]=$val;
			}
		}
		
		//编写一个display方法，读取$tpl_file模板文件并替换相应的内容{%content}等
		function display($tpl_file) {
			
			//读取模板文件并替换成可以运行的php文件(编译后文件)
			$tpl_file_path = $this->template_dir.$tpl_file;
			$complie_file_path = $this->complie_dir."com_".$tpl_file.'.php';
			
			//判断文件存在否
			if (!file_exists($tpl_file_path)) {
				echo "file not exists!!!";
				return false;
			}
			
			//没必要每次都生成一个编译后文件
			//如果编译后的文件不存在 或 模板的更新时间比编译后的文件的更新时间大才需要生成编译后文件
			if (!file_exists($complie_file_path) || filemtime($tpl_file_path) > filemtime($complie_file_path)) {
				//此时数组中保存了 title content 两个key. $this->tpl_vars['title'] => '我的第一个文件title'
				$fpl_file_content = file_get_contents($tpl_file_path);
				
				
				//echo "OK";
				//echo $fpl_file_content;
				//var_dump($this->tpl_vars);
				
				//现在把{%xxx} 替换成相应的值
				$pattern = array (
					'/\{\s*\%([a-zA-Z_][a-zA-Z_0-9]*)\s*\}/i'
				);
				$replace = array (
					'<?php echo $this->tpl_vars["${1}"] ?>'
				);
				$new_str = preg_replace($pattern,$replace,$fpl_file_content);
				
				//输出到编译后的文件
				file_put_contents($complie_file_path,$new_str);
			}
			
			//替换完成后，引入编译后的文件即可
			include $complie_file_path;
		}
	}


/*
类的话可以不用结尾的 '?>' 符号
*/

