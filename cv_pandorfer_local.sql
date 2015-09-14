-- Changes:
-- replaced defc to orea
-- replaced newModel to newModel
-- deleted frontend-data
-- DC_region befor DC_province
-- change period data: new table name ...dc_chronological_system; removed 'id' and values, changed 'period' to cs_name

--
-- Database: `orea`
--


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
(4, 'cementary or grave');

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
(1, 'male individuals: no.'),
(2, 'female individuals: no.'),
(3, 'not specified: no.'),
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
-- Dumping data for table `newModel_dc_country`
--

INSERT INTO `newModel_dc_country` (`id`, `name`, `original_name`, `authorityfile_id`) VALUES
(1, 'Turkey', 'Türkiye', NULL),
(2, 'Greece', 'Ελλάδα', NULL);

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
(1, 'wild boar', NULL),
(2, 'pig', NULL),
(3, 'cattle', NULL),
(4, 'aurochs', NULL),
(5, 'sheep/goat', NULL),
(6, 'sheep', NULL),
(7, 'wild sheep', NULL),
(8, 'goat', NULL),
(9, 'wild goat', NULL),
(10, 'dog', NULL),
(11, 'horse', NULL),
(12, 'hare', NULL),
(13, 'red deer', NULL),
(14, 'fallow deer', NULL),
(15, 'game', NULL),
(16, 'fish', NULL),
(17, 'molluscs', NULL),
(18, 'tuna', NULL);

--
-- Dumping data for table `newModel_dc_finds_botany_species`
--

INSERT INTO `newModel_dc_finds_botany_species` (`id`, `name`, `latin_name`) VALUES
(1, 'apricot', NULL),
(2, 'barley', NULL),
(3, 'bitter vetch', NULL),
(4, 'broomcorn millet', NULL),
(5, 'chickpea', NULL),
(6, 'einkorn wheat', NULL),
(7, 'emmer wheat', NULL),
(8, 'fava bean', NULL),
(9, 'flax', NULL),
(10, 'foxtail millet', NULL),
(11, 'grass pea', NULL),
(12, 'hemp', NULL),
(13, 'lentil', NULL),
(14, 'pea', NULL),
(15, 'peach', NULL),
(16, 'poppy', NULL),
(17, 'rye', NULL),
(18, 'wild barley', NULL),
(19, 'wild bitter vetch', NULL),
(20, 'wild chickpea', NULL),
(21, 'wild einkorn', NULL),
(22, 'wild emmer', NULL),
(23, 'wild flax', NULL),
(24, 'wild lentil', NULL),
(25, 'wild pea', NULL);

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
(1, 'stone'),
(2, 'obsidian'),
(3, 'fabrics'),
(4, 'spondylusshell'),
(5, 'bone'),
(6, 'shell'),
(7, 'antler'),
(8, 'horn'),
(9, 'metal'),
(10, 'marble'),
(11, 'flint'),
(12, 'chert'),
(13, 'obsidian'),
(14, 'chalcedony'),
(15, 'jasper'),
(16, 'quartz'),
(17, 'rock crystal'),
(18, 'quartzite'),
(19, 'radiolarite');

--
-- Dumping data for table `newModel_dc_finds_pottery_decoration`
--

