-- phpMyAdmin SQL Dump
-- version 2.10.2
-- http://www.phpmyadmin.net
-- 
-- 主机: localhost
-- 生成日期: 2011 年 05 月 30 日 13:49
-- 服务器版本: 5.0.45
-- PHP 版本: 5.2.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

-- 
-- 数据库: `guestbook`
-- 
DROP DATABASE IF EXISTS `guestbook`;
CREATE DATABASE IF NOT EXISTS `guestbook`
    DEFAULT CHARACTER SET utf8
    COLLATE utf8_general_ci;
-- --------------------------------------------------------

-- 
-- 表的结构 `info`
-- 
USE `guestbook`;
CREATE TABLE IF NOT EXISTS `info` (
  `id` int(11) NOT NULL auto_increment COMMENT '留言自增id',
  `name` varchar(16) NOT NULL COMMENT '留言名称',
  `content` text NOT NULL COMMENT '发布内容',
  `content_time` varchar(14) NOT NULL COMMENT '发布时间',
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=14 ;

-- 
-- 导出表中的数据 `info`
-- 

INSERT INTO `info` VALUES (5, '张三', '祝福大家节日快乐：）', '2010-02-18 15:');
INSERT INTO `info` VALUES (6, '李四', '给大家拜年了', '2010-02-19 15:');
INSERT INTO `info` VALUES (7, '王五', '送去新年的祝福给大家', '1266571304');
INSERT INTO `info` VALUES (13, 'user', '', '1304426422');
INSERT INTO `info` VALUES (9, '发生的', '份数大幅的', '1266572080');

-- --------------------------------------------------------

-- 
-- 表的结构 `reply`
-- 

CREATE TABLE IF NOT EXISTS `reply` (
  `id` int(11) NOT NULL auto_increment COMMENT '自增id',
  `info_id` varchar(11) NOT NULL COMMENT '留言id',
  `reply` text NOT NULL COMMENT '回复内容',
  `reply_time` varchar(14) NOT NULL COMMENT '回复时间',
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=7 ;

-- 
-- 导出表中的数据 `reply`
-- 

INSERT INTO `reply` VALUES (3, '5', '谢谢热心参与', '2010-02-17 19:');
INSERT INTO `reply` VALUES (4, '6', '感谢', '2010-02-18 19:');
INSERT INTO `reply` VALUES (6, '9 ', '必须飞飞', '1266572999');
