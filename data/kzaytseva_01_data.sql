-- phpMyAdmin SQL Dump
-- version 4.4.14.1
-- http://www.phpmyadmin.net
--
-- Host: helios.arz.oeaw.ac.at
-- Generation Time: Sep 24, 2015 at 08:21 AM
-- Server version: 5.5.44-MariaDB
-- PHP Version: 5.4.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kzaytseva`
--


--
-- Dumping data for table `newModel_dc_country`
--

INSERT INTO `newModel_dc_country` (`id`, `name`, `original_name`, `authorityfile_id`) VALUES
(1, 'Turkey', 'Türkiye', NULL),
(2, 'Greece', 'Ελλάδα', NULL);

--
-- Dumping data for table `newModel_dc_region`
--


INSERT INTO `newModel_dc_region` (`id`, `name`, `original_name`, `authorityfile_id`, `country_id`) VALUES
(1, 'Anatolia/East Aegean', 'Anatolien/Ostägäis', NULL, 1),
(2, 'Crete', 'Kreta', NULL, NULL),
(4, 'Macedonia/Thrace', 'Makedonien/Thrakien', NULL, NULL),
(5, 'Southern and Central Greece, Cyclades', 'Süd- und Zentralgriechenland, Kykladen', NULL, NULL),
(6, 'Thessaly', 'Thessalien', NULL, NULL);


--
-- Dumping data for table `newModel_dc_province`
--

INSERT INTO `newModel_dc_province` (`id`, `name`, `original_name`, `authorityfile_id`, `region_id`) VALUES
(581, ' Adana ', ' Adana ', NULL, 1),
(582, ' Adiyaman ', ' Adıyaman ', NULL, 1),
(583, ' Afyon ', ' Afyonkarahisar ', NULL, 1),
(584, ' Agri ', ' Ağrı ', NULL, 1),
(585, ' Aksaray ', ' Aksaray ', NULL, 1),
(586, ' Amasya ', ' Amasya ', NULL, 1),
(587, ' Ankara ', ' Ankara ', NULL, 1),
(588, ' Antalya ', ' Antalya ', NULL, 1),
(589, ' Ardahan ', ' Ardahan ', NULL, 1),
(590, ' Artvin ', ' Artvin ', NULL, 1),
(591, ' Aydin ', ' Aydın ', NULL, 1),
(592, ' Balikesir ', ' Balıkesir ', NULL, 1),
(593, ' Bartin ', ' Bartın ', NULL, 1),
(594, ' Batman ', ' Batman ', NULL, 1),
(595, ' Bayburt ', ' Bayburt ', NULL, 1),
(596, ' Bilecik ', ' Bilecik ', NULL, 1),
(597, ' Bingol ', ' Bingöl ', NULL, 1),
(598, ' Bitlis ', ' Bitlis ', NULL, 1),
(599, ' Bolu ', ' Bolu ', NULL, 1),
(600, ' Burdur ', ' Burdur ', NULL, 1),
(601, ' Bursa ', ' Bursa ', NULL, 1),
(602, ' Canakkale ', ' Çanakkale ', NULL, 1),
(603, ' Cankiri ', ' Çankırı ', NULL, 1),
(604, ' Corum ', ' Çorum ', NULL, 1),
(605, ' Denizli ', ' Denizli ', NULL, 1),
(606, ' Diyarbakir ', ' Diyarbakır ', NULL, 1),
(607, ' Dodecanese ', ' Dodecanese ', NULL, 1),
(608, ' Duzce ', ' Düzce ', NULL, 1),
(609, ' Edirne ', ' Edirne ', NULL, 1),
(610, ' Elazig ', ' Elazığ ', NULL, 1),
(611, ' Erzincan ', ' Erzincan ', NULL, 1),
(612, ' Erzurum ', ' Erzurum ', NULL, 1),
(613, ' Eskisehir ', ' Eskişehir ', NULL, 1),
(614, ' Gaziantep ', ' Gaziantep ', NULL, 1),
(615, ' Giresun ', ' Giresun ', NULL, 1),
(616, ' Gumushane ', ' Gümüşhane ', NULL, 1),
(617, ' Hakkari ', ' Hakkari ', NULL, 1),
(618, ' Hatay ', ' Hatay ', NULL, 1),
(619, ' Igdir ', ' Iğdır ', NULL, 1),
(620, ' Isparta ', ' Isparta ', NULL, 1),
(621, ' Istanbul ', ' İstanbul ', NULL, 1),
(622, ' Izmir ', ' İzmir ', NULL, 1),
(623, ' Kahramanmaras ', ' Kahramanmaraş ', NULL, 1),
(624, ' Karabuk ', ' Karabük ', NULL, 1),
(625, ' Karaman ', ' Karaman ', NULL, 1),
(626, ' Kars ', ' Kars ', NULL, 1),
(627, ' Kastamonu ', ' Kastamonu ', NULL, 1),
(628, ' Kayseri ', ' Kayseri ', NULL, 1),
(629, ' Kilis ', ' Kilis ', NULL, 1),
(630, ' Kirikkale ', ' Kırıkkale ', NULL, 1),
(631, ' Kirklareli ', ' Kırklareli ', NULL, 1),
(632, ' Kirsehir ', ' Kırşehir ', NULL, 1),
(633, ' Kocaeli ', ' Kocaeli ', NULL, 1),
(634, ' Konya ', ' Konya ', NULL, 1),
(635, ' Kutahya ', ' Kütahya ', NULL, 1),
(636, ' Malatya ', ' Malatya ', NULL, 1),
(637, ' Manisa ', ' Manisa ', NULL, 1),
(638, ' Mardin ', ' Mardin ', NULL, 1),
(639, ' Mersin ', ' Mersin ', NULL, 1),
(640, ' Mugla ', ' Muğla ', NULL, 1),
(641, ' Mus ', ' Muş ', NULL, 1),
(642, ' Nevsehir ', ' Nevşehir ', NULL, 1),
(643, ' Nigde ', ' Niğde ', NULL, 1),
(644, ' Ordu ', ' Ordu ', NULL, 1),
(645, ' Osmaniye ', ' Osmaniye ', NULL, 1),
(646, ' Rize ', ' Rize ', NULL, 1),
(647, ' Sakarya ', ' Sakarya ', NULL, 1),
(648, ' Samsun ', ' Samsun ', NULL, 1),
(649, ' Sanliurfa ', ' Şanlıurfa ', NULL, 1),
(650, ' Siirt ', ' Siirt ', NULL, 1),
(651, ' Sinop ', ' Sinop ', NULL, 1),
(652, ' Sirnak ', ' Şırnak ', NULL, 1),
(653, ' Sivas ', ' Sivas ', NULL, 1),
(654, ' Tekirdag ', ' Tekirdağ ', NULL, 1),
(655, ' Tokat ', ' Tokat ', NULL, 1),
(656, ' Trabzon ', ' Trabzon ', NULL, 1),
(657, ' Tunceli ', ' Tunceli ', NULL, 1),
(658, ' Usak ', ' Uşak ', NULL, 1),
(659, ' Van ', ' Van ', NULL, 1),
(660, ' Yalova ', ' Yalova ', NULL, 1),
(661, ' Yozgat ', ' Yozgat ', NULL, 1),
(662, ' Zonguldak ', ' Zonguldak ', NULL, 1),
(663, ' Xanthos ', ' Xanthos ', NULL, 1),
(664, ' Samos –  Ikaria ', ' Samos –  Ikaria ', NULL, 1),
(665, ' Chios ', ' Chios ', NULL, 1),
(666, ' Lesvos/Lesbos ', ' Lesvos ', NULL, 1),
(667, ' Karditsa ', ' Karditsa ', NULL, 6),
(668, ' Larisa ', ' Larisa ', NULL, 6),
(669, ' Magnisia/Magnesia ', ' Magnisia ', NULL, 6),
(670, ' Trikala ', ' Trikala ', NULL, 6),
(671, ' Aetolia-Acarnania and Lefkada ', ' Aitoloakarnania kai Lefkada ', NULL, 5),
(672, ' Akhaia ', ' Akhaia ', NULL, 5),
(673, ' Arcadia ', ' Arkadia ', NULL, 5),
(674, ' Argolid ', ' Argolida ', NULL, 5),
(675, ' Arta ', ' Arta ', NULL, 5),
(676, ' Athens ', ' Athina ', NULL, 5),
(677, ' Boeotia ', ' Boiotia/Voiotias ', NULL, 5),
(678, ' Corfu ', ' Kerkyra ', NULL, 5),
(679, ' Corinthia ', ' Korinthia ', NULL, 5),
(680, ' Cyclades ', ' Kyklades ', NULL, 5),
(681, ' East Attika ', ' Anatoliki Attiki ', NULL, 5),
(682, ' Elis/Ilia ', ' Ileia ', NULL, 5),
(683, ' Euboea ', ' Evoia ', NULL, 5),
(684, ' Ioannina ', ' Ioannina ', NULL, 5),
(685, ' Kephallinia ', ' Kephallinia ', NULL, 5),
(686, ' Laconia ', ' Lakonia ', NULL, 5),
(687, ' Messinia/Messenia ', ' Messinia ', NULL, 5),
(688, ' Phocis ', ' Phokida ', NULL, 5),
(689, ' Phthiotis and Evritania ', ' Phthiotida kai Evrytania ', NULL, 5),
(690, ' Preveza ', ' Preveza ', NULL, 5),
(691, ' Thesprotia ', ' Thesprotia ', NULL, 5),
(692, ' Western Attica, Piraeus and islands ', ' Dytiki Attiki, Pireas kai Nisia ', NULL, 5),
(693, ' Zakynthos ', ' Zakynthos ', NULL, 5),
(694, ' Chalcidice and Mount Athos ', ' Chalkidiki kai Agion Orous ', NULL, 4),
(695, ' City of Thessaloniki ', ' Poli Thessaloniki ', NULL, 4),
(696, ' Drama ', ' Drama ', NULL, 4),
(697, ' Evros ', ' Evros ', NULL, 4),
(698, ' Florina ', ' Phlorina ', NULL, 4),
(699, ' Grevena ', ' Grevena ', NULL, 4),
(700, ' Imathia ', ' Imathia ', NULL, 4),
(701, ' Kastoria ', ' Kastoria ', NULL, 4),
(702, ' Kavala – Thasos ', ' Kavala – Thasos ', NULL, 4),
(703, ' Kilkis ', ' Kilkis ', NULL, 4),
(704, ' Kozani ', ' Kozani ', NULL, 4),
(705, ' Pella  ', ' Pella ', NULL, 4),
(706, ' Periphery Thessaloniki ', ' Peripheria Thessaloniki ', NULL, 4),
(707, ' Pieria ', ' Pieria ', NULL, 4),
(708, ' Rodopi ', ' Rodopi ', NULL, 4),
(709, ' Serres ', ' Serres ', NULL, 4),
(710, ' Iraklio ', ' Irakleio ', NULL, 2),
(711, ' Khania ', ' Khania ', NULL, 2),
(712, ' Lasithi ', ' Lasithios ', NULL, 2),
(713, ' Rethymno ', ' Rethymno ', NULL, 2);

--
-- Dumping data for table `newModel_dc_area_agegroups`
--

INSERT INTO `newModel_dc_area_agegroups` (`id`, `name`) VALUES
(1, 'neonate '),
(2, 'infans I (0-6)'),
(3, 'infans II (7-12)'),
(4, 'juvenile (13-18)'),
(5, 'adult (19-40)'),
(6, 'adult-mature (19-45)'),
(7, 'mature (41-60)'),
(8, 'mature-senile (51-70)'),
(9, 'senile (60-)'),
(10, 'not recorded'),
(11, 'part of specialist report'),
(12, 'immature'),
(13, 'mature'),
(14, 'children'),
(15, 'adults');

--
-- Dumping data for table `newModel_dc_area_areatype`
--

INSERT INTO `newModel_dc_area_areatype` (`id`, `name`) VALUES
(1, 'quarry'),
(2, 'settlement'),
(3, 'cave or rockshelter'),
(4, 'cemetery or grave');

--
-- Dumping data for table `newModel_dc_area_buildingtechnique`
--

INSERT INTO `newModel_dc_area_buildingtechnique` (`id`, `name`) VALUES
(1, 'mud brick'),
(2, 'pavement'),
(3, 'pisé'),
(4, 'plaster wall'),
(5, 'stone socket'),
(6, 'wattle and daub');

--
-- Dumping data for table `newModel_dc_area_caverockshelterstype`
--

INSERT INTO `newModel_dc_area_caverockshelterstype` (`id`, `name`) VALUES
(1, 'cave'),
(2, 'rock shelter');

--
-- Dumping data for table `newModel_dc_area_constructiontype`
--

INSERT INTO `newModel_dc_area_constructiontype` (`id`, `name`) VALUES
(1, 'apsidal '),
(2, 'circular'),
(3, 'one-room'),
(4, 'rectangular'),
(5, 'Tsangli house');

--
-- Dumping data for table `newModel_dc_area_evidenceofgraveshumanremains`
--

INSERT INTO `newModel_dc_area_evidenceofgraveshumanremains` (`id`, `name`) VALUES
(1, 'not present'),
(2, 'present');

--
-- Dumping data for table `newModel_dc_area_evidenceofoccupation`
--

INSERT INTO `newModel_dc_area_evidenceofoccupation` (`id`, `name`) VALUES
(1, 'fire place'),
(2, 'storage facilities'),
(3, 'post-hole'),
(4, 'stone setting'),
(5, 'pit');

--
-- Dumping data for table `newModel_dc_area_exploitationtype`
--

INSERT INTO `newModel_dc_area_exploitationtype` (`id`, `name`) VALUES
(1, 'pinge'),
(2, 'shaft mining'),
(3, 'surface');

--
-- Dumping data for table `newModel_dc_area_gravetype`
--

INSERT INTO `newModel_dc_area_gravetype` (`id`, `name`) VALUES
(1, 'cist grave'),
(2, 'pit grave'),
(3, 'vessel'),
(4, 'none recorded');

--
-- Dumping data for table `newModel_dc_area_manipulationofgraves`
--

INSERT INTO `newModel_dc_area_manipulationofgraves` (`id`, `name`) VALUES
(1, 'consecutive burials'),
(2, 'construction of settlement'),
(3, 'looting'),
(4, 'none recorded');

--
-- Dumping data for table `newModel_dc_area_mortuaryfeatures`
--

INSERT INTO `newModel_dc_area_mortuaryfeatures` (`id`, `name`) VALUES
(1, 'pyre'),
(2, 'separating wall'),
(3, 'platform');

--
-- Dumping data for table `newModel_dc_area_rawmaterial`
--

INSERT INTO `newModel_dc_area_rawmaterial` (`id`, `name`) VALUES
(1, 'obsidian'),
(2, 'copper'),
(3, 'limestone'),
(4, 'flint'),
(5, 'chert'),
(6, 'clay');

--
-- Dumping data for table `newModel_dc_area_settlementstructure`
--

INSERT INTO `newModel_dc_area_settlementstructure` (`id`, `name`) VALUES
(1, ' enclosure: ditch '),
(2, ' enclosure: rampart '),
(3, ' enclosure: wall '),
(4, ' houses: free-standing '),
(5, ' houses: agglutinated '),
(6, ' houses: radial '),
(7, ' enclosure: undetermined ');

--
-- Dumping data for table `newModel_dc_area_settlementtype`
--

INSERT INTO `newModel_dc_area_settlementtype` (`id`, `name`) VALUES
(1, 'lowland'),
(2, 'tell'),
(3, 'tepe');

--
-- Dumping data for table `newModel_dc_area_sexes`
--

INSERT INTO `newModel_dc_area_sexes` (`id`, `name`) VALUES
(1, 'male individuals'),
(2, 'female individuals'),
(3, 'not specified'),
(4, 'part of specialist report');

--
-- Dumping data for table `newModel_dc_area_specialfeatures`
--

INSERT INTO `newModel_dc_area_specialfeatures` (`id`, `name`) VALUES
(1, 'bench'),
(2, 'channel'),
(3, 'hearth'),
(4, 'pit'),
(5, 'post-hole'),
(6, 'stone setting'),
(7, 'storage building'),
(8, 'storage pit'),
(9, 'storage vessel'),
(10, 'well'),
(11, 'oven');

--
-- Dumping data for table `newModel_dc_area_topography`
--

INSERT INTO `newModel_dc_area_topography` (`id`, `name`) VALUES
(1, 'intra mural'),
(2, 'extra mural'),
(3, 'in cave'),
(4, 'next to cave'),
(5, 'part of house');

--
-- Dumping data for table `newModel_dc_area_typeofhumanremains`
--

INSERT INTO `newModel_dc_area_typeofhumanremains` (`id`, `name`) VALUES
(1, 'cremations'),
(2, 'inhumations: complete bodies'),
(3, 'secondary deposition');

--
-- Dumping data for table `newModel_dc_chronological_system`
--

INSERT INTO `newModel_dc_chronological_system` (`id`, `cs_name`, `period_name`, `start_date1_BC`, `start_date2_BC`, `end_date1_BC`, `end_date2_BC`, `region_id`) VALUES
(1, 'Anatolia', 'Pre-Pottery Neolithic  ', 8000, 8000, 7500, 7500, 1),
(2, 'Anatolia', 'Pre-Pottery Neolithic/Neolithic', 7500, 7500, 7000, 7000, 1),
(3, 'Anatolia', 'Neolithic I', 7000, 7000, 6500, 6500, 1),
(4, 'Anatolia', 'Neolithic II', 6500, 6500, 6000, 6000, 1),
(5, 'Anatolia', 'Early Chalcolithic', 6000, 6000, 5500, 5500, 1),
(6, 'Anatolia', 'Middle Chalcolithic', 5500, 5500, 4250, 4250, 1),
(7, 'Anatolia', 'Late Chalcolithic I', 4250, 4250, 4000, 4000, 1),
(8, 'Anatolia', 'Late Chalcolithic II', 4000, 4000, 3500, 3500, 1),
(9, 'Anatolia', 'Late Chalcolithic III', 3500, 3500, 3000, 3000, 1),
(10, 'Alram-Stern 1996', 'Aceramic Neolithic (?)', 7000, 7000, 6500, 6500, 5),
(11, 'Alram-Stern 1997', 'Early Neolithic', 6500, 6500, 5800, 5800, 5),
(12, 'Alram-Stern 1998', 'Middle Neolithic', 5800, 5800, 5400, 5400, 5),
(13, 'Alram-Stern 1999', 'Late Neolithic (Early)', 5400, 5400, 4900, 4900, 5),
(14, 'Alram-Stern 2000', 'Late Neolithic (Late)', 4900, 4900, 4500, 4300, 5),
(15, 'Alram-Stern 2001', 'Chalcolithic/Final Neolithic', 4500, 4300, 3700, 3700, 5),
(16, 'Alram-Stern 2002', 'Chalcolithic/Final Neolithic (Late)', 3700, 3700, 3300, 3300, 5),
(17, 'Alram-Stern 2003', 'Early Helladic I/Early Cycladic', 3300, 3300, 2900, 2900, 5),
(18, 'K. Gallis in: Papathanassopoulous 1996 (Fig. 3)', 'Early Neolithic: "Protosesklo"', 6500, 6500, 5800, 5800, 6),
(19, 'K. Gallis in: Papathanassopoulous 1996 (Fig. 3)', 'Middle Neolithic: "Sesklo"', 5800, 5800, 5400, 5400, 6),
(20, 'K. Gallis in: Papathanassopoulous 1996 (Fig. 3)', 'Late Neolithic: Tsangli, Arapi', 5400, 5400, 4900, 4900, 6),
(21, 'K. Gallis in: Papathanassopoulous 1996 (Fig. 3)', 'Late Neolithic: Dimini', 4900, 4900, 4500, 4300, 6),
(22, 'K. Gallis in: Papathanassopoulous 1996 (Fig. 3)', 'Chalcolithic/Final Neolithic, Rachmani', 4500, 4300, 3700, 3700, 6),
(23, 'K. Gallis in: Papathanassopoulous 1996 (Fig. 3)', 'Chalcolithic/Final Neolithic (Late)', 3700, 3700, 3300, 3300, 6),
(24, 'K. Gallis in: Papathanassopoulous 1996 (Fig. 3)', 'Early Bronze Age', 3300, 3300, 2900, 2900, 6),
(25, 'Macedonia/Thrace', 'Late Neolithic', 5800, 5800, 4900, 4900, 4),
(26, 'Macedonia/Thrace', 'Chalcolithic', 4900, 4900, 3300, 3300, 4),
(27, 'Macedonia/Thrace', 'Early Bronze Age', 3300, 3300, 2900, 2900, 4),
(28, 'Evans/Vagnetti', 'Aceramic Neolithic ', 7000, 7000, 6500, 6500, 2),
(29, 'Evans/Vagnetti', 'Early Neolithic I', 6500, 6500, 4900, 4900, 2),
(30, 'Evans/Vagnetti', 'Early Neolithic II + Middle Neolithic', 4900, 4900, 4500, 4300, 2),
(31, 'Evans/Vagnetti', 'Late Neolithic', 4500, 4300, 3700, 3700, 2),
(32, 'Evans/Vagnetti', 'Final Neolithic', 3700, 3700, 2900, 2900, 2),
(33, 'Tomkins 2007a', 'Initial Neolithic', 7000, 7000, 6500, 6500, 2),
(34, 'Tomkins 2007a', 'Early Neolithic', 6500, 6500, 5800, 5800, 2),
(35, 'Tomkins 2007a', 'Middle Neolithic', 5800, 5800, 5400, 5400, 2),
(36, 'Tomkins 2007a', 'Late Neolithic I', 5400, 5400, 4900, 4900, 2),
(37, 'Tomkins 2007a', 'Late Neolithic II + Final Neolithic IA', 4900, 4900, 4500, 4300, 2),
(38, 'Tomkins 2007a', 'Final Neolithic IB + Final Neolithic II', 4500, 4300, 3700, 3700, 2),
(39, 'Tomkins 2007a', 'Final Neolithic III', 3700, 3700, 3300, 3300, 2),
(40, 'Tomkins 2007a', 'Final Neolithic IV', 3300, 3300, 2900, 2900, 2);


--
-- Dumping data for table `newModel_dc_finds_amount`
--

INSERT INTO `newModel_dc_finds_amount` (`id`, `name`) VALUES
(1, '1'),
(2, '2-5'),
(3, '6-10'),
(4, '11-20'),
(5, '21-50'),
(6, '51-100'),
(7, '101-250'),
(8, '251-300'),
(9, '301-500'),
(10, '501-1000'),
(11, '1001-5000'),
(12, '5001-10000'),
(13, '10001 and more');

--
-- Dumping data for table `newModel_dc_finds_animal_remains_completeness`
--

INSERT INTO `newModel_dc_finds_animal_remains_completeness` (`id`, `name`) VALUES
(1, 'complete  '),
(2, 'incomplete');

--
-- Dumping data for table `newModel_dc_finds_animal_remains_part`
--

INSERT INTO `newModel_dc_finds_animal_remains_part` (`id`, `name`) VALUES
(1, 'skull'),
(2, 'hindlimb'),
(3, 'forelimb'),
(4, 'extremity'),
(5, 'body '),
(6, 'jaw'),
(7, 'horn'),
(8, 'antler'),
(9, 'unknown'),
(10, 'claw');

--
-- Dumping data for table `newModel_dc_finds_animal_remains_species`
--

INSERT INTO `newModel_dc_finds_animal_remains_species` (`id`, `name`, `latin_name`) VALUES
(1, 'wild boar', 'Sus scrofa\r\n'),
(2, 'pig', 'Sus scrofa domesticus\r\n'),
(3, 'cattle', 'Bos taurus\r\n'),
(4, 'aurochs', 'Bos primigenius\r\n'),
(5, 'sheep/goat', 'Ovis/Capra\r\n'),
(6, 'sheep', 'Ovis aries\r\n'),
(7, 'wild sheep', 'Ovis orientalis\r\n'),
(8, 'goat', 'Capra hircus\r\n'),
(9, 'wild goat', 'Capra aegagrus\r\n'),
(10, 'dog', 'Canis familiaris\r\n'),
(11, 'horse', 'Equus caballus\r\n'),
(12, 'hare', 'Lepus europaeus\r\n'),
(13, 'red deer', 'Cervus elaphus\r\n'),
(14, 'fallow deer', 'Dama dama\r\n'),
(15, 'game', NULL),
(16, 'fish', NULL),
(17, 'molluscs', NULL),
(18, 'tuna', 'thunnus\r\n');

--
-- Dumping data for table `newModel_dc_finds_botany_species`
--

INSERT INTO `newModel_dc_finds_botany_species` (`id`, `name`, `latin_name`) VALUES
(1, 'apricot', 'Armeniaca vulgaris\r\n'),
(2, 'barley', 'Hordeum vulgare\r\n'),
(3, 'bitter vetch', 'Vicia ervilia\r\n'),
(4, 'broomcorn millet', 'Panicum miliaceum\r\n'),
(5, 'chickpea', 'Cicer arietinum\r\n'),
(6, 'einkorn wheat', 'Triticum monococcum\r\n'),
(7, 'emmer wheat', 'Triticum turgidum subsp. dicoccum\r\n'),
(8, 'fava bean', 'Vicia faba\r\n'),
(9, 'flax', 'Linum usitatissimum\r\n'),
(10, 'foxtail millet', 'Setaria italica\r\n'),
(11, 'grass pea', 'Lathyrus sativus\r\n'),
(12, 'hemp', 'Cannabis sativa\r\n'),
(13, 'lentil', 'Lens culinaris\r\n'),
(14, 'pea', 'Pisum sativum\r\n'),
(15, 'peach', 'Persica vulgaris\r\n'),
(16, 'poppy', 'Papaver somniferum\r\n'),
(17, 'rye', 'Secale cereale\r\n'),
(18, 'wild barley', 'Hordeum vulgare subsp. spontaneum\r\n'),
(19, 'wild bitter vetch', 'Vicia ervilia\r\n'),
(20, 'wild chickpea', 'Cicer reticulatum\r\n'),
(21, 'wild einkorn', 'Triticum monococcum subsp. baeoticum\r\n'),
(22, 'wild emmer', 'Triticum turgidum subsp. dicoccoides\r\n'),
(23, 'wild flax', 'Linum bienne\r\n'),
(24, 'wild lentil', 'Lens orientalis\r\n'),
(25, 'wild pea', 'Pisum humile\r\n');

--
-- Dumping data for table `newModel_dc_finds_lithics_core`
--

INSERT INTO `newModel_dc_finds_lithics_core` (`id`, `name`) VALUES
(1, 'core'),
(2, 'bullet core '),
(3, 'polyedric core'),
(4, 'bi-directional core'),
(5, 'uni-directional core'),
(6, 'alternated core'),
(7, 'bi-polar core'),
(8, 'flake-core'),
(9, 'blade-core');

--
-- Dumping data for table `newModel_dc_finds_lithics_debitage`
--

INSERT INTO `newModel_dc_finds_lithics_debitage` (`id`, `name`) VALUES
(1, 'flake'),
(2, 'blade '),
(3, 'debris '),
(4, 'splinter/non-flake ');

--
-- Dumping data for table `newModel_dc_finds_lithics_modified_tools`
--

INSERT INTO `newModel_dc_finds_lithics_modified_tools` (`id`, `name`) VALUES
(1, 'arrowhead'),
(2, 'blade: retouched'),
(3, 'flake: retouched'),
(4, 'non-flake: retouched'),
(5, 'burin '),
(6, 'denticulate'),
(7, 'drill '),
(8, 'projectile point '),
(9, 'perforator '),
(10, 'point '),
(11, 'side scraper '),
(12, 'end scraper '),
(13, 'trapeze'),
(14, 'notched = Spokeshave'),
(15, 'truncation'),
(16, 'double truncation');

--
-- Dumping data for table `newModel_dc_finds_lithics_technology`
--

INSERT INTO `newModel_dc_finds_lithics_technology` (`id`, `name`) VALUES
(1, 'bullet cores'),
(2, 'long blades'),
(3, 'percussion technology'),
(4, 'pressure technology ');

--
-- Dumping data for table `newModel_dc_finds_material`
--

INSERT INTO `newModel_dc_finds_material` (`id`, `name`) VALUES
(22, 'stone'),
(23, 'obsidian'),
(24, 'fabrics'),
(25, 'spondylusshell'),
(26, 'bone'),
(27, 'shell'),
(28, 'antler'),
(29, 'horn'),
(30, 'metal'),
(31, 'marble'),
(32, 'flint'),
(33, 'chert'),
(34, 'obsidian'),
(35, 'chalcedony'),
(36, 'jasper'),
(37, 'quartz'),
(38, 'rock crystal'),
(39, 'quartzite'),
(40, 'radiolarite'),
(41, 'clay');

--
-- Dumping data for table `newModel_dc_finds_pottery_decoration`
--

INSERT INTO `newModel_dc_finds_pottery_decoration` (`id`, `name`, `region`) VALUES
(1, ' Impressed ', ' Anatolia/East Aegean '),
(2, ' Crusted  ', ' Anatolia/East Aegean '),
(3, ' White on red  ', ' Anatolia/East Aegean '),
(4, ' Red on black  ', ' Anatolia/East Aegean '),
(5, ' Black on red  ', ' Anatolia/East Aegean '),
(6, ' Bead inlay ', ' Anatolia/East Aegean '),
(7, ' Incised   ', ' Anatolia/East Aegean '),
(8, ' Pattern burnished ', ' Anatolia/East Aegean '),
(9, ' Mat-impressed ', ' Anatolia/East Aegean '),
(10, ' Grooved ', ' Anatolia/East Aegean '),
(11, ' White  ', ' Anatolia/East Aegean '),
(12, ' Red slipped  ', ' Anatolia/East Aegean '),
(13, ' Black burnished  ', ' Anatolia/East Aegean '),
(14, ' Brown burnished ', ' Anatolia/East Aegean '),
(15, ' Black and red on cream (polychrome) (Β3β) ', ' Thessaly '),
(16, ' Black and red on white (polychrome) (Β3γ) ', ' Thessaly '),
(17, ' Black and white on red black (polychrome) (Β3β) ', ' Thessaly '),
(18, ' Black burnished “Larisa” (Γ1α; A5α/γ) ', ' Thessaly '),
(19, ' Black burnished with channeled decoration (Γ1α3) ', ' Thessaly '),
(20, ' Black burnished with white paint (Γ1α1) ', ' Thessaly '),
(21, ' Black on red (Β3α2b) ', ' Thessaly '),
(22, ' Black on white (B3α3) ', ' Thessaly '),
(23, ' Black pattern burnished (Γ1α2) ', ' Thessaly '),
(24, ' Brown on buff (matt painted) (Β3ε) ', ' Thessaly '),
(25, ' Brown on cream (B3α2a) ', ' Thessaly '),
(26, ' Crusted  ', ' Thessaly '),
(27, ' Grey on grey (Γ1β) ', ' Thessaly '),
(28, ' Impressed  (A2) ', ' Thessaly '),
(29, ' Incised (B2) ', ' Thessaly '),
(30, ' Incised  (Γ2) ', ' Thessaly '),
(31, ' Monochrome red (A1) ', ' Thessaly '),
(32, ' Monochrome undecorated (B1) ', ' Thessaly '),
(33, ' Red burnished (B1) ', ' Thessaly '),
(34, ' Red on white (A3ß) ', ' Thessaly '),
(35, ' Red (A3γ) ', ' Thessaly '),
(36, ' Scraped (A3ε)  ', ' Thessaly '),
(37, ' White on red (A3α) ', ' Thessaly '),
(38, ' White on red (Β3α1) ', ' Thessaly '),
(39, ' Black burnished  ', ' Southern/Central Greece, Cyclades '),
(40, ' Black on red  ', ' Southern/Central Greece, Cyclades '),
(41, ' Coarse Urfirnis  ', ' Southern/Central Greece, Cyclades '),
(42, ' Coarse  ', ' Southern/Central Greece, Cyclades '),
(43, ' Crusted  ', ' Southern/Central Greece, Cyclades '),
(44, ' Grooved  ', ' Southern/Central Greece, Cyclades '),
(45, ' Incised  ', ' Southern/Central Greece, Cyclades '),
(46, ' Matt painted  ', ' Southern/Central Greece, Cyclades '),
(47, ' Monochrome burnished  ', ' Southern/Central Greece, Cyclades '),
(48, ' Monochrome Urfirnis  ', ' Southern/Central Greece, Cyclades '),
(49, ' Pattern burnished ', ' Southern/Central Greece, Cyclades '),
(50, ' Patterned Urfirnis  ', ' Southern/Central Greece, Cyclades '),
(51, ' Plastic  ', ' Southern/Central Greece, Cyclades '),
(52, ' Polychrome  ', ' Southern/Central Greece, Cyclades '),
(53, ' Red on white  ', ' Southern/Central Greece, Cyclades '),
(54, ' Rippled  ', ' Southern/Central Greece, Cyclades '),
(55, ' Stroke-and pattern burnished ', ' Southern/Central Greece, Cyclades '),
(56, ' White on red  ', ' Southern/Central Greece, Cyclades '),
(57, ' White  ', ' Southern/Central Greece, Cyclades '),
(58, ' White on black ', ' Southern/Central Greece, Cyclades '),
(59, ' Barbotine  ', ' Macedonia/Thrace '),
(60, ' Black on red  ', ' Macedonia/Thrace '),
(61, ' Black topped  ', ' Macedonia/Thrace '),
(62, ' Brown on buff  ', ' Macedonia/Thrace '),
(63, ' Brown on red  ', ' Macedonia/Thrace '),
(64, ' Brown on cream  ', ' Macedonia/Thrace '),
(65, ' Burnished  ', ' Macedonia/Thrace '),
(66, ' Channeled  ', ' Macedonia/Thrace '),
(67, ' Coarse  ', ' Macedonia/Thrace '),
(68, ' Excised  ', ' Macedonia/Thrace '),
(69, ' Excised-with-graphite  ', ' Macedonia/Thrace '),
(70, ' Galepsos ware ', ' Macedonia/Thrace '),
(71, ' Graphite painted ', ' Macedonia/Thrace '),
(72, ' Gray lustre  ', ' Macedonia/Thrace '),
(73, ' Grooved  ', ' Macedonia/Thrace '),
(74, ' Grooved with graphite  ', ' Macedonia/Thrace '),
(75, ' Incised  ', ' Macedonia/Thrace '),
(76, ' Matt brown on white  ', ' Macedonia/Thrace '),
(77, ' Orange on orange  ', ' Macedonia/Thrace '),
(78, ' Plastic  ', ' Macedonia/Thrace '),
(79, ' Polychrome ', ' Macedonia/Thrace '),
(80, ' Red crusted  ', ' Macedonia/Thrace '),
(81, ' Red on brown  ', ' Macedonia/Thrace '),
(82, ' Red on white  ', ' Macedonia/Thrace '),
(83, ' Red slipped  ', ' Macedonia/Thrace '),
(84, ' Rippled  ', ' Macedonia/Thrace '),
(85, ' Rusticated ', ' Macedonia/Thrace '),
(86, ' Shell stamped ', ' Macedonia/Thrace '),
(87, ' White on red  ', ' Macedonia/Thrace '),
(88, ' Applied disc ', ' Macedonia/Thrace '),
(89, ' Barbotine  ', ' Crete '),
(90, ' Brushed  ', ' Crete '),
(91, ' Burnished  ', ' Crete '),
(92, ' Coarse  ', ' Crete '),
(93, ' Granulata ware ', ' Crete '),
(94, ' Grooved  ', ' Crete '),
(95, ' Impressed  ', ' Crete '),
(96, ' Incised  ', ' Crete '),
(97, ' Incised-Pointillé decoration ', ' Crete '),
(98, ' Monochrome  ', ' Crete '),
(99, ' Painted  ', ' Crete '),
(100, ' Pattern burnished  ', ' Crete '),
(101, ' Pattern jabbed  ', ' Crete '),
(102, ' Pellet decoration ', ' Crete '),
(103, ' Plastic cordon decoration ', ' Crete '),
(104, ' Plastic  ', ' Crete '),
(105, ' Pointillé decoration ', ' Crete '),
(106, ' Polished ', ' Crete '),
(107, ' Punched ', ' Crete '),
(108, ' Red on buff ', ' Crete '),
(109, ' Rippled burnished ', ' Crete '),
(110, ' Rippled  ', ' Crete '),
(111, ' Scored  ', ' Crete '),
(112, ' Scribble burnished  ', ' Crete '),
(113, ' Single jabbed ', ' Crete '),
(114, ' Wiped  ', ' Crete ');

--
-- Dumping data for table `newModel_dc_finds_pottery_detail`
--

INSERT INTO `newModel_dc_finds_pottery_detail` (`id`, `name`, `region`) VALUES
(1, ' Horned handle ', ' Anatolia/East Aegean '),
(2, ' Mushroom handle ', ' Anatolia/East Aegean '),
(3, ' Bar handle with lug ', ' Anatolia/East Aegean '),
(4, ' Rolled rim ', ' Anatolia/East Aegean '),
(5, ' Everted rim  ', ' Anatolia/East Aegean '),
(6, ' Flaring rim ', ' Anatolia/East Aegean '),
(7, ' Inside bevelled and decorated rim  ', ' Anatolia/East Aegean '),
(8, ' Rim contracting heavily inward ', ' Anatolia/East Aegean '),
(9, ' Foot ', ' Anatolia/East Aegean '),
(10, ' Narrow-mouthed rim ', ' Anatolia/East Aegean '),
(11, ' Elephant lug ', ' Thessaly '),
(12, ' Ledge lug ', ' Thessaly '),
(13, ' Leg ', ' Thessaly '),
(14, ' Spout ', ' Thessaly '),
(15, ' Strap handle ', ' Thessaly '),
(16, ' Tab handle ', ' Thessaly '),
(17, ' Vertically perforated lug ', ' Thessaly '),
(18, ' Rolled rim ', ' Thessaly '),
(19, ' Elephant lug ', ' Southern/Central Greece, Cyclades '),
(20, ' Ledge lug ', ' Southern/Central Greece, Cyclades '),
(21, ' Leg ', ' Southern/Central Greece, Cyclades '),
(22, ' Round bar handle ', ' Southern/Central Greece, Cyclades '),
(23, ' Spout ', ' Southern/Central Greece, Cyclades '),
(24, ' Strap handle ', ' Southern/Central Greece, Cyclades '),
(25, ' Tab handle ', ' Southern/Central Greece, Cyclades '),
(26, ' Tubular lug ', ' Southern/Central Greece, Cyclades '),
(27, ' Vertically perforated lug ', ' Southern/Central Greece, Cyclades '),
(28, ' Ear handle ', ' Macedonia/Thrace '),
(29, ' High strap handle ', ' Macedonia/Thrace '),
(30, ' Knobbed handle ', ' Macedonia/Thrace '),
(31, ' Ledge lug ', ' Macedonia/Thrace '),
(32, ' Leg ', ' Macedonia/Thrace '),
(33, ' Mushroom handle ', ' Macedonia/Thrace '),
(34, ' Prong handle ', ' Macedonia/Thrace '),
(35, ' Strap handle ', ' Macedonia/Thrace '),
(36, ' Stringhole lug ', ' Macedonia/Thrace '),
(37, ' Tab handle ', ' Macedonia/Thrace '),
(38, ' Tunnel lug ', ' Macedonia/Thrace '),
(39, ' Pedestal  ', ' Macedonia/Thrace '),
(40, ' Bridge spout ', ' Crete '),
(41, ' Concave flat base ', ' Crete '),
(42, ' Curved tapered-up rim ', ' Crete '),
(43, ' Ear handle ', ' Crete '),
(44, ' Flaring rim ', ' Crete '),
(45, ' Horned handle ', ' Crete '),
(46, ' Knobbed wishbone handle ', ' Crete '),
(47, ' Ledge lug ', ' Crete '),
(48, ' Leg ', ' Crete '),
(49, ' Miniature strap handle ', ' Crete '),
(50, ' Pronged wishbone handle ', ' Crete '),
(51, ' Strap handle with round hole ', ' Crete '),
(52, ' Strap handle ', ' Crete '),
(53, ' Tubular lug ', ' Crete '),
(54, ' V-shaped spout ', ' Crete '),
(55, ' “winged” strap handle ', ' Crete '),
(56, ' Wishbone handle ', ' Crete '),
(57, ' Tapered-up rim ', ' Crete '),
(58, ' Fenestrated pedestal ', ' Crete '),
(59, ' Flat base ', ' Crete '),
(60, ' Offset rim ', ' Crete '),
(61, ' Pedestal ', ' Crete '),
(62, ' Rounded base ', ' Crete '),
(63, ' Thickened rim ', ' Crete '),
(64, ' Small foot ', ' Crete ');

--
-- Dumping data for table `newModel_dc_finds_pottery_form`
--

INSERT INTO `newModel_dc_finds_pottery_form` (`id`, `name`, `region`) VALUES
(1, ' Anthropomorphic vessel ', ' Anatolia/East Aegean '),
(2, ' Bag shaped vessel (hole mouthed vessel) ', ' Anatolia/East Aegean '),
(3, ' Baking pan ', ' Anatolia/East Aegean '),
(4, ' Box ', ' Anatolia/East Aegean '),
(5, ' Carinated bowl ', ' Anatolia/East Aegean '),
(6, ' Cheese pot ', ' Anatolia/East Aegean '),
(7, ' Globular jar ', ' Anatolia/East Aegean '),
(8, ' Cup ', ' Anatolia/East Aegean '),
(9, ' Dome-shaped shallow bowls ', ' Anatolia/East Aegean '),
(10, ' Jug ', ' Anatolia/East Aegean '),
(11, ' Fikirtepe box  ', ' Anatolia/East Aegean '),
(12, ' Mug ', ' Anatolia/East Aegean '),
(13, ' Vessel ', ' Anatolia/East Aegean '),
(14, ' Necked jars ', ' Anatolia/East Aegean '),
(15, ' Bowl ', ' Anatolia/East Aegean '),
(16, ' Shallow bowl  ', ' Anatolia/East Aegean '),
(17, ' Tulip shaped beaker ', ' Anatolia/East Aegean '),
(18, ' Askos ', ' Thessaly '),
(19, ' Baking pan ', ' Thessaly '),
(20, ' Basin ', ' Thessaly '),
(21, ' Bowl ', ' Thessaly '),
(22, ' Carinated bowl ', ' Thessaly '),
(23, ' Cheese pot ', ' Thessaly '),
(24, ' Collared jar ', ' Thessaly '),
(25, ' Deep, globular jar ', ' Thessaly '),
(26, ' Dimini bowl  ', ' Thessaly '),
(27, ' Kylix ', ' Thessaly '),
(28, ' Fruitstand ', ' Thessaly '),
(29, ' Handless cup ', ' Thessaly '),
(30, ' Hole-mouthed jar ', ' Thessaly '),
(31, ' Mug ', ' Thessaly '),
(32, ' Pithos ', ' Thessaly '),
(33, ' Scoop ', ' Thessaly '),
(34, ' Skyphos ', ' Thessaly '),
(35, ' Askos ', ' Southern/Central Greece, Cyclades '),
(36, ' Baking pan ', ' Southern/Central Greece, Cyclades '),
(37, ' Carinated bowl ', ' Southern/Central Greece, Cyclades '),
(38, ' Cheese pot ', ' Southern/Central Greece, Cyclades '),
(39, ' Jar ', ' Southern/Central Greece, Cyclades '),
(40, ' Collared bowl ', ' Southern/Central Greece, Cyclades '),
(41, ' Collared jar ', ' Southern/Central Greece, Cyclades '),
(42, ' Deep bowl ', ' Southern/Central Greece, Cyclades '),
(43, ' Fruitstand ', ' Southern/Central Greece, Cyclades '),
(44, ' Gouged bowl ', ' Southern/Central Greece, Cyclades '),
(45, ' Husking bowl ', ' Southern/Central Greece, Cyclades '),
(46, ' Medium bowl ', ' Southern/Central Greece, Cyclades '),
(47, ' Piriform jar ', ' Southern/Central Greece, Cyclades '),
(48, ' Pithos ', ' Southern/Central Greece, Cyclades '),
(49, ' Platter ', ' Southern/Central Greece, Cyclades '),
(50, ' Bowl ', ' Southern/Central Greece, Cyclades '),
(51, ' Rhyton ', ' Southern/Central Greece, Cyclades '),
(52, ' Scoop ', ' Southern/Central Greece, Cyclades '),
(53, ' Shoulder bowl ', ' Southern/Central Greece, Cyclades '),
(54, ' Amphora ', ' Macedonia/Thrace '),
(55, ' Bowl ', ' Macedonia/Thrace '),
(56, ' Cup ', ' Macedonia/Thrace '),
(57, ' Jar ', ' Macedonia/Thrace '),
(58, ' Jug ', ' Macedonia/Thrace '),
(59, ' Ladle ', ' Macedonia/Thrace '),
(60, ' Lamp ', ' Macedonia/Thrace '),
(61, ' Lid ', ' Macedonia/Thrace '),
(62, ' Pitcher ', ' Macedonia/Thrace '),
(63, ' Pithos ', ' Macedonia/Thrace '),
(64, ' Plate ', ' Macedonia/Thrace '),
(65, ' Pyxis ', ' Macedonia/Thrace '),
(66, ' Scoop ', ' Macedonia/Thrace '),
(67, ' Strainer ', ' Macedonia/Thrace '),
(68, ' Rectangular vessel ', ' Macedonia/Thrace '),
(69, ' Stand ', ' Macedonia/Thrace '),
(70, ' Tripod ', ' Macedonia/Thrace '),
(71, ' Baking pan ', ' Crete '),
(72, ' Bottle ', ' Crete '),
(73, ' Bowl ', ' Crete '),
(74, ' Bucket-like vessel ', ' Crete '),
(75, ' Carinated bowl ', ' Crete '),
(76, ' Carinated incurved bowl ', ' Crete '),
(77, ' Carinated jar ', ' Crete '),
(78, ' Carinated shallow bowl ', ' Crete '),
(79, ' Cheese pot ', ' Crete '),
(80, ' Cup  ', ' Crete '),
(81, ' Deep bowl ', ' Crete '),
(82, ' Dipper ', ' Crete '),
(83, ' Mug ', ' Crete '),
(84, ' Funnel-necked jar ', ' Crete '),
(85, ' Jar ', ' Crete '),
(86, ' Hole-mouthed jar ', ' Crete '),
(87, ' Incurved bowl ', ' Crete '),
(88, ' Collared jar ', ' Crete '),
(89, ' Medium bowl ', ' Crete '),
(90, ' Chalice ', ' Crete '),
(91, ' Rhyton ', ' Crete '),
(92, ' Shallow bowl  ', ' Crete '),
(93, ' Tray ', ' Crete ');

--
-- Dumping data for table `newModel_dc_finds_small_finds_category`
--

INSERT INTO `newModel_dc_finds_small_finds_category` (`id`, `name`) VALUES
(1, 'tool'),
(2, 'jewellery'),
(3, 'figurines');

--
-- Dumping data for table `newModel_dc_finds_small_finds_type`
--

INSERT INTO `newModel_dc_finds_small_finds_type` (`id`, `name`) VALUES
(1, 'Fish hook'),
(2, 'Sling bullet/missile'),
(3, 'Belt hook'),
(4, 'Axe'),
(5, 'Spatula'),
(6, 'Spindle whorl'),
(7, 'Stone vessel'),
(8, 'Stamp/pintadera'),
(9, 'Pestle'),
(10, 'Table'),
(11, 'Disc perforated'),
(12, 'Disc unperforated'),
(13, 'Smoother'),
(14, 'Object'),
(15, 'Adze'),
(16, 'Crucible'),
(17, 'Shuttle'),
(18, 'Pendant'),
(19, 'Bracelet'),
(20, 'Bead'),
(21, '"Studs/Plugs"'),
(22, 'Necklace'),
(23, 'Split leg'),
(24, 'Steckkopf '),
(25, 'Kiliya'),
(26, 'Abstract'),
(27, 'Naturalistic'),
(28, 'Weight');

--
-- Dumping data for table `newModel_dc_finds_type`
--

INSERT INTO `newModel_dc_finds_type` (`id`, `name`) VALUES
(1, 'small finds'),
(2, 'botany'),
(3, 'animal remains'),
(4, 'lithics'),
(5, 'pottery');

--
-- Dumping data for table `newModel_dc_interpretation_productiontype`
--

INSERT INTO `newModel_dc_interpretation_productiontype` (`id`, `name`) VALUES
(1, ' textile production '),
(2, ' metal production '),
(3, ' chipped stone tool production '),
(4, ' stone tool production '),
(5, ' shell production '),
(6, ' bone tool production  '),
(7, ' pottery production ');

--
-- Dumping data for table `newModel_dc_interpretation_subsistencetype`
--

INSERT INTO `newModel_dc_interpretation_subsistencetype` (`id`, `name`) VALUES
(1, ' fishing '),
(2, ' farming '),
(3, ' animal husbandry '),
(4, ' hunting '),
(5, ' collecting '),
(6, ' storage systems ');

--
-- Dumping data for table `newModel_dc_period_datedby`
--

INSERT INTO `newModel_dc_period_datedby` (`id`, `name`) VALUES
(1, ' charcoal '),
(2, ' bone '),
(3, ' grain '),
(4, ' seed ');

--
-- Dumping data for table `newModel_dc_period_datingmethod`
--

INSERT INTO `newModel_dc_period_datingmethod` (`id`, `name`) VALUES
(1, ' radiocarbon dating '),
(2, ' dendrochronology '),
(3, ' material culture '),
(4, ' none recorded ');



--
-- Dumping data for table `newModel_dc_researchevent_institution`
--

INSERT INTO `newModel_dc_researchevent_institution` (`id`, `name`) VALUES
(239, 'ÖAW - OREA - Ägäis/Anatolien'),
(240, 'ÖAW - OREA - Ägypten/Levante'),
(241, 'ÖAW - OREA - Europa'),
(242, 'Österreichisches Archäologisches Institut - Zweigstelle Wien'),
(243, 'Österreichisches Archäologisches Institut - Zweigstelle Athen'),
(244, 'Österreichisches Archäologisches Institut - Zweigstelle Kairo'),
(245, 'Accademia Etrusca'),
(246, 'Altertumsgesellschaft Prussia'),
(247, 'American Academy in Rome'),
(248, 'American School of Classical Studies at Athens'),
(249, 'Archaeological Institute of America'),
(250, 'Archaeological Scociety of British Columbia'),
(251, 'Archaeolical Survey of India'),
(252, 'Archäologie Schweiz'),
(253, 'Archäologische Gesellschaft Schleswig-Holstein'),
(254, 'Archäologische Gesellschaft Athen'),
(255, 'Archäologische Gesellschaft der Hansestadt Lübeck'),
(256, 'Archäologische Gesellschaft in Berlin und Brandenburg'),
(257, 'Archäologische Gesellschaft in Hessen'),
(258, 'Archäologische Gesellschaft in Sachsen'),
(259, 'Archäologische Gesellschaft Innsbruck'),
(260, 'Archäologische Gesellschaft zu Berlin'),
(261, 'Archäologische Kommission für Niedersachsen'),
(262, 'Archäologischer Arbeitskreis Niedersachsen'),
(263, 'Archäologischer Verein im Landkreis Freising'),
(264, 'Archäologisches Institut der Chinesischen Akademi der Sozialwissenschaften'),
(265, 'Archäologisches Institut der Universität Göttingen'),
(266, 'Archäologisches Institut Prag'),
(267, 'Archäologisches Landesamt Schleswig-Holstein'),
(268, 'Archäologisches Spessartprojekt'),
(269, 'Associazione Internationale de Archeologia Classica'),
(270, 'Außenstelle Olpe der LWL-Archäologie für Westfalen'),
(271, 'Australian Archaeological Institute at Athens'),
(272, 'Ayutthaya Historical Study Center'),
(273, 'Bayrisches Landesamt für Denkmalpflege'),
(274, 'Beazley Archive'),
(275, 'Belgische School te Athene'),
(276, 'Biblisch-Archäologisches Institut Wuppertal'),
(277, 'Brandenburgisches Landesamt für Denkmalpflege und Archäologisches Landesmuseum'),
(278, 'British School at Athens'),
(279, 'British School at Rome'),
(280, 'Bundesdenkmalamt - Österreich'),
(281, 'Burgenfreunde beider Basel'),
(282, 'Cadw'),
(283, 'Canadian Institute in Greece'),
(284, 'AG CAA'),
(285, 'Corpus der minoischen und mykenischen Siegel'),
(286, 'Curt-Engelhorn-Zentrum Archäometrie'),
(287, 'Dachverband archäologischer Studierendenvertretungen'),
(288, 'Danske Institut i Athen (DIA)'),
(289, 'Denkmalamt der Proviz Ostpreußen'),
(290, 'Denkmalbehörde'),
(291, 'Denkmalschutzamt Hamburg'),
(292, 'Deutsche Gesellschaft für Archäologie des Mittelalters und der Neuzeit'),
(293, 'Deutsche Gesellschaft für Ur- und Frühgeschichte'),
(294, 'Deutsche Gesellschaft für Vorgeschichte'),
(295, 'Deutsche Limeskommission'),
(296, 'Deutsche Orient-Gesellschaft'),
(297, 'Deutsche Verbände für Altertumsforschung'),
(298, 'Deutscher Verband für Archäologie'),
(299, 'Deutsches Archäologisches Institut (DAI) - Zentrale Berlin'),
(300, 'Deutsches Archäologisches Institut (DAI) - Abteilung Rom'),
(301, 'Deutsches Archäologisches Institut (DAI) - Abteilung Athen'),
(302, 'Deutsches Archäologisches Institut (DAI) - Römisch-Germanische Kommission (RGK)'),
(303, 'Deutsches Archäologisches Institut (DAI) - Abteilung Kairo'),
(304, 'Deutsches Archäologisches Institut (DAI) - Abteilung Istanbul'),
(305, 'Deutsches Archäologisches Institut (DAI) - Kommission für Alte Geschichte und Epigraphik'),
(306, 'Deutsches Archäologisches Institut (DAI) - Orientabteilung'),
(307, 'Deutsches Archäologisches Institut (DAI) - Kommission für Archäologie Außereuropäischer Kulturen'),
(308, 'Deutsches Archäologisches Institut (DAI) - Euraisienabteilung'),
(309, 'Deutsches Archäologisches Institut (DAI) - Forschungsstelle Jerusalem'),
(310, 'Deutsches Archäologisches Institut (DAI) - Forschungsstelle Amman'),
(311, 'Deutsches Archäologisches Institut Madrid'),
(312, 'Deutsches Evangelisches Institut für Altertumswissenschaft des Heiligen Landes'),
(313, 'Disney Professor of Archaeology'),
(314, 'Egypt Exploration Society'),
(315, 'English Heritage'),
(316, 'Ephoria Kavala'),
(317, 'Europae Archaeologiae Consilium'),
(318, 'European Association of Archaeologists'),
(319, 'EXAR - Europäische Vereinigung zur Förderung der Experimentellen Archäologie e.V.'),
(320, 'Forschungsstelle Asia Minor'),
(321, 'Freunde der Antike auf der Museumsinsel Berlin'),
(322, 'Georgisches Institut in Athen'),
(323, 'Gesellschaft für Archäologie in Würtemberg und Hohenzollern'),
(324, 'Gesellschaft für nützliche Forschungen zu Trier'),
(325, 'Historic Scotland'),
(326, 'Hugo Obermaier Gesellschaft'),
(327, 'Institut Européen d''Archéologie Sous-Marine'),
(328, 'Institut française d''archéologie orientale'),
(329, 'Institutum Romanum Finlandiae'),
(330, 'Irish Institute of Hellenic Studies at Athens'),
(331, 'Israel Antiquities Authority'),
(332, 'Instituto Nazionale de Studi Estruschi ad Italici'),
(333, 'Landesamt für Archäologie Sachsen'),
(334, 'Landesamt für Denkmalpflege Baden-Würtemberg'),
(335, 'Landesamt für Denkmalpflege und Archäologie Sachsen-Anhalt'),
(336, 'Landesamt für Kultur und Denkmalpflege Mecklenburg-Vorpommern'),
(337, 'Landesarchäologie Bremen'),
(338, 'Landesdenkmalamt Berlin'),
(339, 'Landesverband selbstständiger Archäologen in Bayern'),
(340, 'Lincoln Professor of Classical Archaeology and Art'),
(341, 'Lippisches Landesmuseum'),
(342, 'LVR-Amt für Bodendenkmalpflege in Rheinland'),
(343, 'LWL-Archäologie für Westfalen'),
(344, 'Monrepos (Forschungszentrum)'),
(345, 'ÖAW - Mykenische Kommission (heute Abt. Ägäis/Anatolien und OREA)'),
(346, 'National Underwater and Marine Agency'),
(347, 'Nationales Forschungszentrum für Archäologie'),
(348, 'Nederlands Instituut in Athene'),
(349, 'Nordeuropäisches Symposium für Archäologische Textilien (NESAT)'),
(350, 'Niedersächsischer Landesverein für Urgeschichte'),
(351, 'Niedersächsisches Institut für historische Küstenforschung'),
(352, 'Niedersächsisches Landesamt für Denkmalpflege'),
(353, 'Nordic Library at Athens'),
(354, 'Norske Institutt i Athen (NIA)'),
(355, 'Ontario Archaeoligcal Society '),
(356, 'Österreichischer Archäologie-Bund'),
(357, 'Pontificio Instituto di Archaeologia Cristiana'),
(358, 'Polish Centre of Mediterranean Archaeology'),
(359, 'Pontificia Accademia Romana di Archaeologia'),
(360, 'Reichs-Limeskommission'),
(361, 'Römische Hyperboreer'),
(362, 'Römisch-Germanische Kommission'),
(363, 'Schweizerische Arbeitsgemeinschaft für Archäologie des Mittelalters und der Neuzeit'),
(364, 'Schweizerische Archäologische Schule in Griechenland'),
(365, 'Scuola Archeologica Italiana di Atene'),
(366, 'Société préhistorique luxembourgeoise'),
(367, 'Stiftung Archäologie - Deutschland - München'),
(368, 'Suomen Ateenan-instituutti'),
(369, 'Svenska Institutet i Athen'),
(370, 'Svenska Institutet i Rom'),
(371, 'Underwater Archaeological Society of British Columbia'),
(372, 'Verband der Landesarchäologen in der Bundesrepublik Deutschland e.V. (VLA)'),
(373, 'Verband der Restauratoren'),
(374, 'Verbund archäologischer Institutionen in Köln Bonn'),
(375, 'Verein zur Föderung des Ägyptischen Museums Berlin'),
(376, 'Vorderasiatisch-Ägyptische Gesellschaft'),
(377, 'Winckelmann-Gesellschaft'),
(378, 'Yates Professor of Classical Art and Archaeology '),
(379, 'Zentralinstitut für Alte Geschichte und Archäologie (ZIAGA 1969 - 1992)'),
(380, 'Akademie der Wissenschaften der DDR (AdW 1972 - 1991)'),
(381, 'Deutsche Akademie der Wissenschaften der DDR (DAW 1946 - 1972)'),
(382, 'Universität Wien - Institut für Klassische Archäologie'),
(383, 'Universität Wien - Institut für Klassische Archäologie - Abteilung für Frühchritliche Archäologie'),
(384, 'Universität Wien - Institut für Urgeschichte und Historische Archäologie (ehm. Institut für Ur- und '),
(385, 'Universität Wien - Institut für Alttestamentliche Wissenschaft und Biblische Archäologie der Evangel'),
(386, 'Universität Wien - Institut für Kirchengeschichte, Christliche Archäologie und Kirchliche Kunst'),
(387, 'Universität Wien - Institut für Altsemitische Philiologie und Orientalische Archäologie'),
(388, 'Universität Wien - Institut für Alte Geschichte und Altertumskunde'),
(389, 'Universität Wien - Institut für Ägyptologie'),
(390, 'Universität Wien - Institut für Byzantinistik und Neogräzistik'),
(391, 'Universität Wien - Vienna Institute for Archaeological Science (VIAS)'),
(392, 'Universität Salzburg - Institut fürAlte Geschichte und Altertumskunde'),
(393, 'Universität Salzburg - Institut für Klassische Archäologie'),
(394, 'Universität Graz - Institut für Alte Geschichte und Altertumskunde'),
(395, 'Universität Graz - Institut für Klassische Archäologie'),
(396, 'Universität Innsbruck - Institut für Archäologien - Ur- und Frühgeschichte, Mittelalter- und Neuzeit'),
(397, 'Universität Innsbruck - Institut für Archäologien - Klassische und Provinzialrömische Archäologie'),
(398, 'Universität Innsbruck - Institut für Alte Geschichte und Altorientalistik'),
(399, 'Universität Berlin - Institut für Archäologie - Bereich Klassische Archäologie'),
(400, 'Universität Berlin - Institut für Prähistorische Archäologie'),
(401, 'Universität Berlin - Institut für Archäologie - Archäologie und Kulturgeschichte Nordostafrikas'),
(402, 'Universität Bern - Insitut für Klassische Archäologie'),
(403, 'Universität Bern - Institut für Ur- und Frühgeschichte und Archäologie der Römischen Provinzen'),
(404, 'Ruhr-Universität Bochum - Institut für Archäometrie'),
(405, 'Ruhr-Universität Bochum - Institut für Klassische Archäologie'),
(406, 'Ruhr-Universität Bochum - Institut für Ur- und Frühgeschichte'),
(407, 'Universität Bonn - Institut für Kunstgeschichte und Archäologie'),
(408, 'Universität Bonn - Institut für Vor- und Frühgeschichtliche Archäologie'),
(409, 'Technische Universität Darmstadt - Klassische Archäologie'),
(410, 'Katholische Universität Eichstätt - Institut für Klassische Archäologie'),
(411, 'Universität Erlangen - Institut für Klassische Archäologie'),
(412, 'Universität Erlangen - Institut für Ur- und Frühgesichte'),
(413, 'Universität Frankfurt - Institut für Archäologische Wissenschaften - Vorderasiatische und Klassiche '),
(414, 'Universität Frankfurt - Institut für Archäologische Wissenschaften - Archäologie und Geschichte der '),
(415, 'Universität Frankfurt - Institut für Archäologische Wissenschaften - Vor - und Frühgeschichte'),
(416, 'Albert-Ludwigs-Universität Freiburg - IAW - Urgeschichtliche Archäologie'),
(417, 'Albert-Ludwigs-Universität Freiburg - IAW - Vorderasiatische Archäologie und Altorientalische Philol'),
(418, 'Albert-Ludwigs-Universität Freiburg - IAW - Klassische Archäologie'),
(419, 'Albert - Ludwigs - Universität Freiburg - IAW - Provinizalrömische Archäologie'),
(420, 'Albert - Ludwigs - Universität Freiburg - IAW - Christliche Archäologie und Byzantinische Kunstgesch'),
(421, 'Albert - Ludwigs - Universität Freiburg - IAW - Frühgeschichtliche Archäologie und Archäologie des M'),
(422, 'Justus-Liebig-Universität Giessen - Institut für Altertumswissenschaften - Klassische Archäologie'),
(423, 'Justus-Liebig-Universität Giessen - Institut für Altertumswissenschaften - Alte Geschichte'),
(424, 'Universität Göttingen - Archäologisches Institut'),
(425, 'Universität Göttingen - Institut für Christliche Archäologie un Byzantinische Kunstgeschichte'),
(426, 'Martin-Luther-Universität Halle-Wittenberg - Institut für Klassische Altertumswissenschaften - Klass'),
(427, 'Martin-Luther-Universität Halle-Wittenberg - Institut für Klassische Altertumswissenschaften - Klass'),
(428, 'Archäologisches Museum - Martin-Luther-Universität Halle-Wittenberg'),
(429, 'Universität Hamburg - AGIL - Büro für Angewandte Archäologie'),
(430, 'Universität Hamburg - Institut für Vor- und Frühgeschichtliche Archäologie'),
(431, 'Universität Hamburg - Institut für Archäologie und Kulturgeschichte des antiken Mittelmeerraumes'),
(432, 'Universität Heidelberg - Institut für Klassische Archäologie'),
(433, 'Universität Heidelberg - Ägyptologisches Institut'),
(434, 'Universität Heidelberg - Institut für Byzantinische Archäologie und Kunstgeschichte'),
(435, 'Universität Heidelberg - Institut für Ur- und Frühgeschichte und Vorderasiatische Archäologie'),
(436, 'Christian-Albrechts-Universität zu Kiel - Institut für Klassische Altertumskunde - Klassische Archäo'),
(437, 'Christian-Albrechts-Universität zu Kiel - Institut für Ur- und Frühgeschichte'),
(438, 'Universität zu Köln - Archäologisches Institut'),
(439, 'Universität Leipzig - Institut für Ägyptologie'),
(440, 'Ägyptisches Museum - Universität Leipzig'),
(441, 'Universität Leipzig - Institut für Klassische Archäologie'),
(442, 'Universität Leipzig - Antikenmuseum'),
(443, 'Universität Leipzig - Altorientalisches Institut'),
(444, 'Johannes Gutenberg Universität Mainz - Institut für Vor- und Frühgeschichte'),
(445, 'Johannes Gutenberg Universität Mainz - Institut für Ägyptologie und Altorientalistik'),
(446, 'Johannes Gutenberg Universität Mainz - Institut für Klassische Archäologie'),
(447, 'Johannes Gutenberg Universität Mainz - Institut für Kunstgeschichte und Musikwissenschaft'),
(448, 'Philipps Universität Marburg - Vor- und Frühgeschichte'),
(449, 'Philipps Universität Marburg - Klassische Archäologie'),
(450, 'Philipps Universität Marburg - Christliche Archäologie und Byzantinische Kunstgeschichte'),
(451, 'Ludwig-Maximilians-Universität München - Institut für Ägyptologie und Koptologie'),
(452, 'Ludwig-Maximilians-Universität München - Institut für Assyrologie und Hethitologie'),
(453, 'Ludwig-Maximilians Universität München - Institut für Klassische Archäölogie'),
(454, 'Ludwig-Maximilians Universität München - Institut für Vorderasiatische Archäologie'),
(455, 'Ludwig-Maximilians Universität München - Institut für Vor- und Frühgeschichtliche Archäologie und Pr'),
(456, 'Westfälische Wilhelms-Universität Münster - Institut für Klassiche Archäologie und Christliche Archä'),
(457, 'Archäologisches Museum - Universität Münster'),
(458, 'Westfälische Wilhelms-Universität Münster - Institut für Altorientalische Philologie und Vorderasiat'),
(459, 'Westfälische Wilhelms-Universität Münster - Institut für Ägyptolgie und Koptologie'),
(460, 'Westfälische Wilhelms-Universität Münster - Institut für Ur- und Frühgeschichtliche Archäologie'),
(461, 'Universität Regensburg - Institut für Klassische Archäologie'),
(462, 'Universität Rostock - Heinrich Schliemann-Institut für Altertumswissenschaften'),
(463, 'Universität des Saarlandes - Institut für Klassische Archäologie'),
(464, 'Universität des Saarlandes - Institut für Vor- und Frühgeschichte und Vorderasiatische Archäologie'),
(465, 'Universität Trier - Institut für Ägyptologie'),
(466, 'Universität Trier - Institut für Klassiche Archäologie'),
(467, 'Eberhard Karls-Universität Tübingen - Institut für Klassische Archäologie'),
(468, 'Eberhard Karls-Universität Tübingen - Institut für die Kulturen des Alten Orients (IANES)'),
(469, 'Eberhard Karls-Universität Tübingen - Biblisch-Archäologisches Institut'),
(470, 'Eberhard Karls-Universität Tübingen - Institut für Ur- und Frühgeschichte und Archäologie des Mittel'),
(471, 'Julius-Maximilians-Universität Würzburg - IAW - Ägyptologie'),
(472, 'Julius-Maximilians-Universität Würzburg - IAW - Altorientalistik'),
(473, 'Julius-Maximilians-Universität Würzburg - IAW - Klassische Archäologie'),
(474, 'Julius-Maximilians-Universität Würzburg - IAW - Vor- und Frühgeschichtliche Archäologie'),
(475, 'Universität Zürich (UZH) - Institut für Archäologie - Klassische Archäologie'),
(476, 'Universität Zürich (UZH) - Institut für Archäologie - Prähistorische Archäologie'),
(477, 'Panthéon Sorbonne-Université Paris - Department d''art et d''archéologie'),
(478, 'University of Chichago - Oriental Institute'),
(479, 'University of Chichago - Center for Eastern European and Russian/Eurasian Studies (CEERES)'),
(480, 'Yale University - Department of Anthropology'),
(481, 'Havard University - Department of Anthropology'),
(482, 'Oxford University - Institute of Archaeology'),
(483, 'University of Cambridge - Department of Archaeology'),
(484, 'Archäologisches und Anthropologisches Museum Cambridge (MMA)'),
(485, 'University of Cambridge - McDonald Institute for Archaeological Resarch'),
(486, 'Griechisch-Römisches Museum Alexandria'),
(487, 'Ägyptisches Museum - Kairo'),
(488, 'Luxor Museum'),
(489, 'Historisches Museum Shkodra'),
(490, 'Archäologisches Nationalmuseum - Tirana'),
(491, 'Historischesn Nationalmuseum  - Tirana'),
(492, 'Regionaal Archeologisch Museum'),
(493, 'Nationalmuseum von Bosnien und Herzegowina - Sarajewo'),
(494, 'Museum der Republik Srpska - Banja Luka'),
(495, 'Archäologisches Museum Nessebar'),
(496, 'Archäologisches Museum Plowdiw'),
(497, 'Nationales Archäologisches Museum Sofia'),
(498, 'Nationales Historisches Museum Sofia'),
(499, 'Archäologisches Museum Warna'),
(500, 'Archäologisches Museum Weliki Preslaw'),
(501, 'Archäologisches Museum Weliko Tarnowo'),
(502, 'Dänisches Nationalmuseum'),
(503, 'Fotevikens Vikingacenter'),
(504, 'Historisches Museum der Färöer'),
(505, 'Hjemsted Oltidspark'),
(506, 'Moesgaard Museum'),
(507, 'Museet Ribes Vikinger'),
(508, 'Ribe VikingeCenter'),
(509, 'Ägyptisches Museum - Berlin'),
(510, 'Antikensammlung - Berlin'),
(511, 'Märkisches Museum - Berlin'),
(512, 'Museum für Islamische Kunst - Berlin'),
(513, 'Museum für Vor- und Frühgeschichte - Berlin'),
(514, 'Pergamonmuseum'),
(515, 'Vorderasiatisches Museum - Berlin'),
(516, 'Archäologisches Museum Hamburg'),
(517, 'Archäologische Sammlung der Universität Rostock'),
(518, 'Archäologisches Museum Münster'),
(519, 'Ägyptisches Museum Bonn'),
(520, 'Römische-Germanisches Museum Köln'),
(521, 'Römisch-Germanisches Zentralmuseum'),
(522, 'Original- und Abgussammlung des Archäologischen Instituts der Universität des Saarlandes'),
(523, 'Ägyptisches Museum der Universität Leipzig'),
(524, 'Antikenmuseum der Universität Leipzig'),
(525, 'Museum für Ur- und Frühgeschichte Thüringens'),
(526, 'Ur- und frühgeschichtliche Sammlung der Universität Jena'),
(527, 'Musée d''archéologie nationale'),
(528, 'Musée du Louvre - Paris'),
(529, 'Archäologisches Museum - Athen'),
(530, 'Archäologisches Museum - Chania, Kreta'),
(531, 'Archäologisches Museum  - Epidauros'),
(532, 'Archäologisches Museum - Ioannina'),
(533, 'Archäologisches Museum - Iraklio, Kreta'),
(534, 'Archäologisches Museum - Komotini'),
(535, 'Archäologisches Museum - Kornith'),
(536, 'Archäologisches Museum - Olympia'),
(537, 'Archäologisches Museum - Patras'),
(538, 'Archäologisches Museum - Rethymno'),
(539, 'Archäologisches Museum - Theben'),
(540, 'Archäologisches Museum - Vathy, Samos'),
(541, 'Archäologisches Nationalmuseum - Athen'),
(542, 'Archäologisches Museum Kalapodi'),
(543, 'Ashmolian Museum'),
(544, 'Brithish Museum '),
(545, 'Jorvik Viking Centre'),
(546, 'Petrie Museum of Egyptian Archaeology'),
(547, 'World Museum Liverpool'),
(548, 'Bible Lands Museum Jerusalem'),
(549, 'Israel-Museum'),
(550, 'Rockefeller-Museum Jerusalem'),
(551, 'Haifa-Museum'),
(552, 'Archäologisches Nationalmuseum - Florenz'),
(553, 'Archäologisches Nationalmuseum - Neapel'),
(554, 'Archäologisches Museum Vetulonia - Toskana'),
(555, 'Museo Archeologico Regionale Antonino Salinas - Palemo'),
(556, 'Museo Archeologico Regionale Paolo Orsi - Syrakus'),
(557, 'Museum für Ligurische Archäologie - Genua'),
(558, 'Museo Egizio - Turin'),
(559, 'Museum des Kosovo - Priština'),
(560, 'Archälogisches Museum Istriens - Pula'),
(561, 'Archäologisches Museum - Split'),
(562, 'Archäologisches Museum - Zagreb'),
(563, 'Museum für Archäologische Denkmäler Kroatiens - Split'),
(564, 'Lichtensteinisches Landesmuseum'),
(565, 'Musée de l''Etat Luxembourg'),
(566, 'Archäologisches Nationalmuseum Maltas - Valetta'),
(567, 'Drents Museum'),
(568, 'Museum Het Valkhof'),
(569, 'Rijksmuseum van Oudheden'),
(570, 'Staatliches Oman Museum - Qurum'),
(571, 'Archäologisches Museum Fließ'),
(572, 'Museum für Frühgeschichte Traismauer'),
(573, 'Museum für Ur- und Frühgeschichte Wieselburg'),
(574, 'Museum für Urgeschichte des Landes Niederösterreich (Schloss Asparn)'),
(575, 'Römermuseum Tulln'),
(576, 'Schlossmuseum Linz'),
(577, 'Ephesos Museum Wien'),
(578, 'Keltenmuseum Hallein'),
(579, 'Kusthistorisches Museum Wien'),
(580, 'Landesmuseum Joanneum'),
(581, 'Naturhistorisches Museum Wien'),
(582, 'Oberösterreichische Landesmuseen'),
(583, 'Papyrussammlung und Papyrumsmuseum Wien'),
(584, 'Tiroler Landesmuseum'),
(585, 'Vorarlbergmuseum'),
(586, 'Archäologisches Museum Warschau'),
(587, 'Archäologisches Museum Krakau'),
(588, 'Anthropologische und archäologische Sammlungen der Jagiellonischen Universität in Krakau'),
(589, 'Museu Arqueológico do Carmo - Lissabon'),
(590, 'Museu Nacional de Arqueologia - Portugal'),
(591, 'Muzeul Naţional de Istorie a României - Bukarest'),
(592, 'Antikenmuseum Basel und Sammlng Ludwig - Basel'),
(593, 'Historisches Museum Basel'),
(594, 'Musée d''art et d''histoire - Genf'),
(595, 'Museum für Archäologie Thurgau - Frauenfeld'),
(596, 'Museum für Urgeschichte - Zug'),
(597, 'Archäologisches Museum Alicante'),
(598, 'Museo Arqueológico y de Historia de Elche'),
(599, 'Museo Arqueológico Nacional de España'),
(600, 'Archologisches Museum Son Fornés'),
(601, 'Nationalmuseum Sudan'),
(602, 'Nationalmuseum Bardo'),
(603, 'Archäologisches Museum Adana'),
(604, 'Archäologisches Museum Adıyaman'),
(605, 'Museum für anatolische Zivilisationen, Ankara'),
(606, 'Archäologisches Museum Antakya'),
(607, 'Archäologisches Museum Bandırma'),
(608, 'Archäologisches Museum Bergama (Pergamon)'),
(609, 'Archäologisches Museum Çanakkale'),
(610, 'Archäologisches Museum Çorum'),
(611, 'Archäologisches Museum Istanbul'),
(612, 'Archäologisches Museum Kahramanmaraş'),
(613, 'Archäologisches Museum Malatya'),
(614, 'Archäologisches Museum Niğde'),
(615, 'Archäologisches Museum Şanlıurfa'),
(616, 'Ephesos-Museum Selçuk'),
(617, 'Archäologisches Museum Silifke'),
(618, 'Zeugma-Mosaik-Museum, Gaziantep'),
(619, 'Nationales Historisches Museum der Ukraine - Kiew'),
(620, 'Kelsey Museum of Archaeology'),
(621, 'Peabody Museum of Archaeology and Ethnology'),
(622, 'University of Pennsylvania Museum of Archaeology and Anthropology'),
(623, 'University of Chicago - Oriental Institute Museum'),
(624, 'Art Institute of Chicago'),
(625, 'Field Museum Chicago'),
(626, 'New York Archaeology Museum'),
(627, 'The Metropolitan Museum of Art'),
(628, 'Archäologisches Museum Termiz'),
(629, 'Museum für Vor- und Frühgeschichte Weißrusslands - Minsk'),
(630, 'Archäologisches Museum Limassol'),
(631, 'Cyprus Museum'),
(632, 'École française d''Extreme-Orient'),
(633, 'École française d''Athènes'),
(634, 'École française de Rome');

--
-- Dumping data for table `newModel_dc_researchevent_researchtype`
--

INSERT INTO `newModel_dc_researchevent_researchtype` (`id`, `name`) VALUES
(1, 'borehole survey'),
(2, 'excavation: rescue'),
(3, 'excavation: research'),
(4, 'excavation: underwater'),
(5, 'excavation: undetermined'),
(6, 'field observation (monitoring)'),
(7, 'metal detecting use'),
(8, 'test pit'),
(9, 'trial trench'),
(10, 'underwater evaluation'),
(11, 'field walking survey: undetermined'),
(12, 'aerial photograph interpretation'),
(13, 'antiquarian observation'),
(14, 'architectural survey'),
(15, 'field walking survey: non-systematic'),
(16, 'field walking survey: systematic'),
(17, 'geophysical survey: magnetic'),
(18, 'geophysical survey: radar'),
(19, 'laser scanning survey'),
(20, 'metal detecting survey'),
(21, 'remote sensing lidar survey'),
(22, 'satellite imaging'),
(23, 'underwater survey');

--
-- Dumping data for table `newModel_dc_researchevent_special_analysis`
--

INSERT INTO `newModel_dc_researchevent_special_analysis` (`id`, `name`) VALUES
(1, 'animal remains report'),
(2, 'archaeobotany: macro-botany'),
(3, 'archaeobotany: pollen'),
(4, 'ceramics: sourcing'),
(5, 'ceramics: thin section analysis '),
(6, 'dating: archaeomagnetism'),
(7, 'dating: dendrochronology'),
(8, 'dating: lead isotope dating'),
(9, 'dating: luminescence dating'),
(10, 'dating: mitochondrial DNA'),
(11, 'dating: oxygen isotope analysis'),
(12, 'dating: radiocarbon dating'),
(13, 'DNA analysis'),
(14, 'human remains report'),
(15, 'isotopes: carbon (C)'),
(16, 'isotopes: lead (Pb)'),
(17, 'isotopes: nitrogen (N)'),
(18, 'isotopes: oxygen (O)'),
(19, 'isotopes: strontium (Sr)'),
(20, 'lithics: raw material sourcing'),
(21, 'metallurgy'),
(22, 'mineralogy'),
(23, 'soil analysis: particle size analysis'),
(24, 'soil analysis: soil chemistry'),
(25, 'soil analysis: soil micromorphology'),
(26, 'soil analysis: soil phosphorus analysis');

--
-- Dumping data for table `newModel_dc_site_geographicalreferencesystem`
--

INSERT INTO `newModel_dc_site_geographicalreferencesystem` (`id`, `name`) VALUES
(1, 'ED50 - European Datum 1950'),
(2, 'SAD69 - South America Datum 1969'),
(3, 'GRS80 - Geodetic Reference System 1980 '),
(4, 'NAD83 - North American Datum 1983'),
(5, 'WGS84 - World Geodetic System 1984'),
(6, 'NAVD88 - North America Virtual Datum 1988'),
(7, 'ETRS89 - European Terrestrial Reference System 1984'),
(8, 'GCJ02 - Chinese Encrypted Datum 2002'),
(9, 'EPSG - European Petrol Survey Group'),
(10, 'UTM - Universal Transverse Mercator');


INSERT INTO `newModel_site` (`id`, `name`, `alias_name`, `alternative_name`, `description`, `topography`, `gps_data_n`, `gps_data_e`, `gps_data_z`, `coordinate_source`, `number_of_activity_periods`, `geographical_coordinate_reference_system_id`, `province_id`, `comment`) VALUES
(1, 'Site01', '', '', '', '', '', '', '', '', '', 1, 581, ''),
(2, 'PeterchensMondfahrt', 'Märchen', 'Märchenaufenglisch', 'This is the story about Peterchens Mondfahrt', '', '', '', '', '', '', NULL, 581, '');

INSERT INTO `newModel_area` (`id`, `area_nr`, `stratigraphical_unit_id`, `geographical_reference`, `description`, `settlement_human_remains`, `cemetery_or_grave`, `grave_number_of_graves`, `grave_estimated_number_of_individuals`, `area_type_id`, `cave_rockshelters_evidence_of_graves_human_remains_id`, `cave_rockshelters_type_id`, `site_id`, `comment`, `c14_absolute_from`, `c14_absolute_to`, `c14_calibrated`, `grave_number_of_female_sex`, `grave_number_of_male_sex`, `grave_number_of_not_specified_sex`) VALUES
(1, '', '', '', '', NULL, NULL, '', '', 3, NULL, NULL, 1, '', 12, 14, 'yes', NULL, NULL, NULL),
(2, '', '', '', '', NULL, NULL, '32', '', 3, 1, 1, 1, '', -1, 2, 'yes', NULL, NULL, NULL),
(4, '', '', '', '', NULL, NULL, '', '', 4, NULL, NULL, 1, '', 1, -1, 'yes', NULL, NULL, NULL);

--
-- Dumping data for table `newModel_researchevent`
--

INSERT INTO `newModel_researchevent` (`id`, `year_of_activity_start_year`, `year_of_activity_end_year`, `project_name`, `project_id`, `project_leader`, `comment`) VALUES
(1, 2000, 2008, '', '', '', '');

--

--
-- Dumping data for table `newModel_finds`
--

INSERT INTO `newModel_finds` (`id`, `confidence`, `comment`, `amount_id`, `animal_remains_completeness_id`, `area_id`, `finds_type_id`, `research_event_id`, `small_finds_category_id`) VALUES
(1, NULL, '', 2, NULL, 1, 1, 1, 3),
(2, '2', '', 8, NULL, 1, 5, 1, NULL);

--
-- Dumping data for table `newModel_finds_material`
--

INSERT INTO `newModel_finds_material` (`id`, `finds_id`, `dc_finds_material_id`) VALUES
(3, 1, 35);

--
-- Dumping data for table `newModel_finds_pottery_decoration`
--

INSERT INTO `newModel_finds_pottery_decoration` (`id`, `finds_id`, `dc_finds_pottery_decoration_id`) VALUES
(1, 2, 1),
(2, 2, 3);

--
-- Dumping data for table `newModel_finds_pottery_detail`
--

INSERT INTO `newModel_finds_pottery_detail` (`id`, `finds_id`, `dc_finds_pottery_detail_id`) VALUES
(1, 2, 1),
(2, 2, 3);

--
-- Dumping data for table `newModel_finds_pottery_form`
--

INSERT INTO `newModel_finds_pottery_form` (`id`, `finds_id`, `dc_finds_pottery_form_id`) VALUES
(1, 2, 1),
(2, 2, 2);

--
-- Dumping data for table `newModel_finds_small_finds_type`
--

INSERT INTO `newModel_finds_small_finds_type` (`id`, `finds_id`, `dc_finds_small_finds_type_id`) VALUES
(6, 1, 15),
(5, 1, 26);

--
-- Dumping data for table `newModel_interpretation`
--

INSERT INTO `newModel_interpretation` (`id`, `description`, `comment`) VALUES
(2, '', ''),
(3, 'I think this has to be black!', '');

--
-- Dumping data for table `newModel_interpretation_area`
--

INSERT INTO `newModel_interpretation_area` (`id`, `interpretation_id`, `area_id`) VALUES
(2, 2, 1),
(4, 3, 1);

--
-- Dumping data for table `newModel_interpretation_finds`
--

INSERT INTO `newModel_interpretation_finds` (`id`, `interpretation_id`, `finds_id`) VALUES
(2, 2, 1),
(3, 3, 1);

--
-- Dumping data for table `newModel_interpretation_production_type`
--

INSERT INTO `newModel_interpretation_production_type` (`id`, `interpretation_id`, `dc_interpretation_productiontype_id`) VALUES
(4, 2, 3),
(5, 2, 6),
(9, 3, 2),
(10, 3, 3),
(11, 3, 6);

--
-- Dumping data for table `newModel_interpretation_subsistence_type`
--

INSERT INTO `newModel_interpretation_subsistence_type` (`id`, `interpretation_id`, `dc_interpretation_subsistencetype_id`) VALUES
(4, 2, 3),
(5, 2, 5),
(10, 3, 1),
(11, 3, 2),
(12, 3, 4),
(13, 3, 5);

--
-- Dumping data for table `newModel_period`
--

INSERT INTO `newModel_period` (`id`, `comment`, `system_id`) VALUES
(1, '', 1),
(2, '', 1),
(3, '', 10);

--
-- Dumping data for table `newModel_period_dated_by`
--

INSERT INTO `newModel_period_dated_by` (`id`, `period_id`, `dc_period_datedby_id`) VALUES
(1, 2, 1),
(2, 2, 2),
(3, 3, 2),
(4, 3, 3);

--
-- Dumping data for table `newModel_period_dating_method`
--

INSERT INTO `newModel_period_dating_method` (`id`, `period_id`, `dc_period_datingmethod_id`) VALUES
(1, 1, 2),
(2, 1, 3),
(3, 2, 2),
(4, 2, 4),
(5, 3, 3);


-- Dumping data for table `newModel_researchevent_institution`
--

INSERT INTO `newModel_researchevent_institution` (`id`, `researchevent_id`, `dc_researchevent_institution_id`) VALUES
(1, 1, 245);

--
-- Dumping data for table `newModel_researchevent_research_type`
--

INSERT INTO `newModel_researchevent_research_type` (`id`, `researchevent_id`, `dc_researchevent_researchtype_id`) VALUES
(1, 1, 12),
(2, 1, 13);

--
-- Dumping data for table `newModel_researchevent_special_analysis`
--

INSERT INTO `newModel_researchevent_special_analysis` (`id`, `researchevent_id`, `dc_researchevent_special_analysis_id`) VALUES
(1, 1, 2);

--
-- Dumping data for table `newModel_site`
--



--
-- Dumping data for table `newModel_area_cave_rockshelters_evidence_of_occupation`
--

INSERT INTO `newModel_area_cave_rockshelters_evidence_of_occupation` (`id`, `area_id`, `dc_area_evidenceofoccupation_id`) VALUES
(1, 2, 1),
(2, 2, 3),
(3, 2, 5);

--
-- Dumping data for table `newModel_area_cemetery_or_graves_topography`
--

INSERT INTO `newModel_area_cemetery_or_graves_topography` (`id`, `area_id`, `dc_area_topography_id`) VALUES
(1, 4, 1),
(2, 4, 3);

--
-- Dumping data for table `newModel_area_grave_age_groups`
--

INSERT INTO `newModel_area_grave_age_groups` (`id`, `area_id`, `dc_area_agegroups_id`) VALUES
(1, 2, 5);

--
-- Dumping data for table `newModel_area_grave_manipulations_of_graves`
--

INSERT INTO `newModel_area_grave_manipulations_of_graves` (`id`, `area_id`, `dc_area_manipulationofgraves_id`) VALUES
(1, 2, 1);

--
-- Dumping data for table `newModel_area_grave_type`
--

INSERT INTO `newModel_area_grave_type` (`id`, `area_id`, `dc_area_gravetype_id`) VALUES
(1, 2, 4);

--
-- Dumping data for table `newModel_area_grave_type_of_human_remains`
--

INSERT INTO `newModel_area_grave_type_of_human_remains` (`id`, `area_id`, `dc_area_typeofhumanremains_id`) VALUES
(1, 2, 1);

--
-- Dumping data for table `newModel_area_period`
--

INSERT INTO `newModel_area_period` (`id`, `area_id`, `period_id`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 2, 2),
(4, 4, 1),
(5, 4, 2);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