INSERT INTO `newModel_dc_finds_pottery_decoration` (`id`, `name`) VALUES
(1, 'Anatolia/East Aegean_ Impressed'),
(2, 'Anatolia/East Aegean_ Crusted '),
(3, 'Anatolia/East Aegean_ White on red '),
(4, 'Anatolia/East Aegean_ Red on black '),
(5, 'Anatolia/East Aegean_ Black on red '),
(6, 'Anatolia/East Aegean_ Bead inlay'),
(7, 'Anatolia/East Aegean_ Incised  '),
(8, 'Anatolia/East Aegean_ Pattern burnished'),
(9, 'Anatolia/East Aegean_ Mat-impressed'),
(10, 'Anatolia/East Aegean_ Grooved'),
(11, 'Anatolia/East Aegean_ White '),
(12, 'Anatolia/East Aegean_ Red slipped '),
(13, 'Anatolia/East Aegean_ Black burnished '),
(14, 'Anatolia/East Aegean_ Brown burnished'),
(15, 'Thessaly_ Black and red on cream (polychrome) (Β3β)'),
(16, 'Thessaly_ Black and red on white (polychrome) (Β3γ)'),
(17, 'Thessaly_ Black and white on red black (polychrome) (Β3β)'),
(18, 'Thessaly_ Black burnished “Larisa” (Γ1α; A5α/γ)'),
(19, 'Thessaly_ Black burnished with channeled decoration (Γ1α3)'),
(20, 'Thessaly_ Black burnished with white paint (Γ1α1)'),
(21, 'Thessaly_ Black on red (Β3α2b)'),
(22, 'Thessaly_ Black on white (B3α3)'),
(23, 'Thessaly_ Black pattern burnished (Γ1α2)'),
(24, 'Thessaly_ Brown on buff (matt painted) (Β3ε)'),
(25, 'Thessaly_ Brown on cream (B3α2a)'),
(26, 'Thessaly_ Crusted '),
(27, 'Thessaly_ Grey on grey (Γ1β)'),
(28, 'Thessaly_ Impressed  (A2)'),
(29, 'Thessaly_ Incised (B2)'),
(30, 'Thessaly_ Incised  (Γ2)'),
(31, 'Thessaly_ Monochrome red (A1)'),
(32, 'Thessaly_ Monochrome undecorated (B1)'),
(33, 'Thessaly_ Red burnished (B1)'),
(34, 'Thessaly_ Red on white (A3ß)'),
(35, 'Thessaly_ Red (A3γ)'),
(36, 'Thessaly_ Scraped (A3ε) '),
(37, 'Thessaly_ White on red (A3α)'),
(38, 'Thessaly_ White on red (Β3α1)'),
(39, 'Southern/Central Greece, Cyclades_ Black burnished '),
(40, 'Southern/Central Greece, Cyclades_ Black on red '),
(41, 'Southern/Central Greece, Cyclades_ Coarse Urfirnis '),
(42, 'Southern/Central Greece, Cyclades_ Coarse '),
(43, 'Southern/Central Greece, Cyclades_ Crusted '),
(44, 'Southern/Central Greece, Cyclades_ Grooved '),
(45, 'Southern/Central Greece, Cyclades_ Incised '),
(46, 'Southern/Central Greece, Cyclades_ Matt painted '),
(47, 'Southern/Central Greece, Cyclades_ Monochrome burnished '),
(48, 'Southern/Central Greece, Cyclades_ Monochrome Urfirnis '),
(49, 'Southern/Central Greece, Cyclades_ Pattern burnished'),
(50, 'Southern/Central Greece, Cyclades_ Patterned Urfirnis '),
(51, 'Southern/Central Greece, Cyclades_ Plastic '),
(52, 'Southern/Central Greece, Cyclades_ Polychrome '),
(53, 'Southern/Central Greece, Cyclades_ Red on white '),
(54, 'Southern/Central Greece, Cyclades_ Rippled '),
(55, 'Southern/Central Greece, Cyclades_ Stroke-and pattern burnished'),
(56, 'Southern/Central Greece, Cyclades_ White on red '),
(57, 'Southern/Central Greece, Cyclades_ White '),
(58, 'Southern/Central Greece, Cyclades_ White on black'),
(59, 'Macedonia/Thrace_ Barbotine '),
(60, 'Macedonia/Thrace_ Black on red '),
(61, 'Macedonia/Thrace_ Black topped '),
(62, 'Macedonia/Thrace_ Brown on buff '),
(63, 'Macedonia/Thrace_ Brown on red '),
(64, 'Macedonia/Thrace_ Brown on cream '),
(65, 'Macedonia/Thrace_ Burnished '),
(66, 'Macedonia/Thrace_ Channeled '),
(67, 'Macedonia/Thrace_ Coarse '),
(68, 'Macedonia/Thrace_ Excised '),
(69, 'Macedonia/Thrace_ Excised-with-graphite '),
(70, 'Macedonia/Thrace_ Galepsos ware'),
(71, 'Macedonia/Thrace_ Graphite painted'),
(72, 'Macedonia/Thrace_ Gray lustre '),
(73, 'Macedonia/Thrace_ Grooved '),
(74, 'Macedonia/Thrace_ Grooved with graphite '),
(75, 'Macedonia/Thrace_ Incised '),
(76, 'Macedonia/Thrace_ Matt brown on white '),
(77, 'Macedonia/Thrace_ Orange on orange '),
(78, 'Macedonia/Thrace_ Plastic '),
(79, 'Macedonia/Thrace_ Polychrome'),
(80, 'Macedonia/Thrace_ Red crusted '),
(81, 'Macedonia/Thrace_ Red on brown '),
(82, 'Macedonia/Thrace_ Red on white '),
(83, 'Macedonia/Thrace_ Red slipped '),
(84, 'Macedonia/Thrace_ Rippled '),
(85, 'Macedonia/Thrace_ Rusticated'),
(86, 'Macedonia/Thrace_ Shell stamped'),
(87, 'Macedonia/Thrace_ White on red '),
(88, 'Macedonia/Thrace_ Applied disc'),
(89, 'Crete_ Barbotine '),
(90, 'Crete_ Brushed '),
(91, 'Crete_ Burnished '),
(92, 'Crete_ Coarse '),
(93, 'Crete_ Granulata ware'),
(94, 'Crete_ Grooved '),
(95, 'Crete_ Impressed '),
(96, 'Crete_ Incised '),
(97, 'Crete_ Incised-Pointillé decoration'),
(98, 'Crete_ Monochrome '),
(99, 'Crete_ Painted '),
(100, 'Crete_ Pattern burnished '),
(101, 'Crete_ Pattern jabbed '),
(102, 'Crete_ Pellet decoration'),
(103, 'Crete_ Plastic cordon decoration'),
(104, 'Crete_ Plastic '),
(105, 'Crete_ Pointillé decoration'),
(106, 'Crete_ Polished'),
(107, 'Crete_ Punched'),
(108, 'Crete_ Red on buff'),
(109, 'Crete_ Rippled burnished'),
(110, 'Crete_ Rippled '),
(111, 'Crete_ Scored '),
(112, 'Crete_ Scribble burnished '),
(113, 'Crete_ Single jabbed'),
(114, 'Crete_ Wiped ');

