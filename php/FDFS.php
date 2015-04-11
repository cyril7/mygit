<?php

class FDFS {
    protected $group_name;
    protected $tracker_server;
	protected $storage_server;
	
	public function factory($group_name) {
		static $fdfs_obj;
		if ( !$fdfs_obj ) {
			$fdfs_obj = new FDFS($group_name);
		}
		return $fdfs_obj;
	}

	public function __construct($group_name) {
		$this->group_name = $group_name;
		$this->storage_server = null;
		$this->connection();
	}


	public function connection() {
	    $this->tracker_server = fastdfs_tracker_get_connection();
		$this->tracker_conn =  fastdfs_connect_server($this->tracker_server['ip_addr'], $this->tracker_server['port']);
		if ( !$this->tracker_conn ) {
			$this->error_no = fastdfs_get_last_error_no();
			$this->error_info = fastdfs_get_last_error_info();
		     error_log("tracker connect errno: " . $this->error_no . ", error info: " . $this->error_info);
			 exit($this->error_no);
		}

		$this->storage_server = fastdfs_tracker_query_storage_store();
		$this->storage_conn =  fastdfs_connect_server($this->storage_server['ip_addr'], $this->storage_server['port']);
		if ( !$this->storage_conn ) {
			$this->error_no = fastdfs_get_last_error_no();
			$this->error_info = fastdfs_get_last_error_info();
		     error_log("storage connect errno: " . $this->error_no . ", error info: " . $this->error_info);
			 exit($this->error_no);
		}
		//$this->storage_server['sock'] = $this->storage_conn['sock'];
	}

	//public function disconnection() {
	//	fdfs_quit($this->tracker_server);
	//	fastdfs_tracker_close_all_connections();
	//}

	public function __destruct() {
		fastdfs_tracker_close_all_connections();
		//$this->disconnection();
	}
      	/**
		 * Upload_By_Filebuff
         * @param string $local_file_name
         * @param string $file_ext
         * @param array $meta_list
         * @return remote file_id
		 *   string fastdfs_storage_upload_by_filebuff1(string file_buff
    	 *   [, string file_ext_name, array meta_list, string group_name,
    	 *   array tracker_server, array storage_server])
		 *   upload file buff to storage server
		 */
	public function upByBuff( $local_file_name,$file_ext_name,$meta_list = array() ) {
        //$local_file_name = 'nginx.png';
        //$file_ext_name = 'png';
        //$meta_list = array('width' => 1024, 'height' => 768, 'color' => '#c0c0c0');
        //echo FDFS::factory('group1')->upByBuff('nginx.png', 'png')."<br />\n";
		if ( $local_file_name != false ) {
			$file_buff = file_get_contents($local_file_name);
			$remote_file_id = fastdfs_storage_upload_by_filebuff1($file_buff,$file_ext_name,$meta_list,
				$this->group_name,$this->tracker_server, $this->storage_server);
			if ( $remote_file_id != false ) {
				return $remote_file_id;
			}
			else {
				echo "err!!,no remote_file_id.\n";
			}
		}
	}
      	/**
		 * download_By_Filebuff
         * @param string $remote_file_id
         * @return local_file_name
		 *  string fastdfs_storage_download_file_to_buff1(string file_id
         *  [, long file_offset, long download_bytes,
         *  array tracker_server, array storage_server])
         *  get file content from storage server
		 */
	public function downToBuff ( $remote_file_id ) {
        //$remote_file_id = 'ysctest/M00/00/00/cY4h7U-Q02P07DKdAAAABeDOzyU540.png';
        //echo FDFS::factory('group1')->downToBuff( $remote_file_id ),"<br />\n";
		$file_buff = fastdfs_storage_download_file_to_buff1( $remote_file_id, 0, 0,
			$this->tracker_server,$this->storage_server );
		if ( $file_buff != false ) {
			$local_file_name = str_replace('/', '_', $remote_file_id);
			file_put_contents($local_file_name, $file_buff);
			return $local_file_name;
		}
		else {
			echo "err!!,no local_file_name.\n";
		}
	}
      	/**
		 * file_Is_Exist
         * @param string $remote_file_id
         * @return boolean 
		 *  boolean fastdfs_storage_file_exist1(string file_id
    	 *  [, array tracker_server, array storage_server])
		 *  return true for exist, false for not exist
		 */

	public function fileIsExist ( $remote_file_id ) {
		//$remote_file_id = 'ysctest/M00/00/00/cY4h7U-Q02P07DKdAAAABeDOzyU540.png';
		//echo FDFS::factory('group1')->fileIsExist( $remote_file_id )."<br />\n";
		$fileisexist = fastdfs_storage_file_exist1 ( $remote_file_id ,
			$this->tracker_server, $this->storage_server );
		if ( $fileisexist != false ) {
			//echo "good!! " . str_replace('/', '_', $remote_file_id) ." exists.\n";
			return $fileisexist;
		}
		else {
			echo "err!!,no remote_file_id.\n";
		}
	}
      	/**
		 * delFile
         * @param string $remote_file_id
         * @return boolean 
		 *  boolean fastdfs_storage_delete_file1(string file_id
    	 *  [, array tracker_server, array storage_server])
		 *  delete file from storage server
		 *  return true for success, false for error
		 */
	public function delFile ( $remote_file_id ) {
		//$remote_file_id = 'ysctest/M00/00/00/cY4h7U-Q02P07DKdAAAABeDOzyU540.png';
		//echo FDFS::factory('group1')->delFile( $remote_file_id )."<br />\n";
		$boolean_del = fastdfs_storage_delete_file1( $remote_file_id,
			$this->tracker_server, $this->storage_server );
		if ( $boolean_del != false ) {
			echo "Delete file " . str_replace('/', '_', $remote_file_id) ." finished.\n";
			return $boolean_del;
		}
		else {
			echo "err!!,delete file failed!\n";
		}
	}
}

?>
