-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 04 Cze 2020, 18:23
-- Wersja serwera: 10.4.11-MariaDB
-- Wersja PHP: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `lotnisko`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `lot`
--

CREATE TABLE `lot` (
  `Nazwa_lotu` varchar(255) NOT NULL,
  `Numer_rejestracyjny` varchar(20) NOT NULL,
  `Model_samolotu` varchar(50) NOT NULL,
  `Godzina_odlotu` varchar(20) NOT NULL,
  `Godzina_przylotu` varchar(20) NOT NULL,
  `Bramka` varchar(20) NOT NULL,
  `Destynacja` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `lot`
--

INSERT INTO `lot` (`Nazwa_lotu`, `Numer_rejestracyjny`, `Model_samolotu`, `Godzina_odlotu`, `Godzina_przylotu`, `Bramka`, `Destynacja`) VALUES
('AF7777', 'L190', 'airbus a380', '19/6/18 13:55:26', '19/6/18 15:55:26', 'A21', 'Madryt'),
('LF0021', 'K212', 'boeing 777', '25/6/20 03:00:00', '25/6/20 22:40:00', 'A10', 'Kapsztad'),
('RY1082', 'L191', 'airbus a380', '25/6/20 11:03:26', '25/6/20 15:40:26', 'A22', 'Londyn'),
('RY1112', 'L293', 'Airbus A340', '25/6/20 20:00:00', '25/6/20 23:40:00', 'A22', 'Londyn'),
('RY2135', 'L294', 'Airbus A380', '25/6/20 07:00:00', '25/6/20 18:40:00', 'A10', 'Nowy Jork');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pasazer`
--

CREATE TABLE `pasazer` (
  `Numer_biletu` int(255) NOT NULL,
  `Imie` varchar(20) NOT NULL,
  `Nazwisko` varchar(30) NOT NULL,
  `Nazwa_lotu` varchar(20) NOT NULL,
  `Typ_bagazu` varchar(20) NOT NULL,
  `Status_odprawy` varchar(20) NOT NULL,
  `Numer_fotela` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `pasazer`
--

INSERT INTO `pasazer` (`Numer_biletu`, `Imie`, `Nazwisko`, `Nazwa_lotu`, `Typ_bagazu`, `Status_odprawy`, `Numer_fotela`) VALUES
(34, 'Ewa', 'Kowalska', 'LF0021', ' checked baggage', 'Checked in', 46),
(100, 'Maciej', 'Doktor', 'AF7777', 'None', 'Checked in', 23),
(245, 'Jan', 'Duda', 'RY1112', 'None', 'Checked in', 74),
(342, 'Anna', 'Komnena', 'RY1082', 'None', 'Checked in', 84),
(921, 'Adam', 'Nowak', 'RY1112', 'None', 'Checked in', 21);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `lot`
--
ALTER TABLE `lot`
  ADD PRIMARY KEY (`Nazwa_lotu`);

--
-- Indeksy dla tabeli `pasazer`
--
ALTER TABLE `pasazer`
  ADD PRIMARY KEY (`Numer_biletu`),
  ADD KEY `Nazwa_lotu` (`Nazwa_lotu`);

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `pasazer`
--
ALTER TABLE `pasazer`
  ADD CONSTRAINT `pasazer_ibfk_1` FOREIGN KEY (`Nazwa_lotu`) REFERENCES `lot` (`Nazwa_lotu`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
