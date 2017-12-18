/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50720
Source Host           : localhost:3306
Source Database       : customs_edi

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2017-12-09 17:11:06
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for agreement_status
-- ----------------------------
DROP TABLE IF EXISTS `agreement_status`;
CREATE TABLE `agreement_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of agreement_status
-- ----------------------------
INSERT INTO `agreement_status` VALUES ('1', '发起');
INSERT INTO `agreement_status` VALUES ('2', '已建立委托');
INSERT INTO `agreement_status` VALUES ('4', '报关已完成');
INSERT INTO `agreement_status` VALUES ('3', '经营单位已拒绝');

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('d617c9864a99');

-- ----------------------------
-- Table structure for business_content
-- ----------------------------
DROP TABLE IF EXISTS `business_content`;
CREATE TABLE `business_content` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of business_content
-- ----------------------------
INSERT INTO `business_content` VALUES ('1', 'A、填单申报');
INSERT INTO `business_content` VALUES ('2', 'B、辅助查验');
INSERT INTO `business_content` VALUES ('3', 'C、垫付税款');
INSERT INTO `business_content` VALUES ('4', 'D、办理海关证明联');
INSERT INTO `business_content` VALUES ('5', 'E、审批手册');
INSERT INTO `business_content` VALUES ('6', 'F、核销手册');
INSERT INTO `business_content` VALUES ('7', 'G、申办减免税手册');
INSERT INTO `business_content` VALUES ('8', 'H、其他');

-- ----------------------------
-- Table structure for commodity
-- ----------------------------
DROP TABLE IF EXISTS `commodity`;
CREATE TABLE `commodity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item_code` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `hs_code` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `commodity_type` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `quantity_and_unit` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `country` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `unit_price` decimal(10,4) DEFAULT NULL,
  `total_price` decimal(10,2) DEFAULT NULL,
  `currency_id` int(11) DEFAULT NULL,
  `tax_free_mode_id` int(11) DEFAULT NULL,
  `import_declaration_id` int(11) DEFAULT NULL,
  `export_declaration_id` int(11) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `commodity_name` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `currency_id` (`currency_id`),
  KEY `export_declaration_id` (`export_declaration_id`),
  KEY `import_declaration_id` (`import_declaration_id`),
  KEY `tax_free_mode_id` (`tax_free_mode_id`),
  CONSTRAINT `commodity_ibfk_1` FOREIGN KEY (`currency_id`) REFERENCES `currency` (`id`),
  CONSTRAINT `commodity_ibfk_2` FOREIGN KEY (`export_declaration_id`) REFERENCES `export_customs_declaration` (`id`),
  CONSTRAINT `commodity_ibfk_3` FOREIGN KEY (`import_declaration_id`) REFERENCES `import_customs_declaration` (`id`),
  CONSTRAINT `commodity_ibfk_4` FOREIGN KEY (`tax_free_mode_id`) REFERENCES `tax_free_mode` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of commodity
-- ----------------------------
INSERT INTO `commodity` VALUES ('3', '1', '1112223334', '1', '1', null, '1.0000', '7680.00', '1', '1', null, null, '2017-11-16 15:10:51', '中华傲龙蟹');
INSERT INTO `commodity` VALUES ('4', '1', '4445556660', '1', '1', '荷兰', '1.0000', '1230.00', '1', '1', null, null, '2017-11-16 16:37:22', '固态硬盘');
INSERT INTO `commodity` VALUES ('5', '1', '4445556660', '1', '1', '荷兰', '1.0000', '1230.00', '1', '1', null, null, '2017-11-16 18:57:23', '固态硬盘');
INSERT INTO `commodity` VALUES ('6', '1', '4445556660', '1', '1', '荷兰', '1.0000', '1230.00', '1', '1', '4', null, '2017-11-16 19:20:18', '固态硬盘');
INSERT INTO `commodity` VALUES ('7', '1', '2223334440', '1', '1', '美国', '1.0000', '8888.00', '1', '1', '5', null, '2017-11-16 19:48:38', '牛肉');
INSERT INTO `commodity` VALUES ('8', '1', '6667778880', '1', '1', '法国', '1.0000', '348888.00', '1', '1', null, null, '2017-11-16 19:53:59', '医疗设备');
INSERT INTO `commodity` VALUES ('9', '1', '2222255555', '1', '1', '意大利', '1.0000', '4500.00', '1', '1', null, null, '2017-11-16 20:24:41', '化妆品');
INSERT INTO `commodity` VALUES ('10', '1', '1234567890', '1', '1', '美国', '1.0000', '8888.00', '1', '1', null, null, '2017-11-17 19:07:10', 'SD卡');
INSERT INTO `commodity` VALUES ('12', '1', '1234567890', '1', '1', '美国', '1.0000', '8888.00', '1', '1', null, null, '2017-11-17 23:43:57', 'SD卡');
INSERT INTO `commodity` VALUES ('13', '1', '1234567890', '1', '1', '美国', '1.0000', '8888.00', '1', '1', null, null, '2017-11-17 23:45:11', 'SD卡');
INSERT INTO `commodity` VALUES ('14', '1', '1234567890', '1', '1', '美国', '1.0000', '8888.00', '1', '1', null, null, '2017-11-17 23:47:42', 'SD卡');
INSERT INTO `commodity` VALUES ('15', '1', '9876543210', '1', '1', '美国', '1.0000', '8888.00', '1', '1', null, null, '2017-11-18 01:11:04', '测试用货物');
INSERT INTO `commodity` VALUES ('16', '1', '1112223334', '1', '1', 'None', '1.0000', '7680.00', '1', '1', null, null, '2017-11-19 18:47:31', '中华傲龙蟹');
INSERT INTO `commodity` VALUES ('17', '1', '1112223334', '1', '1', 'None', '1.0000', '7680.00', '1', '1', '3', null, '2017-11-19 18:51:51', '中华傲龙蟹');
INSERT INTO `commodity` VALUES ('18', '1', '6667778880', '1', '1', '法国', '1.0000', '348888.00', '1', '1', '6', null, '2017-11-19 18:52:05', '医疗设备');
INSERT INTO `commodity` VALUES ('19', '1', '1234567890', '1', '1', '美国', '1.0000', '8888.00', '1', '1', null, '1', '2017-11-19 18:52:12', 'SD卡');
INSERT INTO `commodity` VALUES ('20', '1', '9876543210', '1', '1', '美国', '1.0000', '8888.00', '1', '1', null, '3', '2017-11-19 18:52:17', '测试用货物');
INSERT INTO `commodity` VALUES ('21', '1', '2222255555', '1', '1', '意大利', '1.0000', '4500.00', '1', '1', '7', null, '2017-11-24 02:54:52', '化妆品');

-- ----------------------------
-- Table structure for company
-- ----------------------------
DROP TABLE IF EXISTS `company`;
CREATE TABLE `company` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uuid` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `company_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `company_address` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `customs_registration_code` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `organization_code` varchar(9) COLLATE utf8_unicode_ci NOT NULL,
  `legal_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `customs_registration_code` (`customs_registration_code`),
  UNIQUE KEY `organization_code` (`organization_code`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of company
-- ----------------------------
INSERT INTO `company` VALUES ('1', '08c89c88-60be-4349-8770-5468ef149dfb', '上海经贸淞海报关有限公司', '上海市杨树浦路147号', '1234567890', '123456789', '强生', '2017-10-25 15:30:19');
INSERT INTO `company` VALUES ('2', '6a52323a-3765-4fc5-8ee1-d80d08077b7f', '测试用有限公司', '测试用地址', '1112223334', '111222333', '用户1', '2017-10-31 00:50:20');
INSERT INTO `company` VALUES ('3', 'b096d95c-0232-4b89-8d06-841d655bc9fc', '测试用企业2', '测试用地址2', '2223334445', '222333444', '用户2', '2017-10-31 01:03:11');
INSERT INTO `company` VALUES ('4', '117eadfc-035b-457e-bcb3-c9f26fe6308e', '测试用有限公司3', '测试用地址3', '4445556667', '444555666', '用户3', '2017-10-31 01:17:48');
INSERT INTO `company` VALUES ('5', 'e0826620-6588-4fa3-9c25-a111f81a7808', '测试用4有限公司', '测试用4地址', '9998887776', '999888777', '测试用4', '2017-10-31 01:29:50');
INSERT INTO `company` VALUES ('6', 'b689b948-99c7-477a-8eea-e8ff5903c006', '测试用企业5', '测试用企业5地址', '8887776665', '888777666', '测试用户5', '2017-10-31 01:36:11');

-- ----------------------------
-- Table structure for currency
-- ----------------------------
DROP TABLE IF EXISTS `currency`;
CREATE TABLE `currency` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` int(11) DEFAULT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `e_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `exchange_rate` decimal(10,4) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of currency
-- ----------------------------
INSERT INTO `currency` VALUES ('1', '110', '港币', 'HKD', '0.8479');
INSERT INTO `currency` VALUES ('2', '113', '伊朗里亚尔', 'IRR', '0.0021');
INSERT INTO `currency` VALUES ('3', '116', '日本元', 'JPY', '0.0019');
INSERT INTO `currency` VALUES ('4', '118', '科威特第纳尔', 'KWD', '21.9642');
INSERT INTO `currency` VALUES ('5', '121', '澳门元', 'MOP', '0.8233');
INSERT INTO `currency` VALUES ('6', '122', '马来西亚林吉特', 'MYR', '1.5971');
INSERT INTO `currency` VALUES ('7', '127', '巴基斯坦卢比', 'PKR', '0.0630');
INSERT INTO `currency` VALUES ('8', '129', '菲律宾比索', 'PHP', '0.1300');
INSERT INTO `currency` VALUES ('9', '132', '新加坡元', 'SGD', '4.8837');
INSERT INTO `currency` VALUES ('10', '136', '泰国铢', 'THB', '0.2014');
INSERT INTO `currency` VALUES ('11', '142', '人民币', 'CNY', '1.0000');
INSERT INTO `currency` VALUES ('12', '143', '台币', 'TWD', '0.2199');
INSERT INTO `currency` VALUES ('13', '201', '阿尔及利亚第纳尔', 'DZD', '0.0578');
INSERT INTO `currency` VALUES ('14', '300', '欧元', 'EUR', '7.7921');
INSERT INTO `currency` VALUES ('15', '301', '比利时法郎', 'BEF', '0.1808');
INSERT INTO `currency` VALUES ('16', '302', '丹麦克朗', 'DKK', '1.0497');
INSERT INTO `currency` VALUES ('17', '303', '英镑', 'GBP', '8.7812');
INSERT INTO `currency` VALUES ('18', '304', '德国马克', 'DEM', '3.8604');
INSERT INTO `currency` VALUES ('19', '305', '法国法郎', 'FRF', '0.0039');
INSERT INTO `currency` VALUES ('20', '307', '意大利里拉', 'ITL', '0.0039');
INSERT INTO `currency` VALUES ('21', '309', '荷兰盾', 'NLG', '3.3100');
INSERT INTO `currency` VALUES ('22', '312', '西班牙比赛塔', 'ESP', '0.0500');
INSERT INTO `currency` VALUES ('23', '315', '奥地利先令', 'ATS', '0.5700');
INSERT INTO `currency` VALUES ('24', '318', '芬兰马克', 'FIM', '1.3100');
INSERT INTO `currency` VALUES ('25', '326', '挪威克朗', 'NOK', '0.8100');
INSERT INTO `currency` VALUES ('26', '330', '瑞典克朗', 'SEK', '0.7830');
INSERT INTO `currency` VALUES ('27', '331', '瑞士法郎', 'CHF', '6.6881');
INSERT INTO `currency` VALUES ('28', '332', '俄罗斯卢布', 'RUB', '0.1111');
INSERT INTO `currency` VALUES ('30', '501', '加拿大元', 'CAD', '5.1812');
INSERT INTO `currency` VALUES ('31', '502', '美元', 'USD', '6.6300');
INSERT INTO `currency` VALUES ('32', '601', '澳大利亚元', 'AUD', '5.0091');
INSERT INTO `currency` VALUES ('33', '609', '新西兰元', 'NZD', '4.5228');

-- ----------------------------
-- Table structure for customs_user
-- ----------------------------
DROP TABLE IF EXISTS `customs_user`;
CREATE TABLE `customs_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `_password` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `is_active` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of customs_user
-- ----------------------------
INSERT INTO `customs_user` VALUES ('1', 'rhj231224', 'rhj231225@gmail.com', 'pbkdf2:sha256:50000$Pthsn01R$caf1944c18c628d245b0184ab73e630eb1085ed468938efb3cdb67ae0a10fbbe', '1');

-- ----------------------------
-- Table structure for customs_user_to_role
-- ----------------------------
DROP TABLE IF EXISTS `customs_user_to_role`;
CREATE TABLE `customs_user_to_role` (
  `customs_user_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`customs_user_id`,`role_id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `customs_user_to_role_ibfk_1` FOREIGN KEY (`customs_user_id`) REFERENCES `customs_user` (`id`),
  CONSTRAINT `customs_user_to_role_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of customs_user_to_role
-- ----------------------------

-- ----------------------------
-- Table structure for customs_zone
-- ----------------------------
DROP TABLE IF EXISTS `customs_zone`;
CREATE TABLE `customs_zone` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of customs_zone
-- ----------------------------
INSERT INTO `customs_zone` VALUES ('8', '上海海关');
INSERT INTO `customs_zone` VALUES ('2', '吴淞海关');
INSERT INTO `customs_zone` VALUES ('9', '大连海关');
INSERT INTO `customs_zone` VALUES ('10', '天津海关');
INSERT INTO `customs_zone` VALUES ('4', '广州关区');
INSERT INTO `customs_zone` VALUES ('7', '浦江海关');
INSERT INTO `customs_zone` VALUES ('3', '深圳海关');
INSERT INTO `customs_zone` VALUES ('5', '香港海关');

-- ----------------------------
-- Table structure for customs_zone_reply
-- ----------------------------
DROP TABLE IF EXISTS `customs_zone_reply`;
CREATE TABLE `customs_zone_reply` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of customs_zone_reply
-- ----------------------------
INSERT INTO `customs_zone_reply` VALUES ('1', '签约入库成功', '2017-10-25 18:28:07');
INSERT INTO `customs_zone_reply` VALUES ('2', '海关解约成功', '2017-10-25 18:29:18');
INSERT INTO `customs_zone_reply` VALUES ('3', '企业解约成功', '2017-10-25 18:31:02');
INSERT INTO `customs_zone_reply` VALUES ('4', '企业不具备进出口资格', '2017-10-25 18:31:02');
INSERT INTO `customs_zone_reply` VALUES ('5', '企业信息不全，请补齐信息', '2017-10-28 22:48:35');

-- ----------------------------
-- Table structure for declaration_status
-- ----------------------------
DROP TABLE IF EXISTS `declaration_status`;
CREATE TABLE `declaration_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of declaration_status
-- ----------------------------
INSERT INTO `declaration_status` VALUES ('1', '未申报');
INSERT INTO `declaration_status` VALUES ('2', '已申报');
INSERT INTO `declaration_status` VALUES ('3', '待查验');
INSERT INTO `declaration_status` VALUES ('4', '待缴税');
INSERT INTO `declaration_status` VALUES ('5', '已退单');
INSERT INTO `declaration_status` VALUES ('6', '待提货');
INSERT INTO `declaration_status` VALUES ('7', '提货完成');

-- ----------------------------
-- Table structure for document
-- ----------------------------
DROP TABLE IF EXISTS `document`;
CREATE TABLE `document` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `url` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `document_type_id` int(11) DEFAULT NULL,
  `upload_user_id` int(11) DEFAULT NULL,
  `import_customs_declaration_id` int(11) DEFAULT NULL,
  `export_customs_declaration_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `document_type_id` (`document_type_id`),
  KEY `export_customs_declaration_id` (`export_customs_declaration_id`),
  KEY `import_customs_declaration_id` (`import_customs_declaration_id`),
  KEY `upload_user_id` (`upload_user_id`),
  CONSTRAINT `document_ibfk_1` FOREIGN KEY (`document_type_id`) REFERENCES `document_type` (`id`),
  CONSTRAINT `document_ibfk_2` FOREIGN KEY (`export_customs_declaration_id`) REFERENCES `export_customs_declaration` (`id`),
  CONSTRAINT `document_ibfk_3` FOREIGN KEY (`import_customs_declaration_id`) REFERENCES `import_customs_declaration` (`id`),
  CONSTRAINT `document_ibfk_4` FOREIGN KEY (`upload_user_id`) REFERENCES `employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of document
-- ----------------------------
INSERT INTO `document` VALUES ('9', '提货单', 'http://oz6hrswkz.bkt.clouddn.com/o_1bv1qkqo41gf11qa41ilo1jsd11t3c.jpg', '2017-11-16 15:10:51', '4', null, null, null);
INSERT INTO `document` VALUES ('10', 'bl', 'http://oz6hrswkz.bkt.clouddn.com/o_1bv1vit9t1kmct8816l2o6p1m2n7.jpg', '2017-11-16 16:37:22', '1', null, null, null);
INSERT INTO `document` VALUES ('11', 'bl', 'http://oz6hrswkz.bkt.clouddn.com/o_1bv1vit9t1kmct8816l2o6p1m2n7.jpg', '2017-11-16 18:57:23', '1', null, null, null);
INSERT INTO `document` VALUES ('12', 'bl', 'http://oz6hrswkz.bkt.clouddn.com/o_1bv1vit9t1kmct8816l2o6p1m2n7.jpg', '2017-11-16 19:20:18', '1', null, '4', null);
INSERT INTO `document` VALUES ('13', '合同', 'http://oz6hrswkz.bkt.clouddn.com/o_1bv2agvl9mnsr4e1d4if7slq7.jpg', '2017-11-16 19:48:38', '1', null, '5', null);
INSERT INTO `document` VALUES ('14', '1', 'http://oz6hrswkz.bkt.clouddn.com/o_1bv2ar3gfcgp1gcgoci1nshib37.jpg', '2017-11-16 19:53:59', '4', null, null, null);
INSERT INTO `document` VALUES ('15', '1', 'http://oz6hrswkz.bkt.clouddn.com/o_1bv2cjc327n3a6117cr13oe1lg47.jpg', '2017-11-16 20:24:41', '1', null, null, null);
INSERT INTO `document` VALUES ('16', '1', 'http://oz6hrswkz.bkt.clouddn.com/o_1bv4qhuo11pvg1n9312bv1mcg1ude7.jpg', '2017-11-17 19:07:10', '1', null, null, null);
INSERT INTO `document` VALUES ('18', '1', 'http://oz6hrswkz.bkt.clouddn.com/o_1bv4qhuo11pvg1n9312bv1mcg1ude7.jpg', '2017-11-17 23:43:57', '1', null, null, null);
INSERT INTO `document` VALUES ('19', '1', 'http://oz6hrswkz.bkt.clouddn.com/o_1bv4qhuo11pvg1n9312bv1mcg1ude7.jpg', '2017-11-17 23:45:11', '1', null, null, null);
INSERT INTO `document` VALUES ('20', '1', 'http://oz6hrswkz.bkt.clouddn.com/o_1bv4qhuo11pvg1n9312bv1mcg1ude7.jpg', '2017-11-17 23:47:42', '1', null, null, null);
INSERT INTO `document` VALUES ('21', '1', 'http://oz6hrswkz.bkt.clouddn.com/o_1bv5fcc9er5o4rv1brv107d14327.jpg', '2017-11-18 01:11:04', '1', null, null, null);
INSERT INTO `document` VALUES ('22', '提货单', 'http://oz6hrswkz.bkt.clouddn.com/o_1bv1qkqo41gf11qa41ilo1jsd11t3c.jpg', '2017-11-19 18:47:31', '1', null, null, null);
INSERT INTO `document` VALUES ('23', '提货单', 'http://oz6hrswkz.bkt.clouddn.com/o_1bv1qkqo41gf11qa41ilo1jsd11t3c.jpg', '2017-11-19 18:51:51', '1', null, '3', null);
INSERT INTO `document` VALUES ('24', '1', 'http://oz6hrswkz.bkt.clouddn.com/o_1bv2ar3gfcgp1gcgoci1nshib37.jpg', '2017-11-19 18:52:05', '1', null, '6', null);
INSERT INTO `document` VALUES ('25', '1', 'http://oz6hrswkz.bkt.clouddn.com/o_1bv4qhuo11pvg1n9312bv1mcg1ude7.jpg', '2017-11-19 18:52:12', '1', null, null, '1');
INSERT INTO `document` VALUES ('26', '1', 'http://oz6hrswkz.bkt.clouddn.com/o_1bv5fcc9er5o4rv1brv107d14327.jpg', '2017-11-19 18:52:17', '1', null, null, '3');
INSERT INTO `document` VALUES ('27', '1', 'http://oz6hrswkz.bkt.clouddn.com/o_1bv2cjc327n3a6117cr13oe1lg47.jpg', '2017-11-24 02:54:52', '1', null, '7', null);

-- ----------------------------
-- Table structure for document_type
-- ----------------------------
DROP TABLE IF EXISTS `document_type`;
CREATE TABLE `document_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of document_type
-- ----------------------------
INSERT INTO `document_type` VALUES ('1', '合同');
INSERT INTO `document_type` VALUES ('2', '发票');
INSERT INTO `document_type` VALUES ('3', '装箱清单');
INSERT INTO `document_type` VALUES ('4', '提(货)单');
INSERT INTO `document_type` VALUES ('5', '加工贸易手册');
INSERT INTO `document_type` VALUES ('6', '许可证号');

-- ----------------------------
-- Table structure for employee
-- ----------------------------
DROP TABLE IF EXISTS `employee`;
CREATE TABLE `employee` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `_password` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `create_time` datetime DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  `is_active` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of employee
-- ----------------------------
INSERT INTO `employee` VALUES ('1', 'rhj231223', 'rhj231224@gmail.com', 'pbkdf2:sha256:50000$DaLHJ2ct$5d3689a86e49621c186596fa94340cd5a5974e7eb1a5d78fd920c5af1aaf8b57', '2017-10-25 15:44:35', '1', '1');
INSERT INTO `employee` VALUES ('3', 'rhj231227', '657930342@qq.com', 'pbkdf2:sha256:50000$8vabcvEb$9c09f5f0099b6e2ace3621b8b9ff4320fd73bf28761dd6038575b2a7e583649e', '2017-11-27 07:35:36', '1', '1');

-- ----------------------------
-- Table structure for employee_to_role
-- ----------------------------
DROP TABLE IF EXISTS `employee_to_role`;
CREATE TABLE `employee_to_role` (
  `employee_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`employee_id`,`role_id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `employee_to_role_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`id`),
  CONSTRAINT `employee_to_role_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of employee_to_role
-- ----------------------------
INSERT INTO `employee_to_role` VALUES ('1', '1');
INSERT INTO `employee_to_role` VALUES ('3', '2');

-- ----------------------------
-- Table structure for export_customs_declaration
-- ----------------------------
DROP TABLE IF EXISTS `export_customs_declaration`;
CREATE TABLE `export_customs_declaration` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uuid` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `pre_entry_code` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `case_code` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `contract_code` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `customs_date` date DEFAULT NULL,
  `consignee` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `trade_type` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `license_code` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `approval_code` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `freight` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `insurance_premiums` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sundry_charges` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `packages_num` int(11) DEFAULT NULL,
  `packing_type` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `gross_weight` decimal(10,2) DEFAULT NULL,
  `net_weight` decimal(10,2) DEFAULT NULL,
  `container_code` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `marks` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `export_port` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `export_date` date DEFAULT NULL,
  `destination_country` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `destination_port` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `goods_origin_place` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `manufacturer` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `settlement_mode_id` int(11) DEFAULT NULL,
  `agreement_id` int(11) DEFAULT NULL,
  `operator_id` int(11) DEFAULT NULL,
  `status_id` int(11) DEFAULT NULL,
  `transport_mode_id` int(11) DEFAULT NULL,
  `transaction_mode_id` int(11) DEFAULT NULL,
  `tax_mode_id` int(11) DEFAULT NULL,
  `business_company_id` int(11) DEFAULT NULL,
  `customs_company_id` int(11) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `vessel_code` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `vessel_name` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `bl_code` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `declaration_code` bigint(20) DEFAULT NULL,
  `trade_mode_id` int(11) DEFAULT NULL,
  `tax_price` decimal(10,2) DEFAULT NULL,
  `refund_reason` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `check_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  UNIQUE KEY `declaration_code` (`declaration_code`),
  KEY `agreement_id` (`agreement_id`),
  KEY `operator_id` (`operator_id`),
  KEY `settlement_mode_id` (`settlement_mode_id`),
  KEY `status_id` (`status_id`),
  KEY `tax_mode_id` (`tax_mode_id`),
  KEY `transaction_mode_id` (`transaction_mode_id`),
  KEY `transport_mode_id` (`transport_mode_id`),
  KEY `business_company_id` (`business_company_id`),
  KEY `customs_company_id` (`customs_company_id`),
  KEY `trade_mode_id` (`trade_mode_id`),
  CONSTRAINT `export_customs_declaration_ibfk_1` FOREIGN KEY (`agreement_id`) REFERENCES `export_proxy_agreement` (`id`),
  CONSTRAINT `export_customs_declaration_ibfk_10` FOREIGN KEY (`trade_mode_id`) REFERENCES `trade_mode` (`id`),
  CONSTRAINT `export_customs_declaration_ibfk_2` FOREIGN KEY (`operator_id`) REFERENCES `employee` (`id`),
  CONSTRAINT `export_customs_declaration_ibfk_3` FOREIGN KEY (`settlement_mode_id`) REFERENCES `settlement_mode` (`id`),
  CONSTRAINT `export_customs_declaration_ibfk_4` FOREIGN KEY (`status_id`) REFERENCES `declaration_status` (`id`),
  CONSTRAINT `export_customs_declaration_ibfk_5` FOREIGN KEY (`tax_mode_id`) REFERENCES `tax_mode` (`id`),
  CONSTRAINT `export_customs_declaration_ibfk_6` FOREIGN KEY (`transaction_mode_id`) REFERENCES `transaction_mode` (`id`),
  CONSTRAINT `export_customs_declaration_ibfk_7` FOREIGN KEY (`transport_mode_id`) REFERENCES `transport_mode` (`id`),
  CONSTRAINT `export_customs_declaration_ibfk_8` FOREIGN KEY (`business_company_id`) REFERENCES `company` (`id`),
  CONSTRAINT `export_customs_declaration_ibfk_9` FOREIGN KEY (`customs_company_id`) REFERENCES `company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of export_customs_declaration
-- ----------------------------
INSERT INTO `export_customs_declaration` VALUES ('1', '1d08dbd4-db9f-4edb-b226-f58176333821', '123321123321', '', '1', '2017-11-17', '1', null, '', '', '', '', '', '1', '1', '1.00', '1.00', '', '', '吴淞海关', '2017-11-17', '美国', '1', '美国', '1', '2', '3', '1', '2', '3', '1', '1', '2', '1', '2017-11-17 19:07:09', '', '1', '12312378', '220520170734180001', '1', '1130.42', null, null);
INSERT INTO `export_customs_declaration` VALUES ('3', 'd18d95ae-3b97-4439-897d-2a4bef3ade0e', '999977775555', '', '1', '2017-11-18', '1', null, '', '', '', '', '', '1', '1', '1.00', '1.00', '', '', '吴淞海关', '2017-11-18', '美国', '1', '1', '1', '1', '4', '1', '5', '1', '1', '1', '2', '1', '2017-11-18 01:11:04', '', '1', '20171118', '220520170734180003', '1', '2260.84', '缺少单证', null);

-- ----------------------------
-- Table structure for export_proxy_agreement
-- ----------------------------
DROP TABLE IF EXISTS `export_proxy_agreement`;
CREATE TABLE `export_proxy_agreement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `goods_name` varchar(60) COLLATE utf8_unicode_ci NOT NULL,
  `hs_code` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `customs_price` decimal(10,2) DEFAULT NULL,
  `import_or_export_date` datetime NOT NULL,
  `telephone` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `proxy_id` int(11) DEFAULT NULL,
  `pay_mode_id` int(11) DEFAULT NULL,
  `trade_mode_id` int(11) DEFAULT NULL,
  `destination_country` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `other` text COLLATE utf8_unicode_ci,
  `bl_code` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `status_id` int(11) DEFAULT NULL,
  `uuid` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `pay_mode_id` (`pay_mode_id`),
  KEY `proxy_id` (`proxy_id`),
  KEY `trade_mode_id` (`trade_mode_id`),
  KEY `status_id` (`status_id`),
  CONSTRAINT `export_proxy_agreement_ibfk_1` FOREIGN KEY (`pay_mode_id`) REFERENCES `trade_mode` (`id`),
  CONSTRAINT `export_proxy_agreement_ibfk_2` FOREIGN KEY (`proxy_id`) REFERENCES `proxy` (`id`),
  CONSTRAINT `export_proxy_agreement_ibfk_3` FOREIGN KEY (`trade_mode_id`) REFERENCES `pay_mode` (`id`),
  CONSTRAINT `export_proxy_agreement_ibfk_4` FOREIGN KEY (`status_id`) REFERENCES `agreement_status` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of export_proxy_agreement
-- ----------------------------
INSERT INTO `export_proxy_agreement` VALUES ('3', 'SD卡', '1234567890', '8888.00', '0.00', '2017-11-10 00:00:00', null, '2', '1', '1', '美国', null, '12312378', '2', '30c842c8-1744-40a0-a870-5a9c98483785');
INSERT INTO `export_proxy_agreement` VALUES ('4', '测试用货物', '9876543210', '8888.00', '0.00', '2017-11-18 00:00:00', null, '2', '1', '1', '美国', null, '20171118', '2', '1f6a9111-5379-4b5e-a5e7-0b6c6d4a9425');

-- ----------------------------
-- Table structure for file
-- ----------------------------
DROP TABLE IF EXISTS `file`;
CREATE TABLE `file` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `document_id` int(11) DEFAULT NULL,
  `permission_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `document_id` (`document_id`),
  KEY `permission_id` (`permission_id`),
  CONSTRAINT `file_ibfk_1` FOREIGN KEY (`document_id`) REFERENCES `document` (`id`),
  CONSTRAINT `file_ibfk_2` FOREIGN KEY (`permission_id`) REFERENCES `permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of file
-- ----------------------------

-- ----------------------------
-- Table structure for front_user
-- ----------------------------
DROP TABLE IF EXISTS `front_user`;
CREATE TABLE `front_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uuid` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `username` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `_password` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `phone` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `create_time` datetime DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  `is_active` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `phone` (`phone`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `front_user_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of front_user
-- ----------------------------
INSERT INTO `front_user` VALUES ('1', '995c5561-9825-497d-bc15-5b896fb3b186', 'rhj231225', 'pbkdf2:sha256:50000$XUebrzxt$2c800d4a24a914db08bb3200ac737e677f6ddfc4798eb21bf9e22b3dce81fb18', '18221968578', '2017-10-31 00:50:20', '2', '1');
INSERT INTO `front_user` VALUES ('2', 'b7af7f63-3178-4b09-bb94-75168723f8ef', 'rhj231226', 'pbkdf2:sha256:50000$xIHZ2pIL$e91371fa17644efe87c48abaeca6f41554cc8e23547e8177892e0ca12bb09135', '13524492402', '2017-10-31 01:03:11', '3', '0');
INSERT INTO `front_user` VALUES ('3', '1f4b1dac-94b0-4f7b-b819-8e9e8adcba6d', 'rhj231227', 'pbkdf2:sha256:50000$4hs5d2z8$8efb083f3d0e303bf590835dedccc794fe5934a3b21fd976ebaf53f6f837ebaa', '44455566677', '2017-10-31 01:17:48', '4', '1');
INSERT INTO `front_user` VALUES ('4', '7a97cb64-2b38-4d86-9f9e-cde36dbabf93', 'rhj231228', 'pbkdf2:sha256:50000$BJ5kkI7b$321d2bc493306ae03f28ea425d45d189b074fe1537e12ea81f6eda742f4a06b9', '99988877766', '2017-10-31 01:29:50', '5', '1');
INSERT INTO `front_user` VALUES ('5', '3e8871f7-979b-457a-ae01-65718ffeeb3f', 'rhj231229', 'pbkdf2:sha256:50000$SzlU56Tk$42b13d90c5e99019baab598ea0a8278e5d728de62d6853990fa3ad061a19775a', '88877766655', '2017-10-31 01:36:11', '6', '1');
INSERT INTO `front_user` VALUES ('6', 'a4fb8a9f-88ea-419e-8256-8aa71c98b096', 'rhj2312221', 'pbkdf2:sha256:50000$12TAXWwb$3fc642622cee673aad74b54bb4acb2161f4d7caab643d37a661ff00b5a8e72bb', '77766655544', '2017-10-31 01:39:30', '6', '1');

-- ----------------------------
-- Table structure for handler
-- ----------------------------
DROP TABLE IF EXISTS `handler`;
CREATE TABLE `handler` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `desc` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of handler
-- ----------------------------
INSERT INTO `handler` VALUES ('1', 'customs_view', '报关功能的视图函数');
INSERT INTO `handler` VALUES ('2', 'manage_view', '管理功能的视图函数');
INSERT INTO `handler` VALUES ('3', 'customs_check_view', '海关功能的视图函数');

-- ----------------------------
-- Table structure for handler_to_permission
-- ----------------------------
DROP TABLE IF EXISTS `handler_to_permission`;
CREATE TABLE `handler_to_permission` (
  `handler_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`handler_id`,`permission_id`),
  KEY `permission_id` (`permission_id`),
  CONSTRAINT `handler_to_permission_ibfk_1` FOREIGN KEY (`handler_id`) REFERENCES `handler` (`id`),
  CONSTRAINT `handler_to_permission_ibfk_2` FOREIGN KEY (`permission_id`) REFERENCES `permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of handler_to_permission
-- ----------------------------
INSERT INTO `handler_to_permission` VALUES ('1', '1');
INSERT INTO `handler_to_permission` VALUES ('2', '2');
INSERT INTO `handler_to_permission` VALUES ('3', '3');

-- ----------------------------
-- Table structure for import_customs_declaration
-- ----------------------------
DROP TABLE IF EXISTS `import_customs_declaration`;
CREATE TABLE `import_customs_declaration` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uuid` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `pre_entry_code` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `declaration_code` bigint(100) DEFAULT NULL,
  `case_code` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `contract_code` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `customs_date` date DEFAULT NULL,
  `consignee` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `trade_type` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `license_code` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `approval_code` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `freight` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `insurance_premiums` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sundry_charges` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `packages_num` int(11) DEFAULT NULL,
  `packing_type` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `gross_weight` decimal(10,2) DEFAULT NULL,
  `net_weight` decimal(10,2) DEFAULT NULL,
  `container_code` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `marks` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `import_port` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tax_rate` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `departure_country` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `loading_port` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `domestic_destination` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `operator_id` int(11) DEFAULT NULL,
  `status_id` int(11) DEFAULT NULL,
  `transport_mode_id` int(11) DEFAULT NULL,
  `transaction_mode_id` int(11) DEFAULT NULL,
  `tax_mode_id` int(11) DEFAULT NULL,
  `use_id` int(11) DEFAULT NULL,
  `business_company_id` int(11) DEFAULT NULL,
  `customs_company_id` int(11) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `vessel_code` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `vessel_name` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `bl_code` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `import_date` date DEFAULT NULL,
  `agreement_id` int(11) DEFAULT NULL,
  `trade_mode_id` int(11) DEFAULT NULL,
  `tax_price` decimal(10,2) DEFAULT NULL,
  `refund_reason` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `check_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  UNIQUE KEY `agreement_id` (`agreement_id`),
  UNIQUE KEY `declaration_code` (`declaration_code`),
  KEY `operator_id` (`operator_id`),
  KEY `status_id` (`status_id`),
  KEY `tax_mode_id` (`tax_mode_id`),
  KEY `transaction_mode_id` (`transaction_mode_id`),
  KEY `transport_mode_id` (`transport_mode_id`),
  KEY `use_id` (`use_id`),
  KEY `customs_company_id` (`customs_company_id`),
  KEY `business_company_id` (`business_company_id`),
  KEY `trade_mode_id` (`trade_mode_id`),
  CONSTRAINT `import_customs_declaration_ibfk_10` FOREIGN KEY (`agreement_id`) REFERENCES `import_proxy_agreement` (`id`),
  CONSTRAINT `import_customs_declaration_ibfk_11` FOREIGN KEY (`trade_mode_id`) REFERENCES `trade_mode` (`id`),
  CONSTRAINT `import_customs_declaration_ibfk_2` FOREIGN KEY (`operator_id`) REFERENCES `employee` (`id`),
  CONSTRAINT `import_customs_declaration_ibfk_3` FOREIGN KEY (`status_id`) REFERENCES `declaration_status` (`id`),
  CONSTRAINT `import_customs_declaration_ibfk_4` FOREIGN KEY (`tax_mode_id`) REFERENCES `tax_mode` (`id`),
  CONSTRAINT `import_customs_declaration_ibfk_5` FOREIGN KEY (`transaction_mode_id`) REFERENCES `transaction_mode` (`id`),
  CONSTRAINT `import_customs_declaration_ibfk_6` FOREIGN KEY (`transport_mode_id`) REFERENCES `transport_mode` (`id`),
  CONSTRAINT `import_customs_declaration_ibfk_7` FOREIGN KEY (`use_id`) REFERENCES `use` (`id`),
  CONSTRAINT `import_customs_declaration_ibfk_8` FOREIGN KEY (`customs_company_id`) REFERENCES `company` (`id`),
  CONSTRAINT `import_customs_declaration_ibfk_9` FOREIGN KEY (`business_company_id`) REFERENCES `company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of import_customs_declaration
-- ----------------------------
INSERT INTO `import_customs_declaration` VALUES ('3', 'b9149421-45cd-4606-92cc-8279c6430f15', '123456781234', '220520170734180003', '', '1', '2017-11-17', '1', null, '', '', '', '', '', '1', '1', '1.00', '1.00', '', '', '吴淞海关', '', '美国', '1', '1', '1', '5', '3', '1', '1', '1', '2', '1', '2017-11-16 15:10:51', '', '1', '12345678', '2017-11-16', '15', '1', null, '单据有误!', null);
INSERT INTO `import_customs_declaration` VALUES ('4', '71df3224-9304-4d8c-8cc9-1df71f5b0fd1', '222233334455', '220520179734180004', '', '1', '2017-11-16', '1', null, '', '', '', '', '', '1', '1', '1.00', '1.00', '', '', '吴淞海关', '', '荷兰', '1', '1', '1', '6', '1', '1', '1', '1', '2', '1', '2017-11-16 16:37:22', '', '1', '12341234', '2017-11-16', '16', '1', '312.88', null, null);
INSERT INTO `import_customs_declaration` VALUES ('5', 'adb392dc-d3eb-42d4-98ff-b6098c372e87', '555566667777', '220520179734180005', '', '1', '2017-11-16', '1', null, '', '', '', '', '', '1', '1', '1.00', '1.00', '', '', '吴淞海关', '', '美国', '1', '1', '1', '1', '3', '1', '1', '1', '2', '1', '2017-11-16 19:48:38', '', '1', '44445555', '2017-11-16', '17', '1', null, null, null);
INSERT INTO `import_customs_declaration` VALUES ('6', '83975a3b-10b8-4e7e-ab7b-755003d05468', '333322221111', '220520170734180006', '', '1', '2017-11-16', '1', null, '', '', '', '', '', '1', '1', '1.00', '1.00', '', '', '吴淞海关', '', '法国', '1', '1', '1', '4', '1', '1', '1', '1', '2', '1', '2017-11-16 19:53:59', '', '1', '99998888', '2017-11-16', '18', '2', null, null, '2017-11-25');
INSERT INTO `import_customs_declaration` VALUES ('7', '100ec789-b6d2-4645-9453-2d9d9cb1aae9', '999988887777', '220520170734180007', '', '1', '2017-11-16', '1', null, '', '', '', '', '', '1', '1', '1.00', '1.00', '', '', '吴淞海关', '', '意大利', '1', '1', '1', '3', '1', '1', '1', '1', '2', '1', '2017-11-16 20:24:41', '', '', '22225555', '2017-11-16', '20', '1', null, null, '2017-11-26');

-- ----------------------------
-- Table structure for import_proxy_agreement
-- ----------------------------
DROP TABLE IF EXISTS `import_proxy_agreement`;
CREATE TABLE `import_proxy_agreement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `goods_name` varchar(60) COLLATE utf8_unicode_ci NOT NULL,
  `hs_code` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `customs_price` decimal(10,2) DEFAULT NULL,
  `import_or_export_date` datetime NOT NULL,
  `origin_country` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `telephone` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `proxy_id` int(11) DEFAULT NULL,
  `pay_mode_id` int(11) DEFAULT NULL,
  `trade_mode_id` int(11) DEFAULT NULL,
  `other` text COLLATE utf8_unicode_ci,
  `bl_code` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `status_id` int(11) DEFAULT NULL,
  `uuid` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `pay_mode_id` (`pay_mode_id`),
  KEY `proxy_id` (`proxy_id`),
  KEY `trade_mode_id` (`trade_mode_id`),
  KEY `status_id` (`status_id`),
  CONSTRAINT `import_proxy_agreement_ibfk_1` FOREIGN KEY (`pay_mode_id`) REFERENCES `trade_mode` (`id`),
  CONSTRAINT `import_proxy_agreement_ibfk_2` FOREIGN KEY (`proxy_id`) REFERENCES `proxy` (`id`),
  CONSTRAINT `import_proxy_agreement_ibfk_3` FOREIGN KEY (`trade_mode_id`) REFERENCES `pay_mode` (`id`),
  CONSTRAINT `import_proxy_agreement_ibfk_4` FOREIGN KEY (`status_id`) REFERENCES `agreement_status` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of import_proxy_agreement
-- ----------------------------
INSERT INTO `import_proxy_agreement` VALUES ('15', '中华傲龙蟹', '1112223334', '7680.00', '0.00', '2017-11-10 00:00:00', '美国', null, '2', '1', '1', null, '12345678', '2', '2ea7ae55-110c-45fa-8322-f3e827041cd3');
INSERT INTO `import_proxy_agreement` VALUES ('16', '固态硬盘', '4445556660', '1230.00', '0.00', '2017-11-12 00:00:00', '荷兰', null, '2', '1', '1', null, '12341234', '2', 'c29b13b7-c255-45bc-bf84-43bf8b054b2e');
INSERT INTO `import_proxy_agreement` VALUES ('17', '牛肉', '2223334440', '8888.00', '0.00', '2017-11-15 00:00:00', '美国', null, '2', '1', '1', null, '44445555', '2', 'e3c6db7f-afaf-4169-803d-cc07a81f3e0d');
INSERT INTO `import_proxy_agreement` VALUES ('18', '医疗设备', '6667778880', '348888.00', '0.00', '2017-11-15 00:00:00', '法国', null, '2', '1', '2', null, '99998888', '2', '6fc33fb6-5e03-4222-a42d-c553e0529615');
INSERT INTO `import_proxy_agreement` VALUES ('20', '化妆品', '2222255555', '4500.00', '0.00', '2017-11-09 00:00:00', '意大利', null, '2', '1', '1', null, '22225555', '2', 'bf404cfa-9fa6-4ac7-b2d5-438b9de66b46');
INSERT INTO `import_proxy_agreement` VALUES ('21', '巧克力', '5555444433', '4800.00', '0.00', '2017-11-24 00:00:00', '美国', null, '2', '1', '1', null, '55447788', '2', 'ccb41797-009c-4a20-857a-8b9f150de8e6');

-- ----------------------------
-- Table structure for menu
-- ----------------------------
DROP TABLE IF EXISTS `menu`;
CREATE TABLE `menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `desc` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of menu
-- ----------------------------
INSERT INTO `menu` VALUES ('1', 'customs_menu', '显示报关功能的菜单');
INSERT INTO `menu` VALUES ('2', 'customs_check_menu', '显示海关功能');
INSERT INTO `menu` VALUES ('3', 'manage_menu', '显示管理功能');
INSERT INTO `menu` VALUES ('4', 'declaration_edit_menu', '显示报关单编辑按钮');
INSERT INTO `menu` VALUES ('5', 'declaration_add_menu', '显示新增报关单按钮');

-- ----------------------------
-- Table structure for menu_to_permission
-- ----------------------------
DROP TABLE IF EXISTS `menu_to_permission`;
CREATE TABLE `menu_to_permission` (
  `menu_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`menu_id`,`permission_id`),
  KEY `permission_id` (`permission_id`),
  CONSTRAINT `menu_to_permission_ibfk_1` FOREIGN KEY (`menu_id`) REFERENCES `menu` (`id`),
  CONSTRAINT `menu_to_permission_ibfk_2` FOREIGN KEY (`permission_id`) REFERENCES `permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of menu_to_permission
-- ----------------------------
INSERT INTO `menu_to_permission` VALUES ('2', '4');
INSERT INTO `menu_to_permission` VALUES ('1', '5');
INSERT INTO `menu_to_permission` VALUES ('3', '6');
INSERT INTO `menu_to_permission` VALUES ('4', '7');
INSERT INTO `menu_to_permission` VALUES ('5', '8');

-- ----------------------------
-- Table structure for message
-- ----------------------------
DROP TABLE IF EXISTS `message`;
CREATE TABLE `message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `create_time` datetime DEFAULT NULL,
  `front_user_id` int(11) DEFAULT NULL,
  `employee_id` int(11) DEFAULT NULL,
  `customs_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `customs_user_id` (`customs_user_id`),
  KEY `employee_id` (`employee_id`),
  KEY `front_user_id` (`front_user_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`customs_user_id`) REFERENCES `customs_user` (`id`),
  CONSTRAINT `message_ibfk_2` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`id`),
  CONSTRAINT `message_ibfk_3` FOREIGN KEY (`front_user_id`) REFERENCES `front_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=223 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of message
-- ----------------------------
INSERT INTO `message` VALUES ('184', '<p>1111</p>', '2017-12-06 13:51:10', null, '1', null);
INSERT INTO `message` VALUES ('185', '<p>2222</p>', '2017-12-06 13:51:17', '1', null, null);
INSERT INTO `message` VALUES ('186', '<p>7777<br></p>', '2017-12-06 13:52:06', null, '3', null);
INSERT INTO `message` VALUES ('187', '<p>qqqq</p>', '2017-12-06 13:56:49', '1', null, null);
INSERT INTO `message` VALUES ('188', '<p>88888</p>', '2017-12-06 14:02:55', null, '1', null);
INSERT INTO `message` VALUES ('189', '<p>qwe</p>', '2017-12-06 14:03:45', null, '1', null);
INSERT INTO `message` VALUES ('190', '<p>99999<br></p>', '2017-12-06 14:11:54', null, '3', null);
INSERT INTO `message` VALUES ('191', '<p>1010</p>', '2017-12-06 14:12:01', null, '1', null);
INSERT INTO `message` VALUES ('192', '<p>ffff</p>', '2017-12-06 14:22:18', null, '1', null);
INSERT INTO `message` VALUES ('193', '<p><br>ssss</p>', '2017-12-06 14:22:40', null, '3', null);
INSERT INTO `message` VALUES ('194', '<p>mmmmmm</p>', '2017-12-06 14:22:48', null, '1', null);
INSERT INTO `message` VALUES ('195', '<p>xxxxxxxx<br></p>', '2017-12-06 14:22:57', null, '3', null);
INSERT INTO `message` VALUES ('196', '<p>oooooo</p>', '2017-12-06 14:23:05', null, '1', null);
INSERT INTO `message` VALUES ('197', '<p>77777</p>', '2017-12-06 14:26:29', null, '1', null);
INSERT INTO `message` VALUES ('198', '<p>88888</p>', '2017-12-06 14:26:37', '1', null, null);
INSERT INTO `message` VALUES ('201', '<p>服务器升级维护</p>', '2017-12-06 14:51:58', null, '1', null);
INSERT INTO `message` VALUES ('202', '<p>123</p>', '2017-12-06 18:24:26', '1', null, null);
INSERT INTO `message` VALUES ('203', '<p>456</p>', '2017-12-06 18:25:18', '1', null, null);
INSERT INTO `message` VALUES ('204', '<p>2</p>', '2017-12-06 18:48:37', '1', null, null);
INSERT INTO `message` VALUES ('205', '<p>3</p>', '2017-12-06 18:48:38', '1', null, null);
INSERT INTO `message` VALUES ('206', '<p>4</p>', '2017-12-06 18:48:40', '1', null, null);
INSERT INTO `message` VALUES ('207', '<p>11111</p>', '2017-12-06 18:49:26', '1', null, null);
INSERT INTO `message` VALUES ('208', '<p>2222</p>', '2017-12-06 18:49:28', '1', null, null);
INSERT INTO `message` VALUES ('209', '<p>11111</p>', '2017-12-06 18:57:11', '1', null, null);
INSERT INTO `message` VALUES ('210', '<p>22222</p>', '2017-12-06 18:58:09', '1', null, null);
INSERT INTO `message` VALUES ('211', '<p>3333</p>', '2017-12-06 18:59:26', '1', null, null);
INSERT INTO `message` VALUES ('212', '<p>34</p>', '2017-12-06 19:01:12', '1', null, null);
INSERT INTO `message` VALUES ('213', '<p>111111</p>', '2017-12-06 19:02:57', '1', null, null);
INSERT INTO `message` VALUES ('214', '<p>23424</p>', '2017-12-06 19:04:52', '1', null, null);
INSERT INTO `message` VALUES ('215', '<p>1</p>', '2017-12-06 19:05:33', '1', null, null);
INSERT INTO `message` VALUES ('216', '<p>2</p>', '2017-12-06 19:05:36', '1', null, null);
INSERT INTO `message` VALUES ('217', '<p><br>11111</p>', '2017-12-07 00:02:57', null, '3', null);
INSERT INTO `message` VALUES ('218', '<p>222<br></p>', '2017-12-07 00:04:44', null, '3', null);
INSERT INTO `message` VALUES ('219', '<p>33333</p>', '2017-12-07 00:06:05', null, '1', null);
INSERT INTO `message` VALUES ('220', '<p><br>11111</p>', '2017-12-07 00:06:29', null, '3', null);
INSERT INTO `message` VALUES ('221', '<p>33333<br></p>', '2017-12-07 00:06:44', null, '3', null);
INSERT INTO `message` VALUES ('222', '<p>4353453<br></p>', '2017-12-07 00:07:52', null, '3', null);

-- ----------------------------
-- Table structure for message_to_customs_user
-- ----------------------------
DROP TABLE IF EXISTS `message_to_customs_user`;
CREATE TABLE `message_to_customs_user` (
  `message_id` int(11) NOT NULL,
  `customs_user_id` int(11) NOT NULL,
  PRIMARY KEY (`message_id`,`customs_user_id`),
  KEY `customs_user_id` (`customs_user_id`),
  CONSTRAINT `message_to_customs_user_ibfk_1` FOREIGN KEY (`customs_user_id`) REFERENCES `customs_user` (`id`),
  CONSTRAINT `message_to_customs_user_ibfk_2` FOREIGN KEY (`message_id`) REFERENCES `message` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of message_to_customs_user
-- ----------------------------

-- ----------------------------
-- Table structure for message_to_employee
-- ----------------------------
DROP TABLE IF EXISTS `message_to_employee`;
CREATE TABLE `message_to_employee` (
  `message_id` int(11) NOT NULL,
  `employee_id` int(11) NOT NULL,
  PRIMARY KEY (`message_id`,`employee_id`),
  KEY `employee_id` (`employee_id`),
  CONSTRAINT `message_to_employee_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`id`),
  CONSTRAINT `message_to_employee_ibfk_2` FOREIGN KEY (`message_id`) REFERENCES `message` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of message_to_employee