--
-- Dumping data for table `newModel_dc_finds_pottery_detail`
--

INSERT INTO `newModel_dc_finds_pottery_detail` (`id`, `name`) VALUES
(1, 'Anatolia/East Aegean_ Horned handle'),
(2, 'Anatolia/East Aegean_ Mushroom handle'),
(3, 'Anatolia/East Aegean_ Bar handle with lug'),
(4, 'Anatolia/East Aegean_ Rolled rim'),
(5, 'Anatolia/East Aegean_ Everted rim '),
(6, 'Anatolia/East Aegean_ Flaring rim'),
(7, 'Anatolia/East Aegean_ Inside bevelled and decorated rim '),
(8, 'Anatolia/East Aegean_ Rim contracting heavily inward'),
(9, 'Anatolia/East Aegean_ Foot'),
(10, 'Anatolia/East Aegean_ Narrow-mouthed rim'),
(11, 'Thessaly_ Elephant lug'),
(12, 'Thessaly_ Ledge lug'),
(13, 'Thessaly_ Leg'),
(14, 'Thessaly_ Spout'),
(15, 'Thessaly_ Strap handle'),
(16, 'Thessaly_ Tab handle'),
(17, 'Thessaly_ Vertically perforated lug'),
(18, 'Thessaly_ Rolled rim'),
(19, 'Southern/Central Greece, Cyclades_ Elephant lug'),
(20, 'Southern/Central Greece, Cyclades_ Ledge lug'),
(21, 'Southern/Central Greece, Cyclades_ Leg'),
(22, 'Southern/Central Greece, Cyclades_ Round bar handle'),
(23, 'Southern/Central Greece, Cyclades_ Spout'),
(24, 'Southern/Central Greece, Cyclades_ Strap handle'),
(25, 'Southern/Central Greece, Cyclades_ Tab handle'),
(26, 'Southern/Central Greece, Cyclades_ Tubular lug'),
(27, 'Southern/Central Greece, Cyclades_ Vertically perforated lug'),
(28, 'Macedonia/Thrace_ Ear handle'),
(29, 'Macedonia/Thrace_ High strap handle'),
(30, 'Macedonia/Thrace_ Knobbed handle'),
(31, 'Macedonia/Thrace_ Ledge lug'),
(32, 'Macedonia/Thrace_ Leg'),
(33, 'Macedonia/Thrace_ Mushroom handle'),
(34, 'Macedonia/Thrace_ Prong handle'),
(35, 'Macedonia/Thrace_ Strap handle'),
(36, 'Macedonia/Thrace_ Stringhole lug'),
(37, 'Macedonia/Thrace_ Tab handle'),
(38, 'Macedonia/Thrace_ Tunnel lug'),
(39, 'Macedonia/Thrace_ Pedestal '),
(40, 'Crete_ Bridge spout'),
(41, 'Crete_ Concave flat base'),
(42, 'Crete_ Curved tapered-up rim'),
(43, 'Crete_ Ear handle'),
(44, 'Crete_ Flaring rim'),
(45, 'Crete_ Horned handle'),
(46, 'Crete_ Knobbed wishbone handle'),
(47, 'Crete_ Ledge lug'),
(48, 'Crete_ Leg'),
(49, 'Crete_ Miniature strap handle'),
(50, 'Crete_ Pronged wishbone handle'),
(51, 'Crete_ Strap handle with round hole'),
(52, 'Crete_ Strap handle'),
(53, 'Crete_ Tubular lug'),
(54, 'Crete_ V-shaped spout'),
(55, 'Crete_ “winged” strap handle'),
(56, 'Crete_ Wishbone handle'),
(57, 'Crete_ Tapered-up rim'),
(58, 'Crete_ Fenestrated pedestal'),
(59, 'Crete_ Flat base'),
(60, 'Crete_ Offset rim'),
(61, 'Crete_ Pedestal'),
(62, 'Crete_ Rounded base'),
(63, 'Crete_ Thickened rim'),
(64, 'Crete_ Small foot');

