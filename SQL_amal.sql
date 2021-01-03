-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: amal_alghad
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill` (
  `ID` int unsigned NOT NULL AUTO_INCREMENT,
  `Deliver_ID` int DEFAULT NULL,
  `Recipient_ID` int DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Notes` text COLLATE utf8_bin,
  `Type` varchar(1) COLLATE utf8_bin NOT NULL DEFAULT 'i',
  `subject_|D` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Re_idx` (`Recipient_ID`),
  KEY `De_idx` (`Deliver_ID`),
  CONSTRAINT `De` FOREIGN KEY (`Deliver_ID`) REFERENCES `person` (`id`),
  CONSTRAINT `Re` FOREIGN KEY (`Recipient_ID`) REFERENCES `person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `city`
--

DROP TABLE IF EXISTS `city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `city` (
  `CityId` int NOT NULL AUTO_INCREMENT,
  `CityName` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`CityId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `city`
--

LOCK TABLES `city` WRITE;
/*!40000 ALTER TABLE `city` DISABLE KEYS */;
/*!40000 ALTER TABLE `city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `family`
--

DROP TABLE IF EXISTS `family`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `family` (
  `id` int NOT NULL AUTO_INCREMENT,
  `   HusbandName` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `  WifeName` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `FamilyId` int DEFAULT NULL,
  ` NationalId` int DEFAULT NULL,
  ` MobileNumber` int DEFAULT NULL,
  ` NumberOfChildren` int DEFAULT NULL,
  `LivingSituation` int DEFAULT NULL,
  `  HusbandWork` varchar(50) COLLATE utf8_bin DEFAULT NULL,
  `CurrentPlaceOfResidence` text COLLATE utf8_bin,
  ` PreviousPlaceOfResidence` text COLLATE utf8_bin,
  `Person_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `person_idx` (`Person_id`),
  CONSTRAINT `person` FOREIGN KEY (`Person_id`) REFERENCES `person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `family`
--

LOCK TABLES `family` WRITE;
/*!40000 ALTER TABLE `family` DISABLE KEYS */;
/*!40000 ALTER TABLE `family` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `person` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `Type` varchar(1) NOT NULL DEFAULT 'B',
  `City_id` int DEFAULT NULL,
  `BirthOfDate` date DEFAULT NULL,
  `Natinal_ID` int DEFAULT NULL,
  `Addrees` text,
  `Phone_Nummber` int DEFAULT NULL,
  `Jurisdiction` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fkcity_idx` (`City_id`),
  CONSTRAINT `fkcity` FOREIGN KEY (`City_id`) REFERENCES `city` (`CityId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subject`
--

DROP TABLE IF EXISTS `subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subject` (
  `id` int NOT NULL,
  `Descrption` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subject`
--

LOCK TABLES `subject` WRITE;
/*!40000 ALTER TABLE `subject` DISABLE KEYS */;
/*!40000 ALTER TABLE `subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subsidessubjects`
--

DROP TABLE IF EXISTS `subsidessubjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subsidessubjects` (
  `SubjectId` int NOT NULL,
  `SubsideId` int NOT NULL,
  PRIMARY KEY (`SubjectId`,`SubsideId`),
  KEY `SubsideId_idx` (`SubsideId`),
  CONSTRAINT `SubjectId` FOREIGN KEY (`SubjectId`) REFERENCES `subject` (`Id`),
  CONSTRAINT `SubsideId` FOREIGN KEY (`SubsideId`) REFERENCES `subsidies` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subsidessubjects`
--

LOCK TABLES `subsidessubjects` WRITE;
/*!40000 ALTER TABLE `subsidessubjects` DISABLE KEYS */;
/*!40000 ALTER TABLE `subsidessubjects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `support`
--

DROP TABLE IF EXISTS `support`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `support` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Star_Date` date DEFAULT NULL,
  `End_Date` date DEFAULT NULL,
  `Sponsor_id` int DEFAULT NULL,
  `Ben_id` int DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `fksp_idx` (`Sponsor_id`),
  KEY `fkb_idx` (`Ben_id`),
  CONSTRAINT `fkb` FOREIGN KEY (`Ben_id`) REFERENCES `person` (`id`),
  CONSTRAINT `fksp` FOREIGN KEY (`Sponsor_id`) REFERENCES `person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_mysql500_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `support`
--

LOCK TABLES `support` WRITE;
/*!40000 ALTER TABLE `support` DISABLE KEYS */;
/*!40000 ALTER TABLE `support` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `support_type`
--

DROP TABLE IF EXISTS `support_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `support_type` (
  `iid` int NOT NULL AUTO_INCREMENT,
  `Descrition` varchar(45) NOT NULL,
  PRIMARY KEY (`iid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `support_type`
--

LOCK TABLES `support_type` WRITE;
/*!40000 ALTER TABLE `support_type` DISABLE KEYS */;
/*!40000 ALTER TABLE `support_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_permissions`
--

DROP TABLE IF EXISTS `users_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_permissions` (
  `username` varchar(10) NOT NULL,
  `Password` varchar(10) NOT NULL,
  `Create_Doctor` tinyint DEFAULT '0',
  `Read_Doctor` tinyint DEFAULT '0',
  `Delete_Doctor` tinyint DEFAULT '0',
  `Update_Doctor` tinyint DEFAULT '0',
  `Create_Beneficiaries` tinyint(1) DEFAULT '0',
  `Delete_Beneficiaries` tinyint(1) DEFAULT '0',
  `Read_Beneficiaries` tinyint(1) DEFAULT '0',
  `Update_Beneficiaries` tinyint(1) DEFAULT '0',
  `Create_Family` tinyint(1) DEFAULT '0',
  `Read_Family` tinyint(1) DEFAULT '0',
  `Updete_Family` tinyint(1) DEFAULT '0',
  `Delete_Family` tinyint(1) DEFAULT '0',
  `Create_Sponser` tinyint(1) DEFAULT '0',
  `Updete_Sponser` tinyint(1) DEFAULT '0',
  `Delete_Sponser` tinyint(1) DEFAULT '0',
  `Update_Family` tinyint(1) DEFAULT '0',
  `inventory` tinyint(1) DEFAULT '0',
  `admin` tinyint(1) DEFAULT '0',
  `Warehouse_Movements` tinyint(1) DEFAULT '0',
  `report` tinyint(1) DEFAULT '0',
  `Create_support_type` tinyint(1) DEFAULT '0',
  `Delete_support_type` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_permissions`
--

LOCK TABLES `users_permissions` WRITE;
/*!40000 ALTER TABLE `users_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `visit`
--

DROP TABLE IF EXISTS `visit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `visit` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Doctor_id` int DEFAULT NULL,
  `Bene_id` int DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Diagnose` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fkDoc_idx` (`Doctor_id`),
  KEY `fkBen_idx` (`Bene_id`),
  CONSTRAINT `fkBen` FOREIGN KEY (`Bene_id`) REFERENCES `person` (`id`),
  CONSTRAINT `fkDoc` FOREIGN KEY (`Doctor_id`) REFERENCES `person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visit`
--

LOCK TABLES `visit` WRITE;
/*!40000 ALTER TABLE `visit` DISABLE KEYS */;
/*!40000 ALTER TABLE `visit` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-14 12:33:45