-- ----------------------------
INSERT INTO `message_to_employee` VALUES ('185', '1');
INSERT INTO `message_to_employee` VALUES ('186', '1');
INSERT INTO `message_to_employee` VALUES ('187', '1');
INSERT INTO `message_to_employee` VALUES ('190', '1');
INSERT INTO `message_to_employee` VALUES ('192', '1');
INSERT INTO `message_to_employee` VALUES ('193', '1');
INSERT INTO `message_to_employee` VALUES ('194', '1');
INSERT INTO `message_to_employee` VALUES ('195', '1');
INSERT INTO `message_to_employee` VALUES ('196', '1');
INSERT INTO `message_to_employee` VALUES ('202', '1');
INSERT INTO `message_to_employee` VALUES ('203', '1');
INSERT INTO `message_to_employee` VALUES ('204', '1');
INSERT INTO `message_to_employee` VALUES ('205', '1');
INSERT INTO `message_to_employee` VALUES ('206', '1');
INSERT INTO `message_to_employee` VALUES ('207', '1');
INSERT INTO `message_to_employee` VALUES ('208', '1');
INSERT INTO `message_to_employee` VALUES ('209', '1');
INSERT INTO `message_to_employee` VALUES ('210', '1');
INSERT INTO `message_to_employee` VALUES ('211', '1');
INSERT INTO `message_to_employee` VALUES ('212', '1');
INSERT INTO `message_to_employee` VALUES ('213', '1');
INSERT INTO `message_to_employee` VALUES ('214', '1');
INSERT INTO `message_to_employee` VALUES ('215', '1');
INSERT INTO `message_to_employee` VALUES ('216', '1');
INSERT INTO `message_to_employee` VALUES ('217', '1');
INSERT INTO `message_to_employee` VALUES ('218', '1');
INSERT INTO `message_to_employee` VALUES ('220', '1');
INSERT INTO `message_to_employee` VALUES ('221', '1');
INSERT INTO `message_to_employee` VALUES ('222', '1');
INSERT INTO `message_to_employee` VALUES ('188', '3');
INSERT INTO `message_to_employee` VALUES ('191', '3');
INSERT INTO `message_to_employee` VALUES ('192', '3');
INSERT INTO `message_to_employee` VALUES ('193', '3');
INSERT INTO `message_to_employee` VALUES ('194', '3');
INSERT INTO `message_to_employee` VALUES ('195', '3');
INSERT INTO `message_to_employee` VALUES ('196', '3');
INSERT INTO `message_to_employee` VALUES ('219', '3');

