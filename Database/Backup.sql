-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tribunal
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `directii`
--

DROP TABLE IF EXISTS `directii`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `directii` (
  `DirectieID` int NOT NULL AUTO_INCREMENT,
  `Nume` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '-',
  `Descriere` text,
  PRIMARY KEY (`DirectieID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `directii`
--

LOCK TABLES `directii` WRITE;
/*!40000 ALTER TABLE `directii` DISABLE KEYS */;
INSERT INTO `directii` VALUES (1,'DNA','Direcția Națională Anticorupție'),(2,'DIICOT','Direcția de Investigare a Infracțiunilor de Criminalitate Organizată și Terorism'),(3,'DGPI','Direcția Generală de Protecție Internă'),(4,'DICE','Direcția de Investigare a Infracțiunilor de Criminalitate Economică'),(5,'ANI','Agenția Națională de Integritate');
/*!40000 ALTER TABLE `directii` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dosare`
--

DROP TABLE IF EXISTS `dosare`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dosare` (
  `DosarID` int NOT NULL AUTO_INCREMENT,
  `LegeID` int NOT NULL,
  `DirectieID` int DEFAULT NULL,
  `Numar` int NOT NULL DEFAULT '0',
  `Descriere` text,
  PRIMARY KEY (`DosarID`),
  UNIQUE KEY `LegeID` (`LegeID`),
  KEY `idx_dosare_legi` (`LegeID`),
  KEY `fk_dosare_directii` (`DirectieID`),
  CONSTRAINT `fk_dosare_directii` FOREIGN KEY (`DirectieID`) REFERENCES `directii` (`DirectieID`),
  CONSTRAINT `fk_dosare_legi` FOREIGN KEY (`LegeID`) REFERENCES `legi` (`LegeID`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dosare`
--

LOCK TABLES `dosare` WRITE;
/*!40000 ALTER TABLE `dosare` DISABLE KEYS */;
INSERT INTO `dosare` VALUES (32,26,1,25,'Furtul unor bunuri materiale dintr-un magazin din centrul Bucurestiului.'),(33,22,3,10,'Obstructionarea de la dreptului de acces la informatii de interes public.'),(34,23,3,11,'Expunerea unor informatii clasificare publicului fara acordul de desecretizare a acestora.'),(35,20,5,17,'Nedeclararea unor bunuri materiale de mare pret.'),(36,25,2,50,'Deconspirarea si arestarea unui grup terorist in Constanta.');
/*!40000 ALTER TABLE `dosare` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `judecatori`
--

DROP TABLE IF EXISTS `judecatori`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `judecatori` (
  `JudecatorID` int NOT NULL AUTO_INCREMENT,
  `Nume` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '-',
  `Prenume` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '-',
  `CNP` varchar(13) NOT NULL DEFAULT '-',
  `Telefon` char(10) DEFAULT NULL,
  `Email` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`JudecatorID`),
  UNIQUE KEY `CNP` (`CNP`),
  UNIQUE KEY `CNP_2` (`CNP`),
  UNIQUE KEY `CNP_3` (`CNP`)
) ENGINE=InnoDB AUTO_INCREMENT=110 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `judecatori`
--

LOCK TABLES `judecatori` WRITE;
/*!40000 ALTER TABLE `judecatori` DISABLE KEYS */;
INSERT INTO `judecatori` VALUES (84,'Popescu','Ana','2900512345678','0721123456','ana.popescu@email.com'),(85,'Ionescu','Radu','1850712345678','0732123456','radu.ionescu@email.com'),(86,'Dumitrescu','Elena','2980823456789','0743123456','elena.dumitrescu@email.com'),(87,'Stanescu','Andrei','1770412345678','0754123456','andrei.stanescu@email.com'),(88,'Gheorghescu','Maria','2680323456789','0765123456','maria.gheorghescu@email.com'),(89,'Vasilescu','Adrian','2030112345678','0776123456','adrian.vasilescu@email.com');
/*!40000 ALTER TABLE `judecatori` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `judecatoridosare`
--

DROP TABLE IF EXISTS `judecatoridosare`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `judecatoridosare` (
  `JudecatorID` int NOT NULL,
  `DosarID` int NOT NULL DEFAULT '0',
  `NrOre` int DEFAULT '0',
  PRIMARY KEY (`JudecatorID`,`DosarID`),
  KEY `fk_dosare_judecatoridosare` (`DosarID`),
  CONSTRAINT `fk_dosare_judecatoridosare` FOREIGN KEY (`DosarID`) REFERENCES `dosare` (`DosarID`),
  CONSTRAINT `fk_judecatori_judecatoridosare` FOREIGN KEY (`JudecatorID`) REFERENCES `judecatori` (`JudecatorID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `judecatoridosare`
--

LOCK TABLES `judecatoridosare` WRITE;
/*!40000 ALTER TABLE `judecatoridosare` DISABLE KEYS */;
INSERT INTO `judecatoridosare` VALUES (84,32,5),(85,36,10),(86,36,15),(87,35,3),(88,33,2),(89,34,0);
/*!40000 ALTER TABLE `judecatoridosare` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `legi`
--

DROP TABLE IF EXISTS `legi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `legi` (
  `LegeID` int NOT NULL AUTO_INCREMENT,
  `Nume` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '-',
  `Descriere` text,
  PRIMARY KEY (`LegeID`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `legi`
--

LOCK TABLES `legi` WRITE;
/*!40000 ALTER TABLE `legi` DISABLE KEYS */;
INSERT INTO `legi` VALUES (20,'115/1996','Declararea şi controlul averii demnitarilor, magistraţilor, a unor persoane cu funcţii de conducere şi de control şi a funcţionarilor publici'),(21,'184/2016','Instituirea unui mecanism de prevenire a conflictului de interese în procedura de atribuire a contractelor de achiziţie publică'),(22,'544/2001','Liberul acces la informaţiile de interes public'),(23,'182/2002','Protecţia informaţiilor clasificate'),(24,'39/2003','Prevenirea şi combaterea criminalităţii organizate.'),(25,'535 /2004','Prevenirea şi combaterea terorismului.'),(26,'286/2009','Codul Penal (cu precizare art. 229 privind furtul calificat)'),(27,'195/2002','Circulatia pe drumurile publice');
/*!40000 ALTER TABLE `legi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `participanti`
--

DROP TABLE IF EXISTS `participanti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `participanti` (
  `ParticipantID` int NOT NULL AUTO_INCREMENT,
  `Nume` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT '-',
  `Prenume` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT '-',
  `CNP` varchar(13) NOT NULL DEFAULT '-',
  `Telefon` varchar(10) DEFAULT '-',
  `email` varchar(30) DEFAULT '-',
  PRIMARY KEY (`ParticipantID`),
  UNIQUE KEY `CNP` (`CNP`),
  UNIQUE KEY `CNP_2` (`CNP`),
  CONSTRAINT `participanti_chk_1` CHECK ((locate(_utf8mb4'@',`email`) > 0))
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `participanti`
--

LOCK TABLES `participanti` WRITE;
/*!40000 ALTER TABLE `participanti` DISABLE KEYS */;
INSERT INTO `participanti` VALUES (13,'Mihai','Georgescu','3050419876543','0722123456','mihai.georgescu@email.com'),(14,'Laura','Constantinescu','2150801234567','0733123456','laura.constantinescu@email.com'),(15,'Dorin','Popa','1980323456789','0744123456','dorin.popa@email.com'),(16,'Simona','Andrei','1760112345678','0755123456','simona.andrei@email.com'),(17,'Alexandru','Iordache','2870623456789','0766123456','alexandru.iordache@email.com'),(18,'Cristina','Dragomir','2031123456789','0777123456','cristina.dragomir@email.com');
/*!40000 ALTER TABLE `participanti` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `participantidosare`
--

DROP TABLE IF EXISTS `participantidosare`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `participantidosare` (
  `DosarID` int NOT NULL,
  `ParticipantID` int NOT NULL,
  `TipParticipantID` int NOT NULL,
  PRIMARY KEY (`DosarID`,`ParticipantID`,`TipParticipantID`),
  KEY `fk_tipparticipanti_participantidosare` (`TipParticipantID`),
  KEY `fk_participanti_participantidosare` (`ParticipantID`),
  CONSTRAINT `fk_dosare_participantidosare` FOREIGN KEY (`DosarID`) REFERENCES `dosare` (`DosarID`) ON DELETE CASCADE,
  CONSTRAINT `fk_participanti_participantidosare` FOREIGN KEY (`ParticipantID`) REFERENCES `participanti` (`ParticipantID`) ON DELETE CASCADE,
  CONSTRAINT `fk_tipparticipanti_participantidosare` FOREIGN KEY (`TipParticipantID`) REFERENCES `tipuriparticipanti` (`TipParticipantID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `participantidosare`
--

LOCK TABLES `participantidosare` WRITE;
/*!40000 ALTER TABLE `participantidosare` DISABLE KEYS */;
INSERT INTO `participantidosare` VALUES (32,13,1),(34,15,1),(35,17,1),(36,13,1),(36,17,2),(36,16,3),(33,18,4),(36,15,4),(36,18,4),(36,14,5);
/*!40000 ALTER TABLE `participantidosare` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipuriparticipanti`
--

DROP TABLE IF EXISTS `tipuriparticipanti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipuriparticipanti` (
  `TipParticipantID` int NOT NULL DEFAULT '0',
  `Nume` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '-',
  `Descriere` text,
  PRIMARY KEY (`TipParticipantID`),
  UNIQUE KEY `TipParticipantID` (`TipParticipantID`),
  UNIQUE KEY `Nume` (`Nume`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipuriparticipanti`
--

LOCK TABLES `tipuriparticipanti` WRITE;
/*!40000 ALTER TABLE `tipuriparticipanti` DISABLE KEYS */;
INSERT INTO `tipuriparticipanti` VALUES (1,'Parte Principală','Persoane sau entități direct implicate în litigiu.'),(2,'Avocat','Profesioniști în domeniul juridic care reprezintă părțile implicate.'),(3,'Executor Judecătoresc','Persoană autorizată să pună în aplicare hotărârile instanței.'),(4,'Martor','Persoane care depun mărturie sub jurământ în fața instanței.'),(5,'Expert','Specialiști într-un anumit domeniu, aduși pentru a oferi opinii profesionale.');
/*!40000 ALTER TABLE `tipuriparticipanti` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-07 10:13:12
