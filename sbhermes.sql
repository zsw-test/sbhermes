SET NAMES utf8mb4;

DROP TABLE IF EXISTS `goods`;

CREATE TABLE `goods` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `image` mediumtext,
  `image_md5` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `image_md5_idx` (`image_md5`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
