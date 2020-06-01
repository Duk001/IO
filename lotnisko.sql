-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 01 Cze 2020, 22:54
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
