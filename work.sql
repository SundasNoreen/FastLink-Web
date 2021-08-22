-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: vacation-planner.mysql.database.azure.com
-- Generation Time: Aug 18, 2021 at 02:49 PM
-- Server version: 5.7.32-log
-- PHP Version: 7.2.24-0ubuntu0.18.04.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fastlink`
--

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--

CREATE TABLE `admins` (
  `Category` varchar(500) NOT NULL,
  `Name` varchar(500) NOT NULL,
  `Login` varchar(500) NOT NULL,
  `Password` varchar(500) NOT NULL,
  `Email` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`Category`, `Name`, `Login`, `Password`, `Email`) VALUES
('Main', 'Bilal Shahid', '123', '123', 'bilalshahid@gmail.com'),
('Main', 'Sundas', 'noreensundas', '1234', 'noreensundus@gmail.com'),
('Secondary', 'Sundas Noreen', 'sundasnoreen', 'sundas', 'noreensundas@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `client`
--

CREATE TABLE `client` (
  `ID` int(200) NOT NULL,
  `Name` varchar(500) NOT NULL,
  `CNIC` varchar(500) NOT NULL,
  `Phone` varchar(500) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `Balance` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `client`
--

INSERT INTO `client` (`ID`, `Name`, `CNIC`, `Phone`, `Address`, `Balance`) VALUES
(1001, 'Sundas Noreen', '3456789', '987654899999999', 'dfghjk', 0),
(1002, 'Amna', '345678', '9096', 'iytre', 0),
(1003, 'Amna Noreen', '345678', '9096', 'iytre', 0);

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `ID` int(200) NOT NULL,
  `Name` varchar(500) NOT NULL,
  `CNIC` varchar(500) NOT NULL,
  `Phone` varchar(500) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `Balance` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`ID`, `Name`, `CNIC`, `Phone`, `Address`, `Balance`) VALUES
(101, 'Ahmad Ali', '31111-3111111-1', '0322-1111111', 'Lahore, Pakistan', 0),
(102, 'Nomi ', '11111-1111111-1', '0301-1111111', 'Lahore, Pakistan', 0),
(103, 'Mudassar', '3456789', '4876543', 'Lahore, Pakistan', 0),
(104, 'Akram', '2345678', '983', 'kjsdfg', 300),
(106, 'Mudassar Aslam', '35202-8250414-7', '03014001041', 'Lahore', 0);

-- --------------------------------------------------------

--
-- Table structure for table `work`
--

CREATE TABLE `work` (
  `WorkID` int(255) NOT NULL,
  `Client` int(255) NOT NULL,
  `Employee` int(255) NOT NULL,
  `Store` varchar(5000) NOT NULL,
  `Purchased` varchar(3000) NOT NULL,
  `Amount` int(255) NOT NULL,
  `Bill` int(255) NOT NULL,
  `Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `work`
--

INSERT INTO `work` (`WorkID`, `Client`, `Employee`, `Store`, `Purchased`, `Amount`, `Bill`, `Date`) VALUES
(1, 1001, 101, '1 Bulb ', '1 Switch, 1 Three Shoe', 500, 800, '2021-08-03'),
(2, 1003, 103, '1 Switch , 1 Capacitor', '1 Wire', 200, 500, '2021-08-07'),
(3, 1001, 102, '1 Switch , 1 Capacitor', '1 Wire', 200, 500, '2021-08-05'),
(4, 1002, 101, '1 Switch , 1 Capacitor', '1 Wire', 300, 500, '2021-08-11'),
(5, 1003, 103, '1 Switch , 1 Capacitor', '', 0, 200, '2021-08-12'),
(6, 1001, 104, '1 Switch , 1 Capacitor', '1 Wire', 100, 500, '2021-08-04'),
(7, 1001, 102, '1 Switch , 1 Capacitor', '1 Wire', 100, 300, '2021-08-04'),
(8, 1001, 102, '1 Switch , 1 Capacitor', '1 Wire', 100, 300, '2021-08-04'),
(9, 1001, 102, '1 Switch , 1 Capacitor', '1 Wire', 100, 300, '2021-08-12'),
(10, 1001, 102, '1 Switch , 1 Capacitor', '1 Wire', 100, 300, '2021-08-12'),
(11, 1001, 102, '1 Switch , 1 Capacitor', '1 Wire', 100, 300, '2021-08-12'),
(12, 1001, 102, '1 Switch , 1 Capacitor', '1 Wire', 100, 300, '2021-08-12'),
(13, 1001, 102, '1 Switch , 1 Capacitor', '1 Wire', 100, 300, '2021-08-12'),
(14, 1001, 102, '1 Switch , 1 Capacitor', '1 Wire', 100, 300, '2021-08-12'),
(15, 1001, 102, '1 Switch , 1 Capacitor', '1 Wire', 100, 300, '2021-08-12'),
(16, 1001, 102, '1 Switch , 1 Capacitor', '1 Wire', 100, 300, '2021-08-04'),
(17, 1001, 102, '1 Switch , 1 Capacitor', '1 Wire', 100, 300, '2021-08-10'),
(18, 1001, 102, '1 Switch , 1 Capacitor', '1 Wire', 100, 300, '2021-08-10'),
(19, 1002, 102, '1 Switch , 1 Capacitor', '1 Wire', 100, 300, '2021-08-15'),
(20, 1002, 102, '1 Switch , 1 Capacitor', '1 Wire', 100, 300, '2021-08-15'),
(21, 1001, 104, '1 Switch , 1 Capacitor', '1 Wire', 1000, 1500, '2021-08-03'),
(22, 1001, 102, '', '1200', 1200, 1800, '2021-08-12'),
(23, 1001, 102, '', '', 0, 0, '2021-06-09'),
(24, 1001, 102, '1 Switch , 1 Capacitor', '1 Wire', 1200, 1800, '2021-08-09'),
(25, 1001, 102, '1', '1 Wire', 1300, 2100, '2021-02-10'),
(26, 1003, 103, '1 Switch', '1 Fan', 1800, 1000, '2021-07-06'),
(27, 1003, 101, '2 Fan', '2 Switch', 500, 2000, '2021-06-01'),
(28, 1003, 104, '1 Switch , 1 Capacitor', '1 Wire', 300, 1200, '2021-06-11');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`Login`),
  ADD UNIQUE KEY `Email` (`Email`);

--
-- Indexes for table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `work`
--
ALTER TABLE `work`
  ADD PRIMARY KEY (`WorkID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `client`
--
ALTER TABLE `client`
  MODIFY `ID` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1004;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `ID` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=107;

--
-- AUTO_INCREMENT for table `work`
--
ALTER TABLE `work`
  MODIFY `WorkID` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
