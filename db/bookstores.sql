CREATE TABLE `bookstores` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `latitude` float DEFAULT NULL,
  `longitude` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique` (`name`,`city`,`state`,`latitude`,`longitude`)
) ENGINE=InnoDB AUTO_INCREMENT=5861 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;