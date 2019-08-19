/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50723
Source Host           : localhost:3306
Source Database       : qyedu_dev

Target Server Type    : MYSQL
Target Server Version : 50723
File Encoding         : 65001

Date: 2018-12-08 09:31:37
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `account_newuser`
-- ----------------------------
DROP TABLE IF EXISTS `account_newuser`;
CREATE TABLE `account_newuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `realname` varchar(15) COLLATE utf8mb4_bin NOT NULL,
  `mobile_number` varchar(15) COLLATE utf8mb4_bin NOT NULL,
  `id_card` varchar(25) COLLATE utf8mb4_bin NOT NULL,
  `birthday` date DEFAULT NULL,
  `info` longtext COLLATE utf8mb4_bin NOT NULL,
  `gender` smallint(5) unsigned NOT NULL,
  `edu_level` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `home_address` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `state` smallint(5) unsigned NOT NULL,
  `is_goodman` smallint(5) unsigned NOT NULL,
  `is_del` smallint(5) unsigned NOT NULL,
  `role_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `account_newuser_role_id_97207b20_fk_account_userrole_id` (`role_id`),
  CONSTRAINT `account_newuser_role_id_97207b20_fk_account_userrole_id` FOREIGN KEY (`role_id`) REFERENCES `account_userrole` (`id`),
  CONSTRAINT `account_newuser_user_id_0b539851_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Records of account_newuser
-- 执行这条语句之前需要先创建管理员账户。
-- python manage.py createsuperuser
-- ----------------------------
INSERT INTO `account_newuser` VALUES ('1', '超管', '13849111111', '410183191108010099', '2018-12-08', '没什么好介绍的', '1', '本科', '郑州', 1, '1', '0', '0', '1', '1')
