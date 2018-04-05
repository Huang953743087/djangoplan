# Host: localhost  (Version 5.7.21)
# Date: 2018-04-05 21:12:32
# Generator: MySQL-Front 6.0  (Build 2.20)


#
# Structure for table "auth_group"
#

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

#
# Data for table "auth_group"
#

INSERT INTO `auth_group` VALUES (1,'超级管理');

#
# Structure for table "auth_user"
#

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "auth_user"
#


#
# Structure for table "captcha_captchastore"
#

CREATE TABLE `captcha_captchastore` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `challenge` varchar(32) NOT NULL,
  `response` varchar(32) NOT NULL,
  `hashkey` varchar(40) NOT NULL,
  `expiration` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hashkey` (`hashkey`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

#
# Data for table "captcha_captchastore"
#

INSERT INTO `captcha_captchastore` VALUES (13,'GBTO','gbto','ab1b0653c293c3ece28363a2fd83de75ba63a4e9',X'323031382D30332D32302030393A35303A32372E303739373534'),(14,'TSQN','tsqn','067ba39b711b721c6cab9ade42ed31e6bd668c55',X'323031382D30332D32302030393A35303A33322E363738393230'),(15,'HVIC','hvic','38077482d2678afd3cad8dff8093982044034d98',X'323031382D30342D30322030393A34343A34302E373030303534'),(16,'DAZB','dazb','5220a6150222cffb7ce7b378d0a9b7b1684da16a',X'323031382D30342D30322030393A34353A33342E323031343736');

#
# Structure for table "django_content_type"
#

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;

#
# Data for table "django_content_type"
#

INSERT INTO `django_content_type` VALUES (1,'auth','permission'),(2,'auth','group'),(3,'contenttypes','contenttype'),(4,'users','userprofile'),(5,'admin','logentry'),(6,'sessions','session'),(7,'users','banner'),(8,'users','emailverifyrecord'),(9,'courses','course'),(10,'courses','courseresource'),(11,'courses','lesson'),(12,'courses','video'),(13,'operation','coursecomments'),(14,'operation','userask'),(15,'operation','usercourse'),(16,'operation','userfavorite'),(17,'operation','usermessage'),(18,'organization','citydict'),(19,'organization','courseorg'),(20,'organization','teacher'),(21,'xadmin','bookmark'),(22,'xadmin','usersettings'),(23,'xadmin','userwidget'),(24,'xadmin','log'),(25,'captcha','captchastore');

#
# Structure for table "auth_permission"
#

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8;

#
# Data for table "auth_permission"
#

INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add content type',3,'add_contenttype'),(8,'Can change content type',3,'change_contenttype'),(9,'Can delete content type',3,'delete_contenttype'),(10,'Can add 用户信息',4,'add_userprofile'),(11,'Can change 用户信息',4,'change_userprofile'),(12,'Can delete 用户信息',4,'delete_userprofile'),(13,'Can add log entry',5,'add_logentry'),(14,'Can change log entry',5,'change_logentry'),(15,'Can delete log entry',5,'delete_logentry'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add 轮播图',7,'add_banner'),(20,'Can change 轮播图',7,'change_banner'),(21,'Can delete 轮播图',7,'delete_banner'),(22,'Can add 邮箱验证码',8,'add_emailverfyrecord'),(23,'Can change 邮箱验证码',8,'change_emailverfyrecord'),(24,'Can delete 邮箱验证码',8,'delete_emailverfyrecord'),(25,'Can add 课程',9,'add_course'),(26,'Can change 课程',9,'change_course'),(27,'Can delete 课程',9,'delete_course'),(28,'Can add 课程资源',10,'add_courseresource'),(29,'Can change 课程资源',10,'change_courseresource'),(30,'Can delete 课程资源',10,'delete_courseresource'),(31,'Can add 章节',11,'add_lesson'),(32,'Can change 章节',11,'change_lesson'),(33,'Can delete 章节',11,'delete_lesson'),(34,'Can add 视频',12,'add_video'),(35,'Can change 视频',12,'change_video'),(36,'Can delete 视频',12,'delete_video'),(37,'Can add 课程评论',13,'add_coursecomments'),(38,'Can change 课程评论',13,'change_coursecomments'),(39,'Can delete 课程评论',13,'delete_coursecomments'),(40,'Can add 用户咨询',14,'add_userask'),(41,'Can change 用户咨询',14,'change_userask'),(42,'Can delete 用户咨询',14,'delete_userask'),(43,'Can add 用户课程',15,'add_usercourse'),(44,'Can change 用户课程',15,'change_usercourse'),(45,'Can delete 用户课程',15,'delete_usercourse'),(46,'Can add 用户收藏',16,'add_userfavorite'),(47,'Can change 用户收藏',16,'change_userfavorite'),(48,'Can delete 用户收藏',16,'delete_userfavorite'),(49,'Can add 用户消息',17,'add_usermessage'),(50,'Can change 用户消息',17,'change_usermessage'),(51,'Can delete 用户消息',17,'delete_usermessage'),(52,'Can add 城市',18,'add_citydict'),(53,'Can change 城市',18,'change_citydict'),(54,'Can delete 城市',18,'delete_citydict'),(55,'Can add 课程机构',19,'add_courseorg'),(56,'Can change 课程机构',19,'change_courseorg'),(57,'Can delete 课程机构',19,'delete_courseorg'),(58,'Can add 教师',20,'add_teacher'),(59,'Can change 教师',20,'change_teacher'),(60,'Can delete 教师',20,'delete_teacher'),(61,'Can view log entry',5,'view_logentry'),(62,'Can view group',2,'view_group'),(63,'Can view permission',1,'view_permission'),(64,'Can view content type',3,'view_contenttype'),(65,'Can view 课程',9,'view_course'),(66,'Can view 课程资源',10,'view_courseresource'),(67,'Can view 章节',11,'view_lesson'),(68,'Can view 视频',12,'view_video'),(69,'Can view 课程评论',13,'view_coursecomments'),(70,'Can view 用户咨询',14,'view_userask'),(71,'Can view 用户课程',15,'view_usercourse'),(72,'Can view 用户收藏',16,'view_userfavorite'),(73,'Can view 用户消息',17,'view_usermessage'),(74,'Can view 城市',18,'view_citydict'),(75,'Can view 课程机构',19,'view_courseorg'),(76,'Can view 教师',20,'view_teacher'),(77,'Can view session',6,'view_session'),(78,'Can view 轮播图',7,'view_banner'),(79,'Can view 邮箱验证码',8,'view_emailverfyrecord'),(80,'Can view 用户信息',4,'view_userprofile'),(81,'Can add Bookmark',21,'add_bookmark'),(82,'Can change Bookmark',21,'change_bookmark'),(83,'Can delete Bookmark',21,'delete_bookmark'),(84,'Can add User Setting',22,'add_usersettings'),(85,'Can change User Setting',22,'change_usersettings'),(86,'Can delete User Setting',22,'delete_usersettings'),(87,'Can add User Widget',23,'add_userwidget'),(88,'Can change User Widget',23,'change_userwidget'),(89,'Can delete User Widget',23,'delete_userwidget'),(90,'Can add log entry',24,'add_log'),(91,'Can change log entry',24,'change_log'),(92,'Can delete log entry',24,'delete_log'),(93,'Can view Bookmark',21,'view_bookmark'),(94,'Can view log entry',24,'view_log'),(95,'Can view User Setting',22,'view_usersettings'),(96,'Can view User Widget',23,'view_userwidget'),(97,'Can add captcha store',25,'add_captchastore'),(98,'Can change captcha store',25,'change_captchastore'),(99,'Can delete captcha store',25,'delete_captchastore'),(100,'Can view captcha store',25,'view_captchastore'),(101,'Can view 邮箱验证码',8,'view_emailverifyrecord'),(102,'Can add 邮箱验证码',8,'add_emailverifyrecord'),(103,'Can change 邮箱验证码',8,'change_emailverifyrecord'),(104,'Can delete 邮箱验证码',8,'delete_emailverifyrecord');

#
# Structure for table "auth_group_permissions"
#

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "auth_group_permissions"
#


#
# Structure for table "django_migrations"
#

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8;

#
# Data for table "django_migrations"
#

INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial',X'323031382D30332D30382030393A32353A35332E313631343233'),(2,'contenttypes','0002_remove_content_type_name',X'323031382D30332D30382030393A32353A35342E303237383438'),(3,'auth','0001_initial',X'323031382D30332D30382030393A32353A35372E323732393034'),(4,'auth','0002_alter_permission_name_max_length',X'323031382D30332D30382030393A32353A35372E383437323839'),(5,'auth','0003_alter_user_email_max_length',X'323031382D30332D30382030393A32353A35372E393235333737'),(6,'auth','0004_alter_user_username_opts',X'323031382D30332D30382030393A32353A35372E393539393138'),(7,'auth','0005_alter_user_last_login_null',X'323031382D30332D30382030393A32353A35372E393932353938'),(8,'auth','0006_require_contenttypes_0002',X'323031382D30332D30382030393A32353A35382E303233363231'),(9,'auth','0007_alter_validators_add_error_messages',X'323031382D30332D30382030393A32353A35382E303539363735'),(10,'auth','0008_alter_user_username_max_length',X'323031382D30332D30382030393A32353A35382E313033373530'),(11,'auth','0009_alter_user_last_name_max_length',X'323031382D30332D30382030393A32353A35382E313430373639'),(12,'users','0001_initial',X'323031382D30332D30382030393A32363A30322E303632363333'),(13,'admin','0001_initial',X'323031382D30332D30392030393A33373A31362E393835353532'),(14,'admin','0002_logentry_remove_auto_add',X'323031382D30332D30392030393A33373A31372E313030343133'),(15,'courses','0001_initial',X'323031382D30332D30392030393A33373A31392E383830303535'),(16,'operation','0001_initial',X'323031382D30332D30392030393A33373A32332E393936333538'),(17,'organization','0001_initial',X'323031382D30332D30392030393A33373A32352E393936363634'),(18,'sessions','0001_initial',X'323031382D30332D30392030393A33373A32362E353230373131'),(19,'users','0002_banner_emailverfyrecord',X'323031382D30332D30392030393A33373A32372E303134313735'),(20,'users','0003_auto_20180309_1751',X'323031382D30332D30392030393A35313A34332E353137313530'),(21,'xadmin','0001_initial',X'323031382D30332D31302030323A34333A33302E333534303639'),(22,'xadmin','0002_log',X'323031382D30332D31302030323A34333A33312E373739303235'),(23,'xadmin','0003_auto_20160715_0100',X'323031382D30332D31302030323A34333A33322E343838373232'),(24,'captcha','0001_initial',X'323031382D30332D31322030373A34333A32322E303332333731'),(25,'users','0004_auto_20180312_1536',X'323031382D30332D31322030373A34333A32322E323934363235'),(26,'users','0005_auto_20180312_1545',X'323031382D30332D31322030373A34353A31382E323430363332'),(27,'organization','0002_courseorg_category',X'323031382D30332D31332031303A34333A32322E363039353235'),(28,'courses','0002_course_course_org',X'323031382D30332D31342031303A30313A32302E323835343835'),(29,'organization','0003_teacher_image',X'323031382D30332D31342031313A33393A30392E303739383836'),(30,'courses','0003_course_category',X'323031382D30332D31352030373A33373A30302E313632373038'),(31,'organization','0004_auto_20180316_1234',X'323031382D30332D31362030343A33353A32302E343839373938'),(32,'courses','0004_auto_20180316_1234',X'323031382D30332D31362030343A33353A32332E343930313838'),(33,'organization','0005_auto_20180316_1235',X'323031382D30332D31362030343A33363A30372E353136333232'),(34,'users','0006_auto_20180317_2227',X'323031382D30332D31372031343A32373A35302E383733363836'),(35,'courses','0005_course_is_banner',X'323031382D30332D31392031333A30343A32332E373436303233'),(36,'organization','0006_courseorg_tag',X'323031382D30332D31392031333A30343A32342E333131333835'),(37,'courses','0006_auto_20180402_1310',X'323031382D30342D30322030353A31303A32342E333534343230');

#
# Structure for table "django_session"
#

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "django_session"
#

INSERT INTO `django_session` VALUES ('lugw7c9ju3q0019q7v22eemedeyu46av','ZGQ5NTJiODBhNjZjNmNjODkyMDI3NzZhM2M4MzBlNDczOTA3YmQzNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMudmlld3MuQ3VzdG9tQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImNkYmUyZjQxZjUyNDYzNTZhYjM4ZDEwNjcwMmJlMmUyNzNjODU2NWIiLCJMSVNUX1FVRVJZIjpbWyJjb3Vyc2VzIiwiY291cnNlIl0sIiJdfQ==',X'323031382D30342D31392031323A32373A32322E323730393435');

#
# Structure for table "operation_userask"
#

CREATE TABLE `operation_userask` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `mobile` varchar(11) NOT NULL,
  `course_name` varchar(50) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "operation_userask"
#


#
# Structure for table "operation_usermessage"
#

CREATE TABLE `operation_usermessage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` int(11) NOT NULL,
  `message` varchar(500) NOT NULL,
  `has_read` tinyint(1) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

#
# Data for table "operation_usermessage"
#

INSERT INTO `operation_usermessage` VALUES (1,0,'nihao',0,X'323031382D30342D30322030353A32323A30302E303030303030');

#
# Structure for table "organization_citydict"
#

CREATE TABLE `organization_citydict` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `desc` varchar(200) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

#
# Data for table "organization_citydict"
#

INSERT INTO `organization_citydict` VALUES (1,'上海','魔都',X'323031382D30332D31332031303A34333A30302E303030303030'),(2,'北京','帝都',X'323031382D30332D31332031303A34343A30302E303030303030'),(3,'郑州','河南省会',X'323031382D30332D31332031303A34343A30302E303030303030'),(4,'南京','金陵',X'323031382D30332D31332031303A34343A30302E303030303030'),(5,'江苏','水乡',X'323031382D30332D31332031303A34343A30302E303030303030'),(6,'杭州','下有苏杭',X'323031382D30332D31332031303A34353A30302E303030303030'),(7,'长春','我也不知道',X'323031382D30332D31332031303A34353A30302E303030303030'),(8,'长沙','橘子',X'323031382D30332D31332031303A34363A30302E303030303030'),(9,'深圳','这是一个圈',X'323031382D30332D31332031303A34373A30302E303030303030'),(10,'广州','咩咩咩',X'323031382D30332D31332031303A34373A30302E303030303030');

#
# Structure for table "organization_courseorg"
#

CREATE TABLE `organization_courseorg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `desc` longtext NOT NULL,
  `click_nums` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `address` varchar(150) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `city_id` int(11) NOT NULL,
  `category` varchar(20) NOT NULL,
  `fav_nums` int(11) NOT NULL,
  `tag` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `organization_courseo_city_id_4a842f85_fk_organizat` (`city_id`),
  CONSTRAINT `organization_courseo_city_id_4a842f85_fk_organizat` FOREIGN KEY (`city_id`) REFERENCES `organization_citydict` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

