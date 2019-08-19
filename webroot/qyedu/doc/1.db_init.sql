/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50723
Source Host           : localhost:3306
Source Database       : qyedu_dev

Target Server Type    : MYSQL
Target Server Version : 50723
File Encoding         : 65001

Date: 2018-12-08 10:38:32
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `account_userrole`
-- ----------------------------
DROP TABLE IF EXISTS `account_userrole`;
CREATE TABLE `account_userrole` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_name` varchar(20) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Records of account_userrole
-- ----------------------------
INSERT INTO `account_userrole` VALUES ('1', '超级管理员');
INSERT INTO `account_userrole` VALUES ('2', '学员');
INSERT INTO `account_userrole` VALUES ('3', '院校经理');
INSERT INTO `account_userrole` VALUES ('4', '咨询顾问');
INSERT INTO `account_userrole` VALUES ('5', '班主任');
INSERT INTO `account_userrole` VALUES ('6', '带课讲师');
INSERT INTO `account_userrole` VALUES ('7', '财务专员');
INSERT INTO `account_userrole` VALUES ('8', '就业专员');
