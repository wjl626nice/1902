# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 47.93.254.45 (MySQL 5.5.5-10.1.19-MariaDB)
# Database: dqb
# Generation Time: 2019-08-13 06:26:27 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table auth_group
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table auth_group_permissions
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table auth_permission
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
	(1,'Can add log entry',1,'add_logentry'),
	(2,'Can change log entry',1,'change_logentry'),
	(3,'Can delete log entry',1,'delete_logentry'),
	(4,'Can add permission',2,'add_permission'),
	(5,'Can change permission',2,'change_permission'),
	(6,'Can delete permission',2,'delete_permission'),
	(7,'Can add group',3,'add_group'),
	(8,'Can change group',3,'change_group'),
	(9,'Can delete group',3,'delete_group'),
	(10,'Can add user',4,'add_user'),
	(11,'Can change user',4,'change_user'),
	(12,'Can delete user',4,'delete_user'),
	(13,'Can add content type',5,'add_contenttype'),
	(14,'Can change content type',5,'change_contenttype'),
	(15,'Can delete content type',5,'delete_contenttype'),
	(16,'Can add session',6,'add_session'),
	(17,'Can change session',6,'change_session'),
	(18,'Can delete session',6,'delete_session'),
	(19,'Can add 活动',7,'add_activity'),
	(20,'Can change 活动',7,'change_activity'),
	(21,'Can delete 活动',7,'delete_activity'),
	(22,'Can add 用户-活动中间表',8,'add_actor_activities'),
	(23,'Can change 用户-活动中间表',8,'change_actor_activities'),
	(24,'Can delete 用户-活动中间表',8,'delete_actor_activities'),
	(25,'Can add 球友列表',9,'add_ball_friends'),
	(26,'Can change 球友列表',9,'change_ball_friends'),
	(27,'Can delete 球友列表',9,'delete_ball_friends'),
	(28,'Can add group',10,'add_group'),
	(29,'Can change group',10,'change_group'),
	(30,'Can delete group',10,'delete_group'),
	(31,'Can add 用户',11,'add_member'),
	(32,'Can change 用户',11,'change_member'),
	(33,'Can delete 用户',11,'delete_member'),
	(34,'Can add 留言',12,'add_message'),
	(35,'Can change 留言',12,'change_message'),
	(36,'Can delete 留言',12,'delete_message'),
	(37,'Can add 消息',13,'add_news'),
	(38,'Can change 消息',13,'change_news'),
	(39,'Can delete 消息',13,'delete_news'),
	(40,'Can add 回复',14,'add_reply'),
	(41,'Can change 回复',14,'change_reply'),
	(42,'Can delete 回复',14,'delete_reply'),
	(43,'Can view log entry',1,'view_logentry'),
	(44,'Can view permission',2,'view_permission'),
	(45,'Can view group',3,'view_group'),
	(46,'Can view user',4,'view_user'),
	(47,'Can view content type',5,'view_contenttype'),
	(48,'Can view session',6,'view_session');

