
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


-
CREATE TABLE `city` (
  `CityId` int NOT NULL AUTO_INCREMENT,
  `CityName` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`CityId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;



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



CREATE TABLE `subject` (
  `id` int NOT NULL,
  `Descrption` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `subsidessubjects` (
  `SubjectId` int NOT NULL,
  `SubsideId` int NOT NULL,
  PRIMARY KEY (`SubjectId`,`SubsideId`),
  KEY `SubsideId_idx` (`SubsideId`),
  CONSTRAINT `SubjectId` FOREIGN KEY (`SubjectId`) REFERENCES `subject` (`Id`),
  CONSTRAINT `SubsideId` FOREIGN KEY (`SubsideId`) REFERENCES `subsidies` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



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


CREATE TABLE `support_type` (
  `iid` int NOT NULL AUTO_INCREMENT,
  `Descrition` varchar(45) NOT NULL,
  PRIMARY KEY (`iid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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