#
# Data for table "organization_courseorg"
#

INSERT INTO `organization_courseorg` VALUES (1,'1号机构','1号机构啊啊啊啊啊',0,'org/2018/03/03087bf40ad162d9db8ea11117dfa9ec8a13cd5f_-_副本.png','上海',X'323031382D30332D31332031303A34383A30302E303030303030',1,'pxjg',0,'国内名校'),(2,'机构2','二号机构啊啊啊啊啊',0,'org/2018/03/03087bf40ad162d9db8ea11117dfa9ec8a13cd5f.png','鬼知道',X'323031382D30332D31332031303A34383A30302E303030303030',2,'pxjg',0,'国内名校'),(3,'3号机构啊','好麻烦啊这个添加',0,'org/2018/03/03087bf40ad162d9db8ea11117dfa9ec8a13cd5f_LryMHyt.png','火星',X'323031382D30332D31332031303A34393A30302E303030303030',1,'pxjg',0,'国内名校'),(4,'机构不知道几','忘了机构几了，，',0,'org/2018/03/fansubThe_Gar00_40_4120130601-101045-9.PNG','月球》？',X'323031382D30332D31332031303A35303A30302E303030303030',2,'pxjg',0,'国内名校');

#
# Structure for table "organization_teacher"
#

CREATE TABLE `organization_teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `work_years` int(11) NOT NULL,
  `work_company` varchar(50) NOT NULL,
  `work_position` varchar(50) NOT NULL,
  `points` varchar(50) NOT NULL,
  `click_nums` int(11) NOT NULL,
  `fav_nums` int(11) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `org_id` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `age` int(11) NOT NULL,
  `teacher_tell` varchar(300) NOT NULL,
  `you_need_know` varchar(300) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `organization_teacher_org_id_cd000a1a_fk_organizat` (`org_id`),
  CONSTRAINT `organization_teacher_org_id_cd000a1a_fk_organizat` FOREIGN KEY (`org_id`) REFERENCES `organization_courseorg` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

#
# Data for table "organization_teacher"
#

INSERT INTO `organization_teacher` VALUES (1,'张大',0,'张大公司','大','没特点',21,0,X'323031382D30332D31342030393A34393A30302E303030303030',1,'teacher/2018/04/壁纸28.jpg',18,'按时交作业,不然叫家长','好好学习天天向上'),(2,'张二',0,'张大公司','张二','也没特地',1,0,X'323031382D30332D31342030393A35303A30302E303030303030',1,'teacher/2018/04/壁纸10.jpg',18,'按时交作业,不然叫家长','好好学习天天向上'),(3,'张三',0,'张大公司','张三','也没',1,0,X'323031382D30332D31342030393A35303A30302E303030303030',1,'teacher/2018/04/壁纸24.jpg',18,'按时交作业,不然叫家长','好好学习天天向上'),(4,'张四',0,'张大公司','张四','超快',0,0,X'323031382D30332D31342030393A35303A30302E303030303030',1,'teacher/2018/04/壁纸11_XdFEx39.jpg',18,'按时交作业,不然叫家长','好好学习天天向上'),(5,'李一',0,'李一公司','李一','累',0,0,X'323031382D30332D31342030393A35313A30302E303030303030',2,'teacher/2018/04/壁纸6_EXA5SZ4.jpg',18,'按时交作业,不然叫家长','好好学习天天向上'),(6,'李二',0,'李一公司','李二','也累',0,0,X'323031382D30332D31342030393A35323A30302E303030303030',2,'',18,'按时交作业,不然叫家长','好好学习天天向上'),(7,'李三',0,'李一公司','离散','不知道累不累',0,0,X'323031382D30332D31342030393A35323A30302E303030303030',2,'teacher/2018/04/壁纸11_Iy0yE1h.jpg',18,'按时交作业,不然叫家长','好好学习天天向上'),(8,'李四',0,'李一公司','李四','他是李四啊',0,0,X'323031382D30332D31342030393A35333A30302E303030303030',2,'teacher/2018/04/壁纸6.jpg',18,'按时交作业,不然叫家长','好好学习天天向上'),(9,'王一',0,'王一公司','王一','忙',0,0,X'323031382D30332D31342030393A35333A30302E303030303030',3,'teacher/2018/04/壁纸11_nBgwZLW.jpg',18,'按时交作业,不然叫家长','好好学习天天向上'),(10,'王二',0,'王一公司','王二','小',0,0,X'323031382D30332D31342030393A35343A30302E303030303030',3,'teacher/2018/04/壁纸2_KTTwJBI.jpg',18,'按时交作业,不然叫家长','好好学习天天向上'),(11,'王三',0,'王一公司','王三','没',0,0,X'323031382D30332D31342030393A35343A30302E303030303030',3,'teacher/2018/04/壁纸2_3msxHUs.jpg',18,'按时交作业,不然叫家长','好好学习天天向上'),(12,'王四',0,'王一公司','万事','没特点',0,0,X'323031382D30332D31342030393A35353A30302E303030303030',3,'teacher/2018/04/壁纸11.jpg',18,'按时交作业,不然叫家长','好好学习天天向上'),(13,'王五',0,'王一公司','王五','王五特点',0,0,X'323031382D30332D31342030393A35353A30302E303030303030',3,'teacher/2018/04/壁纸2_DKjg9r7.jpg',18,'按时交作业,不然叫家长','好好学习天天向上'),(14,'高一',0,'高一公司','高一','高',0,0,X'323031382D30332D31342030393A35363A30302E303030303030',4,'teacher/2018/04/壁纸4.jpg',18,'按时交作业,不然叫家长','好好学习天天向上'),(15,'高二',0,'高一公司','高二','高高',0,0,X'323031382D30332D31342030393A35363A30302E303030303030',4,'teacher/2018/04/壁纸2.jpg',18,'按时交作业,不然叫家长','好好学习天天向上');

#
# Structure for table "courses_course"
#

CREATE TABLE `courses_course` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `desc` varchar(300) NOT NULL,
  `detail` longtext NOT NULL,
  `degree` varchar(2) NOT NULL,
  `learn_times` int(11) NOT NULL,
  `students` int(11) NOT NULL,
  `fav_nums` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `click_nums` int(11) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `course_org_id` int(11) DEFAULT NULL,
  `category` varchar(20) NOT NULL,
  `tag` varchar(15) NOT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  `is_banner` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `courses_course_course_org_id_4d2c4aab_fk_organizat` (`course_org_id`),
  KEY `courses_course_teacher_id_846fa526_fk_organization_teacher_id` (`teacher_id`),
  CONSTRAINT `courses_course_course_org_id_4d2c4aab_fk_organizat` FOREIGN KEY (`course_org_id`) REFERENCES `organization_courseorg` (`id`),
  CONSTRAINT `courses_course_teacher_id_846fa526_fk_organization_teacher_id` FOREIGN KEY (`teacher_id`) REFERENCES `organization_teacher` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

#
# Data for table "courses_course"
#

INSERT INTO `courses_course` VALUES (1,'huang的第一个课程','这是一个测试课程','哪有什么详情','cj',0,4,0,'courses/2018/04/fansubThe_Gar00_04_2320130601-095400-1.PNG',10,X'323031382D30332D31302030373A30323A30302E303030303030',1,'高级','标签',7,0),(2,'傻笑','哈啊哈','为何你爱要晚到','cj',0,2,0,'courses/2018/04/fansubThe_Gar00_09_4720130601-090306-8.PNG',1,X'323031382D30332D31342031303A30323A30302E303030303030',1,'啊啊啊','啊啊啊',13,0),(3,'千里之外','屋檐如悬崖','你悄然走开','cj',0,0,0,'courses/2018/04/fansubThe_Gar00_04_5420130601-095443-2.PNG',0,X'323031382D30332D31342031303A30323A30302E303030303030',1,'啊啊啊','标签1',2,0),(4,'把结局打开','经不起谁来猜','千里之外，你无声黑白','zj',0,0,0,'courses/2018/04/fansubThe_Gar00_40_2520130601-101020-8.PNG',0,X'323031382D30332D31342031303A30343A30302E303030303030',2,'啊啊啊','啊啊啊',5,0),(5,'你是否还在','琴声何来','用一生去等待','gj',0,0,0,'courses/2018/04/fansubThe_Gar00_05_0820130601-095501-3.PNG',0,X'323031382D30332D31342031303A30343A30302E303030303030',2,'高级','啊啊啊',15,0),(6,'一生琉璃白','我迷失现在','你却不回来','gj',0,0,0,'courses/2018/04/fansubThe_Gar00_38_5720130601-100830-3.PNG',0,X'323031382D30332D31342031303A30353A30302E303030303030',2,'啊啊啊','啊啊啊',11,1),(7,'梦醒了是谁在窗台','我送你离开千里之外','沉默年代或许不该','zj',0,0,0,'courses/2018/03/fansubThe_Gar00_11_1820130601-090438-0_0F2k9Vd.PNG',0,X'323031382D30332D31342031303A30353A30302E303030303030',3,'啊啊啊','啊啊啊',2,1),(8,'用一生','你是否还在','太遥远的相爱','zj',0,0,0,'courses/2018/04/fansubThe_Gar00_04_5420130601-095443-2_ef1Sj5K.PNG',0,X'323031382D30332D31342031303A30363A30302E303030303030',3,'啊啊啊','标签',6,0),(9,'等等等','等等等等','千里之外','gj',0,0,0,'courses/2018/04/fansubThe_Gar00_12_0120130601-090520-1.PNG',0,X'323031382D30332D31342031303A30373A30302E303030303030',4,'高级','标签',5,1),(10,'嘲笑谁恃美扬威','我和你最天生一对','没了心才好相配','cj',0,0,0,'courses/2018/04/壁纸6.jpg',0,X'323031382D30332D31342031303A30373A30302E303030303030',4,'哇','标签',2,1),(11,'他们迂回误会','问世间哪有更完美','三尺红台','gj',0,0,0,'courses/2018/03/fansubThe_Gar00_12_3620130601-095927-9_eeckahB.PNG',1,X'323031382D30332D31342031303A30393A30302E303030303030',4,'高级','标签1',1,1);

#
# Structure for table "courses_courseresource"
#

CREATE TABLE `courses_courseresource` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `download` varchar(100) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `course_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `courses_courseresource_course_id_5eba1332_fk_courses_course_id` (`course_id`),
  CONSTRAINT `courses_courseresource_course_id_5eba1332_fk_courses_course_id` FOREIGN KEY (`course_id`) REFERENCES `courses_course` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "courses_courseresource"