/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table auth_user
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`)
VALUES
	(1,'pbkdf2_sha256$120000$g3NzQExBAbtB$aiOs2+K7YmtHMEmBrI1tjaYwxujm4ma8AVoIXTA4VhA=','2019-04-28 07:01:52.402773',0,'qingyun','','','123@163.com',0,1,'2018-11-20 02:15:03.289213'),
	(4,'pbkdf2_sha256$120000$AfnUh38bvu0A$9GZxyUjiBvoEVIXpH+kC3gLxpURxsmB1+YNcsLNxej4=','2018-12-08 06:51:59.068501',0,'yhs','','','123456@qq.com',0,1,'2018-11-20 09:04:49.717349'),
	(9,'pbkdf2_sha256$120000$Ju88wXlgnOaP$lbGRFYhqE4h3lvfjZKk74mHxAPcrXq670eNknWzA4Lw=',NULL,0,'hhjvh','','','1234567@qq.com',0,1,'2018-11-22 02:43:00.890086'),
	(11,'pbkdf2_sha256$120000$UmYx6FYIaIEa$7v2JCp3+Jcn6sqjMAGM2371FfNTvXH73Tcmq54s0lU4=','2019-02-12 09:27:48.712856',0,'zwj','','','zwj@qq.com',0,1,'2018-11-27 02:35:59.040183'),
	(13,'pbkdf2_sha256$120000$B6WW5Ra8MawE$GGoRthtokGeQqDLhId/n2g0QxuNFpzOapkLqz71ZFOk=','2018-12-07 03:20:32.177872',0,'ming','','','123@163.com',0,1,'2018-12-06 03:30:26.958412');

/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table auth_user_groups
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table auth_user_user_permissions
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table django_admin_log
# ------------------------------------------------------------

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table django_content_type
# ------------------------------------------------------------

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;

INSERT INTO `django_content_type` (`id`, `app_label`, `model`)
VALUES
	(1,'admin','logentry'),
	(3,'auth','group'),
	(2,'auth','permission'),
	(4,'auth','user'),
	(5,'contenttypes','contenttype'),
	(7,'dianqiuba','activity'),
	(8,'dianqiuba','actor_activities'),
	(9,'dianqiuba','ball_friends'),
	(10,'dianqiuba','group'),
	(11,'dianqiuba','member'),
	(12,'dianqiuba','message'),
	(13,'dianqiuba','news'),
	(14,'dianqiuba','reply'),
	(6,'sessions','session');

/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table django_migrations
# ------------------------------------------------------------

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
	(1,'contenttypes','0001_initial','2018-10-18 08:22:35.861580'),
	(2,'auth','0001_initial','2018-10-18 08:22:38.298971'),
	(3,'admin','0001_initial','2018-10-18 08:22:38.740906'),
	(4,'admin','0002_logentry_remove_auto_add','2018-10-18 08:22:38.751350'),
	(5,'contenttypes','0002_remove_content_type_name','2018-10-18 08:22:39.030183'),
	(6,'auth','0002_alter_permission_name_max_length','2018-10-18 08:22:39.167189'),
	(7,'auth','0003_alter_user_email_max_length','2018-10-18 08:22:39.295874'),
	(8,'auth','0004_alter_user_username_opts','2018-10-18 08:22:39.305212'),
	(9,'auth','0005_alter_user_last_login_null','2018-10-18 08:22:39.435987'),
	(10,'auth','0006_require_contenttypes_0002','2018-10-18 08:22:39.438131'),
	(11,'auth','0007_alter_validators_add_error_messages','2018-10-18 08:22:39.446978'),
	(12,'auth','0008_alter_user_username_max_length','2018-10-18 08:22:39.561604'),
	(13,'auth','0009_alter_user_last_name_max_length','2018-10-18 08:22:39.695782'),
	(14,'dianqiuba','0001_initial','2018-10-18 08:22:41.312605'),
	(15,'sessions','0001_initial','2018-10-18 08:22:41.610063'),
	(16,'admin','0003_logentry_add_action_flag_choices','2018-10-26 03:22:44.736319'),
	(17,'app','0001_initial','2018-12-08 14:09:14.704295'),
	(18,'app','0002_qygroup_qymessage_qynews_qyput_forward_qyrecharge_qyreply','2018-12-08 14:09:14.831255'),
	(19,'app','0003_qyfeedback','2018-12-08 14:09:14.947083'),
	(20,'app','0004_auto_20181203_1503','2018-12-08 14:09:15.061894'),
	(21,'app','0005_auto_20181207_1054','2018-12-08 14:09:15.178272'),
	(22,'app','0006_qyauditing','2018-12-08 14:09:15.322784'),
	(23,'app','0007_auto_20181208_1453','2018-12-08 14:54:14.435791');

/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table django_session
# ------------------------------------------------------------

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`)
VALUES
	('02knyg1yl5fycfnzjybxyhz8bdsn80pm','MjljNGNhZjA2MDdiOGI2YzIwMDMwMDY2MGNkNjM0MmYzNzllNmI3Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YWIzMTQyMjU0MjYyZjUxNjcxMjE1OWYyZjYwNjYwYTUwZGZiMWJiIn0=','2018-12-11 09:29:04.757738'),
	('0b9r1de0vlqtysyj4l3hw3ybo9plpvln','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-20 01:13:35.565582'),
	('0kk4m0w6o1duwtp03xn3yhye0uylnvrm','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-07 05:58:08.500707'),
	('0pa5hkp7yomo80ge92aqimi8q21zu0ia','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-07 07:11:34.409453'),
	('0xmtm0k23szsz7md56oiu02l4s8hsj8d','NTQ4OTc4NGFiYjVkZDc1MjA2NzU0ZWVkNmYzN2NhMzNlOGEyMWY3YTp7Il9hdXRoX3VzZXJfaWQiOiIxMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZmJjYTViOTJkYmFiMjYwZTUwYjIwN2Y2NTZjM2M1MWU3ZTNiYzI5NiJ9','2019-02-26 09:24:09.565970'),
	('10rdlput5e13nb2y85dbkdvmkn1lulhd','YjZiMDA1MzAxZTljYTI3MGE3ZWVhYWQ2YzY2YWI5OTNkYTI3MTFmZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YjA4NjAwYTJiYzU1NDE4ZTg2NGNhYmM5MTU0ZDM3NDBmZTI2ZjM1In0=','2018-12-04 07:51:58.388372'),
	('13b9js5nrb9cvcsz5czj5kmxa7rqdsma','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-20 01:35:22.495278'),
	('14xryd211hesjmw8fkq02gmmhcswh4me','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 02:18:19.609626'),
	('15gnmmztz6iqod0gj5iy6jr5cxjbesu4','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-10 06:57:06.763463'),
	('1a39dgbwyh3fvrfcv2x8pi3jubzss7rx','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 05:41:45.234005'),
	('1kq2vv35gmrjn8tw1co4nows5jykr74o','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-07 01:45:48.822295'),
	('1pdgg6ece6311xjovrke811lby19wjoz','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 01:21:43.578906'),
	('1x697xf25vibz8bgik2894jloxgomy0j','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-07 01:44:12.359979'),
	('1y6e4ywj0z29vffkhbblc68ve3vhum9q','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 03:38:55.303983'),
	('29c2wngdo2hux6b454f6p8o2he6vzhqy','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 03:03:51.215733'),
	('2a3h6rnf4x5rwhlvy14kiz1vp2bqpc1l','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-19 08:47:08.941562'),
	('2euam62l5aiw504k2lfbz86s422w7v16','OTBjNWYzM2M0NzMwYzkzY2QxZjZjZTM5MjZjNDcwYjNjNDU3ODA3MTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjkzYTc5MGFmY2YyZjlhYzBjMzA0YzI0MWE2NzRhOGZmNTU5YWE3In0=','2018-12-19 09:43:51.800333'),
	('2fij4davueh2nqy1v02w9h1s6occngsn','OTBjNWYzM2M0NzMwYzkzY2QxZjZjZTM5MjZjNDcwYjNjNDU3ODA3MTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjkzYTc5MGFmY2YyZjlhYzBjMzA0YzI0MWE2NzRhOGZmNTU5YWE3In0=','2018-12-22 05:42:22.827409'),
	('2fyz4fjfq5nmvd23zvzx6gqolznq8gu3','ZTA5ZDAyMTg4OWVjYTQ4ZmZhNjI3YjhkYTQxYzgyNjMzYTQ4YWY0ZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YWVhZjY2NGMxYmY4ZGY1OGRjYzZmNThhYWNiOTFlNDIzMzM4M2RjIn0=','2018-12-05 00:47:41.197190'),
	('2ijyo0wsn2t3z6ihlgdsoq548wswltva','ZTA5ZDAyMTg4OWVjYTQ4ZmZhNjI3YjhkYTQxYzgyNjMzYTQ4YWY0ZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YWVhZjY2NGMxYmY4ZGY1OGRjYzZmNThhYWNiOTFlNDIzMzM4M2RjIn0=','2018-12-04 09:06:43.090168'),
	('2pokn9w4kr7naco2wyhf1kku805rvz17','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-19 09:09:34.513283'),
	('2qm1re90mivvb01kvb1r84rd4wxamxhy','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 02:35:20.293695'),
	('2zwjkaho2hixux61tn3kmylm5v4ajk9g','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 01:24:14.727982'),
	('336eadxz74cs0nd9nffd5j9o3r6vb4sg','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-07 01:45:48.537909'),
	('396ddwxu88s09hyxmiojiag5em8dfwec','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 03:38:04.932720'),
	('3oix93ivevfz0qy8p53ytcg2kggsn7r1','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-19 12:16:54.748664'),
	('3y0wb513dkj6bxoci2itko0hqtfojd9v','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-19 08:19:16.405227'),
	('466zsx90emk121bxg31mpezuncw24zl7','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-20 02:00:50.813611'),
	('49pur90kr8onuq5ephbnd1y7wot4ljgt','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-20 03:53:58.991363'),
	('4dngr9uu1aume1pld3arfmccg8tr4vid','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-07 05:51:48.209999'),
	('4j9w7zzkglrlk9775rj6dcby3ogz6xjd','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-19 06:08:26.689264'),
	('4xbyx92572y2dsfx4gydrqa8l2cveypb','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-19 09:26:19.051308'),
	('522zklah7onm6u1h0i154hpp55u1156q','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 08:51:00.386639'),
	('544d99oez5qu95nlf6fji2mdeigtsb88','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 05:27:41.431383'),
	('54hjrqykxzz0phbh83sdvbp0wn6wuq24','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 03:42:22.534620'),
	('55dkrj2w6apyhmz0ggso1iwt9w2380yp','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-20 03:54:12.483247'),
	('5b1y4hbya848mqqdma1zotj23a2xu5yx','MjQyN2E3N2JmZjViNDQ0NzdjMWEwODcyODk3MWQ5NTQxMTE4OGY0NDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjMzODFkOTcwNTM0M2E4NTJkODlhMTU1NTU0MDdmN2QyMGI5NmVhIn0=','2018-12-06 00:30:19.291476'),
	('5bpdmjvro6ikwigh5j8clau95j24yq9k','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-19 09:18:51.586100'),
	('5i9wctairxpb4x1myppem9rv8m7q1hvh','ZTA5ZDAyMTg4OWVjYTQ4ZmZhNjI3YjhkYTQxYzgyNjMzYTQ4YWY0ZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YWVhZjY2NGMxYmY4ZGY1OGRjYzZmNThhYWNiOTFlNDIzMzM4M2RjIn0=','2018-12-04 09:06:39.738658'),
	('5nqt2fmppttzyrjxahheczkqpatoqh62','MjQyN2E3N2JmZjViNDQ0NzdjMWEwODcyODk3MWQ5NTQxMTE4OGY0NDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjMzODFkOTcwNTM0M2E4NTJkODlhMTU1NTU0MDdmN2QyMGI5NmVhIn0=','2018-12-05 10:51:53.330400'),
	('5nszfw6hyqpwxwym6ite8lstat8ntfpd','OTljODFlNTg2ZjIzYWIyMTJmOWIwMjcyMTNiNzBiYmIwNThlM2VmNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxYzc5NTRkYjczMWU2ODMyYzU3MzUyZjNkODM4NjY0MDFkNzAzZjA0In0=','2018-12-11 01:51:48.701931'),
	('5qv59ki7tu6kmhktin2zhsishowndvcm','ZTA5ZDAyMTg4OWVjYTQ4ZmZhNjI3YjhkYTQxYzgyNjMzYTQ4YWY0ZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YWVhZjY2NGMxYmY4ZGY1OGRjYzZmNThhYWNiOTFlNDIzMzM4M2RjIn0=','2018-12-04 09:05:07.185679'),
	('65tgq5ftgvqosaspdeljg03kp9boezve','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 08:57:15.084453'),
	('68bvzwqo6k7o0yu7ve14v6gl68a84e0o','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 03:49:56.903234'),
	('6co5eckhlj9wac88zpvqeonakcwb3ry4','ZTA5ZDAyMTg4OWVjYTQ4ZmZhNjI3YjhkYTQxYzgyNjMzYTQ4YWY0ZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YWVhZjY2NGMxYmY4ZGY1OGRjYzZmNThhYWNiOTFlNDIzMzM4M2RjIn0=','2018-12-04 09:41:27.263593'),
	('6dnyneylwzkhxsq4p0pqi5s9ehi15532','MjQyN2E3N2JmZjViNDQ0NzdjMWEwODcyODk3MWQ5NTQxMTE4OGY0NDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjMzODFkOTcwNTM0M2E4NTJkODlhMTU1NTU0MDdmN2QyMGI5NmVhIn0=','2018-12-05 10:35:44.919693'),
	('6gkvxigjuitk0wvpz6g8s46b9ln3a192','ODc4Y2FiNzgyMzRmYTQ1Y2E0YWNjMzkyY2FmMDI1ZTFlNTVkMTBmMjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYmY2MWQ3NTMzOGRhZmVkZDhmNjJhMWEzNzg4YzNhZThjMzUzMThmIn0=','2019-05-12 06:56:07.079136'),
	('6o0lwscab9dxasyz5y56xxor5aiza1vu','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-20 02:15:16.281588'),
	('6quaelwxe9ho5qzvhju16xbdgm17go5h','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-19 08:57:32.151806'),
	('75z81htemsrsf2vq11rx6lfi4fqx5xmn','OTljODFlNTg2ZjIzYWIyMTJmOWIwMjcyMTNiNzBiYmIwNThlM2VmNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxYzc5NTRkYjczMWU2ODMyYzU3MzUyZjNkODM4NjY0MDFkNzAzZjA0In0=','2018-12-11 02:31:33.091769'),
	('770t0oi0k7it78ysnaehn2bvjp8ztezs','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-19 09:17:25.365357'),
	('7e4ge2fc8qjne7b682hplkztemzspzgz','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 05:27:39.668837'),
	('7i8dajatjth6oau6cuxyn2k1rf8shvf0','MDJmNDAyOTU3ZjI0ZDY0OGRhOTY1Y2EwZDQxOWViNDYwNDQ5OGE2NTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YWQxZjljOWIwZTk5ZDRlZjJkZWQ5MDFmNGJlYTBmNGU1OWM1MjNlIn0=','2018-12-05 02:08:45.986496'),
	('7kwtxb4bcxfr9vuc0yqu2v0hkchdbj26','OTBjNWYzM2M0NzMwYzkzY2QxZjZjZTM5MjZjNDcwYjNjNDU3ODA3MTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjkzYTc5MGFmY2YyZjlhYzBjMzA0YzI0MWE2NzRhOGZmNTU5YWE3In0=','2018-12-19 09:32:32.000938'),
	('7n5a0iksud9h5gkhtna88whxp9895jgp','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-19 12:18:27.102668'),
	('7nubownvqa5yk3qxaryvf0o5vbp8krq7','MDJmNDAyOTU3ZjI0ZDY0OGRhOTY1Y2EwZDQxOWViNDYwNDQ5OGE2NTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YWQxZjljOWIwZTk5ZDRlZjJkZWQ5MDFmNGJlYTBmNGU1OWM1MjNlIn0=','2018-12-05 02:05:27.574730'),
	('7q6rw54zlotb692byh7bl6tgfv86y8xd','ZTA5ZDAyMTg4OWVjYTQ4ZmZhNjI3YjhkYTQxYzgyNjMzYTQ4YWY0ZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YWVhZjY2NGMxYmY4ZGY1OGRjYzZmNThhYWNiOTFlNDIzMzM4M2RjIn0=','2018-12-05 03:00:34.182390'),
	('7s2eoscakcv3n42wrzamve31kqg0et8j','ZmU1MjY5ZTkyODhhYjQzYjI2NDI2NTUzNWZhNGNhZTMxZjFlYTg1YTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YjVlMmZkZWRjMDE3MDNjODQzMjk3YWZiOTI5ZWZiNDc2MjMwOGMwIn0=','2018-12-05 10:28:40.277055'),
	('80gn5aqbs9192i3i4ye6a59fe9g7h55e','OTljODFlNTg2ZjIzYWIyMTJmOWIwMjcyMTNiNzBiYmIwNThlM2VmNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxYzc5NTRkYjczMWU2ODMyYzU3MzUyZjNkODM4NjY0MDFkNzAzZjA0In0=','2018-12-11 02:31:33.487010'),
	('8iolpx3bfki6jcol2ryai78dhit6v58m','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 03:55:15.400252'),
	('8okjyj3hpd9iu46nqoxr4xcaolvnrvgp','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 01:03:43.355789'),
	('8x4f2mqds79ph1t69k3l9xf5zi34u4c6','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-19 09:24:13.629606'),
	('9b9w43mszbdtarwou4usp84jul5fr1kp','OTBjNWYzM2M0NzMwYzkzY2QxZjZjZTM5MjZjNDcwYjNjNDU3ODA3MTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjkzYTc5MGFmY2YyZjlhYzBjMzA0YzI0MWE2NzRhOGZmNTU5YWE3In0=','2018-12-21 00:27:39.506470'),
	('9eufzuk8sw9bnsg56fmubgit7u7jhlod','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 05:30:58.673285'),
	('9h7tqh3trzt5nlwhqffg76tx69yz34v5','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 01:12:25.382154'),
	('9y82w50e9f1lnya9gwxb2bwqoaur44nm','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 01:10:59.117702'),
	('aing1dgpm9ktfbm8i1uligdj8te5v0rf','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-19 09:00:57.242922'),
	('arpzbb8g6kww09z7pl5bvyq3q9xxdwrq','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-19 09:13:27.385875'),
	('aw0lrbzukm8ikz10luirj77m1yt839k7','ZmU1MjY5ZTkyODhhYjQzYjI2NDI2NTUzNWZhNGNhZTMxZjFlYTg1YTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YjVlMmZkZWRjMDE3MDNjODQzMjk3YWZiOTI5ZWZiNDc2MjMwOGMwIn0=','2018-12-05 10:27:08.221062'),
	('b07bn1jt48glytzit4rulhdbwpbhpqp8','ZmU1MjY5ZTkyODhhYjQzYjI2NDI2NTUzNWZhNGNhZTMxZjFlYTg1YTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YjVlMmZkZWRjMDE3MDNjODQzMjk3YWZiOTI5ZWZiNDc2MjMwOGMwIn0=','2018-12-05 10:29:34.970148'),
	('b33bkeqdr32ut8xy4qnxhlht40hgu3er','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 07:45:23.514331'),
	('b4k3xy94o8tgjjbrh4d439x92omzljvp','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-21 03:20:32.218113'),
	('b9uioqxniqrybsosq0iisok8unzceiv5','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 01:08:54.031877'),
	('beewsnq4m7qk1a0vdqf9vnuwu7ahm5ey','OTBjNWYzM2M0NzMwYzkzY2QxZjZjZTM5MjZjNDcwYjNjNDU3ODA3MTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjkzYTc5MGFmY2YyZjlhYzBjMzA0YzI0MWE2NzRhOGZmNTU5YWE3In0=','2018-12-19 09:27:12.645445'),
	('bkqg510mfzk9wnbxe317uwvd542owfgv','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 02:58:06.967081'),
	('boh5944tebz8tbkum6wr2pba2lu4votz','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-07 05:58:47.634193'),
	('bozidhwjuuu38a54d6f5pd5eoitne9l6','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-19 08:50:53.253220'),
	('brs28k10xc9ndpv2clekvf9m3j5l0z9m','MjljNGNhZjA2MDdiOGI2YzIwMDMwMDY2MGNkNjM0MmYzNzllNmI3Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YWIzMTQyMjU0MjYyZjUxNjcxMjE1OWYyZjYwNjYwYTUwZGZiMWJiIn0=','2018-12-19 02:16:04.798907'),
	('bz8odwd3btq9jfgumb3h7ea2dobbcdlj','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-20 01:59:42.060028'),
	('cfo031pt5yn6s2q793fjhiadd2eb10ey','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 01:07:57.535264'),
	('chlz59u4xnxzp7htef8n27rj5cikqww6','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 05:27:41.252627'),
	('ciiu50oce7b4ntqkjlvwlbasqo2sbnpq','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 08:53:38.289890'),
	('cnk2qjsr6g30sr9y457868q9x7cbilth','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 03:58:07.193040'),
	('cpiyv130dbpq84555svogk84dr3vnu5p','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-11 09:33:40.324321'),
	('ctx5k4c9llen8i3kkcqsxuxfzsy408i6','ZTA5ZDAyMTg4OWVjYTQ4ZmZhNjI3YjhkYTQxYzgyNjMzYTQ4YWY0ZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YWVhZjY2NGMxYmY4ZGY1OGRjYzZmNThhYWNiOTFlNDIzMzM4M2RjIn0=','2018-12-05 03:58:09.287454'),
	('cuxdxql2tajz7hyyydlry4ewan2y2t0o','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 05:29:00.525186'),
	('cvqam2nmxuhlmzuo49082ktntti153fq','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 01:06:31.567155'),
	('dk2gnrdeyalo6yk5nrj9hv1p04i78ppi','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 11:39:14.952637'),
	('dmfpq3l74u6o6igsqozt7q298rrdkh2t','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-11 01:34:07.500915'),
	('dsbqdocc6yd1cbh2y0gj0cbdl7byiqlm','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-25 07:55:20.848185'),
	('dxjm85a2p15lv501une6mp23m2czcxx0','MjQyN2E3N2JmZjViNDQ0NzdjMWEwODcyODk3MWQ5NTQxMTE4OGY0NDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjMzODFkOTcwNTM0M2E4NTJkODlhMTU1NTU0MDdmN2QyMGI5NmVhIn0=','2018-12-06 00:31:55.937174'),
	('dxpmjkccelwpeo70yibdwybouqui34uc','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 05:27:40.808973'),
	('e3ohycoc2va1mjyqt2rbv40fo4n6glbv','ZTA5ZDAyMTg4OWVjYTQ4ZmZhNjI3YjhkYTQxYzgyNjMzYTQ4YWY0ZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YWVhZjY2NGMxYmY4ZGY1OGRjYzZmNThhYWNiOTFlNDIzMzM4M2RjIn0=','2018-12-05 02:53:43.507652'),
	('e7iax27v2h99qc4ehssnbfqmo3bivhdr','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-07 05:59:20.420897'),
	('ea5m4f37m0hwftef3hze74172scmptot','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 02:27:36.852291'),
	('ed0c3fqwg934kbroi6somc0erx6u1ncc','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 07:19:16.010230'),
	('efzbgysoeaht2k8sjbke2jvcyo0jmvnn','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 01:28:13.236014'),
	('egcdmy11lxq5umihyxqp3t74wjcki8se','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-11 01:36:29.282384'),
	('ehcf7gvpvk00jm1v81b0ga5czpl8nv1x','ZTA5ZDAyMTg4OWVjYTQ4ZmZhNjI3YjhkYTQxYzgyNjMzYTQ4YWY0ZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YWVhZjY2NGMxYmY4ZGY1OGRjYzZmNThhYWNiOTFlNDIzMzM4M2RjIn0=','2018-12-05 02:02:37.019197'),
	('eijg82nczrrqmj8h7ffbpfob8ztrmjnh','OTBjNWYzM2M0NzMwYzkzY2QxZjZjZTM5MjZjNDcwYjNjNDU3ODA3MTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjkzYTc5MGFmY2YyZjlhYzBjMzA0YzI0MWE2NzRhOGZmNTU5YWE3In0=','2018-12-21 03:46:49.898079'),
	('ewildkuf9p76wta49wg4okmyceotxsgb','NjY5OTAxMzhjODc5YWRlYTEwMTYzZmNkYTQzN2Q3NmQ2ZTQ1NWVmYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkMzdkYTUxZjcwMzRkZjZiN2UzNWI1YTk3Y2Q0M2RiYzMyYzMxNWJiIn0=','2018-12-19 05:47:48.946618'),
	('fcq5fsszq8doixw0v8o301yule96b11c','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-20 01:17:15.136395'),
	('fhr7ph0llab2e7jorgbxj8qifqhjlhmk','ZmU1MjY5ZTkyODhhYjQzYjI2NDI2NTUzNWZhNGNhZTMxZjFlYTg1YTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YjVlMmZkZWRjMDE3MDNjODQzMjk3YWZiOTI5ZWZiNDc2MjMwOGMwIn0=','2018-12-05 10:33:11.695466'),
	('fwzwi9kfo0ftoekn82lbwhq5z5wfrktw','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-20 03:06:51.211741'),
	('fz45aaxnm6cd4lorc88t6atleqotfzai','OTBjNWYzM2M0NzMwYzkzY2QxZjZjZTM5MjZjNDcwYjNjNDU3ODA3MTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjkzYTc5MGFmY2YyZjlhYzBjMzA0YzI0MWE2NzRhOGZmNTU5YWE3In0=','2018-12-22 06:51:59.108347'),
	('g0fan07l8lrz0qd3kfjjwbkome0cccoa','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-07 05:50:26.084113'),
	('g2qkvz4es3rtjyv3pkrrw1wyk66pqks6','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-07 05:55:45.338228'),
	('g7y3hfuw8zta6tl1f13c2axkebpwsd1k','ZTA5ZDAyMTg4OWVjYTQ4ZmZhNjI3YjhkYTQxYzgyNjMzYTQ4YWY0ZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YWVhZjY2NGMxYmY4ZGY1OGRjYzZmNThhYWNiOTFlNDIzMzM4M2RjIn0=','2018-12-05 02:02:02.064906'),
	('gi7rsajrukybzhwefxu5guocw13fphk4','ZTA5ZDAyMTg4OWVjYTQ4ZmZhNjI3YjhkYTQxYzgyNjMzYTQ4YWY0ZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YWVhZjY2NGMxYmY4ZGY1OGRjYzZmNThhYWNiOTFlNDIzMzM4M2RjIn0=','2018-12-05 03:57:59.912229'),
	('gk26t2x45sqndw9xq7orw2l6ytacsflc','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-20 01:16:26.856562'),
	('gs7zzxxe2zhplzsseea14o62hluz3fpt','OTBjNWYzM2M0NzMwYzkzY2QxZjZjZTM5MjZjNDcwYjNjNDU3ODA3MTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjkzYTc5MGFmY2YyZjlhYzBjMzA0YzI0MWE2NzRhOGZmNTU5YWE3In0=','2018-12-19 10:11:54.178588'),
	('gzbvsargasjnvbt020vzoezfkn5xh28p','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-07 07:18:34.942613'),
	('hct5x1divc617mi2pbi40qazdluwxh95','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-11 01:37:31.464031'),
	('hmtqvrw0p9w26o3d32yxvqaogttrsokt','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 07:06:38.999287'),
	('hq4c4c9exhky5dbtaawe53bdozb3mute','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-19 12:19:25.662857'),
	('hsct8xzte8o4ub38fr2fqivn0z6gxg7v','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-07 06:35:24.331560'),
	('huhyy28idf9mh5cg3m3j343vgvhzhqft','MjljNGNhZjA2MDdiOGI2YzIwMDMwMDY2MGNkNjM0MmYzNzllNmI3Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YWIzMTQyMjU0MjYyZjUxNjcxMjE1OWYyZjYwNjYwYTUwZGZiMWJiIn0=','2018-12-11 02:45:12.259767'),
	('hvnl03epzvgusj88psbnflcq0ik2vchp','MjljNGNhZjA2MDdiOGI2YzIwMDMwMDY2MGNkNjM0MmYzNzllNmI3Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YWIzMTQyMjU0MjYyZjUxNjcxMjE1OWYyZjYwNjYwYTUwZGZiMWJiIn0=','2018-12-19 02:12:03.006605'),
	('hzumaq4o8vygj408tkq4ywczsl29qxk1','MjljNGNhZjA2MDdiOGI2YzIwMDMwMDY2MGNkNjM0MmYzNzllNmI3Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YWIzMTQyMjU0MjYyZjUxNjcxMjE1OWYyZjYwNjYwYTUwZGZiMWJiIn0=','2018-12-19 02:20:28.158065'),
	('i55a27stabfjlxi75mu20nnx0fjoex1o','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 03:40:31.461444'),
	('i5o8nizfmshco19h585sk5rjmkyokh5z','MjQyN2E3N2JmZjViNDQ0NzdjMWEwODcyODk3MWQ5NTQxMTE4OGY0NDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjMzODFkOTcwNTM0M2E4NTJkODlhMTU1NTU0MDdmN2QyMGI5NmVhIn0=','2018-12-05 10:38:21.712192'),
	('i6j3590rrrpt6dwmwssi6fnwlaoctsul','ZTA5ZDAyMTg4OWVjYTQ4ZmZhNjI3YjhkYTQxYzgyNjMzYTQ4YWY0ZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YWVhZjY2NGMxYmY4ZGY1OGRjYzZmNThhYWNiOTFlNDIzMzM4M2RjIn0=','2018-12-05 09:33:24.233212'),
	('ig0ewospq6dg0t81698vj9c6bgn3r4jt','MjljNGNhZjA2MDdiOGI2YzIwMDMwMDY2MGNkNjM0MmYzNzllNmI3Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YWIzMTQyMjU0MjYyZjUxNjcxMjE1OWYyZjYwNjYwYTUwZGZiMWJiIn0=','2018-12-19 05:37:51.190889'),
	('igvxe6w23fq4o0d2w8gn8954o1w8iqn8','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 03:53:33.639852'),
	('imo75l3j8mx091equs3a2uzj7s90khew','OTljODFlNTg2ZjIzYWIyMTJmOWIwMjcyMTNiNzBiYmIwNThlM2VmNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxYzc5NTRkYjczMWU2ODMyYzU3MzUyZjNkODM4NjY0MDFkNzAzZjA0In0=','2018-12-10 10:55:00.269603'),
	('io53ifxrzclyss91uhnacolf6jj8cwm8','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-11 02:34:17.199463'),
	('itvgq14qbo0yln4t5ppqwf6d5kj2sv61','NTQ4OTc4NGFiYjVkZDc1MjA2NzU0ZWVkNmYzN2NhMzNlOGEyMWY3YTp7Il9hdXRoX3VzZXJfaWQiOiIxMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZmJjYTViOTJkYmFiMjYwZTUwYjIwN2Y2NTZjM2M1MWU3ZTNiYzI5NiJ9','2019-02-26 09:27:48.758238'),
	('iyg47kvqbtdvzn2vj1gxeqhof1bu24g8','ZmU1MjY5ZTkyODhhYjQzYjI2NDI2NTUzNWZhNGNhZTMxZjFlYTg1YTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YjVlMmZkZWRjMDE3MDNjODQzMjk3YWZiOTI5ZWZiNDc2MjMwOGMwIn0=','2018-12-05 10:31:40.959741'),
	('jf4rpce8nf4n9lm8vmitwurf1b0hy2dd','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2019-01-11 12:36:00.332304'),
	('jhrwrvvhkgubie7b1utvzc1ns4sjpzap','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-19 12:17:56.001203'),
	('jl7hial3jg7vr5bu5jdn9gv1kqyze2gy','ZmU1MjY5ZTkyODhhYjQzYjI2NDI2NTUzNWZhNGNhZTMxZjFlYTg1YTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YjVlMmZkZWRjMDE3MDNjODQzMjk3YWZiOTI5ZWZiNDc2MjMwOGMwIn0=','2018-12-05 10:27:36.850718'),
	('ju9xeaxmdn98gtm7z2lgtr3hhc2iza1w','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-22 03:07:52.631252'),
	('k8cgj7pzgny9d2n8k5pw9thpsfshl7pp','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 03:35:30.388887'),
	('khz852jfuw83mc57lw6h4vursvownsgo','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 05:27:40.982457'),
	('klp3q94dprj1m2o8u5mao65109ay0kvv','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 01:01:13.180754'),
	('km56wbb8a1tb7bihqgxprxu3swt7udsg','ZTA5ZDAyMTg4OWVjYTQ4ZmZhNjI3YjhkYTQxYzgyNjMzYTQ4YWY0ZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YWVhZjY2NGMxYmY4ZGY1OGRjYzZmNThhYWNiOTFlNDIzMzM4M2RjIn0=','2018-12-05 07:36:12.829063'),
	('kx3d4k2h85doqq29t77y2qtirz8kidv6','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-11 02:38:33.007977'),
	('lfer5loanxwbm3eujm0voddxx8gjds1f','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-19 09:07:03.997019'),
	('lo7wn1nawzbt9pnlrdydik6792s58g5k','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 05:33:12.220181'),
	('lv8pfq15e7man2j1chqq3pi2rqxbdv1y','ZWI0MzlhMzE1MGIyYWRkMWU2YmI2NDI2OTBkNzRjODFiYmI4ODRmOTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlMGZmMGUzZDZlY2FmY2I4ZTIzY2YyOTU3NGJhMzViNDBiMWUzOTdmIn0=','2018-12-06 00:41:42.325658'),
	('lvco8hnqc201dozs2fmzfp8hxy80za1t','YjZiMDA1MzAxZTljYTI3MGE3ZWVhYWQ2YzY2YWI5OTNkYTI3MTFmZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YjA4NjAwYTJiYzU1NDE4ZTg2NGNhYmM5MTU0ZDM3NDBmZTI2ZjM1In0=','2018-12-04 08:02:00.737137'),
	('lwcwsy6g8s22qdv9d88ntz3t3f8rmwhq','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-20 01:15:06.991910'),
	('lwgzbc1ptqy1cufwsz183okms5wbfats','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-19 08:48:55.585232'),
	('m1k02uu1taynqs6uptzr1m82hift75pv','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 05:26:40.050799'),
	('m7rfrvwuu729md9v0yq27cvpgabfhkn4','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-11 01:36:07.631133'),
	('m908b5f7r5ugh8iys286catainlw8lkb','ZTA5ZDAyMTg4OWVjYTQ4ZmZhNjI3YjhkYTQxYzgyNjMzYTQ4YWY0ZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YWVhZjY2NGMxYmY4ZGY1OGRjYzZmNThhYWNiOTFlNDIzMzM4M2RjIn0=','2018-12-05 00:31:53.858553'),
	('mmpmuwz90n4qwcupgx7dxp5tzyv4c0p7','ZWI0MzlhMzE1MGIyYWRkMWU2YmI2NDI2OTBkNzRjODFiYmI4ODRmOTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlMGZmMGUzZDZlY2FmY2I4ZTIzY2YyOTU3NGJhMzViNDBiMWUzOTdmIn0=','2018-12-06 00:35:55.320398'),
	('mw6b1zm0ifejrv9bic25m5ir0jjjqgdr','OTBjNWYzM2M0NzMwYzkzY2QxZjZjZTM5MjZjNDcwYjNjNDU3ODA3MTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjkzYTc5MGFmY2YyZjlhYzBjMzA0YzI0MWE2NzRhOGZmNTU5YWE3In0=','2018-12-20 11:42:11.107635'),
	('n3ew7eitl93qzftkdgxhc0uqc17ku36c','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 05:42:09.115852'),
	('nth3jwzx0ct51eawd83m6q8tdrx46msh','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 03:30:41.098194'),
	('nu6nq6fqs4ytuvgqlxdvslzmos5x2436','ODc4Y2FiNzgyMzRmYTQ1Y2E0YWNjMzkyY2FmMDI1ZTFlNTVkMTBmMjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYmY2MWQ3NTMzOGRhZmVkZDhmNjJhMWEzNzg4YzNhZThjMzUzMThmIn0=','2019-05-12 06:56:59.935038'),
	('o0fwy4gtst53hpk84zfe7f8cmkh648no','MDJmNDAyOTU3ZjI0ZDY0OGRhOTY1Y2EwZDQxOWViNDYwNDQ5OGE2NTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YWQxZjljOWIwZTk5ZDRlZjJkZWQ5MDFmNGJlYTBmNGU1OWM1MjNlIn0=','2018-12-05 02:09:22.579724'),
	('o91xm0ibh5rqnimpqedosikcjlkolxri','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 08:08:45.054874'),
	('ogrb3t8l4uueurssmewmv9ry13x72sx9','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 02:13:21.026489'),
	('oist3a5jilmttzpeqpxu1vscha4g5raj','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 05:27:40.444391'),
	('ordxs5igksz5ki1s242a0am0tfb3vsii','ODc4Y2FiNzgyMzRmYTQ1Y2E0YWNjMzkyY2FmMDI1ZTFlNTVkMTBmMjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYmY2MWQ3NTMzOGRhZmVkZDhmNjJhMWEzNzg4YzNhZThjMzUzMThmIn0=','2019-05-12 07:01:52.445934'),
	('p4iox0bvyxtwcb7ufrg2u59efxqkr49i','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-19 08:54:21.144945'),
	('pberhtqcnccw6fnincx5b0gh6ujfhep3','OTBjNWYzM2M0NzMwYzkzY2QxZjZjZTM5MjZjNDcwYjNjNDU3ODA3MTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjkzYTc5MGFmY2YyZjlhYzBjMzA0YzI0MWE2NzRhOGZmNTU5YWE3In0=','2018-12-19 10:10:43.853135'),
	('pbw6fd0tkc42vz5oop3brei7o8ud4me1','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2019-01-11 12:36:15.394344'),
	('pe66xwt4si0526ji23hz3kuoe0hekstc','OTBjNWYzM2M0NzMwYzkzY2QxZjZjZTM5MjZjNDcwYjNjNDU3ODA3MTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjkzYTc5MGFmY2YyZjlhYzBjMzA0YzI0MWE2NzRhOGZmNTU5YWE3In0=','2018-12-22 06:18:40.061538'),
	('peidrtoxr3rcwwimga327ndmbxz76dp5','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2019-01-02 06:48:14.907644'),
	('pf0iu6it9mnn9i2aioryal3fxsqcycfp','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 03:38:43.783366'),
	('phjj7o2hht64bmxg783zu4v80fuljuzl','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-19 09:14:22.423628'),
	('pxmac881jdl6xghj19in4olcgh5lsvtn','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-07 07:09:17.816007'),
	('pygn7z95p4e7bptzehu3d9edt7js9mqi','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-07 05:49:56.779219'),
	('q0rcl4gjpqoqqs9922lnrc24334obnti','OTBjNWYzM2M0NzMwYzkzY2QxZjZjZTM5MjZjNDcwYjNjNDU3ODA3MTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjkzYTc5MGFmY2YyZjlhYzBjMzA0YzI0MWE2NzRhOGZmNTU5YWE3In0=','2018-12-19 10:08:15.274671'),
	('q5dnpuv3990g3q731q7kzxhif7cb4lcz','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-21 03:16:05.781421'),
	('q8yzmnrln3b9jto6d2x5fntr6pfczxdz','OTBjNWYzM2M0NzMwYzkzY2QxZjZjZTM5MjZjNDcwYjNjNDU3ODA3MTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjkzYTc5MGFmY2YyZjlhYzBjMzA0YzI0MWE2NzRhOGZmNTU5YWE3In0=','2018-12-19 09:43:57.413090'),
	('qbckxmg03gfx1fl905zra7h5l6odkbh7','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 05:27:38.102183'),
	('qcd0uwub55bf76kerggv57au8w43avcp','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 01:04:53.160064'),
	('qlprwzrtsp1machwe5ypcmbqyn5fipln','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-07 07:00:18.546435'),
	('qp3w482kk587sltoh495ctsn51a261l9','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 11:18:56.054457'),
	('qp9b4xeqz21tjqq7oy235sre7t1pieu5','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-20 01:31:07.203717'),
	('qy2wn3uq1dhhv17tdisty99ffosi43r2','OTljODFlNTg2ZjIzYWIyMTJmOWIwMjcyMTNiNzBiYmIwNThlM2VmNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxYzc5NTRkYjczMWU2ODMyYzU3MzUyZjNkODM4NjY0MDFkNzAzZjA0In0=','2018-12-06 02:05:24.115467'),
	('r0i0ji0zb8dtgs80vff8f43tgifbo765','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 00:50:58.148485'),
	('r0k41lg8zgh7rhtwni9fdframijhm2am','OTljODFlNTg2ZjIzYWIyMTJmOWIwMjcyMTNiNzBiYmIwNThlM2VmNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxYzc5NTRkYjczMWU2ODMyYzU3MzUyZjNkODM4NjY0MDFkNzAzZjA0In0=','2018-12-11 01:26:21.133777'),
	('r24bebc84jy1jhwi35iqjd0ywx5p5u6k','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-11 01:50:34.739839'),
	('r45l9nbkl5l5nsx3wjjhi21xl62ei8xo','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 09:44:50.652059'),
	('r9kcfh6ohyry0zkbgjos97ehp6bc4loq','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-19 09:15:22.875517'),
	('rby79u08z9gh8la59dw4l7pumrzw0lsc','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-19 08:56:27.056608'),
	('rcr44cndfg6wp72gs41aeyozh57d0rh9','OTljODFlNTg2ZjIzYWIyMTJmOWIwMjcyMTNiNzBiYmIwNThlM2VmNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxYzc5NTRkYjczMWU2ODMyYzU3MzUyZjNkODM4NjY0MDFkNzAzZjA0In0=','2018-12-11 00:59:58.647242'),
	('rhw483g75go7qs5ulgwzo1nr3l9ffbid','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-07 07:20:38.985320'),
	('rixnppqo4qp5xj89m3gw7gl3j7u8vddr','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 05:33:24.540265'),
	('rmdwnc368ao1wnwxlnxho4cwr4wvc6j1','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 02:57:58.641351'),
	('rn321t2l138uq6lgrezg7s8op4ui4thj','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 08:13:39.422944'),
	('rtks2pe9h37jhkxatsg7z3urzrklxj4h','OTBjNWYzM2M0NzMwYzkzY2QxZjZjZTM5MjZjNDcwYjNjNDU3ODA3MTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjkzYTc5MGFmY2YyZjlhYzBjMzA0YzI0MWE2NzRhOGZmNTU5YWE3In0=','2018-12-19 09:46:00.512165'),
	('rwj0jitcxv1gap0cfiwghzpmnjt4p6t6','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-19 08:58:20.427233'),
	('rxlvpy1n4g3wsrkgux427d1w2m4vjo7d','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 01:30:22.372129'),
	('s1b0rilwx21u845hjhz3ieym86b8h8ca','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-19 09:12:31.563461'),
	('s3d01pypcv6odg1d0ppo1z23gd1vlcgr','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-10 10:54:41.401769'),
	('s7l9m9kbwjs82q0pzqvg0z6zoajwamsy','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 08:13:41.185215'),
	('s87fm7vtyed8tnu5uwutp1czmny33xq8','MjQyN2E3N2JmZjViNDQ0NzdjMWEwODcyODk3MWQ5NTQxMTE4OGY0NDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjMzODFkOTcwNTM0M2E4NTJkODlhMTU1NTU0MDdmN2QyMGI5NmVhIn0=','2018-12-05 10:51:04.380722'),
	('s8drr7rozogwimowooyqzf4tjycq9apx','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 03:43:32.367635'),
	('sje8lw33nmrj88j4q901mg85ryg26w95','OTBjNWYzM2M0NzMwYzkzY2QxZjZjZTM5MjZjNDcwYjNjNDU3ODA3MTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjkzYTc5MGFmY2YyZjlhYzBjMzA0YzI0MWE2NzRhOGZmNTU5YWE3In0=','2018-12-19 09:29:23.816425'),
	('sv5whixret7je8b1dv1qcynr782bdtuk','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 03:47:58.971460'),
	('sw716db8hms7uvgdbof79c5bmluynjfx','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-19 08:55:36.233312'),
	('t06ike43z2kcwjo0v2ot3eznlbm06evb','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-07 01:58:36.622677'),
	('t4m2vea7emmprfzyeqtuzru85z6z6pww','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-20 03:39:15.132707'),
	('t5pc4skxvuj4c2x6kw5ikui3zmx0fnqs','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-20 01:29:32.536963'),
	('te2jpu87xvtrdxdz92u6gcsb1husbawc','OTljODFlNTg2ZjIzYWIyMTJmOWIwMjcyMTNiNzBiYmIwNThlM2VmNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxYzc5NTRkYjczMWU2ODMyYzU3MzUyZjNkODM4NjY0MDFkNzAzZjA0In0=','2018-12-10 10:54:47.003101'),
	('tijc3nx45egovv17o5e8nt2dwaesve5v','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 08:13:54.709414'),
	('to6w99s8m6faoadfrtzsf0n63thfk6il','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 00:58:06.445124'),
	('toggl6epqf4effrtfa0fm3r7jcubkp8p','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 03:26:00.909067'),
	('ttxsdbne04f7b60zmvyciaz42evm2mee','ZTA5ZDAyMTg4OWVjYTQ4ZmZhNjI3YjhkYTQxYzgyNjMzYTQ4YWY0ZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YWVhZjY2NGMxYmY4ZGY1OGRjYzZmNThhYWNiOTFlNDIzMzM4M2RjIn0=','2018-12-05 05:58:52.356833'),
	('tvuv6n7vvlk4wff8beoxxhhu6tdo2l53','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 03:50:27.017443'),
	('tztxkglyavt1n1c6c4z0gg3juyj7g99j','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-19 09:08:42.805462'),
	('uaku3dspmnfuocdyjfqtn9jpq8tqsk9h','ZGNkMTY0YmM1MjQwM2Q1OTQzMGM3ZDA4NDlhZDRiYzczYmJiZjc1NDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxZjY4OTNkNzllOThjN2NjNjgwZWEwZDkwZTBkYjU4ZDRkNWJiZTZiIn0=','2018-12-19 05:47:23.306326'),
	('ufjesdl4ittku0foq2fsal7tw5xo1loq','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 03:31:50.693935'),
	('ug07ooi35in0cbvwqalsadv5oae7a9he','ZDRmNWU4NWY3NTRiYTNmYzZjOTA1ZmVmNzJlMTM2NDViYTVkZDc4Zjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkZDhkMjY4ZGQ0MmVkOWIyZjljNDVhY2YxM2FiMjRhZTY0YTU4YjlhIn0=','2018-12-19 09:26:55.387762'),
	('ukqhz9a50uitbm8z1pxqt06z8b8o6qpo','ZmU1MjY5ZTkyODhhYjQzYjI2NDI2NTUzNWZhNGNhZTMxZjFlYTg1YTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YjVlMmZkZWRjMDE3MDNjODQzMjk3YWZiOTI5ZWZiNDc2MjMwOGMwIn0=','2018-12-05 09:37:20.185883'),
	('umizhvbshur5q2ey94grihyb6ntx0ob9','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-20 02:24:29.775720'),
	('uo1z8do1dhaz6e2afz2br0u1v9dqi36r','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-07 00:32:04.837604'),
	('uou604lylp6yu9uaxuct7wdzo30a82f7','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 03:49:23.716748'),
	('ur4p57wp5ne85u6zokma9f6sxbydij85','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-07 07:17:26.119960'),
	('uroik1iz9k89h40vqf1v33vciiqv6e44','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-07 05:50:28.631900'),
	('uv10n03gixepwotnh21lb90puu7x33c3','OTBjNWYzM2M0NzMwYzkzY2QxZjZjZTM5MjZjNDcwYjNjNDU3ODA3MTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjkzYTc5MGFmY2YyZjlhYzBjMzA0YzI0MWE2NzRhOGZmNTU5YWE3In0=','2018-12-21 03:45:45.941366'),
	('uy6logbcengbj0xhc25qqqhswg06fslk','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-19 08:52:49.909144'),
	('v307m6res5x36tad0tgsjsq6umpstt2f','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-07 05:56:38.187461'),
	('v5v90syorgkg9p2w0bmsqg8c6utot5o7','OTBjNWYzM2M0NzMwYzkzY2QxZjZjZTM5MjZjNDcwYjNjNDU3ODA3MTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjkzYTc5MGFmY2YyZjlhYzBjMzA0YzI0MWE2NzRhOGZmNTU5YWE3In0=','2018-12-19 10:11:32.302572'),
	('vdclu2q09awmyhmgxipzxzyscyr14cm1','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-07 07:02:49.553685'),
	('vh9ujnptzhxjt6qc9xl31h3gzbq28b5e','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 03:33:39.707354'),
	('vm5dlz2po484atuyym0lps9jyszccpql','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 03:30:57.462344'),
	('vnwyabyy1u3y6v4cv4my1lhegsk9opmw','OTBjNWYzM2M0NzMwYzkzY2QxZjZjZTM5MjZjNDcwYjNjNDU3ODA3MTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjkzYTc5MGFmY2YyZjlhYzBjMzA0YzI0MWE2NzRhOGZmNTU5YWE3In0=','2018-12-19 09:51:17.613036'),
	('vsf8b8za5uewyqbzk04dclyk5589w696','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-20 03:08:59.171184'),
	('vvtxc5ua1j25k2nm3p097fsqzsdh8791','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-19 12:16:56.839189'),
	('vwd3rrhumywqxjy6ramdbpjl6e2pgazz','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 05:27:41.109064'),
	('w74i8lod1ydkb9ais99wdre2y8t4psqz','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-20 01:32:14.360739'),
	('w7nqh356mias1lcdu2e4c1iz97jml4ip','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 07:39:57.375927'),
	('wgbcpx8pwjbvmvlb3v678u097q7rjbhe','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 01:58:18.202454'),
	('won0z2r2mnqlrqqeqwrk225q2qbrii7l','ZmU1MjY5ZTkyODhhYjQzYjI2NDI2NTUzNWZhNGNhZTMxZjFlYTg1YTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YjVlMmZkZWRjMDE3MDNjODQzMjk3YWZiOTI5ZWZiNDc2MjMwOGMwIn0=','2018-12-05 10:31:15.600334'),
	('wp01n7m6suy26ptr19otwmpkwe8n6ass','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 03:43:15.830869'),
	('wtt38indnlheb9b1v76w2d34yprjj806','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-20 01:30:30.819135'),
	('x3dfrmcbn28g9nxvz28jb2cb6pitauo5','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 05:27:40.649688'),
	('x5c1myrxj5jdybggpfb66ectxw3jc0dt','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-19 09:06:05.941714'),
	('xilcnso3d8lp3e3n8gruixq15qnaodqr','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 02:23:57.784759'),
	('xopcya4k9e2mmtg6faas4xs3nd3kp2gu','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-20 01:36:29.209389'),
	('xw3srq8flp778a87ystiqvcmfn0rngix','OTBjNWYzM2M0NzMwYzkzY2QxZjZjZTM5MjZjNDcwYjNjNDU3ODA3MTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjkzYTc5MGFmY2YyZjlhYzBjMzA0YzI0MWE2NzRhOGZmNTU5YWE3In0=','2018-12-19 09:44:36.593165'),
	('y35gln2f9suw1fqlqv5h039vyl7lx396','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-20 01:36:01.924213'),
	('yna4zcbs3hvap45wb4tigc8i3mwuvfgx','MjQyN2E3N2JmZjViNDQ0NzdjMWEwODcyODk3MWQ5NTQxMTE4OGY0NDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjMzODFkOTcwNTM0M2E4NTJkODlhMTU1NTU0MDdmN2QyMGI5NmVhIn0=','2018-12-06 00:29:24.783110'),
	('yojd2lv17wbfmevkaxpe71mrcnivbog7','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-20 01:09:29.253568'),
	('yq9d3say8vbntl9xunmpjb0zvruvh1kn','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 05:38:31.627781'),
	('yuwzrnx8ouh2t2v320zh29sfasmkdqpe','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-20 03:58:49.815096'),
	('z2i5q40zfv3a3cfc0z6j1p1su6ukxbo5','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 07:15:23.286219'),
	('z3vf1chxud15z807wptc1i212715t7y7','MjE3NDNlNDRhMTdjN2E3OGE1NjNhNzE5MDg1YzAyNzUyZDhiYjE0Mzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4ZmQwNjBmZTVjMTkxYjY0NzEwMTgxMTg4OTc3MGJmOTk3NzdlN2QyIn0=','2018-12-11 02:44:36.303274'),
	('zaarzf2g37k9lv3hhnruasurv00hh9dg','MTQ1Y2JmOTY0NDkxYzQ2NWNiMTMyOGEyOWQwZTBmZWRlYzIxZGM0Nzp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODA1MzU0M2I2ODdjZWI5MzgwMzZiNzAzNjBlNGYwYTdhZGIzOTI5NSJ9','2018-12-20 08:55:34.346075'),
	('zidn1k9b136r3a1a4752cteh5b6fgm3l','NTczZTRiNzFlZjAyNzAzNmU4ZjVkYjNkOWE5OGZjMDNhMjYzMmEyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOWJlZTYzZDVkMDI2YWU0NmZhMjBhYjgwOTZhNzIwMDhkNGI2NmMwIn0=','2018-12-20 01:08:32.470186'),
	('zodvoxtoea5o01tnbqkfw683f43eydk4','YjZiMDA1MzAxZTljYTI3MGE3ZWVhYWQ2YzY2YWI5OTNkYTI3MTFmZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YjA4NjAwYTJiYzU1NDE4ZTg2NGNhYmM5MTU0ZDM3NDBmZTI2ZjM1In0=','2018-12-04 08:07:36.782247'),
	('zoke44o151plucj14aybe8um159o79zd','ZTA5ZDAyMTg4OWVjYTQ4ZmZhNjI3YjhkYTQxYzgyNjMzYTQ4YWY0ZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YWVhZjY2NGMxYmY4ZGY1OGRjYzZmNThhYWNiOTFlNDIzMzM4M2RjIn0=','2018-12-05 05:30:11.453077'),
	('zqn03v25w6anado2xkkojc882phw0v6o','ZTA5ZDAyMTg4OWVjYTQ4ZmZhNjI3YjhkYTQxYzgyNjMzYTQ4YWY0ZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YWVhZjY2NGMxYmY4ZGY1OGRjYzZmNThhYWNiOTFlNDIzMzM4M2RjIn0=','2018-12-05 02:18:04.022279'),
	('zr34n652advkcn5wsfenie5ksqbqzgzn','NTI2NTcyYmQ4ZTE2YmI1Y2FkZjk1ZWQ4ODA2YWUyNDg2MGM3NDIxYjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGZlODI1MDA4ZmFkYzg2N2ZlNmU2OTBhMWJiZDljNmVjOWVhMjA0In0=','2018-12-06 02:49:33.062233'),
	('zrv5gaq7d913vz0btey3n10vybtgtglf','MjQyN2E3N2JmZjViNDQ0NzdjMWEwODcyODk3MWQ5NTQxMTE4OGY0NDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YjMzODFkOTcwNTM0M2E4NTJkODlhMTU1NTU0MDdmN2QyMGI5NmVhIn0=','2018-12-06 00:27:55.758264');