--
-- Dumping data for table `newModel_dc_finds_pottery_form`
--

INSERT INTO `newModel_dc_finds_pottery_form` (`id`, `name`) VALUES
(1, 'Anatolia/East Aegean_ Anthropomorphic vessel'),
(2, 'Anatolia/East Aegean_ Bag shaped vessel (hole mouthed vessel)'),
(3, 'Anatolia/East Aegean_ Baking pan'),
(4, 'Anatolia/East Aegean_ Box'),
(5, 'Anatolia/East Aegean_ Carinated bowl'),
(6, 'Anatolia/East Aegean_ Cheese pot'),
(7, 'Anatolia/East Aegean_ Globular jar'),
(8, 'Anatolia/East Aegean_ Cup'),
(9, 'Anatolia/East Aegean_ Dome-shaped shallow bowls'),
(10, 'Anatolia/East Aegean_ Jug'),
(11, 'Anatolia/East Aegean_ Fikirtepe box '),
(12, 'Anatolia/East Aegean_ Mug'),
(13, 'Anatolia/East Aegean_ Vessel'),
(14, 'Anatolia/East Aegean_ Necked jars'),
(15, 'Anatolia/East Aegean_ Bowl'),
(16, 'Anatolia/East Aegean_ Shallow bowl '),
(17, 'Anatolia/East Aegean_ Tulip shaped beaker'),
(18, 'Thessaly_ Askos'),
(19, 'Thessaly_ Baking pan'),
(20, 'Thessaly_ Basin'),
(21, 'Thessaly_ '),
(22, 'Thessaly_ Bowl'),
(23, 'Thessaly_ Carinated bowl'),
(24, 'Thessaly_ Cheese pot'),
(25, 'Thessaly_ Collared jar'),
(26, 'Thessaly_ Deep, globular jar'),
(27, 'Thessaly_ Dimini bowl '),
(28, 'Thessaly_ Kylix'),
(29, 'Thessaly_ Fruitstand'),
(30, 'Thessaly_ Handless cup'),
(31, 'Thessaly_ Hole-mouthed jar'),
(32, 'Thessaly_ Mug'),
(33, 'Thessaly_ Pithos'),
(34, 'Thessaly_ Scoop'),
(35, 'Thessaly_ Skyphos'),
(36, 'Southern/Central Greece, Cyclades_ Askos'),
(37, 'Southern/Central Greece, Cyclades_ Baking pan'),
(38, 'Southern/Central Greece, Cyclades_ Carinated bowl'),
(39, 'Southern/Central Greece, Cyclades_ Cheese pot'),
(40, 'Southern/Central Greece, Cyclades_ Jar'),
(41, 'Southern/Central Greece, Cyclades_ Collared bowl'),
(42, 'Southern/Central Greece, Cyclades_ Collared jar'),
(43, 'Southern/Central Greece, Cyclades_ Deep bowl'),
(44, 'Southern/Central Greece, Cyclades_ Fruitstand'),
(45, 'Southern/Central Greece, Cyclades_ Gouged bowl'),
(46, 'Southern/Central Greece, Cyclades_ Husking bowl'),
(47, 'Southern/Central Greece, Cyclades_ Medium bowl'),
(48, 'Southern/Central Greece, Cyclades_ Piriform jar'),
(49, 'Southern/Central Greece, Cyclades_ Pithos'),
(50, 'Southern/Central Greece, Cyclades_ Platter'),
(51, 'Southern/Central Greece, Cyclades_ Bowl'),
(52, 'Southern/Central Greece, Cyclades_ Rhyton'),
(53, 'Southern/Central Greece, Cyclades_ Scoop'),
(54, 'Southern/Central Greece, Cyclades_ Shoulder bowl'),
(55, 'Macedonia/Thrace_ Amphora'),
(56, 'Macedonia/Thrace_ Bowl'),
(57, 'Macedonia/Thrace_ Cup'),
(58, 'Macedonia/Thrace_ Jar'),
(59, 'Macedonia/Thrace_ Jug'),
(60, 'Macedonia/Thrace_ Ladle'),
(61, 'Macedonia/Thrace_ Lamp'),
(62, 'Macedonia/Thrace_ Lid'),
(63, 'Macedonia/Thrace_ Pitcher'),
(64, 'Macedonia/Thrace_ Pithos'),
(65, 'Macedonia/Thrace_ Plate'),
(66, 'Macedonia/Thrace_ Pyxis'),
(67, 'Macedonia/Thrace_ Scoop'),
(68, 'Macedonia/Thrace_ Strainer'),
(69, 'Macedonia/Thrace_ Rectangular vessel'),
(70, 'Macedonia/Thrace_ Stand'),
(71, 'Macedonia/Thrace_ Tripod'),
(72, 'Crete_ Baking pan'),
(73, 'Crete_ Bottle'),
(74, 'Crete_ Bowl'),
(75, 'Crete_ Bucket-like vessel'),
(76, 'Crete_ Carinated bowl'),
(77, 'Crete_ Carinated incurved bowl'),
(78, 'Crete_ Carinated jar'),
(79, 'Crete_ Carinated shallow bowl'),
(80, 'Crete_ Cheese pot'),
(81, 'Crete_ Cup '),
(82, 'Crete_ Deep bowl'),
(83, 'Crete_ Dipper'),
(84, 'Crete_ Mug'),
(85, 'Crete_ Funnel-necked jar'),
(86, 'Crete_ Jar'),
(87, 'Crete_ Hole-mouthed jar'),
(88, 'Crete_ Incurved bowl'),
(89, 'Crete_ Collared jar'),
(90, 'Crete_ Medium bowl'),
(91, 'Crete_ Chalice'),
(92, 'Crete_ Rhyton'),
(93, 'Crete_ Shallow bowl '),
(94, 'Crete_ Tray');

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
(27, 'Naturalistic');

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
-- Dumping data for table `newModel_dc_region`
--