#


#
# Structure for table "courses_lesson"
#

CREATE TABLE `courses_lesson` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `course_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `courses_lesson_course_id_16bc4882_fk_courses_course_id` (`course_id`),
  CONSTRAINT `courses_lesson_course_id_16bc4882_fk_courses_course_id` FOREIGN KEY (`course_id`) REFERENCES `courses_course` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

#
# Data for table "courses_lesson"
#

INSERT INTO `courses_lesson` VALUES (1,'第一章节',X'323031382D30332D31302030373A34313A30302E303030303030',1),(2,'你在傻笑',X'323031382D30332D31342031303A31303A30302E303030303030',2);

#
# Structure for table "courses_video"
#

CREATE TABLE `courses_video` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `lesson_id` int(11) NOT NULL,
  `learn_times` int(11) NOT NULL,
  `url` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `courses_video_lesson_id_59f2396e_fk_courses_lesson_id` (`lesson_id`),
  CONSTRAINT `courses_video_lesson_id_59f2396e_fk_courses_lesson_id` FOREIGN KEY (`lesson_id`) REFERENCES `courses_lesson` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

#
# Data for table "courses_video"
#

INSERT INTO `courses_video` VALUES (1,'你一引我懂进退，',X'323031382D30332D31342031303A31303A30302E303030303030',1,0,'http://www.ihave20sp.xyz/'),(2,'你错我不肯对，',X'323031382D30332D31342031303A31303A30302E303030303030',2,0,'http://www.ihave20sp.xyz/');

#
# Structure for table "users_banner"
#

CREATE TABLE `users_banner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `url` varchar(200) NOT NULL,
  `index` int(11) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

