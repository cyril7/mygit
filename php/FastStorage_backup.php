<?php
/**
 * 分布式文件存储（基于fastdfs）处理类
 * 
 * 兼容有两种，支持Yii框架和非Yii框架的情况
 * 
 * 配置：
 * 
 * 1. 在Yii框架内

 *
 * 2. 非Yii框架内，必须修改以下两个常量值

 *
 * 本地测试平台架构过程：
 * 
 * 1. hosts映射一个域名到本地：127.0.0.1  upload.com
 * 2. 本地服务器（apache或nginx）新建一个虚拟站点，域名为upload.com
 * 3. 设置“上传地址的物理路径”为新虚拟站点的目录
 * 4. 设置“上传地址的URL”为新虚拟站点的访问URL
 */

class FastStorage
{
	// tracker服务器实例
	private $_tracker_server = null;  
	// storage服务器实例
	private $_storage_server = null;
	
	// 默认组名
	private $_group_name;
	// 链接重试次数
	private $try_connect_max = 10;
	
	/**
	 * FastStorage实例
	 * @param  $groupName 默认组名
	 */
	public function __construct() {
		defined('FDFS_HTTP_URL_BASE') or define('FDFS_HTTP_URL_BASE', Yii::app()->params['fastdfs_client']['FDFS_HTTP_URL_BASE']);
		defined('FDFS_HTTP_URL_PORT') or define('FDFS_HTTP_URL_PORT', Yii::app()->params['fastdfs_client']['FDFS_HTTP_URL_PORT']);
		defined('FDFS_HTTP_STORAGE_GROUP') or define('FDFS_HTTP_STORAGE_GROUP', Yii::app()->params['fastdfs_client']['FDFS_HTTP_STORAGE_GROUP']);
		defined('FDFS_LOCAL_STORAGE_PATH') or define('FDFS_LOCAL_STORAGE_PATH', Yii::app()->params['fastdfs_client']['FDFS_LOCAL_STORAGE_PATH']);
		defined('FDFS_LOCAL_STORAGE_URL') or define('FDFS_LOCAL_STORAGE_URL', Yii::app()->params['fastdfs_client']['FDFS_LOCAL_STORAGE_URL']);
		$this->_group_name = FDFS_HTTP_STORAGE_GROUP;
		$this->_getTracker();
	}

	/** 
	 * 上传本地文件
	 * @param  $localFile 本地文件路径
	 * @param  $fileExt   网络文件扩展名
	 * @param  $meta      META信息
	 */
	public function uploadFile($localFile, $fileExt = '', $meta = array())
	{
		$result = fastdfs_storage_upload_by_filename($localFile, $fileExt, $meta, $this->_group_name, $this->_tracker_server, $this->_storage_server);
		if( false == $result )throw new Exception(fastdfs_get_last_error_info());
		return array(
			'file_id' => $result['filename'],
			'file_url' => $this->getUrl($result['filename']),
		);
	}

	/**
	 * 上传变量数据
	 * @param  $var       本地变量内容
	 * @param  $fileExt   网络文件扩展名
	 * @param  $meta      META信息
	 */
	public function uploadVar($var, $fileExt = '', $meta = array())
	{
		$result = fastdfs_storage_upload_by_filebuff($var, $fileExt, $meta, $this->_group_name, $this->_tracker_server, $this->_storage_server);
		if( false == $result )throw new Exception(fastdfs_get_last_error_info());
		return $result;
	}
	
	/**
	 * 删除网络文件
	 * @param  $remoteFile 远程文件名称
	 */
	public function deleteFile($remoteFile)
	{
		return fastdfs_storage_delete_file($remoteFile, $this->_group_name);
	}
	
	/**
	 * 从网络生成本地文件
	 * @param  $remoteFile 远程文件名称
	 * @param  $localFile  本地待生成文件名
	 */
	public function downToFile($remoteFile, $localFile)
	{
		return fastdfs_storage_download_file_to_file($this->_group_name, $remoteFile, $localFile);
	}

	/**
	 * 从网络直接的读取文件内容
	 * @param  $remoteFile 远程文件名称
	 */
	public function downToVar($remoteFile)
	{
		return fastdfs_storage_download_file_to_buff($this->_group_name, $remoteFile);
	}
	
	/**
	 * 对网络文件设置META信息
	 * @param  $remoteFile 远程文件名称
	 * @param  $meta       META信息
	 */
	public function setMeta($remoteFile, $meta = array())
	{
		return fastdfs_storage_set_metadata($this->_group_name, $remoteFile, $meta);
	}
	
	/**
	 * 获取网络文件META信息
	 * @param  $remoteFile 远程文件名称
	 */
	public function getMeta($remoteFile)
	{
		return fastdfs_storage_get_metadata($this->_group_name, $remoteFile);
	}
	
	/**
	 * 获取文件URL访问路径
	 * @param  $remoteFile 远程文件名称
	 * @param  $useConfig    使用配置的网址
	 */
	public function getUrl($remoteFile, $useConfig = TRUE)
	{
		if( !$useConfig ){
			$url = $this->_storage_server['ip_addr'];
			if(substr($this->_storage_server['ip_addr'], 0, 7) != 'http://')$url = 'http://'.$url;
			if( 80 != $this->_storage_server['port'] )$url .= ':'.$this->_storage_server['port'];
		}else{
			if(!function_exists('fastdfs_client_version')){
				$url = FDFS_LOCAL_STORAGE_URL.((FDFS_HTTP_URL_PORT || FDFS_HTTP_URL_PORT != 80) ?':'.FDFS_HTTP_URL_PORT : '');
			}else{
				$url = FDFS_HTTP_URL_BASE.((FDFS_HTTP_URL_PORT || FDFS_HTTP_URL_PORT != 80) ?':'.FDFS_HTTP_URL_PORT : '');
			}

		}
		$url .= '/'.$this->_group_name.'/'.$remoteFile;
		return $url;
	}
	
