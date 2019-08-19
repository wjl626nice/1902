/*
Navicat MySQL Data Transfer

Source Server         : data_four
Source Server Version : 50723
Source Host           : 192.168.9.233:3306
Source Database       : qyedu_four

Target Server Type    : MYSQL
Target Server Version : 50723
File Encoding         : 65001

Date: 2018-12-07 19:43:55
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `new_admin_menu_role`
-- ----------------------------
DROP TABLE IF EXISTS `new_admin_menu_role`;
CREATE TABLE `new_admin_menu_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `menu_id` int(11) NOT NULL,
  `userrole_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `new_admin_menu_role_menu_id_userrole_id_32a2613d_uniq` (`menu_id`,`userrole_id`),
  KEY `new_admin_menu_role_userrole_id_67e7af18_fk_account_userrole_id` (`userrole_id`),
  CONSTRAINT `new_admin_menu_role_menu_id_d911c734_fk_new_admin_menu_id` FOREIGN KEY (`menu_id`) REFERENCES `new_admin_menu` (`id`),
  CONSTRAINT `new_admin_menu_role_userrole_id_67e7af18_fk_account_userrole_id` FOREIGN KEY (`userrole_id`) REFERENCES `account_userrole` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of new_admin_menu_role
-- ----------------------------
INSERT INTO `new_admin_menu_role` VALUES ('1', '73', '1');
INSERT INTO `new_admin_menu_role` VALUES ('2', '74', '2');
INSERT INTO `new_admin_menu_role` VALUES ('3', '74', '3');
INSERT INTO `new_admin_menu_role` VALUES ('4', '74', '4');
INSERT INTO `new_admin_menu_role` VALUES ('5', '74', '5');
INSERT INTO `new_admin_menu_role` VALUES ('6', '74', '6');
INSERT INTO `new_admin_menu_role` VALUES ('7', '74', '7');
INSERT INTO `new_admin_menu_role` VALUES ('8', '74', '8');