#
# Data for table "users_banner"
#

INSERT INTO `users_banner` VALUES (1,'第一个轮播图','banner/2018/03/fansubThe_Gar00_41_2820130601-101217-7.PNG','http://127.0.0.1:9999',100,X'323031382D30332D31302030363A30323A30302E303030303030'),(2,'2hao','banner/2018/03/fansubThe_Gar00_39_4820130601-100930-5.PNG','http://127.0.0.1:9999',2,X'323031382D30332D32302030353A32343A30302E303030303030'),(3,'3hao','banner/2018/03/fansubThe_Gar00_00_4820130601-082033-0.PNG','http://127.0.0.1:9999',3,X'323031382D30332D32302030353A32353A30302E303030303030'),(4,'4hao','banner/2018/03/fansubThe_Gar00_10_3220130601-090351-9.PNG','http://127.0.0.1:9999',4,X'323031382D30332D32302030353A32363A30302E303030303030'),(5,'5','banner/2018/03/fansubThe_Gar00_04_5420130601-095443-2.PNG','http://127.0.0.1:9999',100,X'323031382D30332D32302030353A32363A30302E303030303030');

#
# Structure for table "users_emailverifyrecord"
#

CREATE TABLE `users_emailverifyrecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `send_type` varchar(20) NOT NULL,
  `send_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

