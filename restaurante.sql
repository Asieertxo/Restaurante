-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 21-10-2022 a las 00:21:54
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
-- Estructura de tabla para la tabla `carta`
--

DROP TABLE IF EXISTS `carta`;
CREATE TABLE IF NOT EXISTS `carta` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `categoria` enum('plato','hamburguesa','bebida','postre') DEFAULT 'plato',
  `descripcion` varchar(500) DEFAULT NULL,
  `alergenos` enum('free','gluten','lactosa','gluten/lactosa') DEFAULT 'free',
  `precio` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `carta`
--

INSERT INTO `carta` (`id`, `nombre`, `categoria`, `descripcion`, `alergenos`, `precio`) VALUES
(1, 'Clásica', 'hamburguesa', 'Carne de vacuno, queso cheddar, lechuga, tomate y cebolla en pan brioche tostado con dos sésamos.', 'gluten/lactosa', 11.4),
(2, 'Asier', 'hamburguesa', 'Pan brioche potato roll artesano, 200gr de txuleton Tripe, Barbacoa, doble de queso chedar en cada carne, bacon crujiente, huevo y cebolla extracaramelizada', 'gluten/lactosa', 17.8),
(3, 'Vegan', 'hamburguesa', 'Hamburguesa vegana de quinoa, zanahoria y puerro con aguacate, pimientos asados, salsa sweet chili, tomate y lechuga en pan de cristal.', 'gluten', 15.8),
(4, 'Chicken', 'hamburguesa', 'Pollo crujiente, salsa BBQ chipotle sobre tomate, lechuga, pepinillo y salsa baconesa en pan brioche tostado con dos sésamos.', 'gluten/lactosa', 13.6),
(5, 'Venom', 'hamburguesa', 'Pan brioche potato roll artesano negro con tinta de calamar y semillas, 200gr de txuleton, nuestra mostaza dulce con cebolla pochada triturada, doble de queso cheddar, papada adobada, panceta a baja temperatura y glaseada con sirope de arce y un poco de salsa barbacoa', 'gluten', 14.9),
(6, 'Azul', 'hamburguesa', 'Pan brioche potato roll artesano, queso azul, lechuga, tomate y cebolla en pan brioche tostado con dos sésamos.', 'gluten/lactosa', 14.9),
(7, 'Serrana', 'hamburguesa', 'Pan brioche potato roll artesano, queso manchego, jamon ibérico lechuga, tomate y cebolla en pan brioche tostado con dos sésamos.', 'gluten/lactosa', 14.9),
(8, 'Txuleta', 'hamburguesa', 'Pan brioche potato roll artesano, 200gr de txuleton Doble, Mayonesa, doble de queso ahumado scamorza en cada carne y cebolla extracaramelizada', 'gluten/lactosa', 14.9),
(9, 'AllFree', 'hamburguesa', 'Pan brioche sin gluten, queso sin lactosa, lechuga, tomate, cebolla', 'free', 15.3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `faqs`
--

DROP TABLE IF EXISTS `faqs`;
CREATE TABLE IF NOT EXISTS `faqs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `apellido` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `mensaje` varchar(5000) DEFAULT NULL,
  `likes` int DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `faqs`
--

INSERT INTO `faqs` (`id`, `nombre`, `apellido`, `email`, `mensaje`, `likes`, `fecha`) VALUES
(1, 'Asier', 'Garcia', 'asier@gmai.com', 'Mensaje de prueba', 2, '2022-10-21'),
(2, 'Juan', 'Perez', 'juan@gmail.com', 'Lorem Ipsum es simplemente un texto ficticio de la industria de la impresión y la composición tipográfica. Lorem Ipsum ha sido el texto ficticio estándar de la industria desde el año 1500, cuando un impresor desconocido tomó una galera de tipos y la codificó para hacer un libro de muestras tipográficas.', 1, '2022-10-21'),
(3, 'Pedro', 'Fernandez', 'pedro@gmail.com', 'Lorem Ipsum es simplemente un texto ficticio de la industria de la impresión y la composición tipográfica. Lorem Ipsum ha sido el texto ficticio estándar de la industria desde el año 1500, cuando un impresor desconocido tomó una galera de tipos y la codificó para hacer un libro de muestras tipográficas.', 1, '2022-10-21');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