-- ----------------------------
-- Table structure for message_to_front_user
-- ----------------------------
DROP TABLE IF EXISTS `message_to_front_user`;
CREATE TABLE `message_to_front_user` (
  `message_id` int(11) NOT NULL,
  `front_user_id` int(11) NOT NULL,
  PRIMARY KEY (`message_id`,`front_user_id`),
  KEY `front_user_id` (`front_user_id`),
  CONSTRAINT `message_to_front_user_ibfk_1` FOREIGN KEY (`front_user_id`) REFERENCES `front_user` (`id`),
  CONSTRAINT `message_to_front_user_ibfk_2` FOREIGN KEY (`message_id`) REFERENCES `message` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of message_to_front_user
-- ----------------------------
INSERT INTO `message_to_front_user` VALUES ('184', '1');
INSERT INTO `message_to_front_user` VALUES ('189', '1');
INSERT INTO `message_to_front_user` VALUES ('197', '1');
INSERT INTO `message_to_front_user` VALUES ('198', '1');
INSERT INTO `message_to_front_user` VALUES ('197', '2');
INSERT INTO `message_to_front_user` VALUES ('198', '2');
INSERT INTO `message_to_front_user` VALUES ('197', '3');
INSERT INTO `message_to_front_user` VALUES ('198', '3');
INSERT INTO `message_to_front_user` VALUES ('197', '4');
INSERT INTO `message_to_front_user` VALUES ('198', '4');
INSERT INTO `message_to_front_user` VALUES ('197', '5');
INSERT INTO `message_to_front_user` VALUES ('198', '5');
INSERT INTO `message_to_front_user` VALUES ('197', '6');
INSERT INTO `message_to_front_user` VALUES ('198', '6');

-- ----------------------------
-- Table structure for pay_mode
-- ----------------------------
DROP TABLE IF EXISTS `pay_mode`;
CREATE TABLE `pay_mode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of pay_mode
-- ----------------------------
INSERT INTO `pay_mode` VALUES ('1', '由委托方付款');
INSERT INTO `pay_mode` VALUES ('2', '由被委托方垫付');

-- ----------------------------
-- Table structure for permission
-- ----------------------------
DROP TABLE IF EXISTS `permission`;
CREATE TABLE `permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `desc` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `p_code` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of permission
-- ----------------------------
INSERT INTO `permission` VALUES ('1', 'customs_view', '报关功能的视图函数', 'customs_view');
INSERT INTO `permission` VALUES ('2', 'manage_view', '管理功能的视图函数', 'manage_view');
INSERT INTO `permission` VALUES ('3', 'customs_check_view', '海关功能的视图函数', 'customs_check_view');
INSERT INTO `permission` VALUES ('4', 'customs_check_menu', '海关菜单显示权限', 'customs_check_menu');
INSERT INTO `permission` VALUES ('5', 'customs_menu', '报关菜单显示权限', 'customs_menu');
INSERT INTO `permission` VALUES ('6', 'manage_menu', '管理菜单显示权限', 'manage_menu');
INSERT INTO `permission` VALUES ('7', 'declaration_edit_menu', '编辑报关单按钮显示权限', 'declaration_edit_menu');
INSERT INTO `permission` VALUES ('8', 'declaration_add_menu', '新增报关单按钮显示权限', 'declaration_add_menu');

-- ----------------------------
-- Table structure for proxy
-- ----------------------------
DROP TABLE IF EXISTS `proxy`;
CREATE TABLE `proxy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `expiry_time` datetime DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `broker_id` int(11) DEFAULT NULL,
  `client_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `broker_id` (`broker_id`),
  KEY `client_id` (`client_id`),
  CONSTRAINT `proxy_ibfk_1` FOREIGN KEY (`broker_id`) REFERENCES `company` (`id`),
  CONSTRAINT `proxy_ibfk_2` FOREIGN KEY (`client_id`) REFERENCES `company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of proxy
-- ----------------------------
INSERT INTO `proxy` VALUES ('2', '2017-11-04 02:44:54', '2018-11-04 02:44:54', '0', '1', '2');

-- ----------------------------
-- Table structure for proxy_to_business_content
-- ----------------------------
DROP TABLE IF EXISTS `proxy_to_business_content`;
CREATE TABLE `proxy_to_business_content` (
  `proxy_id` int(11) NOT NULL,
  `business_content_id` int(11) NOT NULL,
  PRIMARY KEY (`proxy_id`,`business_content_id`),
  KEY `business_content_id` (`business_content_id`),
  CONSTRAINT `proxy_to_business_content_ibfk_1` FOREIGN KEY (`business_content_id`) REFERENCES `business_content` (`id`),
  CONSTRAINT `proxy_to_business_content_ibfk_2` FOREIGN KEY (`proxy_id`) REFERENCES `proxy` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of proxy_to_business_content
-- ----------------------------
INSERT INTO `proxy_to_business_content` VALUES ('2', '1');
INSERT INTO `proxy_to_business_content` VALUES ('2', '2');
INSERT INTO `proxy_to_business_content` VALUES ('2', '3');
INSERT INTO `proxy_to_business_content` VALUES ('2', '4');

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `desc` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of role
-- ----------------------------
INSERT INTO `role` VALUES ('1', '总经理', '总经理拥有最高权限');
INSERT INTO `role` VALUES ('2', '报关员', '报关员拥有报关功能和操作报关单的权限');

-- ----------------------------
-- Table structure for role_to_permission
-- ----------------------------
DROP TABLE IF EXISTS `role_to_permission`;
CREATE TABLE `role_to_permission` (
  `role_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`role_id`,`permission_id`),
  KEY `permission_id` (`permission_id`),
  CONSTRAINT `role_to_permission_ibfk_1` FOREIGN KEY (`permission_id`) REFERENCES `permission` (`id`),
  CONSTRAINT `role_to_permission_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of role_to_permission
-- ----------------------------
INSERT INTO `role_to_permission` VALUES ('1', '1');
INSERT INTO `role_to_permission` VALUES ('2', '1');
INSERT INTO `role_to_permission` VALUES ('1', '2');
INSERT INTO `role_to_permission` VALUES ('1', '3');
INSERT INTO `role_to_permission` VALUES ('1', '4');
INSERT INTO `role_to_permission` VALUES ('1', '5');
INSERT INTO `role_to_permission` VALUES ('2', '5');
INSERT INTO `role_to_permission` VALUES ('1', '6');
INSERT INTO `role_to_permission` VALUES ('2', '7');
INSERT INTO `role_to_permission` VALUES ('2', '8');

-- ----------------------------
-- Table structure for settlement_mode
-- ----------------------------
DROP TABLE IF EXISTS `settlement_mode`;
CREATE TABLE `settlement_mode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` int(11) DEFAULT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of settlement_mode
-- ----------------------------
INSERT INTO `settlement_mode` VALUES ('1', '1', '信汇');
INSERT INTO `settlement_mode` VALUES ('2', '2', '电汇');
INSERT INTO `settlement_mode` VALUES ('3', '3', '票汇');
INSERT INTO `settlement_mode` VALUES ('4', '4', '付款交单');
INSERT INTO `settlement_mode` VALUES ('5', '5', '承兑交单');
INSERT INTO `settlement_mode` VALUES ('6', '6', '信用证');
INSERT INTO `settlement_mode` VALUES ('7', '7', '先出后结');
INSERT INTO `settlement_mode` VALUES ('8', '8', '先结后出');
INSERT INTO `settlement_mode` VALUES ('9', '9', '其他');

-- ----------------------------
-- Table structure for tax_free_mode
-- ----------------------------
DROP TABLE IF EXISTS `tax_free_mode`;
CREATE TABLE `tax_free_mode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` int(11) DEFAULT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of tax_free_mode
-- ----------------------------
INSERT INTO `tax_free_mode` VALUES ('1', '1', '照章征税');
INSERT INTO `tax_free_mode` VALUES ('2', '2', '折半征税');
INSERT INTO `tax_free_mode` VALUES ('3', '3', '全免');
INSERT INTO `tax_free_mode` VALUES ('4', '4', '特案');
INSERT INTO `tax_free_mode` VALUES ('5', '5', '随征免性');
INSERT INTO `tax_free_mode` VALUES ('6', '6', '保证金');
INSERT INTO `tax_free_mode` VALUES ('7', '7', '保函');
INSERT INTO `tax_free_mode` VALUES ('8', '8', '折半补税');
INSERT INTO `tax_free_mode` VALUES ('9', '9', '全额退税');

-- ----------------------------
-- Table structure for tax_mode
-- ----------------------------
DROP TABLE IF EXISTS `tax_mode`;
CREATE TABLE `tax_mode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` int(11) DEFAULT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `desc` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of tax_mode
-- ----------------------------
INSERT INTO `tax_mode` VALUES ('1', '101', '一般征税', '一般征税进出口货物');
INSERT INTO `tax_mode` VALUES ('2', '118', '整车征税', '构成整车特征的汽车零部件纳税');
INSERT INTO `tax_mode` VALUES ('3', '119', '零部件征税', '不构成整车特征的汽车零部件纳税');
INSERT INTO `tax_mode` VALUES ('4', '201', '无偿援助', '无偿援助进出口物资');
INSERT INTO `tax_mode` VALUES ('5', '299', '其他法定', '其他法定减免税进出口货物');
INSERT INTO `tax_mode` VALUES ('6', '301', '特定区域', '特定区域进口自用物资及出口货物');
INSERT INTO `tax_mode` VALUES ('7', '307', '保税区', '保税区进口自用物资');
INSERT INTO `tax_mode` VALUES ('8', '399', '其他地区', '其他执行特殊政策地区出口货物');
INSERT INTO `tax_mode` VALUES ('9', '401', '科教用品', '大专院校及科研机构进口科教用品');
INSERT INTO `tax_mode` VALUES ('10', '402', '示范平台用品', '　　');
INSERT INTO `tax_mode` VALUES ('11', '403', '技术改造', '企业技术改造进口货物');
INSERT INTO `tax_mode` VALUES ('12', '405', '科技开发用品', '科学研究、技术开发机构进口科研开发用品');
INSERT INTO `tax_mode` VALUES ('13', '406', '重大项目', '国家重大项目进口货物');
INSERT INTO `tax_mode` VALUES ('14', '407', '动漫用品', '动漫开发生产用品');
INSERT INTO `tax_mode` VALUES ('15', '408', '重大技术装备', '生产重大技术装备进口关键零部件及原部件');
INSERT INTO `tax_mode` VALUES ('16', '409', '科技重大专项', '科技重大专项进口关键设备、零部件和原材料');
INSERT INTO `tax_mode` VALUES ('17', '412', '基础设施', '通信、港口、铁路、公路、机场建设进口设备');
INSERT INTO `tax_mode` VALUES ('18', '413', '残疾人', '残疾人组织和企业进出口货物');
INSERT INTO `tax_mode` VALUES ('19', '417', '远洋渔业', '远洋渔业自捕水产品');
INSERT INTO `tax_mode` VALUES ('20', '418', '国产化', '国家定点生产小轿车和摄录机企业进口散件');
INSERT INTO `tax_mode` VALUES ('21', '419', '整车特征', '构成整车特征的汽车零部件进口');
INSERT INTO `tax_mode` VALUES ('22', '422', '集成电路', '集成电路生产企业进口货物');
INSERT INTO `tax_mode` VALUES ('23', '423', '新型显示器件', '新型显示器件生产企业进口物质');
INSERT INTO `tax_mode` VALUES ('24', '499', 'ITA产品', '非全税号信息技术产品');
INSERT INTO `tax_mode` VALUES ('25', '501', '加工设备', '加工贸易外商提供的不作价进口设备');
INSERT INTO `tax_mode` VALUES ('26', '502', '来料加工', '来料加工装配和补偿贸易进口料件及出口成品');
INSERT INTO `tax_mode` VALUES ('27', '503', '进料加工', '进料加工贸易进口料件及出口成品');
INSERT INTO `tax_mode` VALUES ('28', '506', '边境小额', '边境小额贸易进口货物');
INSERT INTO `tax_mode` VALUES ('29', '510', '港澳OPA', '港澳在内地加工的纺织品获证出口');
INSERT INTO `tax_mode` VALUES ('30', '601', '中外合资', '中外合资经营企业进出口货物');
INSERT INTO `tax_mode` VALUES ('31', '602', '中外合作', '中外合作经营企业进出口货物');
INSERT INTO `tax_mode` VALUES ('32', '603', '外资企业', '外商独资企业进出口货物');
INSERT INTO `tax_mode` VALUES ('33', '605', '勘探开发', '勘探开发煤层气');
INSERT INTO `tax_mode` VALUES ('34', '606', '海洋石油', '勘探、开发海洋石油进口货物');
INSERT INTO `tax_mode` VALUES ('35', '608', '陆上石油', '勘探、开发陆上石油进口货物');
INSERT INTO `tax_mode` VALUES ('36', '609', '贷款项目', '利用贷款进口货物');
INSERT INTO `tax_mode` VALUES ('37', '611', '贷款中标', '国际金融组织贷款、外国政府贷款中标机电设备零部件');
INSERT INTO `tax_mode` VALUES ('38', '789', '鼓励项目', '国家鼓励发展的内外资项目进口设备');
INSERT INTO `tax_mode` VALUES ('39', '799', '自有资金', '外商投资额度外利用自有资金进口设备、备件、配件');
INSERT INTO `tax_mode` VALUES ('40', '801', '救灾捐赠', '救灾捐赠进口物资');
INSERT INTO `tax_mode` VALUES ('41', '802', '扶贫慈善', '境外向我境内无偿捐赠用于扶贫慈善的免税进口物资');
INSERT INTO `tax_mode` VALUES ('42', '888', '航材减免', '经核准的航空公司进口维修用航空器材');
INSERT INTO `tax_mode` VALUES ('43', '898', '国批减免', '国务院特准减免税的进出口货物');
INSERT INTO `tax_mode` VALUES ('44', '998', '内部暂定', '享受内部暂定税率的进出口货物');
INSERT INTO `tax_mode` VALUES ('45', '999', '例外减免', '例外减免税进出口货物');

-- ----------------------------
-- Table structure for tax_rate
-- ----------------------------
DROP TABLE IF EXISTS `tax_rate`;
CREATE TABLE `tax_rate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hs_code` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `desc` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `export_tax_rate` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `import_tax_rate` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of tax_rate
-- ----------------------------
INSERT INTO `tax_rate` VALUES ('1', '0650000000', '箱包及鞋靴', '鞋靴：包括皮鞋、皮靴、运动鞋、其他鞋靴等。', '0.1', '0.3');
INSERT INTO `tax_rate` VALUES ('2', '0750000000', '表、钟及其配件、附件', '表：包括高档手表外其他各种表；', '0.15', '0.3');
INSERT INTO `tax_rate` VALUES ('3', '0850000000', '金银、贵重首饰及珠宝玉石', '金银：包括金、银、铂等贵金属及包贵金属，贵金属及包贵金属制的首饰（以贱金属为底的非镶嵌钻石的包贵金属首饰除外）、金银器和其他制品。', '0.15', '0.15');
INSERT INTO `tax_rate` VALUES ('4', '0880000000', '金银、贵重首饰及珠宝玉石', '钻石及钻石首饰。', '0.15', '0.3');
INSERT INTO `tax_rate` VALUES ('5', '0950000000', '化妆品、洗护用品', '洗护用品：包括清洁用品、护肤用品、护发用品和其他洗护用品。', '0.1', '0.3');
INSERT INTO `tax_rate` VALUES ('6', '0100000000', '食品、饮料', '食品：包括乳制品、糖制品、调味品，冬虫夏草、高丽参、红参、西洋参、人参、鹿茸、阿胶、奶粉及其他保健品、补品等；', '0.05', '0.15');
INSERT INTO `tax_rate` VALUES ('7', '0200000000', '酒', '包括啤酒、葡萄酒（香槟酒）、黄酒、果酒、清酒、米酒、白兰地、威士忌、伏特加、朗姆酒、金酒、白酒、药酒、保健酒、鸡尾酒、利口酒、龙舌兰、柯迪尔酒、梅子酒等用粮食、水果等含淀粉或糖的物质发酵或配制而制成的含乙醇的酒精饮料。', '0.2', '0.6');
INSERT INTO `tax_rate` VALUES ('8', '0300000000', '烟', '包括卷烟、雪茄烟、再造烟草、均化烟草、其他烟草及烟草代用品的制品，烟丝、斗烟、水烟、烟末等。', '0.2', '0.6');
INSERT INTO `tax_rate` VALUES ('9', '0400000000', '纺织品及其制成品', '衣着：包括外衣、外裤、内衣裤、衬衫/T恤衫、其他衣着等；', '0.05', '0.3');
INSERT INTO `tax_rate` VALUES ('10', '0500000000', '皮革服装及配饰', '包括各式皮革服装及皮质配饰。', '0.1', '0.3');
INSERT INTO `tax_rate` VALUES ('11', '0600000000', '箱包及鞋靴', '箱：包括各种材质的箱子；', '0.15', '0.3');
INSERT INTO `tax_rate` VALUES ('12', '0700000000', '表、钟及其配件、附件', '高档手表：完税价格在人民币10000元及以上的手表。', '0.15', '0.6');
INSERT INTO `tax_rate` VALUES ('13', '0800000000', '金银、贵重首饰及珠宝玉石', '贵重首饰及珠宝玉石（不含钻石）：包括天然或养殖珍珠、宝石或半宝石（不含钻石），用天然或养殖珍珠、宝石或半宝石（不含钻石）制成的物品，以贱金属为底的非镶嵌钻石的包贵金属首饰。', '0.2', '0.6');
INSERT INTO `tax_rate` VALUES ('14', '0900000000', '化妆品、洗护用品', '化妆品：包括芳香类化妆品、唇用化妆品、眼用化妆品、指（趾）甲化妆品、粉状化妆品和特殊功能类化妆品等。', '0.15', '0.6');
INSERT INTO `tax_rate` VALUES ('15', '1000000000', '家用医疗、保健及美容器材', '医疗器材：包括呼吸器具、矫形器具、夹板及其他骨折用具，血糖计、血糖试纸、电动洗眼器、红外线耳探热针、空气制氧机、治疗用雾化机、电动血压计、病人用拐杖、病人用轮椅等及上述物品的配件、附件；', '0.05', '0.3');
INSERT INTO `tax_rate` VALUES ('16', '1100000000', '厨卫用具及小家电', '厨房用具：包括各种材料制的餐具、刀具、炊具、灶具，锅、壶、杯、盘、碗、筷子、勺、铲、餐刀、餐叉、切菜刀、案板、削皮刀、绞肉机、食品研磨机、搅拌器、净水器、煤气灶、煤气点火器等；电饭煲、微波炉、电磁炉、抽油烟机、消毒碗柜、家用洗碗机、电烤箱、面包机、豆浆机、酸奶机、榨汁机、咖啡机、制冰机、饮水机、食品调理机、煮蛋器等厨房用具及配件、附件；', '0.05', '0.3');
INSERT INTO `tax_rate` VALUES ('17', '1150000000', '厨卫用具及小家电', '电话机等信息技术产品：包括固定电话机、手持移动电话机、可视电话机、寻呼机等。', '0.05', '0.15');
INSERT INTO `tax_rate` VALUES ('18', '1200000000', '家具', '包括各种材料制的沙发、组合式家具、柜、橱、台、桌、椅、书架、床、床垫、坐具等。', '0.05', '0.15');
INSERT INTO `tax_rate` VALUES ('19', '1300000000', '空调及其配件、附件', '包括空气调节器及其配件、附件等。', '0.05', '0.3');
INSERT INTO `tax_rate` VALUES ('20', '1400000000', '电冰箱及其配件、附件', '包括各式电冰箱、冰柜、红酒柜及其配件、附件等。', '0.07', '0.3');
INSERT INTO `tax_rate` VALUES ('21', '1500000000', '洗衣设备及其配件、附件', '包括波轮式洗衣机、滚筒式洗衣机、干衣机/烘干机、脱水机、家用地毯洗涤机等及上述物品的配件、附件。', '0.07', '0.3');
INSERT INTO `tax_rate` VALUES ('22', '1600000000', '电视机及其配件、附件', '包括各式电视机、电视收音联合机、电视收音录音联合机、电视录像联合机等及上述物品的配件、附件。', '0.1', '0.3');
INSERT INTO `tax_rate` VALUES ('23', '1700000000', '摄影（像）设备及其配件、附件', '视频摄录一体机、数字照相机、数码存储卡等信息技术产品。', '0.05', '0.15');
INSERT INTO `tax_rate` VALUES ('24', '1750000000', '摄影（像）设备及其配件、附件', '包括电视摄像机、照相机（数字照相机除外）、照相制版机、放大机，胶卷、胶片、感光纸、镜箱、闪光灯、滤色镜、测光表、曝光表、遮光罩、水下摄影罩、半身镜、接镜环、取景器、自拍器、洗像盒、显影罐等。', '0.1', '0.3');
INSERT INTO `tax_rate` VALUES ('25', '1800000000', '影音设备及其配件、附件', '包括录音笔、录音机、收音机、MP3播放机、MP4播放机、收录音机、数码录放音器、电唱机、激光电唱机、放像机、录像机、激光视盘机、（单）功能座、音箱、自动伴唱机、卡拉OK混音器等及上述物品的配件、附件。', '0.1', '0.3');
INSERT INTO `tax_rate` VALUES ('26', '1850000000', '影音设备及其配件、附件', '耳机及耳塞机，磁盘、磁带、半导体媒体以及其他影音类信息技术产品。', '0.05', '0.15');
INSERT INTO `tax_rate` VALUES ('27', '1900000000', '计算机及其外围设备', '包括个人计算机及其存储、输入、输出设备和附件、零部件。', '0.05', '0.15');
INSERT INTO `tax_rate` VALUES ('28', '2000000000', '书报、刊物及其他各类印刷品', '包括书报、刊物及其他各类印刷品。', '0.05', '0.15');
INSERT INTO `tax_rate` VALUES ('29', '2100000000', '教育用影视资料', '包括教育专用的电影片、幻灯片，原版录音带、录像带、磁盘、磁带、光学媒体、半导体媒体、唱片，地球仪、解剖模型、人体骨骼模型、教育用示意牌等。', '0.05', '0.15');
INSERT INTO `tax_rate` VALUES ('30', '2200000000', '文具用品、玩具、游戏品、节日或其他娱乐用品', '文具用品：包括各种书写用具及材料、照像簿、集邮簿、印刷日历、月历、放大镜、望远镜、绘图用颜料、装订用具、誊写钢板等各种文具用品。', '0.15', '0.3');
INSERT INTO `tax_rate` VALUES ('31', '2250000000', '文具用品、玩具、游戏品、节日或其他娱乐用品', '玩具：包括三轮车、单脚滑行车、踏板车及类似的带轮玩具；玩偶车；玩偶；缩小（按比例缩小）的模型及类似娱乐用模型；智力玩具等及上述物品的配件及附件。', '0.1', '0.15');
INSERT INTO `tax_rate` VALUES ('32', '2300000000', '邮票、艺术品、收藏品', '包括中国大陆及境外各种邮票、小型张、纪念封等，纪念币，以及艺术品、收藏品。', '0.07', '0.3');
INSERT INTO `tax_rate` VALUES ('33', '2400000000', '乐器', '包括各种键盘类、弓弦类、拨弦类、打击类、管乐类等乐器及节拍器、音叉、定音器等器具及上述乐器的配件、附件。', '0.07', '0.3');
INSERT INTO `tax_rate` VALUES ('34', '2500000000', '运动用品、钓鱼用品', '除高尔夫球以外各种球类，各种棋类、健身器具、航空和航海模型、钓鱼用品等，一般体育活动、体操、竞技、游泳、滑冰、滑雪及其他户内外活动用具及其配件、附件。', '0.15', '0.3');
INSERT INTO `tax_rate` VALUES ('35', '2550000000', '运动用品、钓鱼用品', '高尔夫球及球具：包括高尔夫球杆和高尔夫球。', '0.2', '0.6');
INSERT INTO `tax_rate` VALUES ('36', '2600000000', '自行车', '包括不带发动机、电动机的自行车、三轮脚踏车、婴孩车及其他非机动脚踏车，及上述物品的配件、附件。', '0.05', '0.3');
INSERT INTO `tax_rate` VALUES ('37', '2700000000', '其他物品', '其他不能归入上述类别的物品。', '0.1', '0.3');

-- ----------------------------
-- Table structure for trade_mode
-- ----------------------------
DROP TABLE IF EXISTS `trade_mode`;
CREATE TABLE `trade_mode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of trade_mode
-- ----------------------------
INSERT INTO `trade_mode` VALUES ('1', '110', '一般贸易');
INSERT INTO `trade_mode` VALUES ('2', '130', '易货贸易');
INSERT INTO `trade_mode` VALUES ('3', '139', '旅游购物商品');
INSERT INTO `trade_mode` VALUES ('4', '200', '料件放弃');
INSERT INTO `trade_mode` VALUES ('5', '214', '来料加工');
INSERT INTO `trade_mode` VALUES ('6', '245', '来料料件内销');
INSERT INTO `trade_mode` VALUES ('7', '255', '来料深加工');
INSERT INTO `trade_mode` VALUES ('8', '258', '来料余料结转');
INSERT INTO `trade_mode` VALUES ('9', '265', '来料料件复出');
INSERT INTO `trade_mode` VALUES ('10', '300', '来料料件退换');
INSERT INTO `trade_mode` VALUES ('11', '314', '加工专用油');
INSERT INTO `trade_mode` VALUES ('12', '320', '不作价设备');
INSERT INTO `trade_mode` VALUES ('13', '345', '来料成品减免');
INSERT INTO `trade_mode` VALUES ('14', '400', '成品放弃');
INSERT INTO `trade_mode` VALUES ('15', '420', '加工贸易设备');
INSERT INTO `trade_mode` VALUES ('16', '444', '保区进料成品');
INSERT INTO `trade_mode` VALUES ('17', '445', '保区来料成品');
INSERT INTO `trade_mode` VALUES ('18', '446', '加工设备内销');
INSERT INTO `trade_mode` VALUES ('19', '456', '加工设备结转');
INSERT INTO `trade_mode` VALUES ('20', '466', '加工设备退运');
INSERT INTO `trade_mode` VALUES ('21', '500', '减免设备结转');
INSERT INTO `trade_mode` VALUES ('22', '513', '补偿贸易');
INSERT INTO `trade_mode` VALUES ('23', '544', '保区进料料件');
INSERT INTO `trade_mode` VALUES ('24', '545', '保区来料料件');
INSERT INTO `trade_mode` VALUES ('25', '615', '进料对口');
INSERT INTO `trade_mode` VALUES ('26', '642', '进料以产顶进');
INSERT INTO `trade_mode` VALUES ('27', '644', '进料料件内销');
INSERT INTO `trade_mode` VALUES ('28', '654', '进料深加工');
INSERT INTO `trade_mode` VALUES ('29', '657', '进料余料结转');
INSERT INTO `trade_mode` VALUES ('30', '664', '进料料件复出');
INSERT INTO `trade_mode` VALUES ('31', '700', '进料料件退换');
INSERT INTO `trade_mode` VALUES ('32', '715', '进料非对口');
INSERT INTO `trade_mode` VALUES ('33', '744', '进料成品减免');
INSERT INTO `trade_mode` VALUES ('34', '815', '低值辅料');
INSERT INTO `trade_mode` VALUES ('35', '844', '进料边角料内销');
INSERT INTO `trade_mode` VALUES ('36', '845', '来料边角料内销');
INSERT INTO `trade_mode` VALUES ('37', '864', '进料边角料复出');
INSERT INTO `trade_mode` VALUES ('38', '865', '来料边角料复出');
INSERT INTO `trade_mode` VALUES ('39', '1139', '国轮油物料');
INSERT INTO `trade_mode` VALUES ('40', '1200', '保税间货物');
INSERT INTO `trade_mode` VALUES ('41', '1215', '保税工厂');
INSERT INTO `trade_mode` VALUES ('42', '1233', '保税仓库货物');
INSERT INTO `trade_mode` VALUES ('43', '1234', '保税区仓储转口');
INSERT INTO `trade_mode` VALUES ('44', '1300', '修理物品');
INSERT INTO `trade_mode` VALUES ('45', '1427', '出料加工');
INSERT INTO `trade_mode` VALUES ('46', '1500', '租赁不满一年');
INSERT INTO `trade_mode` VALUES ('47', '1523', '租赁贸易');
INSERT INTO `trade_mode` VALUES ('48', '1616', '寄售代销');
INSERT INTO `trade_mode` VALUES ('49', '1741', '免税品');
INSERT INTO `trade_mode` VALUES ('50', '1831', '外汇商品');
INSERT INTO `trade_mode` VALUES ('51', '2025', '合资合作设备');
INSERT INTO `trade_mode` VALUES ('52', '2225', '外资设备物品');
INSERT INTO `trade_mode` VALUES ('53', '2400', '外航公务货');
INSERT INTO `trade_mode` VALUES ('54', '2439', '常驻机构公用');
INSERT INTO `trade_mode` VALUES ('55', '2600', '暂时进出货物');
INSERT INTO `trade_mode` VALUES ('56', '2700', '展览品');
INSERT INTO `trade_mode` VALUES ('57', '2939', '陈列样品');
INSERT INTO `trade_mode` VALUES ('58', '3010', '货样广告品Ａ');
INSERT INTO `trade_mode` VALUES ('59', '3039', '货样广告品Ｂ');
INSERT INTO `trade_mode` VALUES ('60', '3100', '无代价抵偿');
INSERT INTO `trade_mode` VALUES ('61', '3339', '其他进出口免费');
INSERT INTO `trade_mode` VALUES ('62', '3410', '承包工程进口');
INSERT INTO `trade_mode` VALUES ('63', '3422', '对外承包出口');
INSERT INTO `trade_mode` VALUES ('64', '3511', '援助物资');
INSERT INTO `trade_mode` VALUES ('65', '3611', '无偿军援');
INSERT INTO `trade_mode` VALUES ('66', '3612', '捐赠物资');
INSERT INTO `trade_mode` VALUES ('67', '3910', '军事装备');
INSERT INTO `trade_mode` VALUES ('68', '4019', '边境小额');
INSERT INTO `trade_mode` VALUES ('69', '4039', '对台小额');
INSERT INTO `trade_mode` VALUES ('70', '4139', '对台小额商品交易');
INSERT INTO `trade_mode` VALUES ('71', '4200', '驻外机构运回');
INSERT INTO `trade_mode` VALUES ('72', '4239', '驻外机构购进');
INSERT INTO `trade_mode` VALUES ('73', '4400', '来料成品退换');
INSERT INTO `trade_mode` VALUES ('74', '4500', '直接退运');
INSERT INTO `trade_mode` VALUES ('75', '4539', '进口溢误卸');
INSERT INTO `trade_mode` VALUES ('76', '4561', '退运货物');
INSERT INTO `trade_mode` VALUES ('77', '4600', '进料成品退换');
INSERT INTO `trade_mode` VALUES ('78', '5000', '料件进出区');
INSERT INTO `trade_mode` VALUES ('79', '5010', '出口加工区研发货');
INSERT INTO `trade_mode` VALUES ('80', '5015', '区内加工货物');
INSERT INTO `trade_mode` VALUES ('81', '5033', '区内仓储货物');
INSERT INTO `trade_mode` VALUES ('82', '5100', '成品进出区');
INSERT INTO `trade_mode` VALUES ('83', '5200', '区内边角调出');
INSERT INTO `trade_mode` VALUES ('84', '5300', '设备进出区');
INSERT INTO `trade_mode` VALUES ('85', '5335', '境外设备进区');
INSERT INTO `trade_mode` VALUES ('86', '5361', '区内设备退运');
INSERT INTO `trade_mode` VALUES ('87', '6033', '物流中心进出境货');
INSERT INTO `trade_mode` VALUES ('88', '9600', '内贸货物跨境运输');
INSERT INTO `trade_mode` VALUES ('89', '9639', '海关处理货物');
INSERT INTO `trade_mode` VALUES ('90', '9700', '后续补税');
INSERT INTO `trade_mode` VALUES ('91', '9739', '其他贸易');
INSERT INTO `trade_mode` VALUES ('92', '9800', '租赁征税');
INSERT INTO `trade_mode` VALUES ('93', '9839', '留赠转卖物品');
INSERT INTO `trade_mode` VALUES ('94', '9900', '其他');