#
# Data for table "users_emailverifyrecord"
#

INSERT INTO `users_emailverifyrecord` VALUES (1,'wasdadw','953743087@qq.com','register',X'323031382D30332D31302030343A35313A30302E303030303030'),(4,'1D4nTEeqAQdHhOth','2206094398@qq.com','register',X'323031382D30332D31332030323A30323A32392E373431333738'),(5,'Gx7nCGLnFwr1qe3G','2206094398@qq.com','forget',X'323031382D30332D31332030323A31303A33322E383530373532'),(6,'9Vqd4wsA1Stvzn7r','2206094398@qq.com','forget',X'323031382D30332D31332030323A31333A32362E303335303535');

#
# Structure for table "users_userprofile"
#

CREATE TABLE `users_userprofile` (
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
  `nick_name` varchar(20) NOT NULL,
  `birthday` date DEFAULT NULL,
  `gender` varchar(6) NOT NULL,
  `address` varchar(100) NOT NULL,
  `mobile` varchar(11) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

#
# Data for table "users_userprofile"
#

INSERT INTO `users_userprofile` VALUES (1,'pbkdf2_sha256$100000$ATQcZHZxROdU$1dfr0UclFklMgbQyWukvAOd5Imsh+rDuwzd36v/qgIk=',X'323031382D30342D30322030393A34303A34332E373339333136',1,'huang','Mr.huang','','953743087@qq.com',1,1,X'323031382D30332D30392030393A35353A30302E303030303030','hao',NULL,'male','address',NULL,'image/2018/03/0.jpg'),(3,'pbkdf2_sha256$100000$DKLk6D6YZsTH$Loq2Tf6saPXwdFt2ZWGYfiMsIGvH5lIa/9HLagiOkfY=',NULL,0,'2206094398@qq.com','','','2206094398@qq.com',0,1,X'323031382D30332D31332030323A30323A32392E353439323330','',NULL,'female','',NULL,'image/default.png');

#
# Structure for table "operation_usercourse"
#

CREATE TABLE `operation_usercourse` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) NOT NULL,
  `course_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `operation_usercourse_course_id_9f1eab2e_fk_courses_course_id` (`course_id`),
  KEY `operation_usercourse_user_id_835fe81a_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `operation_usercourse_course_id_9f1eab2e_fk_courses_course_id` FOREIGN KEY (`course_id`) REFERENCES `courses_course` (`id`),
  CONSTRAINT `operation_usercourse_user_id_835fe81a_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "operation_usercourse"
#


#
# Structure for table "operation_userfavorite"
#

CREATE TABLE `operation_userfavorite` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fav_id` int(11) NOT NULL,
  `fav_type` int(11) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `operation_userfavorite_user_id_ad46a6af_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `operation_userfavorite_user_id_ad46a6af_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "operation_userfavorite"
