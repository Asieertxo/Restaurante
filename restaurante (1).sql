-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 12-10-2022 a las 17:51:08
-- Versión del servidor: 8.0.22
-- Versión de PHP: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `restaurante`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

DROP TABLE IF EXISTS `clientes`;
CREATE TABLE IF NOT EXISTS `clientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `pass` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id`, `nombre`, `email`, `pass`) VALUES
(1, 'Asier', 'asier@gmail.com', '1234');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

DROP TABLE IF EXISTS `empleados`;
CREATE TABLE IF NOT EXISTS `empleados` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `sueldo` float DEFAULT NULL,
  `restaurante` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `empleados_id` (`restaurante`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `menu`
--

DROP TABLE IF EXISTS `carta`;
CREATE TABLE IF NOT EXISTS `menu` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `categoria` enum('plato','hamburguesa','bebida','postre') DEFAULT 'plato',
  `descripcion` varchar(255) DEFAULT NULL,
  `alergenos` enum('free','gluten','lactosa','gluten/lactosa') DEFAULT 'free',
  `precio` float DEFAULT NULL,
  `img` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `menu`
--

INSERT INTO `carta` (`id`, `nombre`, `categoria`, `descripcion`, `alergenos`, `precio`, `img`) VALUES
(1, 'Clásica', 'hamburguesa', 'Carne de vacuno, queso cheddar, lechuga, tomate y cebolla en pan brioche tostado con dos sésamos.', 'gluten/lactosa', 11.4, 'Clásica.jpg'),
(2, 'Asier', 'hamburguesa', 'Doble carne de vacuno, huevo frito, queso estilo americano y cheddar fundidos, bacon  crujiente, salsa BBQ ahumada, cebolla caramelizada y salsa barbacoa en pan brioche tostado con dos sésamos.', 'gluten/lactosa', 17.8, 'Clásica.jpg'),
(3, 'Vegan', 'hamburguesa', 'Hamburguesa vegana de quinoa, zanahoria y puerro con aguacate, pimientos asados, salsa sweet chili, tomate y lechuga en pan de cristal.', 'gluten', 15.8, 'Clásica.jpg'),
(4, 'Chicken', 'hamburguesa', 'Pollo crujiente, salsa BBQ chipotle sobre tomate, lechuga, pepinillo y salsa baconesa en pan brioche tostado con dos sésamos.', 'gluten/lactosa', 13.6, 'Clásica.jpg'),
(5, 'Aguacate', 'hamburguesa', 'Pechuga de pollo a la plancha, aguacate, pomodoro seco, cebolla roja a la plancha, tomate, lechuga y salsa de yogur sin lactosa en pan de mollete.', 'gluten', 14.9, 'Clásica.jpg'),
(6, 'Azul', 'hamburguesa', 'Carne de vacuno, queso azul, lechuga, tomate y cebolla en pan brioche tostado con dos sésamos.', 'gluten/lactosa', 14.9, 'Clásica.jpg'),
(7, 'Serrana', 'hamburguesa', 'Carne de vacuno, queso manchego, jamon ibérico lechuga, tomate y cebolla en pan brioche tostado con dos sésamos.', 'gluten/lactosa', 14.9, 'Clásica.jpg'),
(8, 'North', 'hamburguesa', 'Carne de vacuno, queso cheddar, aros de cebolla, lechuga, tomate y cebolla en pan brioche tostado con dos sésamos.', 'gluten/lactosa', 14.9, 'Clásica.jpg'),
(9, 'AllFree', 'hamburguesa', 'Carne de vacuno, queso sin lactosa, lechuga, tomate, cebolla y bacon en pan sin gluten.', 'free', 15.3, 'Clásica.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `restaurante`
--

DROP TABLE IF EXISTS `restaurante`;
CREATE TABLE IF NOT EXISTS `restaurante` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ciudad` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD CONSTRAINT `empleados_id` FOREIGN KEY (`restaurante`) REFERENCES `restaurante` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