-- ----------------------------
-- Table structure for transaction_mode
-- ----------------------------
DROP TABLE IF EXISTS `transaction_mode`;
CREATE TABLE `transaction_mode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` int(11) DEFAULT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of transaction_mode
-- ----------------------------
INSERT INTO `transaction_mode` VALUES ('1', '1', 'CIF');
INSERT INTO `transaction_mode` VALUES ('2', '2', 'C&F');
INSERT INTO `transaction_mode` VALUES ('3', '3', 'FOB');
INSERT INTO `transaction_mode` VALUES ('4', '4', 'C&I');
INSERT INTO `transaction_mode` VALUES ('5', '5', '市场价');
INSERT INTO `transaction_mode` VALUES ('6', '6', '垫仓');

-- ----------------------------
-- Table structure for transport_mode
-- ----------------------------
DROP TABLE IF EXISTS `transport_mode`;
CREATE TABLE `transport_mode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sign_id` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sign_id` (`sign_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of transport_mode
-- ----------------------------
INSERT INTO `transport_mode` VALUES ('1', '0', '非保税区');
INSERT INTO `transport_mode` VALUES ('2', '1', '监管仓库');
INSERT INTO `transport_mode` VALUES ('3', '2', '江海运输');
INSERT INTO `transport_mode` VALUES ('4', '3', '铁路运输');
INSERT INTO `transport_mode` VALUES ('5', '4', '汽车运输');
INSERT INTO `transport_mode` VALUES ('6', '5', '航空运输');
INSERT INTO `transport_mode` VALUES ('7', '6', '邮件运输');
INSERT INTO `transport_mode` VALUES ('8', '7', '保税区');
INSERT INTO `transport_mode` VALUES ('9', '8', '保税仓库');
INSERT INTO `transport_mode` VALUES ('10', '9', '其它运输');
INSERT INTO `transport_mode` VALUES ('11', 'A', '全部运输');
INSERT INTO `transport_mode` VALUES ('12', 'H', '边境特殊');
INSERT INTO `transport_mode` VALUES ('13', 'W', '物流中心');
INSERT INTO `transport_mode` VALUES ('14', 'X', '物流园区');
INSERT INTO `transport_mode` VALUES ('15', 'Y', '保税港区');
INSERT INTO `transport_mode` VALUES ('16', 'Z', '出口加工');