#


#
# Structure for table "operation_coursecomments"
#

CREATE TABLE `operation_coursecomments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comments` varchar(250) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `course_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `operation_coursecomments_course_id_c88f1b6a_fk_courses_course_id` (`course_id`),
  KEY `operation_coursecomm_user_id_f5ff70b3_fk_users_use` (`user_id`),
  CONSTRAINT `operation_coursecomm_user_id_f5ff70b3_fk_users_use` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`),
  CONSTRAINT `operation_coursecomments_course_id_c88f1b6a_fk_courses_course_id` FOREIGN KEY (`course_id`) REFERENCES `courses_course` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "operation_coursecomments"
#


#
# Structure for table "django_admin_log"
#

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
  KEY `django_admin_log_user_id_c564eba6_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

#
# Data for table "django_admin_log"
#

INSERT INTO `django_admin_log` VALUES (1,X'323031382D30332D30392031303A31343A32302E393537373935','2','test',1,'[{\"added\": {}}]',4,1),(2,X'323031382D30332D30392031303A31343A34312E363539353137','2','test',3,'',4,1);

#
# Structure for table "users_userprofile_groups"
#

CREATE TABLE `users_userprofile_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_groups_userprofile_id_group_id_823cf2fc_uniq` (`userprofile_id`,`group_id`),
  KEY `users_userprofile_groups_group_id_3de53dbf_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_userprofile_gr_userprofile_id_a4496a80_fk_users_use` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`),
  CONSTRAINT `users_userprofile_groups_group_id_3de53dbf_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

#
# Data for table "users_userprofile_groups"
#

INSERT INTO `users_userprofile_groups` VALUES (1,1,1);

#
# Structure for table "users_userprofile_user_permissions"
#

CREATE TABLE `users_userprofile_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_user_p_userprofile_id_permissio_d0215190_uniq` (`userprofile_id`,`permission_id`),
  KEY `users_userprofile_us_permission_id_393136b6_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_userprofile_us_permission_id_393136b6_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_userprofile_us_userprofile_id_34544737_fk_users_use` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "users_userprofile_user_permissions"
#


#
# Structure for table "xadmin_bookmark"
#

CREATE TABLE `xadmin_bookmark` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL,
  `url_name` varchar(64) NOT NULL,
  `query` varchar(1000) NOT NULL,
  `is_share` tinyint(1) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_bookmark_content_type_id_60941679_fk_django_co` (`content_type_id`),
  KEY `xadmin_bookmark_user_id_42d307fc_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_bookmark_content_type_id_60941679_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_bookmark_user_id_42d307fc_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "xadmin_bookmark"
#


#
# Structure for table "xadmin_log"
#

CREATE TABLE `xadmin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `ip_addr` char(39) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` varchar(32) NOT NULL,
  `message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` (`content_type_id`),
  KEY `xadmin_log_user_id_bb16a176_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_log_user_id_bb16a176_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8;

#
# Data for table "xadmin_log"
#

