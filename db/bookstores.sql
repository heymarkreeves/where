CREATE TABLE `bookstores` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `latitude` decimal(20,10) DEFAULT NULL,
  `longitude` decimal(20,10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique` (`name`,`city`,`state`,`latitude`,`longitude`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;