INSERT INTO `newModel_dc_region` (`id`, `name`, `original_name`, `authorityfile_id`, `country_id`) VALUES
(1, 'Anatolia/East Aegean', 'Anatolien/Ostägäis', NULL, 1),
(2, 'Crete', 'Kreta', NULL, NULL),
(3, 'Cyclades', 'Kykladen', NULL, NULL),
(4, 'Macedonia/Thrace', 'Makedonien/Thrakien', NULL, NULL),
(5, 'Southern and Central Greece', 'Süd- und Zentralgriechenland', NULL, NULL),
(6, 'Thessaly', 'Thessalien', NULL, NULL);


--
-- Dumping data for table `newModel_dc_province`
--

INSERT INTO `newModel_dc_province` (`id`, `name`, `original_name`, `authorityfile_id`, `region_id`) VALUES
(448, 'Adana', 'Adana', NULL, 1),
(449, 'Adıyaman', 'Adiyaman', NULL, 1),
(450, 'Afyonkarahisar', 'Afyon', NULL, 1),
(451, 'Ağrı', 'Agri', NULL, 1),
(452, 'Aksaray', 'Aksaray', NULL, 1),
(453, 'Amasya', 'Amasya', NULL, 1),
(454, 'Ankara', 'Ankara', NULL, 1),
(455, 'Antalya', 'Antalya', NULL, 1),
(456, 'Ardahan', 'Ardahan', NULL, 1),
(457, 'Artvin', 'Artvin', NULL, 1),
(458, 'Aydın', 'Aydin', NULL, 1),
(459, 'Balıkesir', 'Balikesir', NULL, 1),
(460, 'Bartın', 'Bartin', NULL, 1),
(461, 'Batman', 'Batman', NULL, 1),
(462, 'Bayburt', 'Bayburt', NULL, 1),
(463, 'Bilecik', 'Bilecik', NULL, 1),
(464, 'Bingöl', 'Bingol', NULL, 1),
(465, 'Bitlis', 'Bitlis', NULL, 1),
(466, 'Bolu', 'Bolu', NULL, 1),
(467, 'Burdur', 'Burdur', NULL, 1),
(468, 'Bursa', 'Bursa', NULL, 1),
(469, 'Çanakkale', 'Canakkale', NULL, 1),
(470, 'Çankırı', 'Cankiri', NULL, 1),
(471, 'Çorum', 'Corum', NULL, 1),
(472, 'Denizli', 'Denizli', NULL, 1),
(473, 'Diyarbakır', 'Diyarbakir', NULL, 1),
(474, 'Dodecanese', 'Dodecanese', NULL, 1),
(475, 'Düzce', 'Duzce', NULL, 1),
(476, 'Edirne', 'Edirne', NULL, 1),
(477, 'Elazığ', 'Elazig', NULL, 1),
(478, 'Erzincan', 'Erzincan', NULL, 1),
(479, 'Erzurum', 'Erzurum', NULL, 1),
(480, 'Eskişehir', 'Eskisehir', NULL, 1),
(481, 'Gaziantep', 'Gaziantep', NULL, 1),
(482, 'Giresun', 'Giresun', NULL, 1),
(483, 'Gümüşhane', 'Gumushane', NULL, 1),
(484, 'Hakkari', 'Hakkari', NULL, 1),
(485, 'Hatay', 'Hatay', NULL, 1),
(486, 'Iğdır', 'Igdir', NULL, 1),
(487, 'Isparta', 'Isparta', NULL, 1),
(488, 'İstanbul', 'Istanbul', NULL, 1),
(489, 'İzmir', 'Izmir', NULL, 1),
(490, 'Kahramanmaraş', 'Kahramanmaras', NULL, 1),
(491, 'Karabük', 'Karabuk', NULL, 1),
(492, 'Karaman', 'Karaman', NULL, 1),
(493, 'Kars', 'Kars', NULL, 1),
(494, 'Kastamonu', 'Kastamonu', NULL, 1),
(495, 'Kayseri', 'Kayseri', NULL, 1),
(496, 'Kilis', 'Kilis', NULL, 1),
(497, 'Kırıkkale', 'Kirikkale', NULL, 1),
(498, 'Kırklareli', 'Kirklareli', NULL, 1),
(499, 'Kırşehir', 'Kirsehir', NULL, 1),
(500, 'Kocaeli', 'Kocaeli', NULL, 1),
(501, 'Konya', 'Konya', NULL, 1),
(502, 'Kütahya', 'Kutahya', NULL, 1),
(503, 'Malatya', 'Malatya', NULL, 1),
(504, 'Manisa', 'Manisa', NULL, 1),
(505, 'Mardin', 'Mardin', NULL, 1),
(506, 'Mersin', 'Mersin', NULL, 1),
(507, 'Muğla', 'Mugla', NULL, 1),
(508, 'Muş', 'Mus', NULL, 1),
(509, 'Nevşehir', 'Nevsehir', NULL, 1),
(510, 'Niğde', 'Nigde', NULL, 1),
(511, 'Ordu', 'Ordu', NULL, 1),
(512, 'Osmaniye', 'Osmaniye', NULL, 1),
(513, 'Rize', 'Rize', NULL, 1),
(514, 'Sakarya', 'Sakarya', NULL, 1),
(515, 'Samsun', 'Samsun', NULL, 1),
(516, 'Şanlıurfa', 'Sanliurfa', NULL, 1),
(517, 'Siirt', 'Siirt', NULL, 1),
(518, 'Sinop', 'Sinop', NULL, 1),
(519, 'Şırnak', 'Sirnak', NULL, 1),
(520, 'Sivas', 'Sivas', NULL, 1),
(521, 'Tekirdağ', 'Tekirdag', NULL, 1),
(522, 'Tokat', 'Tokat', NULL, 1),
(523, 'Trabzon', 'Trabzon', NULL, 1),
(524, 'Tunceli', 'Tunceli', NULL, 1),
(525, 'Uşak', 'Usak', NULL, 1),
(526, 'Van', 'Van', NULL, 1),
(527, 'Yalova', 'Yalova', NULL, 1),
(528, 'Yozgat', 'Yozgat', NULL, 1),
(529, 'Zonguldak', 'Zonguldak', NULL, 1),
(530, 'Xanthos', 'Xanthos', NULL, 1),
(531, 'Samos –  Ikaria', 'Samos –  Ikaria', NULL, 1),
(532, 'Chios', 'Chios', NULL, 1),
(533, 'Lesvos', 'Lesvos/Lesbos', NULL, 1),
(534, 'Karditsa', 'Karditsa', NULL, 1),
(535, 'Larisa', 'Larisa', NULL, 1),
(536, 'Magnisia', 'Magnisia/Magnesia', NULL, 1),
(537, 'Trikala', 'Trikala', NULL, 1),
(538, 'Aitoloakarnania kai Lefkada', 'Aetolia-Acarnania and Lefkada', NULL, 6),
(539, 'Akhaia', 'Akhaia', NULL, 6),
(540, 'Arkadia', 'Arcadia', NULL, 6),
(541, 'Argolida', 'Argolid', NULL, 6),
(542, 'Arta', 'Arta', NULL, 6),
(543, 'Athina', 'Athens', NULL, 6),
(544, 'Boiotia/Voiotias', 'Boeotia', NULL, 6),
(545, 'Kerkyra', 'Corfu', NULL, 6),
(546, 'Korinthia', 'Corinthia', NULL, 6),
(547, 'Kyklades', 'Cyclades', NULL, 6),
(548, 'Anatoliki Attiki', 'East Attika', NULL, 6),
(549, 'Ileia', 'Elis/Ilia', NULL, 6),
(550, 'Evoia', 'Euboea', NULL, 6),
(551, 'Ioannina', 'Ioannina', NULL, 6),
(552, 'Kephallinia', 'Kephallinia', NULL, 6),
(553, 'Lakonia', 'Laconia', NULL, 6),
(554, 'Messinia', 'Messinia/Messenia', NULL, 6),
(555, 'Phokida', 'Phocis', NULL, 6),
(556, 'Phthiotida kai Evrytania', 'Phthiotis and Evritania', NULL, 6),
(557, 'Preveza', 'Preveza', NULL, 6),
(558, 'Thesprotia', 'Thesprotia', NULL, 6),
(559, 'Dytiki Attiki, Pireas kai Nisia', 'Western Attica, Piraeus and islands', NULL, 6),
(560, 'Zakynthos', 'Zakynthos', NULL, 6),
(561, 'Chalkidiki kai Agion Orous', 'Chalcidice and Mount Athos', NULL, 2),
(562, 'Poli Thessaloniki', 'City of Thessaloniki', NULL, 2),
(563, 'Drama', 'Drama', NULL, 2),
(564, 'Evros', 'Evros', NULL, 2),
(565, 'Phlorina', 'Florina', NULL, 2),
(566, 'Grevena', 'Grevena', NULL, 2),
(567, 'Imathia', 'Imathia', NULL, 2),
(568, 'Kastoria', 'Kastoria', NULL, 2),
(569, 'Kavala – Thasos', 'Kavala – Thasos', NULL, 2),
(570, 'Kilkis', 'Kilkis', NULL, 2),
(571, 'Kozani', 'Kozani', NULL, 2),
(572, 'Pella', 'Pella ', NULL, 2),
(573, 'Peripheria Thessaloniki', 'Periphery Thessaloniki', NULL, 2),
(574, 'Pieria', 'Pieria', NULL, 2),
(575, 'Rodopi', 'Rodopi', NULL, 2),
(576, 'Serres', 'Serres', NULL, 2),
(577, 'Irakleio', 'Iraklio', NULL, 2),
(578, 'Khania', 'Khania', NULL, 2),
(579, 'Lasithios', 'Lasithi', NULL, 2),
(580, 'Rethymno', 'Rethymno', NULL, 2);


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
(326, 'Hugo Obermaier Gesellschaft');

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