INSERT INTO `xadmin_log` VALUES (1,X'323031382D30332D31302030343A35323A30332E363330303335','127.0.0.1','1','EmailVerfyRecord object (1)','create','已添加',8,1),(2,X'323031382D30332D31302030353A30343A34362E323936303030','127.0.0.1','2','12334(2206094398@qq.com)','create','已添加',8,1),(3,X'323031382D30332D31302030363A30333A33362E313233363737','127.0.0.1','1','Banner object (1)','create','已添加',7,1),(4,X'323031382D30332D31302030373A30333A35332E343337353034','127.0.0.1','1','Course object (1)','create','已添加',9,1),(5,X'323031382D30332D31302030373A34313A34392E343235373437','127.0.0.1','1','《《huang的第一个课程》》课程的《第一章节》章节','create','已添加',11,1),(6,X'323031382D30332D31332031303A34343A31352E383931353434','127.0.0.1','1','上海','create','已添加',18,1),(7,X'323031382D30332D31332031303A34343A32352E393831363236','127.0.0.1','2','北京','create','已添加',18,1),(8,X'323031382D30332D31332031303A34343A34312E383735363636','127.0.0.1','3','郑州','create','已添加',18,1),(9,X'323031382D30332D31332031303A34343A35312E313135333831','127.0.0.1','4','南京','create','已添加',18,1),(10,X'323031382D30332D31332031303A34353A31342E313438333639','127.0.0.1','5','江苏','create','已添加',18,1),(11,X'323031382D30332D31332031303A34353A32342E303537393738','127.0.0.1','6','杭州','create','已添加',18,1),(12,X'323031382D30332D31332031303A34363A30372E383130373434','127.0.0.1','7','长春','create','已添加',18,1),(13,X'323031382D30332D31332031303A34363A33372E373436323138','127.0.0.1','8','长沙','create','已添加',18,1),(14,X'323031382D30332D31332031303A34373A32352E333532333436','127.0.0.1','9','深圳','create','已添加',18,1),(15,X'323031382D30332D31332031303A34373A34312E383630323138','127.0.0.1','10','广州','create','已添加',18,1),(16,X'323031382D30332D31332031303A34383A35352E343832393937','127.0.0.1','1','1号机构','create','已添加',19,1),(17,X'323031382D30332D31332031303A34393A35332E343131323835','127.0.0.1','2','机构2','create','已添加',19,1),(18,X'323031382D30332D31332031303A35303A33332E393938373536','127.0.0.1','3','3号机构啊','create','已添加',19,1),(19,X'323031382D30332D31332031303A35343A35312E393530303738','127.0.0.1','4','机构不知道几','create','已添加',19,1),(20,X'323031382D30332D31342030393A35303A30342E373433313035','127.0.0.1','1','1号机构机构的张大老师','create','已添加',20,1),(21,X'323031382D30332D31342030393A35303A33342E393436383833','127.0.0.1','2','1号机构机构的张二老师','create','已添加',20,1),(22,X'323031382D30332D31342030393A35303A35352E333832393737','127.0.0.1','3','1号机构机构的张三老师','create','已添加',20,1),(23,X'323031382D30332D31342030393A35313A33332E353338383133','127.0.0.1','4','1号机构机构的张四老师','create','已添加',20,1),(24,X'323031382D30332D31342030393A35323A32322E363932303135','127.0.0.1','5','机构2机构的李一老师','create','已添加',20,1),(25,X'323031382D30332D31342030393A35323A34392E303035313431','127.0.0.1','6','机构2机构的李二老师','create','已添加',20,1),(26,X'323031382D30332D31342030393A35333A31332E373332373139','127.0.0.1','7','机构2机构的李三老师','create','已添加',20,1),(27,X'323031382D30332D31342030393A35333A34332E383031343138','127.0.0.1','8','机构2机构的李四老师','create','已添加',20,1),(28,X'323031382D30332D31342030393A35343A33302E303834373737','127.0.0.1','9','3号机构啊机构的王一老师','create','已添加',20,1),(29,X'323031382D30332D31342030393A35343A35302E393031383631','127.0.0.1','10','3号机构啊机构的王二老师','create','已添加',20,1),(30,X'323031382D30332D31342030393A35353A33322E323132343336','127.0.0.1','11','3号机构啊机构的王三老师','create','已添加',20,1),(31,X'323031382D30332D31342030393A35353A35372E343634333233','127.0.0.1','12','3号机构啊机构的王四老师','create','已添加',20,1),(32,X'323031382D30332D31342030393A35363A32332E343133343434','127.0.0.1','13','3号机构啊机构的王五老师','create','已添加',20,1),(33,X'323031382D30332D31342030393A35363A35302E343233393234','127.0.0.1','14','机构不知道几机构的高一老师','create','已添加',20,1),(34,X'323031382D30332D31342030393A35373A30332E343734313834','127.0.0.1','15','机构不知道几机构的高二老师','create','已添加',20,1),(35,X'323031382D30332D31342031303A30323A30382E393430353734','127.0.0.1','1','《huang的第一个课程》','change','修改 course_org 和 image',9,1),(36,X'323031382D30332D31342031303A30323A35382E383437333532','127.0.0.1','2','《傻笑》','create','已添加',9,1),(37,X'323031382D30332D31342031303A30343A31312E343234373835','127.0.0.1','3','《千里之外》','create','已添加',9,1),(38,X'323031382D30332D31342031303A30343A34372E373637353032','127.0.0.1','4','《把结局打开》','create','已添加',9,1),(39,X'323031382D30332D31342031303A30353A31362E373031363033','127.0.0.1','5','《你是否还在》','create','已添加',9,1),(40,X'323031382D30332D31342031303A30353A35332E383839353230','127.0.0.1','6','《一生琉璃白》','create','已添加',9,1),(41,X'323031382D30332D31342031303A30363A33342E323537303736','127.0.0.1','7','《梦醒了是谁在窗台》','create','已添加',9,1),(42,X'323031382D30332D31342031303A30373A31312E353830373335','127.0.0.1','8','《用一生》','create','已添加',9,1),(43,X'323031382D30332D31342031303A30373A34362E393333353130','127.0.0.1','9','《等等等》','create','已添加',9,1),(44,X'323031382D30332D31342031303A30393A31322E363734363335','127.0.0.1','10','《嘲笑谁恃美扬威》','create','已添加',9,1),(45,X'323031382D30332D31342031303A30393A35382E333936393534','127.0.0.1','11','《他们迂回误会》','create','已添加',9,1),(46,X'323031382D30332D31342031303A31303A31362E353330333035','127.0.0.1','2','《《傻笑》》课程的《你在傻笑》章节','create','已添加',11,1),(47,X'323031382D30332D31342031303A31303A33372E363338343134','127.0.0.1','1','《《huang的第一个课程》》课程的《第一章节》章节章，你一引我懂进退，','create','已添加',12,1),(48,X'323031382D30332D31342031303A31303A34372E323437323538','127.0.0.1','2','《《傻笑》》课程的《你在傻笑》章节章，你错我不肯对，','create','已添加',12,1),(49,X'323031382D30332D32302030353A32353A34352E323132383937','127.0.0.1','2','2hao轮播','create','已添加',7,1),(50,X'323031382D30332D32302030353A32363A30342E393937323839','127.0.0.1','3','3hao轮播','create','已添加',7,1),(51,X'323031382D30332D32302030353A32363A32302E343433373738','127.0.0.1','4','4hao轮播','create','已添加',7,1),(52,X'323031382D30332D32302030353A32363A33302E383933353331','127.0.0.1','5','5轮播','create','已添加',7,1),(53,X'323031382D30332D32302030353A33333A34312E393034363639','127.0.0.1','1','第一个轮播图轮播','change','修改 image 和 url',7,1),(54,X'323031382D30332D32302030353A33373A35342E393631353531','127.0.0.1','11','《他们迂回误会》','change','修改 teacher，is_banner，tag，image 和 category',9,1),(55,X'323031382D30332D32302030353A33383A31392E343534373832','127.0.0.1','10','《嘲笑谁恃美扬威》','change','修改 is_banner，tag，image 和 category',9,1),(56,X'323031382D30332D32302030353A33383A34392E323638323830','127.0.0.1','7','《梦醒了是谁在窗台》','change','修改 teacher，is_banner，tag，image 和 category',9,1),(57,X'323031382D30332D32302031313A31393A32382E323036313032','127.0.0.1','1','huang','change','修改 last_login，first_name，nick_name，gender，address 和 image',4,1),(58,X'323031382D30332D32302031333A30323A34342E363636393637','127.0.0.1','1','超级管理','create','已添加',2,1),(59,X'323031382D30332D32302031333A30333A31332E343131313432','127.0.0.1','1','huang','change','修改 groups 和 image',4,1),(60,X'323031382D30342D30322030353A31323A34332E383134313533','127.0.0.1','15','机构不知道几机构的高二老师','change','修改 image',20,1),(61,X'323031382D30342D30322030353A31323A35362E343032373235','127.0.0.1','14','机构不知道几机构的高一老师','change','修改 image',20,1),(62,X'323031382D30342D30322030353A31333A30372E303837383839','127.0.0.1','13','3号机构啊机构的王五老师','change','修改 image',20,1),(63,X'323031382D30342D30322030353A31343A32302E343338303033','127.0.0.1','12','3号机构啊机构的王四老师','change','修改 image',20,1),(64,X'323031382D30342D30322030353A31343A33322E353237333438','127.0.0.1','11','3号机构啊机构的王三老师','change','修改 image',20,1),(65,X'323031382D30342D30322030353A31353A34312E393830313535','127.0.0.1','10','3号机构啊机构的王二老师','change','修改 image',20,1),(66,X'323031382D30342D30322030353A31363A30322E333931393837','127.0.0.1','9','3号机构啊机构的王一老师','change','修改 image',20,1),(67,X'323031382D30342D30322030353A31363A31322E373737343137','127.0.0.1','8','机构2机构的李四老师','change','修改 image',20,1),(68,X'323031382D30342D30322030353A31363A33302E383437313838','127.0.0.1','7','机构2机构的李三老师','change','修改 image',20,1),(69,X'323031382D30342D30322030353A31363A34332E333831363437','127.0.0.1','5','机构2机构的李一老师','change','修改 image',20,1),(70,X'323031382D30342D30322030353A31363A35312E353835313535','127.0.0.1','4','1号机构机构的张四老师','change','修改 image',20,1),(71,X'323031382D30342D30322030353A31373A30352E363238363132','127.0.0.1','3','1号机构机构的张三老师','change','修改 image',20,1),(72,X'323031382D30342D30322030353A31373A31342E323432303730','127.0.0.1','2','1号机构机构的张二老师','change','修改 image',20,1),(73,X'323031382D30342D30322030353A31373A32332E333238343731','127.0.0.1','1','1号机构机构的张大老师','change','修改 image',20,1),(74,X'323031382D30342D30322030353A32323A34322E303435363530','127.0.0.1','1','0的消息','create','已添加',17,1),(75,X'323031382D30342D30322030383A30303A33382E303830303831','127.0.0.1',NULL,'','delete','批量删除 1 个 用户信息',NULL,1),(76,X'323031382D30342D30352031323A32333A35332E303138303836','127.0.0.1','10','《嘲笑谁恃美扬威》','change','修改 teacher 和 image',9,1),(77,X'323031382D30342D30352031323A32343A34342E373337303338','127.0.0.1','9','《等等等》','change','修改 teacher，is_banner，tag，image 和 category',9,1),(78,X'323031382D30342D30352031323A32353A30342E333933313732','127.0.0.1','1','《huang的第一个课程》','change','修改 teacher，tag，image 和 category',9,1),(79,X'323031382D30342D30352031323A32353A32352E323931393933','127.0.0.1','2','《傻笑》','change','修改 teacher，tag，image 和 category',9,1),(80,X'323031382D30342D30352031323A32353A34332E323138313831','127.0.0.1','3','《千里之外》','change','修改 teacher，tag，image 和 category',9,1),(81,X'323031382D30342D30352031323A32363A31312E303537373336','127.0.0.1','4','《把结局打开》','change','修改 teacher，tag，image 和 category',9,1),(82,X'323031382D30342D30352031323A32363A33322E313038383731','127.0.0.1','5','《你是否还在》','change','修改 teacher，tag，image 和 category',9,1),(83,X'323031382D30342D30352031323A32363A35382E353531373836','127.0.0.1','6','《一生琉璃白》','change','修改 teacher，is_banner，tag，image 和 category',9,1),(84,X'323031382D30342D30352031323A32373A31382E333639303533','127.0.0.1','8','《用一生》','change','修改 teacher，tag，image 和 category',9,1);

#
# Structure for table "xadmin_usersettings"
#

CREATE TABLE `xadmin_usersettings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(256) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_usersettings_user_id_edeabe4a_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_usersettings_user_id_edeabe4a_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

#
# Data for table "xadmin_usersettings"
#

INSERT INTO `xadmin_usersettings` VALUES (1,'dashboard:home:pos','',1),(2,'site-theme','/static/xadmin/css/themes/bootstrap-theme.css',1);

#
# Structure for table "xadmin_userwidget"
#

CREATE TABLE `xadmin_userwidget` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` varchar(256) NOT NULL,
  `widget_type` varchar(50) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_userwidget_user_id_c159233a_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_userwidget_user_id_c159233a_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "xadmin_userwidget"
#

