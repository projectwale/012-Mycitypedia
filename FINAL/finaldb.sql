/*
SQLyog Community Edition- MySQL GUI v7.01 
MySQL - 5.0.27-community-nt : Database - 012-mycitypedia
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`012-mycitypedia` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `012-mycitypedia`;

/*Table structure for table `addlisting` */

DROP TABLE IF EXISTS `addlisting`;

CREATE TABLE `addlisting` (
  `Id` int(255) NOT NULL auto_increment,
  `Title` varchar(255) default NULL,
  `categorySelect` varchar(255) default NULL,
  `Contact` varchar(255) default NULL,
  `Email` varchar(255) default NULL,
  `Description` longtext,
  `City` varchar(255) default NULL,
  `Current_Address` varchar(255) default NULL,
  `State` varchar(255) default NULL,
  `Zip` varchar(255) default NULL,
  `Facebook` varchar(255) default NULL,
  `Pinterest` varchar(255) default NULL,
  `Twitter` varchar(255) default NULL,
  `random_number` varchar(255) default NULL,
  `openingTimeSelect` varchar(255) default NULL,
  `closing` varchar(255) default NULL,
  `status` varchar(255) default 'PENDING',
  `User` varchar(255) default NULL,
  PRIMARY KEY  (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `addlisting` */

insert  into `addlisting`(`Id`,`Title`,`categorySelect`,`Contact`,`Email`,`Description`,`City`,`Current_Address`,`State`,`Zip`,`Facebook`,`Pinterest`,`Twitter`,`random_number`,`openingTimeSelect`,`closing`,`status`,`User`) values (1,'ZUDIO','Shopping','7302408690','ZUDIO@gmail.com','ZUDIO, a leading retail and e-commerce conglomerate headquartered in India, has established itself as a premier destination for consumer electronics and durables. With a rich history dating back to its inception in 2006, ZUDIO has continuously evolved to meet the ever-changing demands of the tech-savvy consumer market. Offering a wide range of products, including smartphones, laptops, home appliances, and more, ZUDIO boasts an expansive network of physical stores across the country, providing customers with a hands-on shopping experience and expert guidance from knowledgeable staff. Complementing its brick-and-mortar presence, ZUDIO robust online platform ensures convenience and accessibility, enabling customers to browse and purchase products from the comfort of their homes. Renowned for its commitment to quality, competitive pricing, and customer-centric approach, ZUDIO has earned the trust and loyalty of millions of customers, making it a household name\r\nsynonymous with reliability and innovation in the world of electronics retail.','panvel','Shop No. 3 to 7 Ground & First Floor, opp. Rajiv Gandhi Maidan, Sector No. 10, New Panvel East, Panvel, Navi Mumbai, Maharashtra 410206','Ketan salvi','410206','https://drive.google.com/file/d/1zVWxWr6HRTP_j2F0NmKv5LRh6884Gyy9/view','https://drive.google.com/file/d/1zVWxWr6HRTP_j2F0NmKv5LRh6884Gyy9/view','https://drive.google.com/file/d/1zVWxWr6HRTP_j2F0NmKv5LRh6884Gyy9/view','9860','10.00 am','10.00 pm','ACCEPT','amit'),(2,'NUCLEUS ACADEMY','Education','8850812034','NUCLEUSACADEMY@gmail.com','Nucleus Academy in New Panel, Navi Mumbai\r\nClass X is a very important year in every students life as this is the foundation year for their future. The performance this year has an impact on the\r\nstudents potential career path. Most class 10 students experience anxiety as a result of the vast syllabus, and performance pressure so that they get\r\ninto the desired school and stream. Tutorials For Class X offers interactive sessions to help students in clearing their doubts and make the concepts\r\neasier for them.\r\nTutorials For Class X in New Panel, Navi Mumbai are given by Nucleus Academy, which has established its name in the market.','panvel','Shop Number 2, Shanti Appartment,, Sector 4, New Panvel, near Siciliano pzza store, Navi Mumbai, Maharashtra 410206','Amol prasad','410206','https://drive.google.com/file/d/10zsFLcsOLbBoDkj6qVgxUKQ1OpKqlb2B/view','https://drive.google.com/file/d/10zsFLcsOLbBoDkj6qVgxUKQ1OpKqlb2B/view','https://drive.google.com/file/d/10zsFLcsOLbBoDkj6qVgxUKQ1OpKqlb2B/view','3904','7.00 am','10.00 pm','ACCEPT','amit'),(3,'MSEB','Event','9632587414','MSEB@gmail.com','MSEB in Panvel, Navi Mumbai\r\nElectricity Suppliers\r\nWe make use of electricity in our homes and offices every day. Without electricity, we would not be able to conduct our day-to-day activities. Thus, it\r\nis safe to say that without electricity supply our lives would come to a standstill. Hence it is very critical to have a regular supply of electricity at our\r\nhomes and offices. Electricity Suppliers provide electricity to many users and charge them for using their services.\r\nIf you are looking for a reliable Electricity Suppliers, we highly advise you to contact MSEB in Panel, Navi Mumbai. to make our lives easier.','panvel','Shop No. 9, Shiva Complex, Matheran Road, Panvel, Navi Mumbai - 410206 (Near Vishwas Bazaar)','SONALI BAIT','410206','https://twitter.com/MSEDCL','https://twitter.com/MSEDCL','https://www.mahadiscom.in/','4782','8.00 am','5.00 pm','ACCEPT','amit'),(4,'Shubham Plywood & Hardware','Motor_Training_Schools','7419598692','Shubham@gmail.com','Shubham Plywood & Hardware in New Panel, Navi Mumbai, Mumbai\r\nShubham Plywood & Hardware in Navi Mumbai, Mumbai is one of the leading businesses in the Commercial Plywood Dealers. Also known for\r\nHardware Shops, Wall Paper Dealers, Plywood Dealers, Acrylic Sheet Dealers, Laser Cutting Services, Pipe Dealers, Power Tool Dealers, Hardware\r\nDealers and much more. Find Address, Contact Number, Reviews & Ratings, Photos, Maps of Shubham Plywood & Hardware, Navi Mumbai, Mumbai.','panvel','Shop No-9 Neel Gagan, Sector-1/S, Plot No-102, New Panvel, Navi Mumbai - 410206 (Near Shabari Hotel)','amin tadvi','410206','https://drive.google.com/file/d/1n99miLffJOaLD7A66R_2mdp6rPRCWzek/view','https://drive.google.com/file/d/1n99miLffJOaLD7A66R_2mdp6rPRCWzek/view','https://drive.google.com/file/d/1n99miLffJOaLD7A66R_2mdp6rPRCWzek/view','3051','9.00 am','9.00 pm','ACCEPT','amit'),(5,'My Gym Pro','GYM','9972932686','stawar59@gmail.com','My Gym Pro in Panel, Mumbai\r\nMy Gym Pro in Mumbai is one of the leading businesses in the Gyms. Also known for Gyms,\r\nGyms, Yoga Classes At Home, Zumba Classes For Women, Fitness Centres and much mor\r\nPhotos, Maps of My Gym Pro, Mumbai. All scientific evidence and studies prove that being physically active enables you to lead a healthier life. Not just your physical health, but even your emotional and mental well-being is impacted positively when your body is hail and hearty. In the pursuit of holistic wellness, there has been an overall increase across all demographics in the number of people who wish to exercise.\r\nSeveral Gyms have mushroomed in and around Mumbai. My Gym Pro in Panel, Mumbai is a popular choice among fitness enthusiasts in the area\r\nThis gym has existed since 2014. It has received an average 5.0 rating. Here is a list of their offerings: Meditation Counselling, Get Your Own Trainer,\r\nWeight Gain Program. Of course, a gym may help you build muscles and look fab. But remember people who regularly exercise have a lower risk of\r\ndeveloping several health concerns, so you might want to check out this place.','panvel','Plot No -205/74, 2nd Floor, Shree Sahayya Galaxy, Shivaji Chowk Road, Panvel, Mumbai - 410206 (Above P N G Jewellers,Opposite MTNL)','sahil ghadge','410206','https://www.instagram.com/mygym_propanvel/','https://www.instagram.com/mygym_propanvel/','https://www.instagram.com/mygym_propanvel/','6340','6.00 am','10.00 pm','ACCEPT','amit'),(6,'Ingole\'s Physiotherapy Clinic','Dentists','7419897593','Ingole@gmail.com','Ingle\'s Physiotherapy Clinic in Panel City, Navi Mumbai, Mumbai\r\nIngole\'s Physiotherapy Clinic in Navi Mumbai, Mumbai is one of the leading businesses in the Physiotherapists. Also known for Orthopaedic Doctors,\r\nPhysiotherapists, Clinics, Rehabilitation Centres, Physiotherapist For Home Visits, Physiotherapy Centres, Arthritis Doctors, Pediatric Physiotherapy\r\nDoctors and much more. Find Address, Contact Number, Reviews & Ratings, Photos, Maps of Ingole\'s Physiotherapy Clinic, Navi Mumbai, Mumbai.\r\nMost people underestimate this form of practice until they actually need it. Physiotherapists specialise in musculoskeletal functions and help\r\nimprove the efficiency of their performance. One may require the expertise of such a practitioner due to genetics or birth complications, but even\r\nafter an incident or accident, a physiotherapist can help alleviate bodily pain and hasten your recovery.\r\nSo, while looking for Physiotherapists, you should check out Ingle\'s Physiotherapy Clinic in Panel City, Navi Mumbai. This physiotherapist has\r\nreceived an average 4.9 rating. Here is a list of this practitioners offerings: Geriatric Physiotherapy Consultation, Joint and Musculoskeletal Disorder\r\nTreatment, Clinical Physiotherapy.','panvel','Row House Number 1 Suyash CHS Plot Number 2 Sector 2, Vijay Marg Opposite Of Shabri Hotel, Panvel City, Navi Mumbai - 410206 (Shabri Pure Veg Restaurant)','roshan munde','410206','https://www.justdial.com/Mumbai/Ingoles-Physiotherapy-Clinic-Shabri-Pure-Veg-Restaurant-Panvel-City/022PXX22-XX22-180222190234-I6B7_BZDET','https://www.justdial.com/Mumbai/Ingoles-Physiotherapy-Clinic-Shabri-Pure-Veg-Restaurant-Panvel-City/022PXX22-XX22-180222190234-I6B7_BZDET','https://www.justdial.com/Mumbai/Ingoles-Physiotherapy-Clinic-Shabri-Pure-Veg-Restaurant-Panvel-City/022PXX22-XX22-180222190234-I6B7_BZDET','1416','6.00 am','5.00 pm','ACCEPT','amit');

/*Table structure for table `contact` */

DROP TABLE IF EXISTS `contact`;

CREATE TABLE `contact` (
  `id` int(255) NOT NULL auto_increment,
  `name` varchar(255) default NULL,
  `email` varchar(255) default NULL,
  `massage` longtext,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `contact` */

/*Table structure for table `review` */

DROP TABLE IF EXISTS `review`;

CREATE TABLE `review` (
  `id` int(255) NOT NULL auto_increment,
  `username` varchar(255) default NULL,
  `comments` varchar(255) default NULL,
  `rating` varchar(255) default NULL,
  `randomno` varchar(255) default NULL,
  `userimage` varchar(255) default NULL,
  `BUSSNESS` varchar(255) default NULL,
  `IDBUSS` varchar(255) default NULL,
  `USERID` int(255) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `review` */

insert  into `review`(`id`,`username`,`comments`,`rating`,`randomno`,`userimage`,`BUSSNESS`,`IDBUSS`,`USERID`) values (3,'yash','ZUDIO is one of the best shopping market','5','1900','static/profile/pic-1.png','ZUDIO','1',3),(5,'yash','Nucleus Academy in New Panel, Navi Mumbai Class X is a very important year in every students life as this is the foundation year for their future. ','4','9282','static/profile/pic-1.png','NUCLEUS ACADEMY','2',3),(6,'yash','MSEB in Panvel, Navi Mumbai Electricity Suppliers We make use of electricity in our homes and offices every day.','4','9795','static/profile/pic-1.png','MSEB','3',3),(7,'yash','Shubham Plywood & Hardware in New Panel, Navi Mumbai, Mumbai Shubham Plywood & Hardware in Navi Mumbai, Mumbai is one of the leading businesses in the Commercial Plywood Dealers','5','2283','static/profile/pic-1.png','Shubham Plywood & Hardware','4',3),(10,'Ketan','nice look envirnment','3','1659','static/profile/parent3.png','ZUDIO','1',4),(11,'jay','this was nice','3','3710','static/profile/course-2-1.jpg','ZUDIO','1',5);

/*Table structure for table `userregisters` */

DROP TABLE IF EXISTS `userregisters`;

CREATE TABLE `userregisters` (
  `Id` int(255) NOT NULL auto_increment,
  `Username` varchar(255) default NULL,
  `Email` varchar(255) default NULL,
  `Mobile` varchar(255) default NULL,
  `Password` varchar(255) default NULL,
  `Profile_Img` varchar(255) default NULL,
  `Address` varchar(255) default NULL,
  `Pancard` varchar(255) default NULL,
  PRIMARY KEY  (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `userregisters` */

insert  into `userregisters`(`Id`,`Username`,`Email`,`Mobile`,`Password`,`Profile_Img`,`Address`,`Pancard`) values (2,'amit','jackspaarow51@gmail.com','8383838382','Amit@12345','static/profile/pic-3.png','mumbai','789456123963'),(3,'yash','yashsalvi1999@gmail.com','8768658678','Yash@12345','static/profile/pic-1.png','aroli','147852369696'),(4,'Ketan','hp690175@gmail.com','8783247333','Ketan@12345','static/profile/parent3.png','Diva','741258963321'),(5,'jay','abhisontakke3930@gmail.com','9632587414','Jay@12345','static/profile/course-2-1.jpg','aroli','963258741478'),(6,'hemant','raskajay458@gmail.com','8783247337','Hemant@123','static/profile/course-2-8.jpg','vidya vihar','789654123214');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