--
-- Dumping data for table `newModel_finds`
--


INSERT INTO `newModel_dc_chronological_system` (`cs_name`, `period_name`, `start_date1_BC`, `start_date2_BC`, `end_date1_BC`, `end_date2_BC`, `region_id`) VALUES
('Anatolia', 'Pre-Pottery Neolithic  ', 8000, 8000, 7500, 7500, 1),
('Anatolia', 'Pre-Pottery Neolithic/Neolithic', 7500, 7500, 7000, 7000, 1),
('Anatolia', 'Neolithic I', 7000, 7000, 6500, 6500, 1),
('Anatolia', 'Neolithic II', 6500, 6500, 6000, 6000, 1),
('Anatolia', 'Early Chalcolithic', 6000, 6000, 5500, 5500, 1),
('Anatolia', 'Middle Chalcolithic', 5500, 5500, 4250, 4250, 1),
('Anatolia', 'Late Chalcolithic I', 4250, 4250, 4000, 4000, 1),
('Anatolia', 'Late Chalcolithic II', 4000, 4000, 3500, 3500, 1),
('Anatolia', 'Late Chalcolithic III', 3500, 3500, 3000, 3000, 1),
('Alram-Stern 1996', 'Aceramic Neolithic (?)', 7000, 7000, 6500, 6500, 5),
('Alram-Stern 1997', 'Early Neolithic', 6500, 6500, 5800, 5800, 5),
('Alram-Stern 1998', 'Middle Neolithic', 5800, 5800, 5400, 5400, 5),
('Alram-Stern 1999', 'Late Neolithic (Early)', 5400, 5400, 4900, 4900, 5),
('Alram-Stern 2000', 'Late Neolithic (Late)', 4900, 4900, 4500, 4300, 5),
('Alram-Stern 2001', 'Chalcolithic/Final Neolithic', 4500, 4300, 3700, 3700, 5),
('Alram-Stern 2002', 'Chalcolithic/Final Neolithic (Late)', 3700, 3700, 3300, 3300, 5),
('Alram-Stern 2003', 'Early Helladic I/Early Cycladic', 3300, 3300, 2900, 2900, 5),
('K. Gallis in: Papathanassopoulous 1996 (Fig. 3)', 'Early Neolithic: "Protosesklo"', 6500, 6500, 5800, 5800, 6),
('K. Gallis in: Papathanassopoulous 1996 (Fig. 3)', 'Middle Neolithic: "Sesklo"', 5800, 5800, 5400, 5400, 6),
('K. Gallis in: Papathanassopoulous 1996 (Fig. 3)', 'Late Neolithic: Tsangli, Arapi', 5400, 5400, 4900, 4900, 6),
('K. Gallis in: Papathanassopoulous 1996 (Fig. 3)', 'Late Neolithic: Dimini', 4900, 4900, 4500, 4300, 6),
('K. Gallis in: Papathanassopoulous 1996 (Fig. 3)', 'Chalcolithic/Final Neolithic, Rachmani', 4500, 4300, 3700, 3700, 6),
('K. Gallis in: Papathanassopoulous 1996 (Fig. 3)', 'Chalcolithic/Final Neolithic (Late)', 3700, 3700, 3300, 3300, 6),
('K. Gallis in: Papathanassopoulous 1996 (Fig. 3)', 'Early Bronze Age', 3300, 3300, 2900, 2900, 6),
('Macedonia/Thrace', 'Late Neolithic', 5800, 5800, 4900, 4900, 4),
('Macedonia/Thrace', 'Chalcolithic', 4900, 4900, 3300, 3300, 4),
('Macedonia/Thrace', 'Early Bronze Age', 3300, 3300, 2900, 2900, 4),
('Evans/Vagnetti', 'Aceramic Neolithic ', 7000, 7000, 6500, 6500, 2),
('Evans/Vagnetti', 'Early Neolithic I', 6500, 6500, 4900, 4900, 2),
('Evans/Vagnetti', 'Early Neolithic II + Middle Neolithic', 4900, 4900, 4500, 4300, 2),
('Evans/Vagnetti', 'Late Neolithic', 4500, 4300, 3700, 3700, 2),
('Evans/Vagnetti', 'Final Neolithic', 3700, 3700, 2900, 2900, 2),
('Tomkins 2007a', 'Initial Neolithic', 7000, 7000, 6500, 6500, 2),
('Tomkins 2007a', 'Early Neolithic', 6500, 6500, 5800, 5800, 2),
('Tomkins 2007a', 'Middle Neolithic', 5800, 5800, 5400, 5400, 2),
('Tomkins 2007a', 'Late Neolithic I', 5400, 5400, 4900, 4900, 2),
('Tomkins 2007a', 'Late Neolithic II + Final Neolithic IA', 4900, 4900, 4500, 4300, 2),
('Tomkins 2007a', 'Final Neolithic IB + Final Neolithic II', 4500, 4300, 3700, 3700, 2),
('Tomkins 2007a', 'Final Neolithic III', 3700, 3700, 3300, 3300, 2),
('Tomkins 2007a', 'Final Neolithic IV', 3300, 3300, 2900, 2900, 2);