/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table qy_activity
# ------------------------------------------------------------

DROP TABLE IF EXISTS `qy_activity`;

CREATE TABLE `qy_activity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `notice` longtext COMMENT '活动公告',
  `activity_time` int(20) DEFAULT NULL COMMENT '活动开始时间',
  `address_province` varchar(20) DEFAULT '' COMMENT '省份',
  `address_city` varchar(20) DEFAULT '' COMMENT '城市',
  `address_area` varchar(20) DEFAULT '' COMMENT '区/县',
  `address_detailed` varchar(256) DEFAULT '' COMMENT '详细地点',
  `formater` int(4) NOT NULL DEFAULT '0' COMMENT '赛制0: 待定, 1: 5人制, 2: 6人制, 3: 7人制, 4: 8人制, 5: 9人制, 6: 10人制, 7: 11人制',
  `type` int(4) NOT NULL DEFAULT '0' COMMENT '活动类型:0散踢 1队内活动 2球队比赛',
  `upper_limit` int(11) DEFAULT NULL COMMENT '人数上限',
  `lower_limit` int(11) DEFAULT NULL COMMENT '人数下限',
  `is_limit` int(11) NOT NULL DEFAULT '0' COMMENT '是否为限时报名:0不限时 1限时',
  `limit_time` varchar(20) DEFAULT '' COMMENT '报名截止时间',
  `price` varchar(16) NOT NULL DEFAULT '0.00' COMMENT '参加费用',
  `activity_img` text COMMENT '活动宣传照',
  `originator_id` int(11) NOT NULL COMMENT '活动发起人ID',
  `activity_state` int(4) NOT NULL DEFAULT '1' COMMENT '活动所处状态:0已取消 1可参加 2已过期 3隐藏',
  `add_time` varchar(20) DEFAULT '' COMMENT '创建时间',
  `is_irres` int(11) NOT NULL DEFAULT '0' COMMENT '限时无责(0无责，有责)',
  `irres_time` varchar(20) DEFAULT NULL COMMENT '无责时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='活动';

LOCK TABLES `qy_activity` WRITE;
/*!40000 ALTER TABLE `qy_activity` DISABLE KEYS */;

INSERT INTO `qy_activity` (`id`, `notice`, `activity_time`, `address_province`, `address_city`, `address_area`, `address_detailed`, `formater`, `type`, `upper_limit`, `lower_limit`, `is_limit`, `limit_time`, `price`, `activity_img`, `originator_id`, `activity_state`, `add_time`, `is_irres`, `irres_time`)
VALUES
	(1,'一起玩',12324,'河南省','郑州市','管城区','河南郑州管城区',1,1,20,3,0,'135678652','0.00','',2,3,'1544166414',0,'12345673456'),
	(2,'',1544238600,'河南省','郑州市','管城回族区','人民路1号郑州体育馆',4,0,20,1,0,'1544238600','0.00','[\'static/image/jpeg/20181207/15441664306412160.jpeg\']',1,2,'1544166472',0,'1544238600'),
	(3,'仙路尽头谁为峰,一遇明晋道成空',1544198400,'河南省','郑州市','河南省郑州市','河南省郑州市',3,0,7,3,0,'1544198400','0.00','[\'static/image/jpeg/20181207/15441686055633084.jpg\']',2,0,'1544166487',0,'1544198400'),
	(4,'春晓岂是池中物,一遇风云便化虫;',1544284800,'','北京市','东城区','东长安街天安门广场',5,1,9,6,0,'1544284800','0.00','[\'static/image/png/20181207/15441664891391998.png\']',2,0,'1544166636',0,'1544284800'),
	(5,'纵览千古风流人物, 也没明晋骚',1545543000,'河南省','郑州市','管城回族区','文兴路7号九六健身学院(郑州校区)',1,0,20,1,0,'1545535800','0.00','[\'static/image/jpg/20181207/15441667838437124.jpg\', \'static/image/jpg/20181207/15441667845535550.jpg\']',1,2,'1544166786',0,'1545539400'),
	(6,'双十二',1544238000,'河南省','郑州市','管城回族区','商城路217号郑州市管城区委(商城路北)',7,0,12,2,0,'1544238000','0.00','[\'static/image/png/20181207/15441667886547404.png\', \'static/image/jpeg/20181207/15441667886558780.jpeg\', \'static/image/jpeg/20181207/15441667886568842.jpg\']',3,2,'1544166792',0,'1544238000'),
	(7,'春眠不觉晓,处处蚊子咬',1545066600,'','','澳门特别行政区','澳门半岛文第士街39-b附近耶路撒冷之城',0,0,2,1,0,'1545066600','0.00','[\'static/image/jpeg/20181207/15441683917578544.jpg\', \'static/image/jpeg/20181207/15441683918007846.jpg\']',2,2,'1544166877',0,'1545066600'),
	(8,'房价高',1544391000,'河南省','郑州市','管城回族区','商城路217号郑州市管城区委(商城路北)',6,1,10,2,0,'1544391000','0.00','[\'static/image/png/20181207/15441669042009070.png\']',3,0,'1544166908',0,'1544391000'),
	(9,'目空一切',1544167200,'河南省','郑州市','管城回族区','商城路217号郑州市管城回族区政府',4,0,16,8,0,'1544167200','0.00','[\'static/image/png/20181207/15441670252486208.png\']',3,0,'1544167028',0,'1544167200'),
	(10,'雾都一日游',1544803800,'河南省','郑州市','管城回族区','石化路1号世纪欢乐园伦敦之眼',0,0,4,2,0,'1544803800','0.00','[\'static/image/jpeg/20181207/15441685400831388.jpg\', \'static/image/jpeg/20181207/15441685401506250.jpg\']',2,2,'1544167081',0,'1544803800'),
	(11,'专心一事',1544167200,'河南省','郑州市','管城回族区','商城路217号郑州市管城区委(商城路北)',2,0,6,2,0,'1544167200','0.00','[\'static/image/png/20181207/15441670909599686.png\']',3,0,'1544167091',0,'1544167200'),
	(12,'面向前方,拿出你自信的眼神,爱谁谁的表情,走出六亲不认的步伐',1544634600,'河南省','郑州市','管城回族区','紫荆山路紫荆山路',0,2,3,1,0,'1544634600','0.00','[\'static/image/png/20181207/15441672905067342.png\']',2,2,'1544167291',0,'1544634600'),
	(13,'2',1544198400,'河南省','平顶山市','新华区','光明路与建设路交叉口南300米路西星公馆KTV',0,0,3,2,0,'1544198400','0.00','[]',4,3,'1544169935',0,'1544198400'),
	(14,'',1544170200,'河南省','平顶山市','新华区','建设西路6号新华区政府(建设路南)',0,0,2,1,0,'1544170200','0.00','[]',4,0,'1544170273',0,'1544170200'),
	(15,'',1544371200,'河南省','平顶山市','新华区','建设西路6号新华区政府(建设路南)',0,0,2,1,0,'1544371200','0.00','[]',4,0,'1544170804',0,'1544371200'),
	(16,'',1544371200,'河南省','平顶山市','新华区','建设西路6号新华区政府(建设路南)',0,0,2,1,1,'1544367600','0.00','[]',4,0,'1544170830',1,'1544360400'),
	(17,'',1544576400,'','万盟家纺城(郑州市','万盟家纺城(郑州市','万盟家纺城(郑州市管城南三环文兴路7号)万盟家纺城(郑州市管城南三环文兴路7号)',1,0,10,2,0,'1544576400','0.00','[]',1,0,'1544172759',0,'1544576400'),
	(18,'',1544238600,'','','','万盟家居电子商务产业园(管城文兴路7号)万盟家居电子商务产业园(管城文兴路7号)',0,0,3,1,0,'1544238600','0.00','[]',5,3,'1544238585',0,'1544238600'),
	(19,'',1544252400,'','万盟家纺城(郑州市','万盟家纺城(郑州市','万盟家纺城(郑州市管城南三环文兴路7号)万盟家纺城(郑州市管城南三环文兴路7号)',0,0,3,1,0,'1544252400','1.00','[]',5,3,'1544247702',0,'1544252400'),
	(20,'玩的开心',12324,'河南省','郑州市','管城区','河南郑州管城区',1,1,20,3,0,'135678652','10.00','',6,3,'1544254794',0,'12345673456'),
	(21,'开始报名了',1544849400,'','','','平安果酒店(中州大道三环店)平安果酒店(中州大道三环店)',7,0,11,10,0,'1544849400','1.00','[\'static/image/jpg/20181215/15448483596340728.jpg\']',7,0,'1544848370',0,'1544849400'),
	(22,'',1545393600,'','北京市','大兴区','世界之花假日广场(久敬庄路南)世界之花假日广场',3,0,10,7,1,'1545393600','30.00','[\'static/image/jpg/20181221/15453689208019030.jpg\', \'static/image/jpg/20181221/15453689212666746.jpg\']',13,3,'1545368937',0,'1545375600'),
	(23,'',1545393600,'','北京市','大兴区','世界之花假日广场(久敬庄路南)世界之花假日广场',3,0,10,7,1,'1545393600','30.00','[\'static/image/jpg/20181221/15453689208019030.jpg\', \'static/image/jpg/20181221/15453689212666746.jpg\']',13,3,'1545368937',0,'1545375600'),
	(24,'',1545906600,'','武汉市','武汉市无线电小区','(洪山区鲁磨路428号)武汉市无线电小区(洪山区鲁磨路428号)',6,0,21,14,1,'1545892200','30.00','[\'static/image/jpg/20181226/15458212129705088.jpg\', \'static/image/jpg/20181226/15458212130380848.jpg\']',13,0,'1545821213',1,'1545892200'),
	(25,'撒大声地',1556035200,'河南省','郑州市','金水区','金水东路22号河南省人民政府',0,0,7,2,0,'1556035200','1.00','[\'static/image/jpeg/20190421/15558499262339074.jpg\']',4,0,'1555849930',0,'1556035200'),
	(26,'',1556640000,'河南省','平顶山市','新华区','长青路与建设路交叉口鹰城广场',0,2,6,1,0,'1556640000','1.00','[]',4,0,'1556435005',0,'1556640000');

/*!40000 ALTER TABLE `qy_activity` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table qy_actor_activities
# ------------------------------------------------------------

DROP TABLE IF EXISTS `qy_actor_activities`;

CREATE TABLE `qy_actor_activities` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) NOT NULL COMMENT '参加人员ID',
  `reg_state` int(4) NOT NULL DEFAULT '2' COMMENT '参加人员状态:1报名 2待定 3请假',
  `free_state` int(4) NOT NULL DEFAULT '0' COMMENT '参加人员是否需要付费:0付费 1免费',
  `add_time` varchar(20) NOT NULL DEFAULT '' COMMENT '创建时间',
  `activity_id` int(11) NOT NULL COMMENT '所参加的活动(外键)',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='参加人员表(中间表)';

LOCK TABLES `qy_actor_activities` WRITE;
/*!40000 ALTER TABLE `qy_actor_activities` DISABLE KEYS */;

INSERT INTO `qy_actor_activities` (`id`, `member_id`, `reg_state`, `free_state`, `add_time`, `activity_id`)
VALUES
	(3,3,1,0,'1544167404',3),
	(4,3,1,0,'1544167412',10),
	(6,3,1,0,'1544167448',6),
	(7,3,1,0,'1544167470',8),
	(14,2,1,0,'1544167764',12),
	(19,2,2,0,'1544168415',7),
	(20,2,3,0,'1544168483',5),
	(21,2,1,0,'1544168548',10),
	(23,2,1,0,'1544168930',2),
	(24,2,1,0,'1544168943',6),
	(25,4,2,0,'1544169949',13),
	(32,3,1,0,'1544172885',2),
	(34,3,1,0,'1544172900',17),
	(38,1,1,0,'1544173831',5),
	(40,7,2,0,'1544848266',5),
	(41,7,1,0,'1544848286',7),
	(42,1,1,0,'1544848422',7),
	(45,8,1,0,'1544848527',7),
	(46,4,2,0,'1556435014',26);

/*!40000 ALTER TABLE `qy_actor_activities` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table qy_auditing
# ------------------------------------------------------------

DROP TABLE IF EXISTS `qy_auditing`;

CREATE TABLE `qy_auditing` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `is_auditing` int(11) DEFAULT NULL COMMENT '是否审核 0否',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

LOCK TABLES `qy_auditing` WRITE;
/*!40000 ALTER TABLE `qy_auditing` DISABLE KEYS */;

INSERT INTO `qy_auditing` (`id`, `is_auditing`)
VALUES
	(1,0);

/*!40000 ALTER TABLE `qy_auditing` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table qy_feedback
# ------------------------------------------------------------

DROP TABLE IF EXISTS `qy_feedback`;

CREATE TABLE `qy_feedback` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `member_id` int(11) DEFAULT NULL COMMENT '用户ID',
  `content` longtext COLLATE utf8mb4_unicode_ci COMMENT '反馈的意见内容',
  `add_time` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '创建时间',
  `Feedback_state` int(4) NOT NULL DEFAULT '0' COMMENT '是否已查看:0未查看,1已查看',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

LOCK TABLES `qy_feedback` WRITE;
/*!40000 ALTER TABLE `qy_feedback` DISABLE KEYS */;

INSERT INTO `qy_feedback` (`id`, `member_id`, `content`, `add_time`, `Feedback_state`)
VALUES
	(1,1,'仙路尽头谁为峰,一遇明晋道成空','1544237495.9473627',0);

/*!40000 ALTER TABLE `qy_feedback` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table qy_group
# ------------------------------------------------------------

DROP TABLE IF EXISTS `qy_group`;

CREATE TABLE `qy_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_a_id` int(11) NOT NULL COMMENT '用户',
  `member_b_id` int(11) NOT NULL COMMENT '被打标签用户',
  `group` varchar(32) NOT NULL DEFAULT '我的球友' COMMENT '分组',
  `add_time` varchar(20) DEFAULT '' COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='标签/分组';

LOCK TABLES `qy_group` WRITE;
/*!40000 ALTER TABLE `qy_group` DISABLE KEYS */;

INSERT INTO `qy_group` (`id`, `member_a_id`, `member_b_id`, `group`, `add_time`)
VALUES
	(7,2,3,'路人',''),
	(8,3,2,'我的球友','');

/*!40000 ALTER TABLE `qy_group` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table qy_member
# ------------------------------------------------------------

DROP TABLE IF EXISTS `qy_member`;

CREATE TABLE `qy_member` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `avatar` varchar(256) DEFAULT '' COMMENT '头像',
  `openid` varchar(30) NOT NULL DEFAULT '' COMMENT 'openid',
  `unionid` varchar(30) DEFAULT '' COMMENT 'unionid',
  `age` int(11) DEFAULT NULL COMMENT '年龄',
  `nickname` varchar(56) DEFAULT '' COMMENT '昵称',
  `balance` varchar(20) NOT NULL DEFAULT '0.00' COMMENT '余额',
  `profession` varchar(256) DEFAULT '' COMMENT '职业',
  `phonenum` bigint(20) DEFAULT NULL COMMENT '电话',
  `add_time` varchar(20) DEFAULT '' COMMENT '创建时间',
  `cardholder` varchar(56) DEFAULT '' COMMENT '持卡人',
  `ID_number` varchar(20) DEFAULT '' COMMENT '身份证号',
  `bank_card_number` varchar(22) DEFAULT '' COMMENT '银行卡号',
  `reserved_phone_number` bigint(20) DEFAULT NULL COMMENT '银行预留手机号',
  `opening_bank` varchar(36) DEFAULT '' COMMENT '开户行',
  PRIMARY KEY (`id`),
  KEY `openidIndex` (`openid`(10))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户信息';

LOCK TABLES `qy_member` WRITE;
/*!40000 ALTER TABLE `qy_member` DISABLE KEYS */;

INSERT INTO `qy_member` (`id`, `avatar`, `openid`, `unionid`, `age`, `nickname`, `balance`, `profession`, `phonenum`, `add_time`, `cardholder`, `ID_number`, `bank_card_number`, `reserved_phone_number`, `opening_bank`)
VALUES
	(1,'https://wx.qlogo.cn/mmopen/vi_32/PqLVnhPYLok74f9NctaPW4icUO6EcDxEw2omQ8MzcGgyicaTsgFqRZenDX6ExjMeoibFDCKHQhzFdJxuJsKj6ryoQ/132','ovjD15UjkjH6dLRJjr7dLwr2X7fs','',NULL,'晓','0.00','',13245678900,'1544166296','','','',NULL,''),
	(2,'https://wx.qlogo.cn/mmopen/vi_32/fAg6J52UDa5QKefPvTgyBXGLT1KBasYO5cQ23fY9AWZdF6zjXBYGwJicgwcZxFCibpmyfTOkJL6aicOxop6lnkU0Q/132','ovjD15WRy0c8qcqWFyBcf7X2aqBw','',NULL,'神凌法圣','0.00','',NULL,'1544166299','','','',NULL,''),
	(3,'https://wx.qlogo.cn/mmopen/vi_32/5eVwzxXSbL4Oa3296UnAqUic3TuDZsKmiagBU83ibDVlQH1ibHWMc8MyfnxLT7poRw7xOtpXibvNevibgibpHHCZKJYGA/132','ovjD15Ty3R4NkJvnxCj8xAOHB3TM','',NULL,'浩','0.00','',NULL,'1544166626','','','',NULL,''),
	(4,'https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKbt3JKCxyeRuk8km9vtfibRYw4icEBn8YH18Y6B3YGqt7gUYEibn8Ka2LiatgZOBCVHM5q6ic8Kxz3DtA/132','ovjD15VQq3bre2HsiT8mgTUYuw5I','',NULL,'leer','0.00','',NULL,'1544169863','','','',NULL,''),
	(5,'https://wx.qlogo.cn/mmopen/vi_32/LDvwPrLsA0tETDoqcSpd33sOxqGibYlpH1ZfjQt5LjhTibHOxjYBWDz7HRmrC9aibLqvNy2VSNGokGfe62blfRaibw/132','ovjD15UlUB3dMEgGzDeLwckqAKGs','',20,'北梦','0.00','行业1',15896582501,'1544238120','','','',NULL,''),
	(6,'https://wx.qlogo.cn/mmopen/vi_32/DYAIOgq83er6pW4cyqSlOPjiaHygg0G2xMhbjAcHZlIpmkibIXqibc1kC7iaibd94f5o7wVBjvAUoIiat5DC5nibiaFQlg/132','ovjD15TYpbxdy7N0C3Ta2jEdF1jU','',NULL,'we love the basketball ','0.00','',NULL,'1544239634','','','',NULL,''),
	(7,'https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJDeiaTzibGBEreIHwt2FgicrtibWAYy0ueEHrjp6yE9Qy3jLOaicj8nMXLZVB96s2M3O4jic5EYKzibWM4g/132','ovjD15YlATh3aqQlHd4vA08ZWpU0','',NULL,'o.o','0.00','',NULL,'1544240068','','','',NULL,''),
	(8,'https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTLJrErsicq2tscfZ46URiaTRmNib2XBHVqOSoTbSjEzw7qKrGzEuL1m4MGibh05JQaarCTznHpXN1YyEQ/132','ovjD15R8c_JJeOEGxhwcp3pNXyno','',NULL,'周奥琪','0.00','',NULL,'1544249322','','','',NULL,''),
	(9,'https://wx.qlogo.cn/mmhead/Q3auHgzwzM5e7zoGwzbStibbUYEyvzA1M5Aa9K2tdcribjaxV7B8C5GQ/0/132','ovjD15adwdH_5m5h5qhJOvmnkK6k','',NULL,'邹渊','0.00','',NULL,'1544251614','','','',NULL,''),
	(10,'https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJ8Kll5vd9fXqNWetHdbhibYjz70SwmLicM2WguHLPdthhdppVVxAZevb63zLQIAIZf1Pwjw44vc1AA/132','undefined','',NULL,'o.o','0.00','',NULL,'1544257434','','','',NULL,''),
	(11,'https://wx.qlogo.cn/mmhead/Q3auHgzwzM5e7zoGwzbStibbUYEyvzA1M5Aa9K2tdcribjaxV7B8C5GQ/0/132','ovjD15YA69KILqosA1et3nbkD6Nc','',NULL,'武松','0.00','',NULL,'1544323605','','','',NULL,''),
	(12,'https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTLpo3rCE1Q2cTjOshYwA12QCTticyJPCBb1jMX9rLiblmC6PBJ8M2JgZHlkTScyWeDBicOuH3r9B45gg/132','ovjD15cPRrS7KpglYC3VNLmiqPek','',NULL,'谜一样的男人','0.00','',NULL,'1545016699','','','',NULL,''),
	(13,'https://wx.qlogo.cn/mmopen/vi_32/DYAIOgq83erqGaEwWPh6gRr7mgwOZ3sCwG9BN3XjC3agMP5kQgY8pqANSsgwWiaxJuJfiauk6LvBZqmlqJiaTKbIw/132','ovjD15esYx-m0EAOflEVpkQ-y248','',NULL,'HAKUNA MATATA','0.00','',NULL,'1545016706','','','',NULL,'');

/*!40000 ALTER TABLE `qy_member` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table qy_message
# ------------------------------------------------------------

DROP TABLE IF EXISTS `qy_message`;

CREATE TABLE `qy_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) NOT NULL COMMENT '留言人',
  `message_img` longtext COMMENT '留言图片',
  `message_content` longtext COMMENT '留言内容',
  `add_time` varchar(20) DEFAULT '' COMMENT '创建时间',
  `activity` int(11) DEFAULT NULL COMMENT '活动外键',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='留言';

