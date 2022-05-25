/*
 Navicat Premium Data Transfer

 Source Server         : 本地
 Source Server Type    : MySQL
 Source Server Version : 50726
 Source Host           : localhost:3306
 Source Schema         : face

 Target Server Type    : MySQL
 Target Server Version : 50726
 File Encoding         : 65001

 Date: 25/05/2022 19:22:34
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for sys_coka
-- ----------------------------
DROP TABLE IF EXISTS `sys_coka`;
CREATE TABLE `sys_coka`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data` json NULL,
  `time` datetime NULL DEFAULT NULL,
  `turn` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 9 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_coka
-- ----------------------------
INSERT INTO `sys_coka` VALUES (1, '{\"total\": 1, \"turn1\": {\"signed\": 1, \"unsigned\": 0, \"signed_students\": {\"py/set\": [\"庞宇宇\"]}, \"unsigned_students\": {\"py/set\": []}}, \"turn2\": {\"signed\": 1, \"unsigned\": 0, \"signed_students\": {\"py/set\": [\"庞宇宇\"]}, \"unsigned_students\": {\"py/set\": []}}, \"all_students\": {\"py/set\": [\"庞宇宇\"]}, \"might_students\": {\"py/set\": []}, \"confirm_students\": {\"py/set\": [\"庞宇宇\"]}, \"unsigned_students\": {\"py/set\": []}}', '2022-05-25 13:09:33', 1);
INSERT INTO `sys_coka` VALUES (2, '{\"total\": 1, \"turn1\": {\"signed\": 1, \"unsigned\": 0, \"signed_students\": {\"py/set\": [\"庞宇宇\"]}, \"unsigned_students\": {\"py/set\": []}}, \"turn2\": {\"signed\": 1, \"unsigned\": 0, \"signed_students\": {\"py/set\": [\"庞宇宇\"]}, \"unsigned_students\": {\"py/set\": []}}, \"all_students\": {\"py/set\": [\"庞宇宇\"]}, \"might_students\": {\"py/set\": []}, \"confirm_students\": {\"py/set\": [\"庞宇宇\"]}, \"unsigned_students\": {\"py/set\": []}}', '2022-05-25 13:09:33', 2);
INSERT INTO `sys_coka` VALUES (3, '{\"total\": 1, \"turn1\": {\"signed\": 1, \"unsigned\": 0, \"signed_students\": {\"py/set\": [\"庞宇宇\"]}, \"unsigned_students\": {\"py/set\": []}}, \"turn2\": {\"signed\": 1, \"unsigned\": 0, \"signed_students\": {\"py/set\": [\"庞宇宇\"]}, \"unsigned_students\": {\"py/set\": []}}, \"all_students\": {\"py/set\": [\"庞宇宇\"]}, \"might_students\": {\"py/set\": []}, \"confirm_students\": {\"py/set\": [\"庞宇宇\"]}, \"unsigned_students\": {\"py/set\": []}}', '2022-05-25 13:09:33', 3);
INSERT INTO `sys_coka` VALUES (4, '{\"total\": 1, \"turn1\": {\"signed\": 1, \"unsigned\": 0, \"signed_students\": {\"py/set\": [\"庞宇宇\"]}, \"unsigned_students\": {\"py/set\": []}}, \"turn2\": {\"signed\": 1, \"unsigned\": 0, \"signed_students\": {\"py/set\": [\"庞宇宇\"]}, \"unsigned_students\": {\"py/set\": []}}, \"all_students\": {\"py/set\": [\"庞宇宇\"]}, \"might_students\": {\"py/set\": []}, \"confirm_students\": {\"py/set\": [\"庞宇宇\"]}, \"unsigned_students\": {\"py/set\": []}}', '2022-05-25 13:13:46', 4);
INSERT INTO `sys_coka` VALUES (5, '{\"total\": 1, \"turn1\": {\"signed\": 1, \"unsigned\": 0, \"signed_students\": {\"py/set\": [\"庞宇宇\"]}, \"unsigned_students\": {\"py/set\": []}}, \"turn2\": {\"signed\": 1, \"unsigned\": 0, \"signed_students\": {\"py/set\": [\"庞宇宇\"]}, \"unsigned_students\": {\"py/set\": []}}, \"all_students\": {\"py/set\": [\"庞宇宇\"]}, \"might_students\": {\"py/set\": []}, \"confirm_students\": {\"py/set\": [\"庞宇宇\"]}, \"unsigned_students\": {\"py/set\": []}}', '2022-05-25 13:18:34', 5);
INSERT INTO `sys_coka` VALUES (6, '{\"total\": 1, \"turn1\": {\"signed\": 1, \"unsigned\": 0, \"signed_students\": {\"py/set\": [\"庞宇宇\"]}, \"unsigned_students\": {\"py/set\": []}}, \"turn2\": {\"signed\": 1, \"unsigned\": 0, \"signed_students\": {\"py/set\": [\"庞宇宇\"]}, \"unsigned_students\": {\"py/set\": []}}, \"all_students\": {\"py/set\": [\"庞宇宇\"]}, \"might_students\": {\"py/set\": []}, \"confirm_students\": {\"py/set\": [\"庞宇宇\"]}, \"unsigned_students\": {\"py/set\": []}}', '2022-05-25 13:19:27', 6);

-- ----------------------------
-- Table structure for sys_user
-- ----------------------------
DROP TABLE IF EXISTS `sys_user`;
CREATE TABLE `sys_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sno` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `sname` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `college` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_user
-- ----------------------------
INSERT INTO `sys_user` VALUES (5, '庞宇宇', '2018061136', '数信学院');

SET FOREIGN_KEY_CHECKS = 1;
