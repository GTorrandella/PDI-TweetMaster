-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: BDTweetMaster
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `campaign`
--

DROP TABLE IF EXISTS `campaign`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `campaign` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `startDate` varchar(30) DEFAULT NULL,
  `finDate` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `hashtags` varchar(50) DEFAULT NULL,
  `mentions` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `campaign`
--

LOCK TABLES `campaign` WRITE;
/*!40000 ALTER TABLE `campaign` DISABLE KEYS */;
INSERT INTO `campaign` VALUES (1,'16 12 2018 18:22:00','10 01 2019 18:22:00','activa@gmail.com','#noBorrrar-#412','@fedecalongeOK-@mauriciomacriOKkk'),(2,'22 12 2018 18:22:00','10 01 2019 18:22:00','activaConTw@gmail.com','#tieneTw-#noBorrarNada-#412','@fedecalongeOK-@mauriciomacriOKkk'),(3,'16 12 2018 18:22:00','28 12 2018 18:22:00','finalizadaConTw@gmail.com','#tieneTw-#borrarTodo-#200','@fedecalongeOK-@mauriciomacriOKkk'),(4,'10 01 2019 18:22:00','20 01 2019 18:22:00','noEmpezada@gmail.com','#borrar-#200','@fedecalongeOK-@mauriciomacriOKkk'),(5,'24 12 2018 18:22:00','25 12 2018 18:22:00','finalizada@gmail.com','#borrar-#200','@fedecalongeOK-@mauriciomacriOKkk'),(6,'10 01 2019 18:22:00','20 01 2019 18:22:00','noEmpezadaConTw@gmail.com','#tieneTw-#borrarTodo-#200','@fedecalongeOK-@mauriciomacriOKkk'),(7,'22 12 2018 18:22:00','10 01 2019 18:22:00','activaConTw@gmail.com','#tieneTw-#noBorrarNada-#412','@fedecalongeOK-@mauriciomacriOKkk'),(8,'16 12 2018 18:22:00','28 12 2018 18:22:00','finalizadaConTw@gmail.com','#tieneTw-#borrarTodo-#200','@fedecalongeOK-@mauriciomacriOKkk'),(9,'24 12 2018 18:22:00','25 12 2018 18:22:00','mezclada@gmail.com','#borrar-#200','@fedecalongeOK-@mauriciomacriOKkk'),(10,'16 12 2018 18:22:00','10 01 2019 18:22:00','mezclada@gmail.com','#noBorrrar-#412','@fedecalongeOK-@mauriciomacriOKkk');
/*!40000 ALTER TABLE `campaign` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tweets`
--

DROP TABLE IF EXISTS `tweets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tweets` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `userName` varchar(50) DEFAULT NULL,
  `userid` varchar(30) DEFAULT NULL,
  `hashtags` varchar(50) DEFAULT NULL,
  `mentions` varchar(50) DEFAULT NULL,
  `date` varchar(30) DEFAULT NULL,
  `idCampaign` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `idCampaign` (`idCampaign`),
  CONSTRAINT `tweets_ibfk_1` FOREIGN KEY (`idCampaign`) REFERENCES `campaign` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=896 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tweets`
--

LOCK TABLES `tweets` WRITE;
/*!40000 ALTER TABLE `tweets` DISABLE KEYS */;
INSERT INTO `tweets` VALUES (223,'NASAOk','789456','#mars-#venus-#earth','@NASA-@planets','2018-03-20 15:11:01',2),(224,'MiauricioOK','451325','#DonaldNoMeDejes','@donaldTrump-@G20','2018-03-20 21:08:01',2),(323,'NASAOk','789456','#mars-#venus-#earth','@NASA-@planets','2018-03-20 15:11:01',3),(324,'MiauricioOK','451325','#DonaldNoMeDejes','@donaldTrump-@G20','2018-03-20 21:08:01',3),(623,'NASAOk','789456','#mars-#venus-#earth','@NASA-@planets','2018-03-20 15:11:01',6),(624,'MiauricioOK','451325','#DonaldNoMeDejes','@donaldTrump-@G20','2018-03-20 21:08:01',6),(724,'MiauricioOK','451325','#DonaldNoMeDejes','@donaldTrump-@G20','2018-03-20 21:08:01',7),(732,'MiauricioOK','451325','#mars-#venus-#earth','@NASA-@planets','2018-03-20 15:11:01',7),(845,'NASAOk','451325','#DonaldNoMeDejes','@donaldTrump-@G20','2018-03-20 21:08:01',8),(895,'MiauricioOK','789456','#mars-#venus-#earth','@NASA-@planets','2018-03-20 15:11:01',8);
/*!40000 ALTER TABLE `tweets` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-28 22:09:13