LOCK TABLES `qy_message` WRITE;
/*!40000 ALTER TABLE `qy_message` DISABLE KEYS */;

INSERT INTO `qy_message` (`id`, `member_id`, `message_img`, `message_content`, `add_time`, `activity`)
VALUES
	(1,1,'[]','草22,太坑了','1544237030',10),
	(2,1,'[\'static/image/jpeg/20181208/15442371784567408.jpg\']','SB举办的','1544237182',7),
	(3,1,'[]','hdb','1544238676',2),
	(4,4,'[]','111','1555849965',25),
	(5,4,'[]','撒大大撒旦','1556435025',26),
	(6,4,'[]','dsaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa','1559218861',26);

/*!40000 ALTER TABLE `qy_message` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table qy_news
# ------------------------------------------------------------

DROP TABLE IF EXISTS `qy_news`;

CREATE TABLE `qy_news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `applicant_id` int(11) NOT NULL COMMENT '申请人',
  `respondent_id` int(11) NOT NULL COMMENT '被申请人',
  `content` longtext COMMENT '消息内容',
  `apply_time` varchar(20) DEFAULT '' COMMENT '申请时间',
  `new_state` int(4) NOT NULL DEFAULT '2' COMMENT '0 拒绝  1 同意  2 待处理',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='球友请求';

LOCK TABLES `qy_news` WRITE;
/*!40000 ALTER TABLE `qy_news` DISABLE KEYS */;