-- ----------------------------
-- Table structure for triple_agreement
-- ----------------------------
DROP TABLE IF EXISTS `triple_agreement`;
CREATE TABLE `triple_agreement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `zone_id` int(11) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  `status_id` int(11) DEFAULT NULL,
  `reply_id` int(11) DEFAULT NULL,
  `cancel_time` datetime DEFAULT NULL,
  `sign_time` datetime DEFAULT NULL,
  `cancel_name` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sign_name` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_id` (`company_id`),
  KEY `reply_id` (`reply_id`),
  KEY `status_id` (`status_id`),
  KEY `zone_id` (`zone_id`),
  CONSTRAINT `triple_agreement_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `company` (`id`),
  CONSTRAINT `triple_agreement_ibfk_2` FOREIGN KEY (`reply_id`) REFERENCES `customs_zone_reply` (`id`),
  CONSTRAINT `triple_agreement_ibfk_3` FOREIGN KEY (`status_id`) REFERENCES `triple_status` (`id`),
  CONSTRAINT `triple_agreement_ibfk_4` FOREIGN KEY (`zone_id`) REFERENCES `customs_zone` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of triple_agreement
-- ----------------------------
INSERT INTO `triple_agreement` VALUES ('1', '2', '1', '1', '1', null, '2017-10-26 17:51:54', null, '强生');
INSERT INTO `triple_agreement` VALUES ('2', '3', '1', '2', null, null, '2017-10-26 17:51:54', null, null);
INSERT INTO `triple_agreement` VALUES ('3', '4', '1', '2', null, '2017-10-27 20:18:30', '2017-10-26 17:51:54', '强生', '强生');
INSERT INTO `triple_agreement` VALUES ('4', '5', '1', '2', null, null, '2017-10-26 17:59:33', null, null);
INSERT INTO `triple_agreement` VALUES ('5', '7', '1', '2', null, null, '2017-10-26 17:59:34', null, null);
INSERT INTO `triple_agreement` VALUES ('6', '2', '2', '1', '1', null, '2017-11-15 15:46:50', null, '用户1');
INSERT INTO `triple_agreement` VALUES ('7', '3', '2', '3', '3', '2017-11-15 16:10:18', '2017-11-15 16:07:20', '用户1', '用户1');
INSERT INTO `triple_agreement` VALUES ('8', '4', '2', '2', null, null, '2017-11-15 16:07:47', null, null);

