-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2020-06-20 05:46:59
-- 服务器版本： 10.4.11-MariaDB
-- PHP 版本： 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `bookdb`
--

-- --------------------------------------------------------

--
-- 表的结构 `admin`
--

CREATE TABLE `admin` (
  `a_id` varchar(5) NOT NULL,
  `a_passwd` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `admin`
--

INSERT INTO `admin` (`a_id`, `a_passwd`) VALUES
('15547', '22447865'),
('89564', '189651');

-- --------------------------------------------------------

--
-- 表的结构 `book`
--

CREATE TABLE `book` (
  `isbn` varchar(30) NOT NULL,
  `book_name` varchar(100) NOT NULL,
  `book_type` varchar(50) NOT NULL,
  `author` varchar(40) NOT NULL,
  `publisher` varchar(40) NOT NULL,
  `price` float NOT NULL,
  `publish_time` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `book`
--

INSERT INTO `book` (`isbn`, `book_name`, `book_type`, `author`, `publisher`, `price`, `publish_time`) VALUES
('9787020125265', '方向', '文学', '马克-安托万·马修 ', '后浪丨北京联合出版公司', 99.8, 2017),
('9787111126768', '经济学原理（上下）', '经济', '[美] 曼昆 ', '机械工业出版社', 88, 2003),
('9787501162734', '追寻生命的意义', '文学', '[奥] 维克多·弗兰克 ', '新华出版社', 12, 2003),
('9787505414709', '何以笙箫默', '文化', '顾漫 ', '朝华出版社', 15, 2007),
('9787508647357', '人类简史', '历史地理', '[以色列] 尤瓦尔·赫拉利 ', '中信出版社', 68, 2014),
('9787513325745', '控方证人', '文学', '阿加莎·克里斯蒂 ', '新星出版社', 35, 2017),
('9787530216835', '大雪中的山庄', '文学', '东野圭吾 ', '北京十月文艺出版社', 35, 2017),
('9787530216859', '造彩虹的人', '文学', '东野圭吾 ', '北京十月文艺出版社', 39.5, 2017),
('9787539943893', '11处特工皇妃', '文化', '潇湘冬儿', '江苏文艺出版社', 74.8, 2011),
('9787544138000', '三生三世 十里桃花', '文化', '唐七公子 ', '沈阳出版社', 26.8, 2009),
('9787550252585', '秘密花园', '文学', '乔汉娜·贝斯福 ', '北京联合出版公司', 42, 2015),
('9787550265608', '画的秘密', '文学', '马克-安托万·马修 ', '北京联合出版公司·后浪出版公司', 60, 2016),
('9787801656087', '明朝那些事儿（1-9）', '历史地理', '当年明月 ', '中国海关出版社', 358.2, 2009),
('9787807023777', '少有人走的路', '文学', 'M·斯科特·派克 ', '吉林文史出版社', 26, 2007);

-- --------------------------------------------------------

--
-- 表的结构 `borrow`
--

CREATE TABLE `borrow` (
  `b_id` varchar(10) NOT NULL,
  `isbn` varchar(30) NOT NULL,
  `r_id` varchar(10) NOT NULL,
  `borrow_time` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `borrow`
--

INSERT INTO `borrow` (`b_id`, `isbn`, `r_id`, `borrow_time`) VALUES
('12045', '9787550265608', '25123', '2020-06-19'),
('13456', '9787544138000', '07582', '2020-06-19'),
('13516', '9787801656087', '25123', '2020-06-19'),
('17102', '9787020125265', '06895', '2020-06-19'),
('21541', '9787550252585', '07589', '2020-06-19'),
('22343', '9787513325745', '06895', '2020-06-19'),
('23992', '9787530216835', '07582', '2020-06-19'),
('38382', '9787539943893', '07582', '2020-06-19'),
('51159', '9787508647357', '06895', '2020-06-19'),
('54451', '9787501162734', '06895', '2020-06-19'),
('65004', '9787807023777', '25123', '2020-06-19');

-- --------------------------------------------------------

--
-- 表的结构 `reader`
--

CREATE TABLE `reader` (
  `r_id` varchar(10) NOT NULL,
  `r_passwd` varchar(128) NOT NULL,
  `reader_name` varchar(20) NOT NULL,
  `sex` varchar(4) NOT NULL,
  `max_previlige` int(11) NOT NULL,
  `previlige` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `reader`
--

INSERT INTO `reader` (`r_id`, `r_passwd`, `reader_name`, `sex`, `max_previlige`, `previlige`) VALUES
('06834', '895421', 'Foxer', 'M', 3, 0),
('06895', '189456', 'Amy', 'F', 5, 1),
('07582', '123789', 'Jack', 'M', 3, 1),
('07589', '123456', 'Harry', 'M', 3, 1),
('07598', '46589', 'Emma', 'F', 3, 0),
('25123', '596553', 'Toby', 'M', 3, 1),
('52718', '456314', 'John', 'M', 3, 1);

--
-- 转储表的索引
--

--
-- 表的索引 `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`a_id`);

--
-- 表的索引 `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`isbn`);

--
-- 表的索引 `borrow`
--
ALTER TABLE `borrow`
  ADD PRIMARY KEY (`b_id`),
  ADD KEY `isbn` (`isbn`),
  ADD KEY `r_id` (`r_id`);

--
-- 表的索引 `reader`
--
ALTER TABLE `reader`
  ADD PRIMARY KEY (`r_id`);

--
-- 限制导出的表
--

--
-- 限制表 `borrow`
--
ALTER TABLE `borrow`
  ADD CONSTRAINT `borrow_ibfk_1` FOREIGN KEY (`isbn`) REFERENCES `book` (`isbn`),
  ADD CONSTRAINT `borrow_ibfk_2` FOREIGN KEY (`r_id`) REFERENCES `reader` (`r_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;