INSERT INTO `qy_news` (`id`, `applicant_id`, `respondent_id`, `content`, `apply_time`, `new_state`)
VALUES
	(1,1,1,'1','1',1);

/*!40000 ALTER TABLE `qy_news` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table qy_pay
# ------------------------------------------------------------

DROP TABLE IF EXISTS `qy_pay`;

CREATE TABLE `qy_pay` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `member_id` int(11) DEFAULT NULL COMMENT '支付人ID',
  `pay_type` int(4) NOT NULL DEFAULT '0' COMMENT '支付类型 0:默认,1: 充值,2: 提现,3:退款, 4: 支付',
  `pay_amount` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '' COMMENT '支付金额',
  `pay_state` int(4) NOT NULL DEFAULT '2' COMMENT '支付状态 0:''默认'', 1失败, 2:中, 3:成功',
  `add_time` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '创建时间',
  `out_trade_no` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT '' COMMENT '订单号',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

LOCK TABLES `qy_pay` WRITE;
/*!40000 ALTER TABLE `qy_pay` DISABLE KEYS */;

INSERT INTO `qy_pay` (`id`, `member_id`, `pay_type`, `pay_amount`, `pay_state`, `add_time`, `out_trade_no`)
VALUES
	(1,13,1,'30.00',2,'1545821356','1545821356407330'),
	(2,6,1,'20.00',2,'1553322097','1553322097275541'),
	(3,6,1,'1.00',2,'1553322106','1553322106131310');

/*!40000 ALTER TABLE `qy_pay` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table qy_replay
# ------------------------------------------------------------

DROP TABLE IF EXISTS `qy_replay`;

CREATE TABLE `qy_replay` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reply_member` int(11) NOT NULL COMMENT '回复人ID',
  `to_reply_member` int(11) NOT NULL COMMENT '被回复人ID',
  `reply_content` longtext COMMENT '回复内容',
  `add_time` varchar(20) DEFAULT '' COMMENT '创建时间',
  `message_id` int(11) DEFAULT NULL COMMENT '留言外键',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='回复';

LOCK TABLES `qy_replay` WRITE;
/*!40000 ALTER TABLE `qy_replay` DISABLE KEYS */;

INSERT INTO `qy_replay` (`id`, `reply_member`, `to_reply_member`, `reply_content`, `add_time`, `message_id`)
VALUES
	(1,3,1,'hf','1544238736',3),
	(2,6,1,'活动呢?','1544252114',3);

/*!40000 ALTER TABLE `qy_replay` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