-- ----------------------------
-- Table structure for triple_status
-- ----------------------------
DROP TABLE IF EXISTS `triple_status`;
CREATE TABLE `triple_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of triple_status
-- ----------------------------
INSERT INTO `triple_status` VALUES ('1', '签约成功');
INSERT INTO `triple_status` VALUES ('2', '海关审批中');
INSERT INTO `triple_status` VALUES ('3', '已解约');
INSERT INTO `triple_status` VALUES ('4', '审批未通过');

-- ----------------------------
-- Table structure for use
-- ----------------------------
DROP TABLE IF EXISTS `use`;
CREATE TABLE `use` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` int(11) DEFAULT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of use
-- ----------------------------
INSERT INTO `use` VALUES ('1', '1', '外贸自营内销');
INSERT INTO `use` VALUES ('2', '2', '特区内销');
INSERT INTO `use` VALUES ('3', '3', '其它内销');
INSERT INTO `use` VALUES ('4', '4', '企业自用');
INSERT INTO `use` VALUES ('5', '5', '加工返销');
INSERT INTO `use` VALUES ('6', '6', '借用');
INSERT INTO `use` VALUES ('7', '7', '收保证金');
INSERT INTO `use` VALUES ('8', '8', '免费提供');
INSERT INTO `use` VALUES ('9', '9', '作价提供');
INSERT INTO `use` VALUES ('10', '10', '货样,广告品');
INSERT INTO `use` VALUES ('11', '11', '其它');
INSERT INTO `use` VALUES ('12', '13', '以产顶进');
