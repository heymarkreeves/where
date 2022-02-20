# ************************************************************
# Sequel Ace SQL dump
# Version 20025
#
# https://sequel-ace.com/
# https://github.com/Sequel-Ace/Sequel-Ace
#
# Host: localhost (MySQL 8.0.27)
# Database: wheredb
# Generation Time: 2022-02-19 23:47:47 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
SET NAMES utf8mb4;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE='NO_AUTO_VALUE_ON_ZERO', SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table cities
# ------------------------------------------------------------

DROP TABLE IF EXISTS `cities`;

CREATE TABLE `cities` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `city` varchar(100) DEFAULT NULL,
  `state` varchar(2) DEFAULT NULL,
  `outside_2021` tinyint DEFAULT NULL,
  `created_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `cities` WRITE;
/*!40000 ALTER TABLE `cities` DISABLE KEYS */;

INSERT INTO `cities` (`id`, `city`, `state`, `outside_2021`, `created_date`)
VALUES
	(1,'Atlanta','GA',1,'2022-02-19 18:44:06'),
	(2,'Charlotte','NC',1,'2022-02-19 18:44:19'),
	(3,'Saint Paul','MN',1,'2022-02-19 18:44:30'),
	(4,'Albuquerque','NM',1,'2022-02-19 18:44:45'),
	(5,'Philadelphia','PA',1,'2022-02-19 18:44:55'),
	(6,'Chicago','IL',1,'2022-02-19 18:45:03'),
	(7,'Jacksonville','FL',1,'2022-02-19 18:45:14'),
	(8,'Aurora','CO',1,'2022-02-19 18:45:22'),
	(9,'North Las Vegas','NV',1,'2022-02-19 18:45:34'),
	(10,'Norfolk','VA',1,'2022-02-19 18:45:42'),
	(11,'Tulsa','OK',1,'2022-02-19 18:45:53'),
	(12,'Sacramento','CA',1,'2022-02-19 18:45:57'),
	(13,'Austin','TX',1,'2022-02-19 18:46:04'),
	(14,'Newburgh','NY',1,'2022-02-19 18:46:13'),
	(15,'Fayetteville','WV',1,'2022-02-19 18:46:23'),
	(16,'Old Fort','NC',1,'2022-02-19 18:46:29'),
	(17,'Kalispell','MT',1,'2022-02-19 18:46:35'),
	(18,'Ely','NV',1,'2022-02-19 18:46:40'),
	(19,'Rangeley','ME',1,'2022-02-19 18:46:48'),
	(20,'Desert Hot Springs','CA',1,'2022-02-19 18:46:57');

/*!40000 ALTER TABLE `cities` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
