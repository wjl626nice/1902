/*
Navicat MySQL Data Transfer

Source Server         : data_four
Source Server Version : 50723
Source Host           : 192.168.9.233:3306
Source Database       : qyedu_four

Target Server Type    : MYSQL
Target Server Version : 50723
File Encoding         : 65001

Date: 2018-12-07 19:43:44
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `new_admin_menu`
-- ----------------------------
DROP TABLE IF EXISTS `new_admin_menu`;
CREATE TABLE `new_admin_menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `menu_name` varchar(20) COLLATE utf8_bin NOT NULL,
  `page_url` varchar(100) COLLATE utf8_bin NOT NULL,
  `parent_id` int(11) NOT NULL,
  `is_del` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of new_admin_menu
-- ----------------------------
INSERT INTO `new_admin_menu` VALUES ('1', '招生管理', '暂无', '0', '0');
INSERT INTO `new_admin_menu` VALUES ('2', '训练营', '暂无', '0', '0');
INSERT INTO `new_admin_menu` VALUES ('3', '入学手续', '暂无', '0', '0');
INSERT INTO `new_admin_menu` VALUES ('4', '授课管理', '暂无', '0', '0');
INSERT INTO `new_admin_menu` VALUES ('5', '学习管理', '暂无', '0', '0');
INSERT INTO `new_admin_menu` VALUES ('6', '访谈管理', '暂无', '0', '0');
INSERT INTO `new_admin_menu` VALUES ('7', '考试管理', '暂无', '0', '0');
INSERT INTO `new_admin_menu` VALUES ('8', '职业素养课', '暂无', '0', '0');
INSERT INTO `new_admin_menu` VALUES ('9', '评测管理', '暂无', '0', '0');
INSERT INTO `new_admin_menu` VALUES ('10', '结业管理', '暂无', '0', '0');
INSERT INTO `new_admin_menu` VALUES ('11', '就业管理', '暂无', '0', '0');
INSERT INTO `new_admin_menu` VALUES ('12', '人才库', '暂无', '0', '0');
INSERT INTO `new_admin_menu` VALUES ('13', '宿舍管理', 'domitory/', '0', '0');
INSERT INTO `new_admin_menu` VALUES ('14', '系统管理', '暂无', '0', '0');
INSERT INTO `new_admin_menu` VALUES ('15', '生源录入', '暂无', '1', '0');
INSERT INTO `new_admin_menu` VALUES ('16', '生源分发', '暂无', '1', '0');
INSERT INTO `new_admin_menu` VALUES ('17', '生源信息更改', '暂无', '1', '0');
INSERT INTO `new_admin_menu` VALUES ('18', '跟进状态录入', '暂无', '1', '0');
INSERT INTO `new_admin_menu` VALUES ('19', '训练营管理', '暂无', '2', '0');
INSERT INTO `new_admin_menu` VALUES ('20', '训练营学生分配', '暂无', '2', '0');
INSERT INTO `new_admin_menu` VALUES ('21', '补贴发放计划', '暂无', '3', '0');
INSERT INTO `new_admin_menu` VALUES ('22', '住宿缴费计划', '暂无', '3', '0');
INSERT INTO `new_admin_menu` VALUES ('23', '授课计划录入', '暂无', '4', '0');
INSERT INTO `new_admin_menu` VALUES ('24', '签到', '暂无', '5', '0');
INSERT INTO `new_admin_menu` VALUES ('25', '自我评价 ', '暂无', '5', '0');
INSERT INTO `new_admin_menu` VALUES ('26', '周末总结', '暂无', '5', '0');
INSERT INTO `new_admin_menu` VALUES ('27', '违纪处罚', '暂无', '6', '0');
INSERT INTO `new_admin_menu` VALUES ('28', '访谈记录', '暂无', '6', '0');
INSERT INTO `new_admin_menu` VALUES ('29', '考试成绩', '暂无', '7', '0');
INSERT INTO `new_admin_menu` VALUES ('30', '周考', '暂无', '7', '0');
INSERT INTO `new_admin_menu` VALUES ('31', '阶段考试', '暂无', '7', '0');
INSERT INTO `new_admin_menu` VALUES ('32', '课程', '暂无', '8', '0');
INSERT INTO `new_admin_menu` VALUES ('33', '考试', '暂无', '8', '0');
INSERT INTO `new_admin_menu` VALUES ('34', '题目录入', '暂无', '9', '0');
INSERT INTO `new_admin_menu` VALUES ('35', '讲师评测', '暂无', '9', '0');
INSERT INTO `new_admin_menu` VALUES ('36', '班主任评测', '暂无', '9', '0');
INSERT INTO `new_admin_menu` VALUES ('37', '后期服务评测', '暂无', '9', '0');
INSERT INTO `new_admin_menu` VALUES ('38', '违纪处罚记录', '暂无', '10', '0');
INSERT INTO `new_admin_menu` VALUES ('39', '费用补贴', '暂无', '10', '0');
INSERT INTO `new_admin_menu` VALUES ('40', '技能成绩统计', '暂无', '10', '0');
INSERT INTO `new_admin_menu` VALUES ('41', '职业素养成绩统计', '暂无', '10', '0');
INSERT INTO `new_admin_menu` VALUES ('42', '访谈记录', '暂无', '10', '0');
INSERT INTO `new_admin_menu` VALUES ('43', '能力评估报告', '暂无', '10', '0');
INSERT INTO `new_admin_menu` VALUES ('44', '推荐就业记录', '暂无', '11', '0');
INSERT INTO `new_admin_menu` VALUES ('45', '合作企业库', '暂无', '11', '0');
INSERT INTO `new_admin_menu` VALUES ('46', '回访记录', '暂无', '11', '0');
INSERT INTO `new_admin_menu` VALUES ('47', '添加人才库', '暂无', '12', '0');
INSERT INTO `new_admin_menu` VALUES ('48', '人才评级系统', '暂无', '12', '0');
INSERT INTO `new_admin_menu` VALUES ('49', '学生宿舍调整', '暂无', '13', '0');
INSERT INTO `new_admin_menu` VALUES ('50', '学生入住状态', '暂无', '13', '0');
INSERT INTO `new_admin_menu` VALUES ('51', '宿舍问题处理记录', '暂无', '13', '0');
INSERT INTO `new_admin_menu` VALUES ('52', '管理员管理', '/new_admin/admin/', '14', '0');
INSERT INTO `new_admin_menu` VALUES ('53', '宿舍管理', '/new_admin/dorm/', '14', '0');
INSERT INTO `new_admin_menu` VALUES ('54', '班级管理', '/new_admin/classgrade/', '14', '0');
INSERT INTO `new_admin_menu` VALUES ('55', '学员管理', '/new_admin/student_list/', '14', '0');
INSERT INTO `new_admin_menu` VALUES ('56', '学生违纪查询', '暂无', '14', '0');
INSERT INTO `new_admin_menu` VALUES ('57', '评测管理', '暂无', '14', '0');
INSERT INTO `new_admin_menu` VALUES ('58', '访谈记录', '暂无', '14', '0');
INSERT INTO `new_admin_menu` VALUES ('59', '回访记录', '暂无', '14', '0');
INSERT INTO `new_admin_menu` VALUES ('60', '人才库', '暂无', '14', '0');
INSERT INTO `new_admin_menu` VALUES ('61', '签到记录', '暂无', '14', '0');
INSERT INTO `new_admin_menu` VALUES ('62', '宿舍问题处理记录', '暂无', '14', '0');
INSERT INTO `new_admin_menu` VALUES ('63', '考试管理', '暂无', '14', '0');
INSERT INTO `new_admin_menu` VALUES ('64', '授课计划管理', '暂无', '14', '0');
INSERT INTO `new_admin_menu` VALUES ('65', '菜单管理', '/new_admin/category/', '14', '0');
INSERT INTO `new_admin_menu` VALUES ('66', '修改密码', '暂无', '14', '0');
INSERT INTO `new_admin_menu` VALUES ('67', '操作学生', '暂无', '2', '1');
INSERT INTO `new_admin_menu` VALUES ('73', '哈哈', '暂无', '0', '1');
INSERT INTO `new_admin_menu` VALUES ('74', 'haha', 'http://www.baidu.com', '2', '1');
