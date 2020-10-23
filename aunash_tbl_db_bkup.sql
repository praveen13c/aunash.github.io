-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 23, 2020 at 10:03 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aunash`
--

-- --------------------------------------------------------

--
-- Table structure for table `aunash_content`
--

CREATE TABLE `aunash_content` (
  `index_content` text NOT NULL,
  `contact_content` text NOT NULL,
  `services_content` text NOT NULL,
  `blog_content` text NOT NULL,
  `vlog_content` text NOT NULL,
  `extra1_content` text NOT NULL,
  `extra2_content` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `cont_srno` int(12) NOT NULL,
  `cont_name` text NOT NULL,
  `cont_email` varchar(20) NOT NULL,
  `cont_phone_num` varchar(15) NOT NULL,
  `cont_message` text NOT NULL,
  `cont_date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`cont_srno`, `cont_name`, `cont_email`, `cont_phone_num`, `cont_message`, `cont_date`) VALUES
(1, 'Jay Ganesh', 'ganeshji@ganeshji.co', '9753740009', 'sabh shubh hoga .. \r\nsabh laabh hoga', '2020-10-22 08:26:26');

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

CREATE TABLE `post` (
  `post_srno` int(12) NOT NULL,
  `postr_title` text NOT NULL,
  `post_sub_title` text NOT NULL,
  `post_content` text NOT NULL,
  `post_by` text NOT NULL,
  `post_date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `post`
--

INSERT INTO `post` (`post_srno`, `postr_title`, `post_sub_title`, `post_content`, `post_by`, `post_date`) VALUES
(1, 'Shri Ganesh', 'Jay Ganesh Jay Ganesh', 'This site is multipurpose one, we provide various services like Editing videos, Cinematography, Photography, Web Development, Coding, Studio Hiring for Casting & Video Shoot & Portfolio Shoot, Voice Over, Sound Recording, Portfolio shoot, Casting, Tech Review, Fair Unboxing, Motivational Speaker', 'Praveen Singh Chauhan', '2020-10-22 12:17:53');

-- --------------------------------------------------------

--
-- Table structure for table `quotes`
--

CREATE TABLE `quotes` (
  `q_srno` int(12) NOT NULL,
  `q_content` text NOT NULL,
  `q_author` text NOT NULL,
  `q_date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `quotes`
--

INSERT INTO `quotes` (`q_srno`, `q_content`, `q_author`, `q_date`) VALUES
(1, 'Never Ever Give-up', 'Anonymous', '2020-10-22 12:19:54');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`cont_srno`);

--
-- Indexes for table `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`post_srno`);

--
-- Indexes for table `quotes`
--
ALTER TABLE `quotes`
  ADD PRIMARY KEY (`q_srno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `cont_srno` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `post`
--
ALTER TABLE `post`
  MODIFY `post_srno` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `quotes`
--
ALTER TABLE `quotes`
  MODIFY `q_srno` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