	public function __destruct()
	{  
		fastdfs_tracker_close_all_connections();
	}  
	
	private function _getTracker()
	{  
		fastdfs_tracker_make_all_connections();
		$this->_tracker_server = fastdfs_tracker_get_connection();
		if ($this->_tracker_server == false || !fastdfs_active_test($this->_tracker_server)) { 
			throw new Exception(fastdfs_get_last_error_info());  
		}
		fastdfs_connect_server($this->_tracker_server['ip_addr'], $this->_tracker_server['port']);
		$this->_storage_server = fastdfs_tracker_query_storage_store();
		if (!$this->_storage_server){
			throw new Exception(fastdfs_get_last_error_info());  
		}
		do{
			$server = fastdfs_connect_server($this->_storage_server['ip_addr'], $this->_storage_server['port']);
			if (!$server || !fastdfs_active_test($server)){
				if($this->try_connect_max > 0){
					$this->try_connect_max--;
				}else{
					throw new Exception(fastdfs_get_last_error_info());
				}
			}else{
				break;
			}
		}while(1);
		$this->_storage_server['sock'] = $server['sock'];
	}
}

// 对当前环境进行判断，不能支持fastdfs的环境中，自动加载伪fastdfs函数，以保存测试正常。
if(!function_exists('fastdfs_client_version')){

	function fastdfs_tracker_make_all_connections(){}
	function fastdfs_tracker_close_all_connections(){}
	function fastdfs_tracker_get_connection(){return true;}
	function fastdfs_active_test(){return true;}
	function fastdfs_connect_server(){return true;}
	function fastdfs_get_last_error_info(){return ;}
	
	/**
	 * 检查本地配置和读写权限，同时返回访问URL和端口数组。
	 * 
	 * 这里同时检查环境是否Yii框架内
	 */
	function fastdfs_tracker_query_storage_store(){
		return array(
			'ip_addr' => FDFS_LOCAL_STORAGE_URL,
			'port'    => 80,
		);
	}
	
	function fastdfs_storage_upload_by_filename($localFile, $fileExt, $meta = array(), $groupName)
	{
		$filename = md5(time().mt_rand(200, 300));
		__fastdfs__mkdirs(FDFS_LOCAL_STORAGE_PATH.'/'.$groupName);
		copy($localFile, FDFS_LOCAL_STORAGE_PATH.'/'.$groupName.'/'.$filename.'.'. $fileExt);
		if(!empty($meta)){
			$meta = serialize($meta);
			file_put_contents($meta, FDFS_LOCAL_STORAGE_PATH.'/'.$groupName.'/'.'meta_'.$filename.'.'. $fileExt);
		}
		return array(
			'filename'   => $filename.'.'. $fileExt,
			'group_name' => $groupName,
		);
	}
	
	function fastdfs_storage_upload_by_filebuff($var, $fileExt, $meta = array(), $groupName)
	{
		$filename = md5(time().mt_rand(200, 300));
		__fastdfs__mkdirs(FDFS_LOCAL_STORAGE_PATH.'/'.$groupName);
		file_put_contents(FDFS_LOCAL_STORAGE_PATH.'/'.$groupName.'/'.$filename.'.'. $fileExt, $var);
		if(!empty($meta)){
			$meta = serialize($meta);
			file_put_contents($meta, FDFS_LOCAL_STORAGE_PATH.'/'.$groupName.'/'.'meta_'.$filename.'.'. $fileExt);
		}
		return array(
			'filename'   => $filename.'.'. $fileExt,
			'group_name' => $groupName,
		);
	}
	
	
	function fastdfs_storage_download_file_to_file($groupName, $remoteFile, $localFile)
	{
		$data = file_get_contents(FDFS_LOCAL_STORAGE_PATH.'/'.$groupName.'/'.$remoteFile);
		file_put_contents($localFile, $data);
	}
	function fastdfs_storage_download_file_to_buff($groupName, $remoteFile)
	{
		return file_get_contents(FDFS_LOCAL_STORAGE_PATH.'/'.$groupName.'/'.$remoteFile);
	}
	
	function fastdfs_storage_set_metadata($groupName, $remoteFile, $meta)
	{
		if(!empty($meta)){
			$meta = serialize($meta);
			file_put_contents($meta, FDFS_LOCAL_STORAGE_PATH.'/'.$groupName.'/'.'meta_'.$remoteFile);
		}
	}
	function fastdfs_storage_get_metadata($groupName, $remoteFile)
	{
		$data = file_get_contents(FDFS_LOCAL_STORAGE_PATH.'/'.$groupName.'/'.'meta_'.$remoteFile);
		return empty($data) ? '' : unserialize($data);
	}
	
	function fastdfs_storage_delete_file($remoteFile, $groupName)
	{
		$file=FDFS_LOCAL_STORAGE_PATH.'/'.$groupName.'/'.'meta_'.$remoteFile;
		@unlink($file);
	}
	
	function __fastdfs__mkdirs($dir, $mode = 0777)
	{
	        if (!is_dir($dir)) {
	                __fastdfs__mkdirs(dirname($dir), $mode);
	                return @mkdir($dir, $mode);
	        }
	        return true;
	}
}