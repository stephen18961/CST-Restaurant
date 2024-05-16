-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 19, 2023 at 04:25 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cstresto`
--

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `category_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`category_id`, `name`) VALUES
(1, 'Food'),
(2, 'Beverage');

-- --------------------------------------------------------

--
-- Table structure for table `invoice`
--

CREATE TABLE `invoice` (
  `id` int(11) NOT NULL,
  `table_number` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `total_amount` int(11) NOT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `invoice`
--

INSERT INTO `invoice` (`id`, `table_number`, `created_at`, `total_amount`, `status_id`) VALUES
(15, 3, '2023-12-18 12:10:18', 67000, 3),
(16, 7, '2023-12-18 12:22:38', 67000, 3),
(17, 2, '2023-12-18 12:31:55', 70500, 3),
(18, 3, '2023-12-18 12:44:16', 112500, 3),
(19, 3, '2023-12-18 12:46:20', 67000, 3),
(20, 3, '2023-12-19 01:24:59', 42000, 3),
(21, 3, '2023-12-19 01:25:12', 61500, 3),
(22, 2, '2023-12-18 15:56:22', 67000, 1),
(23, 4, '2023-12-18 16:46:09', 59500, 3),
(24, 1, '2023-12-19 01:58:06', 32500, 3),
(25, 3, '2023-12-19 02:01:53', 48500, 3),
(26, 3, '2023-12-19 02:01:07', 192500, 1);

-- --------------------------------------------------------

--
-- Table structure for table `invoice_detail`
--

CREATE TABLE `invoice_detail` (
  `id` int(11) NOT NULL,
  `invoice_id` int(11) NOT NULL,
  `menu_item_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `invoice_detail`
--

INSERT INTO `invoice_detail` (`id`, `invoice_id`, `menu_item_id`) VALUES
(16, 15, 1),
(17, 15, 4),
(18, 16, 1),
(19, 16, 4),
(20, 17, 1),
(21, 17, 19),
(22, 17, 10),
(23, 18, 12),
(24, 18, 12),
(25, 18, 11),
(26, 19, 1),
(27, 19, 4),
(28, 20, 1),
(29, 20, 5),
(30, 21, 10),
(31, 21, 9),
(32, 22, 1),
(33, 22, 4),
(34, 23, 1),
(35, 23, 6),
(36, 24, 5),
(37, 24, 20),
(38, 25, 1),
(39, 25, 19),
(40, 26, 4),
(41, 26, 13);

-- --------------------------------------------------------

--
-- Table structure for table `menu_item`
--

CREATE TABLE `menu_item` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `price` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `image` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `menu_item`
--

INSERT INTO `menu_item` (`id`, `name`, `price`, `category_id`, `image`) VALUES
(1, 'Chicken Roll', 27500, 1, 'chicken_roll.jpg'),
(4, 'American Brunch (Full set)', 42500, 1, 'american_brunch_full_set.jpg'),
(5, 'French Toast', 17500, 1, 'french_toast.jpg'),
(6, 'Grilled Chicken Salad', 32000, 1, 'grilled_chicken_salad.jpg'),
(7, 'Gyudon Mentai', 55000, 1, 'gyudon_mentai.jpg'),
(8, 'Parmesan Fries', 20000, 1, 'parmesan_fries.jpg'),
(9, 'Salmon Avocado Salad', 36500, 1, 'salmon_avocado_salad.jpg'),
(10, 'Smores Pie Cake', 25000, 1, 'smores_pie_cake.jpg'),
(11, 'Spaghetti Carbonara', 27500, 1, 'spaghetti_carbonara.jpg'),
(12, 'Steak and French Fries', 42500, 1, 'steak_fries.jpg'),
(13, 'Toffe Nut Latte Cake', 150000, 1, 'toffe_nut_latte_cake.jpg'),
(15, 'Waffle with Ice Cream', 25000, 1, 'waffle_with_ice_cream.jpg'),
(19, 'Affogato', 21000, 2, 'affogato.jpg'),
(20, 'Cappucino', 15000, 2, 'cappucino.jpg'),
(21, 'Choco Banana Blended', 19000, 2, 'choco_banana_blended.jpg'),
(22, 'Green Tea Kitkat Blended', 24500, 2, 'green_tea_kitkat_blended.jpg'),
(23, 'Meeple Mojito Soda', 16000, 2, 'meeple_mojito_soda.jpg'),
(25, 'Speculous Blended', 22500, 2, 'speculous_bended.jpg'),
(27, 'Es teh manis', 5000, 2, 'esteh.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `status`
--

CREATE TABLE `status` (
  `id` int(11) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `status`
--

INSERT INTO `status` (`id`, `status`) VALUES
(1, 'Open'),
(2, 'Invoiced'),
(3, 'Closed');

-- --------------------------------------------------------

--
-- Table structure for table `table_status`
--

CREATE TABLE `table_status` (
  `id` int(11) NOT NULL,
  `occupied` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `table_status`
--

INSERT INTO `table_status` (`id`, `occupied`) VALUES
(1, 0),
(2, 1),
(3, 0),
(4, 0),
(5, 0),
(6, 0),
(7, 0),
(8, 0),
(9, 0),
(10, 0),
(11, 0),
(12, 0),
(13, 0),
(14, 0),
(15, 0),
(16, 0),
(17, 0),
(18, 0),
(19, 0),
(20, 0);

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

CREATE TABLE `transaction` (
  `id` int(11) NOT NULL,
  `invoice_id` int(11) NOT NULL,
  `payment_method` varchar(50) NOT NULL,
  `amount_paid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `transaction`
--

INSERT INTO `transaction` (`id`, `invoice_id`, `payment_method`, `amount_paid`) VALUES
(1, 1, 'Credit Card', 25),
(2, 2, 'Cash', 30),
(3, 3, 'Debit Card', 15),
(4, 15, 'CASH', 67000),
(5, 16, 'CASH', 67000),
(6, 17, 'CASH', 70500),
(7, 18, 'CASH', 112500),
(8, 19, 'CASH', 67000),
(9, 23, 'CASH', 59500),
(10, 20, 'CASH', 42000),
(11, 21, 'CASH', 61500),
(12, 24, 'CASH', 32500),
(13, 25, 'CASH', 48500);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`category_id`);

--
-- Indexes for table `invoice`
--
ALTER TABLE `invoice`
  ADD PRIMARY KEY (`id`),
  ADD KEY `status_id` (`status_id`);

--
-- Indexes for table `invoice_detail`
--
ALTER TABLE `invoice_detail`
  ADD PRIMARY KEY (`id`),
  ADD KEY `invoice_id` (`invoice_id`),
  ADD KEY `menu_item_id` (`menu_item_id`);

--
-- Indexes for table `menu_item`
--
ALTER TABLE `menu_item`
  ADD PRIMARY KEY (`id`),
  ADD KEY `category_id` (`category_id`);

--
-- Indexes for table `status`
--
ALTER TABLE `status`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `table_status`
--
ALTER TABLE `table_status`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transaction`
--
ALTER TABLE `transaction`
  ADD PRIMARY KEY (`id`),
  ADD KEY `invoice_id` (`invoice_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `invoice`
--
ALTER TABLE `invoice`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `invoice_detail`
--
ALTER TABLE `invoice_detail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT for table `menu_item`
--
ALTER TABLE `menu_item`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `status`
--
ALTER TABLE `status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `table_status`
--
ALTER TABLE `table_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `transaction`
--
ALTER TABLE `transaction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `invoice`
--
ALTER TABLE `invoice`
  ADD CONSTRAINT `invoice_ibfk_1` FOREIGN KEY (`status_id`) REFERENCES `status` (`id`);

--
-- Constraints for table `invoice_detail`
--
ALTER TABLE `invoice_detail`
  ADD CONSTRAINT `invoice_detail_ibfk_1` FOREIGN KEY (`invoice_id`) REFERENCES `invoice` (`id`),
  ADD CONSTRAINT `invoice_detail_ibfk_2` FOREIGN KEY (`menu_item_id`) REFERENCES `menu_item` (`id`);

--
-- Constraints for table `menu_item`
--
ALTER TABLE `menu_item`
  ADD CONSTRAINT `menu_item_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`category_id`);

--
-- Constraints for table `transaction`
--
ALTER TABLE `transaction`
  ADD CONSTRAINT `transaction_ibfk_1` FOREIGN KEY (`invoice_id`) REFERENCES `invoice` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
