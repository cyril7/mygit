DROP DATABASE IF EXISTS `phpMysqlData_LogicShowSeparated`;

CREATE DATABASE IF NOT EXISTS `phpMysqlData_LogicShowSeparated` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

USE `phpMysqlData_LogicShowSeparated`;


CREATE TABLE IF NOT EXISTS `t_student` (
  `id` int(8) NOT NULL AUTO_INCREMENT,
  `name` char(50) NOT NULL,
  `age` int(3) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

INSERT INTO `t_student` (`name`, `age` ) VALUES ('MoreWindow', '24');
INSERT INTO `t_student` (`name`, `age` ) VALUES ('MW', '19');
INSERT INTO `t_student` (`name`, `age` ) VALUES ('zcc', '21');
