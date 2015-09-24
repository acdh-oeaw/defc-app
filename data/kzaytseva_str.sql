-- phpMyAdmin SQL Dump
-- version 4.4.14.1
-- http://www.phpmyadmin.net
--
-- Host: helios.arz.oeaw.ac.at
-- Generation Time: Sep 24, 2015 at 09:19 AM
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

-- --------------------------------------------------------

--
-- Table structure for table `newModel_area`
--

CREATE TABLE IF NOT EXISTS `newModel_area` (
  `id` int(11) NOT NULL,
  `area_nr` varchar(45) DEFAULT NULL,
  `stratigraphical_unit_id` varchar(100) DEFAULT NULL,
  `geographical_reference` varchar(100) DEFAULT NULL,
  `description` longtext,
  `settlement_human_remains` varchar(3) DEFAULT NULL,
  `cemetery_or_grave` varchar(100) DEFAULT NULL,
  `grave_number_of_graves` varchar(100) DEFAULT NULL,
  `grave_estimated_number_of_individuals` varchar(100) DEFAULT NULL,
  `area_type_id` int(11),
  `cave_rockshelters_evidence_of_graves_human_remains_id` int(11),
  `cave_rockshelters_type_id` int(11),
  `site_id` int(11),
  `comment` longtext,
  `c14_absolute_from` int(11),
  `c14_absolute_to` int(11),
  `c14_calibrated` varchar(100),
  `grave_number_of_female_sex` int(11),
  `grave_number_of_male_sex` int(11),
  `grave_number_of_not_specified_sex` int(11)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_area_cave_rockshelters_evidence_of_occupation`
--

CREATE TABLE IF NOT EXISTS `newModel_area_cave_rockshelters_evidence_of_occupation` (
  `id` int(11) NOT NULL,
  `area_id` int(11) NOT NULL,
  `dc_area_evidenceofoccupation_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_area_cemetery_or_graves_mortuary_features`
--

CREATE TABLE IF NOT EXISTS `newModel_area_cemetery_or_graves_mortuary_features` (
  `id` int(11) NOT NULL,
  `area_id` int(11) NOT NULL,
  `dc_area_mortuaryfeatures_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_area_cemetery_or_graves_topography`
--

CREATE TABLE IF NOT EXISTS `newModel_area_cemetery_or_graves_topography` (
  `id` int(11) NOT NULL,
  `area_id` int(11) NOT NULL,
  `dc_area_topography_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_area_grave_age_groups`
--

CREATE TABLE IF NOT EXISTS `newModel_area_grave_age_groups` (
  `id` int(11) NOT NULL,
  `area_id` int(11) NOT NULL,
  `dc_area_agegroups_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_area_grave_manipulations_of_graves`
--

CREATE TABLE IF NOT EXISTS `newModel_area_grave_manipulations_of_graves` (
  `id` int(11) NOT NULL,
  `area_id` int(11) NOT NULL,
  `dc_area_manipulationofgraves_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_area_grave_sexes`
--

CREATE TABLE IF NOT EXISTS `newModel_area_grave_sexes` (
  `id` int(11) NOT NULL,
  `area_id` int(11) NOT NULL,
  `dc_area_sexes_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_area_grave_type`
--

CREATE TABLE IF NOT EXISTS `newModel_area_grave_type` (
  `id` int(11) NOT NULL,
  `area_id` int(11) NOT NULL,
  `dc_area_gravetype_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_area_grave_type_of_human_remains`
--

CREATE TABLE IF NOT EXISTS `newModel_area_grave_type_of_human_remains` (
  `id` int(11) NOT NULL,
  `area_id` int(11) NOT NULL,
  `dc_area_typeofhumanremains_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_area_period`
--

CREATE TABLE IF NOT EXISTS `newModel_area_period` (
  `id` int(11) NOT NULL,
  `area_id` int(11) NOT NULL,
  `period_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_area_quarry_exploitation_type`
--

CREATE TABLE IF NOT EXISTS `newModel_area_quarry_exploitation_type` (
  `id` int(11) NOT NULL,
  `area_id` int(11) NOT NULL,
  `dc_area_exploitationtype_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_area_quarry_raw_material`
--

CREATE TABLE IF NOT EXISTS `newModel_area_quarry_raw_material` (
  `id` int(11) NOT NULL,
  `area_id` int(11) NOT NULL,
  `dc_area_rawmaterial_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_area_reference`
--

CREATE TABLE IF NOT EXISTS `newModel_area_reference` (
  `id` int(11) NOT NULL,
  `area_id` int(11) NOT NULL,
  `reference_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_area_settlement_building_technique`
--

CREATE TABLE IF NOT EXISTS `newModel_area_settlement_building_technique` (
  `id` int(11) NOT NULL,
  `area_id` int(11) NOT NULL,
  `dc_area_buildingtechnique_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_area_settlement_construction_type`
--

CREATE TABLE IF NOT EXISTS `newModel_area_settlement_construction_type` (
  `id` int(11) NOT NULL,
  `area_id` int(11) NOT NULL,
  `dc_area_constructiontype_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_area_settlement_special_features`
--

CREATE TABLE IF NOT EXISTS `newModel_area_settlement_special_features` (
  `id` int(11) NOT NULL,
  `area_id` int(11) NOT NULL,
  `dc_area_specialfeatures_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_area_settlement_structure`
--

CREATE TABLE IF NOT EXISTS `newModel_area_settlement_structure` (
  `id` int(11) NOT NULL,
  `area_id` int(11) NOT NULL,
  `dc_area_settlementstructure_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_area_settlement_type`
--

CREATE TABLE IF NOT EXISTS `newModel_area_settlement_type` (
  `id` int(11) NOT NULL,
  `area_id` int(11) NOT NULL,
  `dc_area_settlementtype_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_area_agegroups`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_area_agegroups` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_area_areatype`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_area_areatype` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_area_buildingtechnique`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_area_buildingtechnique` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_area_caverockshelterstype`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_area_caverockshelterstype` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_area_constructiontype`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_area_constructiontype` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_area_evidenceofgraveshumanremains`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_area_evidenceofgraveshumanremains` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_area_evidenceofoccupation`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_area_evidenceofoccupation` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_area_exploitationtype`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_area_exploitationtype` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_area_gravetype`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_area_gravetype` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_area_manipulationofgraves`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_area_manipulationofgraves` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_area_mortuaryfeatures`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_area_mortuaryfeatures` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_area_rawmaterial`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_area_rawmaterial` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_area_settlementstructure`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_area_settlementstructure` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_area_settlementtype`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_area_settlementtype` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_area_sexes`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_area_sexes` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_area_specialfeatures`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_area_specialfeatures` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_area_topography`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_area_topography` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_area_typeofhumanremains`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_area_typeofhumanremains` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_chronological_system`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_chronological_system` (
  `id` int(11) NOT NULL,
  `cs_name` varchar(100) DEFAULT NULL,
  `period_name` varchar(100) DEFAULT NULL,
  `start_date1_BC` int(11) DEFAULT NULL,
  `start_date2_BC` int(11) DEFAULT NULL,
  `end_date1_BC` int(11) DEFAULT NULL,
  `end_date2_BC` int(11) DEFAULT NULL,
  `region_id` int(11)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_country`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_country` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `original_name` varchar(100) DEFAULT NULL,
  `authorityfile_id` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_finds_amount`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_finds_amount` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_finds_animal_remains_completeness`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_finds_animal_remains_completeness` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_finds_animal_remains_part`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_finds_animal_remains_part` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_finds_animal_remains_species`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_finds_animal_remains_species` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `latin_name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_finds_botany_species`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_finds_botany_species` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `latin_name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_finds_lithics_core`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_finds_lithics_core` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_finds_lithics_debitage`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_finds_lithics_debitage` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_finds_lithics_modified_tools`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_finds_lithics_modified_tools` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_finds_lithics_technology`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_finds_lithics_technology` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_finds_material`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_finds_material` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_finds_pottery_decoration`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_finds_pottery_decoration` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `region` varchar(100)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_finds_pottery_detail`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_finds_pottery_detail` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `region` varchar(100)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_finds_pottery_form`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_finds_pottery_form` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `region` varchar(100)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_finds_small_finds_category`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_finds_small_finds_category` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_finds_small_finds_type`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_finds_small_finds_type` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_finds_type`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_finds_type` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_interpretation_productiontype`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_interpretation_productiontype` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_interpretation_subsistencetype`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_interpretation_subsistencetype` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_period_datedby`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_period_datedby` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_period_datingmethod`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_period_datingmethod` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_province`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_province` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `original_name` varchar(100) DEFAULT NULL,
  `authorityfile_id` varchar(100) DEFAULT NULL,
  `region_id` int(11)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_reference_type`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_reference_type` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_region`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_region` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `original_name` varchar(100) DEFAULT NULL,
  `authorityfile_id` varchar(100) DEFAULT NULL,
  `country_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_researchevent_institution`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_researchevent_institution` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_researchevent_researchtype`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_researchevent_researchtype` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_researchevent_special_analysis`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_researchevent_special_analysis` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_dc_site_geographicalreferencesystem`
--

CREATE TABLE IF NOT EXISTS `newModel_dc_site_geographicalreferencesystem` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_finds`
--

CREATE TABLE IF NOT EXISTS `newModel_finds` (
  `id` int(11) NOT NULL,
  `confidence` varchar(50) DEFAULT NULL,
  `comment` longtext,
  `amount_id` int(11) DEFAULT NULL,
  `animal_remains_completeness_id` int(11) DEFAULT NULL,
  `area_id` int(11) DEFAULT NULL,
  `finds_type_id` int(11) DEFAULT NULL,
  `research_event_id` int(11),
  `small_finds_category_id` int(11)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_finds_animal_remains_part`
--

CREATE TABLE IF NOT EXISTS `newModel_finds_animal_remains_part` (
  `id` int(11) NOT NULL,
  `finds_id` int(11) NOT NULL,
  `dc_finds_animal_remains_part_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_finds_animal_remains_species`
--

CREATE TABLE IF NOT EXISTS `newModel_finds_animal_remains_species` (
  `id` int(11) NOT NULL,
  `finds_id` int(11) NOT NULL,
  `dc_finds_animal_remains_species_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_finds_botany_species`
--

CREATE TABLE IF NOT EXISTS `newModel_finds_botany_species` (
  `id` int(11) NOT NULL,
  `finds_id` int(11) NOT NULL,
  `dc_finds_botany_species_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_finds_lithics_cores`
--

CREATE TABLE IF NOT EXISTS `newModel_finds_lithics_cores` (
  `id` int(11) NOT NULL,
  `finds_id` int(11) NOT NULL,
  `dc_finds_lithics_core_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_finds_lithics_debitage`
--

CREATE TABLE IF NOT EXISTS `newModel_finds_lithics_debitage` (
  `id` int(11) NOT NULL,
  `finds_id` int(11) NOT NULL,
  `dc_finds_lithics_debitage_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_finds_lithics_modified_tools`
--

CREATE TABLE IF NOT EXISTS `newModel_finds_lithics_modified_tools` (
  `id` int(11) NOT NULL,
  `finds_id` int(11) NOT NULL,
  `dc_finds_lithics_modified_tools_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_finds_lithics_technology`
--

CREATE TABLE IF NOT EXISTS `newModel_finds_lithics_technology` (
  `id` int(11) NOT NULL,
  `finds_id` int(11) NOT NULL,
  `dc_finds_lithics_technology_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_finds_material`
--

CREATE TABLE IF NOT EXISTS `newModel_finds_material` (
  `id` int(11) NOT NULL,
  `finds_id` int(11) NOT NULL,
  `dc_finds_material_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_finds_pottery_decoration`
--

CREATE TABLE IF NOT EXISTS `newModel_finds_pottery_decoration` (
  `id` int(11) NOT NULL,
  `finds_id` int(11) NOT NULL,
  `dc_finds_pottery_decoration_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_finds_pottery_detail`
--

CREATE TABLE IF NOT EXISTS `newModel_finds_pottery_detail` (
  `id` int(11) NOT NULL,
  `finds_id` int(11) NOT NULL,
  `dc_finds_pottery_detail_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_finds_pottery_form`
--

CREATE TABLE IF NOT EXISTS `newModel_finds_pottery_form` (
  `id` int(11) NOT NULL,
  `finds_id` int(11) NOT NULL,
  `dc_finds_pottery_form_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_finds_reference`
--

CREATE TABLE IF NOT EXISTS `newModel_finds_reference` (
  `id` int(11) NOT NULL,
  `finds_id` int(11) NOT NULL,
  `reference_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_finds_small_finds_type`
--

CREATE TABLE IF NOT EXISTS `newModel_finds_small_finds_type` (
  `id` int(11) NOT NULL,
  `finds_id` int(11) NOT NULL,
  `dc_finds_small_finds_type_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_interpretation`
--

CREATE TABLE IF NOT EXISTS `newModel_interpretation` (
  `id` int(11) NOT NULL,
  `description` longtext,
  `comment` longtext
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_interpretation_area`
--

CREATE TABLE IF NOT EXISTS `newModel_interpretation_area` (
  `id` int(11) NOT NULL,
  `interpretation_id` int(11) NOT NULL,
  `area_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_interpretation_finds`
--

CREATE TABLE IF NOT EXISTS `newModel_interpretation_finds` (
  `id` int(11) NOT NULL,
  `interpretation_id` int(11) NOT NULL,
  `finds_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_interpretation_production_type`
--

CREATE TABLE IF NOT EXISTS `newModel_interpretation_production_type` (
  `id` int(11) NOT NULL,
  `interpretation_id` int(11) NOT NULL,
  `dc_interpretation_productiontype_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_interpretation_reference`
--

CREATE TABLE IF NOT EXISTS `newModel_interpretation_reference` (
  `id` int(11) NOT NULL,
  `interpretation_id` int(11) NOT NULL,
  `reference_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_interpretation_subsistence_type`
--

CREATE TABLE IF NOT EXISTS `newModel_interpretation_subsistence_type` (
  `id` int(11) NOT NULL,
  `interpretation_id` int(11) NOT NULL,
  `dc_interpretation_subsistencetype_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_period`
--

CREATE TABLE IF NOT EXISTS `newModel_period` (
  `id` int(11) NOT NULL,
  `comment` longtext,
  `system_id` int(11)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_period_dated_by`
--

CREATE TABLE IF NOT EXISTS `newModel_period_dated_by` (
  `id` int(11) NOT NULL,
  `period_id` int(11) NOT NULL,
  `dc_period_datedby_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_period_dating_method`
--

CREATE TABLE IF NOT EXISTS `newModel_period_dating_method` (
  `id` int(11) NOT NULL,
  `period_id` int(11) NOT NULL,
  `dc_period_datingmethod_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_period_reference`
--

CREATE TABLE IF NOT EXISTS `newModel_period_reference` (
  `id` int(11) NOT NULL,
  `period_id` int(11) NOT NULL,
  `reference_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_reference`
--

CREATE TABLE IF NOT EXISTS `newModel_reference` (
  `id` int(11) NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `creator` varchar(100) DEFAULT NULL,
  `creation_time` int(11) DEFAULT NULL,
  `url` varchar(100) DEFAULT NULL,
  `reference_type_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_researchevent`
--

CREATE TABLE IF NOT EXISTS `newModel_researchevent` (
  `id` int(11) NOT NULL,
  `year_of_activity_start_year` int(11) DEFAULT NULL,
  `year_of_activity_end_year` int(11) DEFAULT NULL,
  `project_name` varchar(100) DEFAULT NULL,
  `project_id` varchar(100) DEFAULT NULL,
  `project_leader` varchar(100) DEFAULT NULL,
  `comment` longtext
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_researchevent_institution`
--

CREATE TABLE IF NOT EXISTS `newModel_researchevent_institution` (
  `id` int(11) NOT NULL,
  `researchevent_id` int(11) NOT NULL,
  `dc_researchevent_institution_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_researchevent_reference`
--

CREATE TABLE IF NOT EXISTS `newModel_researchevent_reference` (
  `id` int(11) NOT NULL,
  `researchevent_id` int(11) NOT NULL,
  `reference_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_researchevent_research_type`
--

CREATE TABLE IF NOT EXISTS `newModel_researchevent_research_type` (
  `id` int(11) NOT NULL,
  `researchevent_id` int(11) NOT NULL,
  `dc_researchevent_researchtype_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_researchevent_special_analysis`
--

CREATE TABLE IF NOT EXISTS `newModel_researchevent_special_analysis` (
  `id` int(11) NOT NULL,
  `researchevent_id` int(11) NOT NULL,
  `dc_researchevent_special_analysis_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_site`
--

CREATE TABLE IF NOT EXISTS `newModel_site` (
  `id` int(11) NOT NULL,
  `name` varchar(350) DEFAULT NULL,
  `alias_name` varchar(350) DEFAULT NULL,
  `alternative_name` varchar(350) DEFAULT NULL,
  `description` longtext,
  `topography` varchar(400) DEFAULT NULL,
  `gps_data_n` varchar(50) DEFAULT NULL,
  `gps_data_e` varchar(50) DEFAULT NULL,
  `gps_data_z` varchar(50) DEFAULT NULL,
  `coordinate_source` varchar(100) DEFAULT NULL,
  `number_of_activity_periods` varchar(100) DEFAULT NULL,
  `geographical_coordinate_reference_system_id` int(11) DEFAULT NULL,
  `province_id` int(11) DEFAULT NULL,
  `comment` longtext
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `newModel_site_reference_site`
--

CREATE TABLE IF NOT EXISTS `newModel_site_reference_site` (
  `id` int(11) NOT NULL,
  `site_id` int(11) NOT NULL,
  `reference_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `newModel_area`
--
ALTER TABLE `newModel_area`
  ADD PRIMARY KEY (`id`),
  ADD KEY `newModel_area_2401735c` (`area_type_id`),
  ADD KEY `newModel_area_05b9be38` (`cave_rockshelters_evidence_of_graves_human_remains_id`),
  ADD KEY `newModel_area_b4cdce93` (`cave_rockshelters_type_id`),
  ADD KEY `newModel_area_9365d6e7` (`site_id`);

--
-- Indexes for table `newModel_area_cave_rockshelters_evidence_of_occupation`
--
ALTER TABLE `newModel_area_cave_rockshelters_evidence_of_occupation`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `area_id` (`area_id`,`dc_area_evidenceofoccupation_id`),
  ADD KEY `D7be113089d97762aa629115ec407782` (`dc_area_evidenceofoccupation_id`);

--
-- Indexes for table `newModel_area_cemetery_or_graves_mortuary_features`
--
ALTER TABLE `newModel_area_cemetery_or_graves_mortuary_features`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `area_id` (`area_id`,`dc_area_mortuaryfeatures_id`),
  ADD KEY `D9ad7dc0b589334b98db3366cbbaaf8b` (`dc_area_mortuaryfeatures_id`);

--
-- Indexes for table `newModel_area_cemetery_or_graves_topography`
--
ALTER TABLE `newModel_area_cemetery_or_graves_topography`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `area_id` (`area_id`,`dc_area_topography_id`),
  ADD KEY `dc_area_topography_id_2513089_fk_newModel_dc_area_topography_id` (`dc_area_topography_id`);

--
-- Indexes for table `newModel_area_grave_age_groups`
--
ALTER TABLE `newModel_area_grave_age_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `area_id` (`area_id`,`dc_area_agegroups_id`),
  ADD KEY `n_dc_area_agegroups_id_2ab0a984_fk_newModel_dc_area_agegroups_id` (`dc_area_agegroups_id`);

--
-- Indexes for table `newModel_area_grave_manipulations_of_graves`
--
ALTER TABLE `newModel_area_grave_manipulations_of_graves`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `area_id` (`area_id`,`dc_area_manipulationofgraves_id`),
  ADD KEY `D5885d00e74dbc49099888cae55d6e4d` (`dc_area_manipulationofgraves_id`);

--
-- Indexes for table `newModel_area_grave_sexes`
--
ALTER TABLE `newModel_area_grave_sexes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `area_id` (`area_id`,`dc_area_sexes_id`),
  ADD KEY `newModel__dc_area_sexes_id_6bf0733a_fk_newModel_dc_area_sexes_id` (`dc_area_sexes_id`);

--
-- Indexes for table `newModel_area_grave_type`
--
ALTER TABLE `newModel_area_grave_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `area_id` (`area_id`,`dc_area_gravetype_id`),
  ADD KEY `n_dc_area_gravetype_id_395f3214_fk_newModel_dc_area_gravetype_id` (`dc_area_gravetype_id`);

--
-- Indexes for table `newModel_area_grave_type_of_human_remains`
--
ALTER TABLE `newModel_area_grave_type_of_human_remains`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `area_id` (`area_id`,`dc_area_typeofhumanremains_id`),
  ADD KEY `a83eb68cb062b6e64fd448c89145d278` (`dc_area_typeofhumanremains_id`);

--
-- Indexes for table `newModel_area_period`
--
ALTER TABLE `newModel_area_period`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `area_id` (`area_id`,`period_id`),
  ADD KEY `newModel_area_period_period_id_35681d9e_fk_newModel_period_id` (`period_id`);

--
-- Indexes for table `newModel_area_quarry_exploitation_type`
--
ALTER TABLE `newModel_area_quarry_exploitation_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `area_id` (`area_id`,`dc_area_exploitationtype_id`),
  ADD KEY `e5642b71bcb30d8dcd1035d0cfb428bb` (`dc_area_exploitationtype_id`);

--
-- Indexes for table `newModel_area_quarry_raw_material`
--
ALTER TABLE `newModel_area_quarry_raw_material`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `area_id` (`area_id`,`dc_area_rawmaterial_id`),
  ADD KEY `b1bb125475f238b1b8b5bb304fa0cc35` (`dc_area_rawmaterial_id`);

--
-- Indexes for table `newModel_area_reference`
--
ALTER TABLE `newModel_area_reference`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `area_id` (`area_id`,`reference_id`),
  ADD KEY `newModel_area_ref_reference_id_195096de_fk_newModel_reference_id` (`reference_id`);

--
-- Indexes for table `newModel_area_settlement_building_technique`
--
ALTER TABLE `newModel_area_settlement_building_technique`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `area_id` (`area_id`,`dc_area_buildingtechnique_id`),
  ADD KEY `D199a60093250b03a31bdb5ec0f40ec7` (`dc_area_buildingtechnique_id`);

--
-- Indexes for table `newModel_area_settlement_construction_type`
--
ALTER TABLE `newModel_area_settlement_construction_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `area_id` (`area_id`,`dc_area_constructiontype_id`),
  ADD KEY `D63bbdd924c6dcf4e9bd1c908ebf017b` (`dc_area_constructiontype_id`);

--
-- Indexes for table `newModel_area_settlement_special_features`
--
ALTER TABLE `newModel_area_settlement_special_features`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `area_id` (`area_id`,`dc_area_specialfeatures_id`),
  ADD KEY `D33c58d5c75f198cea8e9f1599bd0471` (`dc_area_specialfeatures_id`);

--
-- Indexes for table `newModel_area_settlement_structure`
--
ALTER TABLE `newModel_area_settlement_structure`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `area_id` (`area_id`,`dc_area_settlementstructure_id`),
  ADD KEY `b1258f0d5c612f554963764681887975` (`dc_area_settlementstructure_id`);

--
-- Indexes for table `newModel_area_settlement_type`
--
ALTER TABLE `newModel_area_settlement_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `area_id` (`area_id`,`dc_area_settlementtype_id`),
  ADD KEY `b0d42efb2f6cc90883584e2bfb4ea642` (`dc_area_settlementtype_id`);

--
-- Indexes for table `newModel_dc_area_agegroups`
--
ALTER TABLE `newModel_dc_area_agegroups`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_area_areatype`
--
ALTER TABLE `newModel_dc_area_areatype`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_area_buildingtechnique`
--
ALTER TABLE `newModel_dc_area_buildingtechnique`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_area_caverockshelterstype`
--
ALTER TABLE `newModel_dc_area_caverockshelterstype`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_area_constructiontype`
--
ALTER TABLE `newModel_dc_area_constructiontype`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_area_evidenceofgraveshumanremains`
--
ALTER TABLE `newModel_dc_area_evidenceofgraveshumanremains`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_area_evidenceofoccupation`
--
ALTER TABLE `newModel_dc_area_evidenceofoccupation`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_area_exploitationtype`
--
ALTER TABLE `newModel_dc_area_exploitationtype`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_area_gravetype`
--
ALTER TABLE `newModel_dc_area_gravetype`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_area_manipulationofgraves`
--
ALTER TABLE `newModel_dc_area_manipulationofgraves`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_area_mortuaryfeatures`
--
ALTER TABLE `newModel_dc_area_mortuaryfeatures`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_area_rawmaterial`
--
ALTER TABLE `newModel_dc_area_rawmaterial`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_area_settlementstructure`
--
ALTER TABLE `newModel_dc_area_settlementstructure`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_area_settlementtype`
--
ALTER TABLE `newModel_dc_area_settlementtype`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_area_sexes`
--
ALTER TABLE `newModel_dc_area_sexes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_area_specialfeatures`
--
ALTER TABLE `newModel_dc_area_specialfeatures`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_area_topography`
--
ALTER TABLE `newModel_dc_area_topography`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_area_typeofhumanremains`
--
ALTER TABLE `newModel_dc_area_typeofhumanremains`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_chronological_system`
--
ALTER TABLE `newModel_dc_chronological_system`
  ADD PRIMARY KEY (`id`),
  ADD KEY `newModel_dc_chronological_system_0f442f96` (`region_id`);

--
-- Indexes for table `newModel_dc_country`
--
ALTER TABLE `newModel_dc_country`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_finds_amount`
--
ALTER TABLE `newModel_dc_finds_amount`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_finds_animal_remains_completeness`
--
ALTER TABLE `newModel_dc_finds_animal_remains_completeness`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_finds_animal_remains_part`
--
ALTER TABLE `newModel_dc_finds_animal_remains_part`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_finds_animal_remains_species`
--
ALTER TABLE `newModel_dc_finds_animal_remains_species`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_finds_botany_species`
--
ALTER TABLE `newModel_dc_finds_botany_species`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_finds_lithics_core`
--
ALTER TABLE `newModel_dc_finds_lithics_core`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_finds_lithics_debitage`
--
ALTER TABLE `newModel_dc_finds_lithics_debitage`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_finds_lithics_modified_tools`
--
ALTER TABLE `newModel_dc_finds_lithics_modified_tools`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_finds_lithics_technology`
--
ALTER TABLE `newModel_dc_finds_lithics_technology`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_finds_material`
--
ALTER TABLE `newModel_dc_finds_material`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_finds_pottery_decoration`
--
ALTER TABLE `newModel_dc_finds_pottery_decoration`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_finds_pottery_detail`
--
ALTER TABLE `newModel_dc_finds_pottery_detail`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_finds_pottery_form`
--
ALTER TABLE `newModel_dc_finds_pottery_form`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_finds_small_finds_category`
--
ALTER TABLE `newModel_dc_finds_small_finds_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_finds_small_finds_type`
--
ALTER TABLE `newModel_dc_finds_small_finds_type`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_finds_type`
--
ALTER TABLE `newModel_dc_finds_type`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_interpretation_productiontype`
--
ALTER TABLE `newModel_dc_interpretation_productiontype`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_interpretation_subsistencetype`
--
ALTER TABLE `newModel_dc_interpretation_subsistencetype`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_period_datedby`
--
ALTER TABLE `newModel_dc_period_datedby`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_period_datingmethod`
--
ALTER TABLE `newModel_dc_period_datingmethod`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_province`
--
ALTER TABLE `newModel_dc_province`
  ADD PRIMARY KEY (`id`),
  ADD KEY `newModel_dc_province_0f442f96` (`region_id`);

--
-- Indexes for table `newModel_dc_reference_type`
--
ALTER TABLE `newModel_dc_reference_type`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_region`
--
ALTER TABLE `newModel_dc_region`
  ADD PRIMARY KEY (`id`),
  ADD KEY `newModel_dc_region_country_id_5c0a7dbf_fk_newModel_dc_country_id` (`country_id`);

--
-- Indexes for table `newModel_dc_researchevent_institution`
--
ALTER TABLE `newModel_dc_researchevent_institution`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_researchevent_researchtype`
--
ALTER TABLE `newModel_dc_researchevent_researchtype`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_researchevent_special_analysis`
--
ALTER TABLE `newModel_dc_researchevent_special_analysis`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_dc_site_geographicalreferencesystem`
--
ALTER TABLE `newModel_dc_site_geographicalreferencesystem`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_finds`
--
ALTER TABLE `newModel_finds`
  ADD PRIMARY KEY (`id`),
  ADD KEY `newModel_finds_area_id_622097c9_fk_newModel_area_id` (`area_id`),
  ADD KEY `newModel_finds_d479fd74` (`research_event_id`),
  ADD KEY `newModel_finds_8b00793d` (`small_finds_category_id`),
  ADD KEY `newModel_finds_amount_id_6c5d63b2_fk_newModel_dc_finds_amount_id` (`amount_id`),
  ADD KEY `D67a90a0073b70aed6c4fc583251e27e` (`animal_remains_completeness_id`),
  ADD KEY `newModel_fin_finds_type_id_674826ad_fk_newModel_dc_finds_type_id` (`finds_type_id`);

--
-- Indexes for table `newModel_finds_animal_remains_part`
--
ALTER TABLE `newModel_finds_animal_remains_part`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `finds_id` (`finds_id`,`dc_finds_animal_remains_part_id`),
  ADD KEY `D4616511b466a7e00a3590b668f5f08a` (`dc_finds_animal_remains_part_id`);

--
-- Indexes for table `newModel_finds_animal_remains_species`
--
ALTER TABLE `newModel_finds_animal_remains_species`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `finds_id` (`finds_id`,`dc_finds_animal_remains_species_id`),
  ADD KEY `b9fea0fcadc0206d8f9e805d2d4efa82` (`dc_finds_animal_remains_species_id`);

--
-- Indexes for table `newModel_finds_botany_species`
--
ALTER TABLE `newModel_finds_botany_species`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `finds_id` (`finds_id`,`dc_finds_botany_species_id`),
  ADD KEY `D50e57b9c5d5d5d3091611dbe3b22760` (`dc_finds_botany_species_id`);

--
-- Indexes for table `newModel_finds_lithics_cores`
--
ALTER TABLE `newModel_finds_lithics_cores`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `finds_id` (`finds_id`,`dc_finds_lithics_core_id`),
  ADD KEY `D4379fc7c9ce0816705e2bf7814a33f1` (`dc_finds_lithics_core_id`);

--
-- Indexes for table `newModel_finds_lithics_debitage`
--
ALTER TABLE `newModel_finds_lithics_debitage`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `finds_id` (`finds_id`,`dc_finds_lithics_debitage_id`),
  ADD KEY `D25e79bae57f7dc3ba7fd158068ef25c` (`dc_finds_lithics_debitage_id`);

--
-- Indexes for table `newModel_finds_lithics_modified_tools`
--
ALTER TABLE `newModel_finds_lithics_modified_tools`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `finds_id` (`finds_id`,`dc_finds_lithics_modified_tools_id`),
  ADD KEY `D2c6161ec57a04632a210ef88e8332d3` (`dc_finds_lithics_modified_tools_id`);

--
-- Indexes for table `newModel_finds_lithics_technology`
--
ALTER TABLE `newModel_finds_lithics_technology`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `finds_id` (`finds_id`,`dc_finds_lithics_technology_id`),
  ADD KEY `D0b25e199423fb666d41982ecf0d323e` (`dc_finds_lithics_technology_id`);

--
-- Indexes for table `newModel_finds_material`
--
ALTER TABLE `newModel_finds_material`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `finds_id` (`finds_id`,`dc_finds_material_id`),
  ADD KEY `n_dc_finds_material_id_7e4da936_fk_newModel_dc_finds_material_id` (`dc_finds_material_id`);

--
-- Indexes for table `newModel_finds_pottery_decoration`
--
ALTER TABLE `newModel_finds_pottery_decoration`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `finds_id` (`finds_id`,`dc_finds_pottery_decoration_id`),
  ADD KEY `D893ea096a0195b49d58c7849c5dc244` (`dc_finds_pottery_decoration_id`);

--
-- Indexes for table `newModel_finds_pottery_detail`
--
ALTER TABLE `newModel_finds_pottery_detail`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `finds_id` (`finds_id`,`dc_finds_pottery_detail_id`),
  ADD KEY `dcbf5be20477b0280832f0d22467411e` (`dc_finds_pottery_detail_id`);

--
-- Indexes for table `newModel_finds_pottery_form`
--
ALTER TABLE `newModel_finds_pottery_form`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `finds_id` (`finds_id`,`dc_finds_pottery_form_id`),
  ADD KEY `D37c6d88e3756151f6568e5eaa99289a` (`dc_finds_pottery_form_id`);

--
-- Indexes for table `newModel_finds_reference`
--
ALTER TABLE `newModel_finds_reference`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `finds_id` (`finds_id`,`reference_id`),
  ADD KEY `newModel_finds_re_reference_id_47f2ba56_fk_newModel_reference_id` (`reference_id`);

--
-- Indexes for table `newModel_finds_small_finds_type`
--
ALTER TABLE `newModel_finds_small_finds_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `finds_id` (`finds_id`,`dc_finds_small_finds_type_id`),
  ADD KEY `D454d16301b122e2828f370cb22575e0` (`dc_finds_small_finds_type_id`);

--
-- Indexes for table `newModel_interpretation`
--
ALTER TABLE `newModel_interpretation`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_interpretation_area`
--
ALTER TABLE `newModel_interpretation_area`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `interpretation_id` (`interpretation_id`,`area_id`),
  ADD KEY `newModel_interpretation_are_area_id_69b6b7d1_fk_newModel_area_id` (`area_id`);

--
-- Indexes for table `newModel_interpretation_finds`
--
ALTER TABLE `newModel_interpretation_finds`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `interpretation_id` (`interpretation_id`,`finds_id`),
  ADD KEY `newModel_interpretation_f_finds_id_58d3c71f_fk_newModel_finds_id` (`finds_id`);

--
-- Indexes for table `newModel_interpretation_production_type`
--
ALTER TABLE `newModel_interpretation_production_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `interpretation_id` (`interpretation_id`,`dc_interpretation_productiontype_id`),
  ADD KEY `D882d0d99db74141ea875872b5b5c222` (`dc_interpretation_productiontype_id`);

--
-- Indexes for table `newModel_interpretation_reference`
--
ALTER TABLE `newModel_interpretation_reference`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `interpretation_id` (`interpretation_id`,`reference_id`),
  ADD KEY `newModel_interpret_reference_id_3446b25_fk_newModel_reference_id` (`reference_id`);

--
-- Indexes for table `newModel_interpretation_subsistence_type`
--
ALTER TABLE `newModel_interpretation_subsistence_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `interpretation_id` (`interpretation_id`,`dc_interpretation_subsistencetype_id`),
  ADD KEY `a2694417ce02afe61e972bfc0784b646` (`dc_interpretation_subsistencetype_id`);

--
-- Indexes for table `newModel_period`
--
ALTER TABLE `newModel_period`
  ADD PRIMARY KEY (`id`),
  ADD KEY `newModel_period_c18a5443` (`system_id`);

--
-- Indexes for table `newModel_period_dated_by`
--
ALTER TABLE `newModel_period_dated_by`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `period_id` (`period_id`,`dc_period_datedby_id`),
  ADD KEY `n_dc_period_datedby_id_4c63992a_fk_newModel_dc_period_datedby_id` (`dc_period_datedby_id`);

--
-- Indexes for table `newModel_period_dating_method`
--
ALTER TABLE `newModel_period_dating_method`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `period_id` (`period_id`,`dc_period_datingmethod_id`),
  ADD KEY `cd390487ce41c46a7cc3aa5984bdb044` (`dc_period_datingmethod_id`);

--
-- Indexes for table `newModel_period_reference`
--
ALTER TABLE `newModel_period_reference`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `period_id` (`period_id`,`reference_id`),
  ADD KEY `newModel_period_ref_reference_id_59c954_fk_newModel_reference_id` (`reference_id`);

--
-- Indexes for table `newModel_reference`
--
ALTER TABLE `newModel_reference`
  ADD PRIMARY KEY (`id`),
  ADD KEY `newM_reference_type_id_53c24dd5_fk_newModel_dc_reference_type_id` (`reference_type_id`);

--
-- Indexes for table `newModel_researchevent`
--
ALTER TABLE `newModel_researchevent`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newModel_researchevent_institution`
--
ALTER TABLE `newModel_researchevent_institution`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `researchevent_id` (`researchevent_id`,`dc_researchevent_institution_id`),
  ADD KEY `c3ee549ad5d6ab575638cd546de0ba4c` (`dc_researchevent_institution_id`);

--
-- Indexes for table `newModel_researchevent_reference`
--
ALTER TABLE `newModel_researchevent_reference`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `researchevent_id` (`researchevent_id`,`reference_id`),
  ADD KEY `newModel_researche_reference_id_6de0707_fk_newModel_reference_id` (`reference_id`);

--
-- Indexes for table `newModel_researchevent_research_type`
--
ALTER TABLE `newModel_researchevent_research_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `researchevent_id` (`researchevent_id`,`dc_researchevent_researchtype_id`),
  ADD KEY `ccd1e7ac8d2ac2a1fddd85bd0e1fc35e` (`dc_researchevent_researchtype_id`);

--
-- Indexes for table `newModel_researchevent_special_analysis`
--
ALTER TABLE `newModel_researchevent_special_analysis`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `researchevent_id` (`researchevent_id`,`dc_researchevent_special_analysis_id`),
  ADD KEY `D9cc0e4eb8a424dfaf7aa79c19fc6a7a` (`dc_researchevent_special_analysis_id`);

--
-- Indexes for table `newModel_site`
--
ALTER TABLE `newModel_site`
  ADD PRIMARY KEY (`id`),
  ADD KEY `D185e0f3f8532029d9ed510bfb4f9645` (`geographical_coordinate_reference_system_id`),
  ADD KEY `newModel_site_province_id_63de6422_fk_newModel_dc_province_id` (`province_id`);

--
-- Indexes for table `newModel_site_reference_site`
--
ALTER TABLE `newModel_site_reference_site`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `site_id` (`site_id`,`reference_id`),
  ADD KEY `newModel_site_refe_reference_id_bdd10ef_fk_newModel_reference_id` (`reference_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `newModel_area`
--
ALTER TABLE `newModel_area`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_area_cave_rockshelters_evidence_of_occupation`
--
ALTER TABLE `newModel_area_cave_rockshelters_evidence_of_occupation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_area_cemetery_or_graves_mortuary_features`
--
ALTER TABLE `newModel_area_cemetery_or_graves_mortuary_features`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_area_cemetery_or_graves_topography`
--
ALTER TABLE `newModel_area_cemetery_or_graves_topography`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_area_grave_age_groups`
--
ALTER TABLE `newModel_area_grave_age_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_area_grave_manipulations_of_graves`
--
ALTER TABLE `newModel_area_grave_manipulations_of_graves`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_area_grave_sexes`
--
ALTER TABLE `newModel_area_grave_sexes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_area_grave_type`
--
ALTER TABLE `newModel_area_grave_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_area_grave_type_of_human_remains`
--
ALTER TABLE `newModel_area_grave_type_of_human_remains`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_area_period`
--
ALTER TABLE `newModel_area_period`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_area_quarry_exploitation_type`
--
ALTER TABLE `newModel_area_quarry_exploitation_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_area_quarry_raw_material`
--
ALTER TABLE `newModel_area_quarry_raw_material`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_area_reference`
--
ALTER TABLE `newModel_area_reference`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_area_settlement_building_technique`
--
ALTER TABLE `newModel_area_settlement_building_technique`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_area_settlement_construction_type`
--
ALTER TABLE `newModel_area_settlement_construction_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_area_settlement_special_features`
--
ALTER TABLE `newModel_area_settlement_special_features`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_area_settlement_structure`
--
ALTER TABLE `newModel_area_settlement_structure`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_area_settlement_type`
--
ALTER TABLE `newModel_area_settlement_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_area_agegroups`
--
ALTER TABLE `newModel_dc_area_agegroups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_area_areatype`
--
ALTER TABLE `newModel_dc_area_areatype`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_area_buildingtechnique`
--
ALTER TABLE `newModel_dc_area_buildingtechnique`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_area_caverockshelterstype`
--
ALTER TABLE `newModel_dc_area_caverockshelterstype`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_area_constructiontype`
--
ALTER TABLE `newModel_dc_area_constructiontype`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_area_evidenceofgraveshumanremains`
--
ALTER TABLE `newModel_dc_area_evidenceofgraveshumanremains`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_area_evidenceofoccupation`
--
ALTER TABLE `newModel_dc_area_evidenceofoccupation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_area_exploitationtype`
--
ALTER TABLE `newModel_dc_area_exploitationtype`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_area_gravetype`
--
ALTER TABLE `newModel_dc_area_gravetype`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_area_manipulationofgraves`
--
ALTER TABLE `newModel_dc_area_manipulationofgraves`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_area_mortuaryfeatures`
--
ALTER TABLE `newModel_dc_area_mortuaryfeatures`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_area_rawmaterial`
--
ALTER TABLE `newModel_dc_area_rawmaterial`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_area_settlementstructure`
--
ALTER TABLE `newModel_dc_area_settlementstructure`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_area_settlementtype`
--
ALTER TABLE `newModel_dc_area_settlementtype`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_area_sexes`
--
ALTER TABLE `newModel_dc_area_sexes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_area_specialfeatures`
--
ALTER TABLE `newModel_dc_area_specialfeatures`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_area_topography`
--
ALTER TABLE `newModel_dc_area_topography`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_area_typeofhumanremains`
--
ALTER TABLE `newModel_dc_area_typeofhumanremains`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_chronological_system`
--
ALTER TABLE `newModel_dc_chronological_system`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_country`
--
ALTER TABLE `newModel_dc_country`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_finds_amount`
--
ALTER TABLE `newModel_dc_finds_amount`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_finds_animal_remains_completeness`
--
ALTER TABLE `newModel_dc_finds_animal_remains_completeness`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_finds_animal_remains_part`
--
ALTER TABLE `newModel_dc_finds_animal_remains_part`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_finds_animal_remains_species`
--
ALTER TABLE `newModel_dc_finds_animal_remains_species`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_finds_botany_species`
--
ALTER TABLE `newModel_dc_finds_botany_species`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_finds_lithics_core`
--
ALTER TABLE `newModel_dc_finds_lithics_core`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_finds_lithics_debitage`
--
ALTER TABLE `newModel_dc_finds_lithics_debitage`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_finds_lithics_modified_tools`
--
ALTER TABLE `newModel_dc_finds_lithics_modified_tools`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_finds_lithics_technology`
--
ALTER TABLE `newModel_dc_finds_lithics_technology`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_finds_material`
--
ALTER TABLE `newModel_dc_finds_material`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_finds_pottery_decoration`
--
ALTER TABLE `newModel_dc_finds_pottery_decoration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_finds_pottery_detail`
--
ALTER TABLE `newModel_dc_finds_pottery_detail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_finds_pottery_form`
--
ALTER TABLE `newModel_dc_finds_pottery_form`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_finds_small_finds_category`
--
ALTER TABLE `newModel_dc_finds_small_finds_category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_finds_small_finds_type`
--
ALTER TABLE `newModel_dc_finds_small_finds_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_finds_type`
--
ALTER TABLE `newModel_dc_finds_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_interpretation_productiontype`
--
ALTER TABLE `newModel_dc_interpretation_productiontype`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_interpretation_subsistencetype`
--
ALTER TABLE `newModel_dc_interpretation_subsistencetype`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_period_datedby`
--
ALTER TABLE `newModel_dc_period_datedby`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_period_datingmethod`
--
ALTER TABLE `newModel_dc_period_datingmethod`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_province`
--
ALTER TABLE `newModel_dc_province`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_reference_type`
--
ALTER TABLE `newModel_dc_reference_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_region`
--
ALTER TABLE `newModel_dc_region`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_researchevent_institution`
--
ALTER TABLE `newModel_dc_researchevent_institution`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_researchevent_researchtype`
--
ALTER TABLE `newModel_dc_researchevent_researchtype`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_researchevent_special_analysis`
--
ALTER TABLE `newModel_dc_researchevent_special_analysis`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_dc_site_geographicalreferencesystem`
--
ALTER TABLE `newModel_dc_site_geographicalreferencesystem`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_finds`
--
ALTER TABLE `newModel_finds`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_finds_animal_remains_part`
--
ALTER TABLE `newModel_finds_animal_remains_part`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_finds_animal_remains_species`
--
ALTER TABLE `newModel_finds_animal_remains_species`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_finds_botany_species`
--
ALTER TABLE `newModel_finds_botany_species`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_finds_lithics_cores`
--
ALTER TABLE `newModel_finds_lithics_cores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_finds_lithics_debitage`
--
ALTER TABLE `newModel_finds_lithics_debitage`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_finds_lithics_modified_tools`
--
ALTER TABLE `newModel_finds_lithics_modified_tools`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_finds_lithics_technology`
--
ALTER TABLE `newModel_finds_lithics_technology`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_finds_material`
--
ALTER TABLE `newModel_finds_material`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_finds_pottery_decoration`
--
ALTER TABLE `newModel_finds_pottery_decoration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_finds_pottery_detail`
--
ALTER TABLE `newModel_finds_pottery_detail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_finds_pottery_form`
--
ALTER TABLE `newModel_finds_pottery_form`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_finds_reference`
--
ALTER TABLE `newModel_finds_reference`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_finds_small_finds_type`
--
ALTER TABLE `newModel_finds_small_finds_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_interpretation`
--
ALTER TABLE `newModel_interpretation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_interpretation_area`
--
ALTER TABLE `newModel_interpretation_area`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_interpretation_finds`
--
ALTER TABLE `newModel_interpretation_finds`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_interpretation_production_type`
--
ALTER TABLE `newModel_interpretation_production_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_interpretation_reference`
--
ALTER TABLE `newModel_interpretation_reference`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_interpretation_subsistence_type`
--
ALTER TABLE `newModel_interpretation_subsistence_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_period`
--
ALTER TABLE `newModel_period`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_period_dated_by`
--
ALTER TABLE `newModel_period_dated_by`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_period_dating_method`
--
ALTER TABLE `newModel_period_dating_method`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_period_reference`
--
ALTER TABLE `newModel_period_reference`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_reference`
--
ALTER TABLE `newModel_reference`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_researchevent`
--
ALTER TABLE `newModel_researchevent`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_researchevent_institution`
--
ALTER TABLE `newModel_researchevent_institution`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_researchevent_reference`
--
ALTER TABLE `newModel_researchevent_reference`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_researchevent_research_type`
--
ALTER TABLE `newModel_researchevent_research_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_researchevent_special_analysis`
--
ALTER TABLE `newModel_researchevent_special_analysis`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_site`
--
ALTER TABLE `newModel_site`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `newModel_site_reference_site`
--
ALTER TABLE `newModel_site_reference_site`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `newModel_area`
--
ALTER TABLE `newModel_area`
  ADD CONSTRAINT `b545a9c82bf30739aab82a20de788cf2` FOREIGN KEY (`cave_rockshelters_type_id`) REFERENCES `newModel_dc_area_caverockshelterstype` (`id`),
  ADD CONSTRAINT `D2c47ca2818141646b0be7aa77101551` FOREIGN KEY (`cave_rockshelters_evidence_of_graves_human_remains_id`) REFERENCES `newModel_dc_area_evidenceofgraveshumanremains` (`id`),
  ADD CONSTRAINT `newModel_area_site_id_1a5faf65_fk_newModel_site_id` FOREIGN KEY (`site_id`) REFERENCES `newModel_site` (`id`),
  ADD CONSTRAINT `newModel_a_area_type_id_7def0727_fk_newModel_dc_area_areatype_id` FOREIGN KEY (`area_type_id`) REFERENCES `newModel_dc_area_areatype` (`id`);

--
-- Constraints for table `newModel_area_cave_rockshelters_evidence_of_occupation`
--
ALTER TABLE `newModel_area_cave_rockshelters_evidence_of_occupation`
  ADD CONSTRAINT `D7be113089d97762aa629115ec407782` FOREIGN KEY (`dc_area_evidenceofoccupation_id`) REFERENCES `newModel_dc_area_evidenceofoccupation` (`id`),
  ADD CONSTRAINT `newModel_area_cave_rockshel_area_id_111a7a26_fk_newModel_area_id` FOREIGN KEY (`area_id`) REFERENCES `newModel_area` (`id`);

--
-- Constraints for table `newModel_area_cemetery_or_graves_mortuary_features`
--
ALTER TABLE `newModel_area_cemetery_or_graves_mortuary_features`
  ADD CONSTRAINT `D9ad7dc0b589334b98db3366cbbaaf8b` FOREIGN KEY (`dc_area_mortuaryfeatures_id`) REFERENCES `newModel_dc_area_mortuaryfeatures` (`id`),
  ADD CONSTRAINT `newModel_area_cemetery_or_g_area_id_7bee311e_fk_newModel_area_id` FOREIGN KEY (`area_id`) REFERENCES `newModel_area` (`id`);

--
-- Constraints for table `newModel_area_cemetery_or_graves_topography`
--
ALTER TABLE `newModel_area_cemetery_or_graves_topography`
  ADD CONSTRAINT `dc_area_topography_id_2513089_fk_newModel_dc_area_topography_id` FOREIGN KEY (`dc_area_topography_id`) REFERENCES `newModel_dc_area_topography` (`id`),
  ADD CONSTRAINT `newModel_area_cemetery_or_g_area_id_26c37d2f_fk_newModel_area_id` FOREIGN KEY (`area_id`) REFERENCES `newModel_area` (`id`);

--
-- Constraints for table `newModel_area_grave_age_groups`
--
ALTER TABLE `newModel_area_grave_age_groups`
  ADD CONSTRAINT `newModel_area_grave_age_gro_area_id_13cd2c77_fk_newModel_area_id` FOREIGN KEY (`area_id`) REFERENCES `newModel_area` (`id`),
  ADD CONSTRAINT `n_dc_area_agegroups_id_2ab0a984_fk_newModel_dc_area_agegroups_id` FOREIGN KEY (`dc_area_agegroups_id`) REFERENCES `newModel_dc_area_agegroups` (`id`);

--
-- Constraints for table `newModel_area_grave_manipulations_of_graves`
--
ALTER TABLE `newModel_area_grave_manipulations_of_graves`
  ADD CONSTRAINT `D5885d00e74dbc49099888cae55d6e4d` FOREIGN KEY (`dc_area_manipulationofgraves_id`) REFERENCES `newModel_dc_area_manipulationofgraves` (`id`),
  ADD CONSTRAINT `newModel_area_grave_manipul_area_id_430624eb_fk_newModel_area_id` FOREIGN KEY (`area_id`) REFERENCES `newModel_area` (`id`);

--
-- Constraints for table `newModel_area_grave_sexes`
--
ALTER TABLE `newModel_area_grave_sexes`
  ADD CONSTRAINT `newModel_area_grave_sexes_area_id_40e53368_fk_newModel_area_id` FOREIGN KEY (`area_id`) REFERENCES `newModel_area` (`id`),
  ADD CONSTRAINT `newModel__dc_area_sexes_id_6bf0733a_fk_newModel_dc_area_sexes_id` FOREIGN KEY (`dc_area_sexes_id`) REFERENCES `newModel_dc_area_sexes` (`id`);

--
-- Constraints for table `newModel_area_grave_type`
--
ALTER TABLE `newModel_area_grave_type`
  ADD CONSTRAINT `newModel_area_grave_type_area_id_3bcec80d_fk_newModel_area_id` FOREIGN KEY (`area_id`) REFERENCES `newModel_area` (`id`),
  ADD CONSTRAINT `n_dc_area_gravetype_id_395f3214_fk_newModel_dc_area_gravetype_id` FOREIGN KEY (`dc_area_gravetype_id`) REFERENCES `newModel_dc_area_gravetype` (`id`);

--
-- Constraints for table `newModel_area_grave_type_of_human_remains`
--
ALTER TABLE `newModel_area_grave_type_of_human_remains`
  ADD CONSTRAINT `a83eb68cb062b6e64fd448c89145d278` FOREIGN KEY (`dc_area_typeofhumanremains_id`) REFERENCES `newModel_dc_area_typeofhumanremains` (`id`),
  ADD CONSTRAINT `newModel_area_grave_type_of_area_id_1bbd075c_fk_newModel_area_id` FOREIGN KEY (`area_id`) REFERENCES `newModel_area` (`id`);

--
-- Constraints for table `newModel_area_period`
--
ALTER TABLE `newModel_area_period`
  ADD CONSTRAINT `newModel_area_period_area_id_29fe9a0_fk_newModel_area_id` FOREIGN KEY (`area_id`) REFERENCES `newModel_area` (`id`),
  ADD CONSTRAINT `newModel_area_period_period_id_35681d9e_fk_newModel_period_id` FOREIGN KEY (`period_id`) REFERENCES `newModel_period` (`id`);

--
-- Constraints for table `newModel_area_quarry_exploitation_type`
--
ALTER TABLE `newModel_area_quarry_exploitation_type`
  ADD CONSTRAINT `e5642b71bcb30d8dcd1035d0cfb428bb` FOREIGN KEY (`dc_area_exploitationtype_id`) REFERENCES `newModel_dc_area_exploitationtype` (`id`),
  ADD CONSTRAINT `newModel_area_quarry_exploi_area_id_21955a01_fk_newModel_area_id` FOREIGN KEY (`area_id`) REFERENCES `newModel_area` (`id`);

--
-- Constraints for table `newModel_area_quarry_raw_material`
--
ALTER TABLE `newModel_area_quarry_raw_material`
  ADD CONSTRAINT `b1bb125475f238b1b8b5bb304fa0cc35` FOREIGN KEY (`dc_area_rawmaterial_id`) REFERENCES `newModel_dc_area_rawmaterial` (`id`),
  ADD CONSTRAINT `newModel_area_quarry_raw_ma_area_id_6409033b_fk_newModel_area_id` FOREIGN KEY (`area_id`) REFERENCES `newModel_area` (`id`);

--
-- Constraints for table `newModel_area_reference`
--
ALTER TABLE `newModel_area_reference`
  ADD CONSTRAINT `newModel_area_reference_area_id_3c1ede83_fk_newModel_area_id` FOREIGN KEY (`area_id`) REFERENCES `newModel_area` (`id`),
  ADD CONSTRAINT `newModel_area_ref_reference_id_195096de_fk_newModel_reference_id` FOREIGN KEY (`reference_id`) REFERENCES `newModel_reference` (`id`);

--
-- Constraints for table `newModel_area_settlement_building_technique`
--
ALTER TABLE `newModel_area_settlement_building_technique`
  ADD CONSTRAINT `D199a60093250b03a31bdb5ec0f40ec7` FOREIGN KEY (`dc_area_buildingtechnique_id`) REFERENCES `newModel_dc_area_buildingtechnique` (`id`),
  ADD CONSTRAINT `newModel_area_settlement_bu_area_id_58369427_fk_newModel_area_id` FOREIGN KEY (`area_id`) REFERENCES `newModel_area` (`id`);

--
-- Constraints for table `newModel_area_settlement_construction_type`
--
ALTER TABLE `newModel_area_settlement_construction_type`
  ADD CONSTRAINT `D63bbdd924c6dcf4e9bd1c908ebf017b` FOREIGN KEY (`dc_area_constructiontype_id`) REFERENCES `newModel_dc_area_constructiontype` (`id`),
  ADD CONSTRAINT `newModel_area_settlement_co_area_id_7782a7cf_fk_newModel_area_id` FOREIGN KEY (`area_id`) REFERENCES `newModel_area` (`id`);

--
-- Constraints for table `newModel_area_settlement_special_features`
--
ALTER TABLE `newModel_area_settlement_special_features`
  ADD CONSTRAINT `D33c58d5c75f198cea8e9f1599bd0471` FOREIGN KEY (`dc_area_specialfeatures_id`) REFERENCES `newModel_dc_area_specialfeatures` (`id`),
  ADD CONSTRAINT `newModel_area_settlement_sp_area_id_1b70393d_fk_newModel_area_id` FOREIGN KEY (`area_id`) REFERENCES `newModel_area` (`id`);

--
-- Constraints for table `newModel_area_settlement_structure`
--
ALTER TABLE `newModel_area_settlement_structure`
  ADD CONSTRAINT `b1258f0d5c612f554963764681887975` FOREIGN KEY (`dc_area_settlementstructure_id`) REFERENCES `newModel_dc_area_settlementstructure` (`id`),
  ADD CONSTRAINT `newModel_area_settlement_st_area_id_52e25fae_fk_newModel_area_id` FOREIGN KEY (`area_id`) REFERENCES `newModel_area` (`id`);

--
-- Constraints for table `newModel_area_settlement_type`
--
ALTER TABLE `newModel_area_settlement_type`
  ADD CONSTRAINT `b0d42efb2f6cc90883584e2bfb4ea642` FOREIGN KEY (`dc_area_settlementtype_id`) REFERENCES `newModel_dc_area_settlementtype` (`id`),
  ADD CONSTRAINT `newModel_area_settlement_ty_area_id_13f04e5e_fk_newModel_area_id` FOREIGN KEY (`area_id`) REFERENCES `newModel_area` (`id`);

--
-- Constraints for table `newModel_dc_chronological_system`
--
ALTER TABLE `newModel_dc_chronological_system`
  ADD CONSTRAINT `newModel_dc_chronolo_region_id_401f4410_fk_newModel_dc_region_id` FOREIGN KEY (`region_id`) REFERENCES `newModel_dc_region` (`id`);

--
-- Constraints for table `newModel_dc_province`
--
ALTER TABLE `newModel_dc_province`
  ADD CONSTRAINT `newModel_dc_province_region_id_332d10e2_fk_newModel_dc_region_id` FOREIGN KEY (`region_id`) REFERENCES `newModel_dc_region` (`id`);

--
-- Constraints for table `newModel_dc_region`
--
ALTER TABLE `newModel_dc_region`
  ADD CONSTRAINT `newModel_dc_region_country_id_5c0a7dbf_fk_newModel_dc_country_id` FOREIGN KEY (`country_id`) REFERENCES `newModel_dc_country` (`id`);

--
-- Constraints for table `newModel_finds`
--
ALTER TABLE `newModel_finds`
  ADD CONSTRAINT `D67a90a0073b70aed6c4fc583251e27e` FOREIGN KEY (`animal_remains_completeness_id`) REFERENCES `newModel_dc_finds_animal_remains_completeness` (`id`),
  ADD CONSTRAINT `fe56767e7464cbad0f3cd6b9d6c8e1c3` FOREIGN KEY (`small_finds_category_id`) REFERENCES `newModel_dc_finds_small_finds_category` (`id`),
  ADD CONSTRAINT `newModel_finds_amount_id_6c5d63b2_fk_newModel_dc_finds_amount_id` FOREIGN KEY (`amount_id`) REFERENCES `newModel_dc_finds_amount` (`id`),
  ADD CONSTRAINT `newModel_finds_area_id_622097c9_fk_newModel_area_id` FOREIGN KEY (`area_id`) REFERENCES `newModel_area` (`id`),
  ADD CONSTRAINT `newModel_fin_finds_type_id_674826ad_fk_newModel_dc_finds_type_id` FOREIGN KEY (`finds_type_id`) REFERENCES `newModel_dc_finds_type` (`id`),
  ADD CONSTRAINT `newModel_research_event_id_6f838050_fk_newModel_researchevent_id` FOREIGN KEY (`research_event_id`) REFERENCES `newModel_researchevent` (`id`);

--
-- Constraints for table `newModel_finds_animal_remains_part`
--
ALTER TABLE `newModel_finds_animal_remains_part`
  ADD CONSTRAINT `D4616511b466a7e00a3590b668f5f08a` FOREIGN KEY (`dc_finds_animal_remains_part_id`) REFERENCES `newModel_dc_finds_animal_remains_part` (`id`),
  ADD CONSTRAINT `newModel_finds_animal_rem_finds_id_6304a4de_fk_newModel_finds_id` FOREIGN KEY (`finds_id`) REFERENCES `newModel_finds` (`id`);

--
-- Constraints for table `newModel_finds_animal_remains_species`
--
ALTER TABLE `newModel_finds_animal_remains_species`
  ADD CONSTRAINT `b9fea0fcadc0206d8f9e805d2d4efa82` FOREIGN KEY (`dc_finds_animal_remains_species_id`) REFERENCES `newModel_dc_finds_animal_remains_species` (`id`),
  ADD CONSTRAINT `newModel_finds_animal_rema_finds_id_370cb34_fk_newModel_finds_id` FOREIGN KEY (`finds_id`) REFERENCES `newModel_finds` (`id`);

--
-- Constraints for table `newModel_finds_botany_species`
--
ALTER TABLE `newModel_finds_botany_species`
  ADD CONSTRAINT `D50e57b9c5d5d5d3091611dbe3b22760` FOREIGN KEY (`dc_finds_botany_species_id`) REFERENCES `newModel_dc_finds_botany_species` (`id`),
  ADD CONSTRAINT `newModel_finds_botany_spe_finds_id_56761969_fk_newModel_finds_id` FOREIGN KEY (`finds_id`) REFERENCES `newModel_finds` (`id`);

--
-- Constraints for table `newModel_finds_lithics_cores`
--
ALTER TABLE `newModel_finds_lithics_cores`
  ADD CONSTRAINT `D4379fc7c9ce0816705e2bf7814a33f1` FOREIGN KEY (`dc_finds_lithics_core_id`) REFERENCES `newModel_dc_finds_lithics_core` (`id`),
  ADD CONSTRAINT `newModel_finds_lithics_co_finds_id_2116a9a9_fk_newModel_finds_id` FOREIGN KEY (`finds_id`) REFERENCES `newModel_finds` (`id`);

--
-- Constraints for table `newModel_finds_lithics_debitage`
--
ALTER TABLE `newModel_finds_lithics_debitage`
  ADD CONSTRAINT `D25e79bae57f7dc3ba7fd158068ef25c` FOREIGN KEY (`dc_finds_lithics_debitage_id`) REFERENCES `newModel_dc_finds_lithics_debitage` (`id`),
  ADD CONSTRAINT `newModel_finds_lithics_de_finds_id_7c9b05e5_fk_newModel_finds_id` FOREIGN KEY (`finds_id`) REFERENCES `newModel_finds` (`id`);

--
-- Constraints for table `newModel_finds_lithics_modified_tools`
--
ALTER TABLE `newModel_finds_lithics_modified_tools`
  ADD CONSTRAINT `D2c6161ec57a04632a210ef88e8332d3` FOREIGN KEY (`dc_finds_lithics_modified_tools_id`) REFERENCES `newModel_dc_finds_lithics_modified_tools` (`id`),
  ADD CONSTRAINT `newModel_finds_lithics_mo_finds_id_1ea0e60b_fk_newModel_finds_id` FOREIGN KEY (`finds_id`) REFERENCES `newModel_finds` (`id`);

--
-- Constraints for table `newModel_finds_lithics_technology`
--
ALTER TABLE `newModel_finds_lithics_technology`
  ADD CONSTRAINT `D0b25e199423fb666d41982ecf0d323e` FOREIGN KEY (`dc_finds_lithics_technology_id`) REFERENCES `newModel_dc_finds_lithics_technology` (`id`),
  ADD CONSTRAINT `newModel_finds_lithics_tec_finds_id_82e5f30_fk_newModel_finds_id` FOREIGN KEY (`finds_id`) REFERENCES `newModel_finds` (`id`);

--
-- Constraints for table `newModel_finds_material`
--
ALTER TABLE `newModel_finds_material`
  ADD CONSTRAINT `newModel_finds_material_finds_id_19703f40_fk_newModel_finds_id` FOREIGN KEY (`finds_id`) REFERENCES `newModel_finds` (`id`),
  ADD CONSTRAINT `n_dc_finds_material_id_7e4da936_fk_newModel_dc_finds_material_id` FOREIGN KEY (`dc_finds_material_id`) REFERENCES `newModel_dc_finds_material` (`id`);

--
-- Constraints for table `newModel_finds_pottery_decoration`
--
ALTER TABLE `newModel_finds_pottery_decoration`
  ADD CONSTRAINT `D893ea096a0195b49d58c7849c5dc244` FOREIGN KEY (`dc_finds_pottery_decoration_id`) REFERENCES `newModel_dc_finds_pottery_decoration` (`id`),
  ADD CONSTRAINT `newModel_finds_pottery_de_finds_id_2e8fa275_fk_newModel_finds_id` FOREIGN KEY (`finds_id`) REFERENCES `newModel_finds` (`id`);

--
-- Constraints for table `newModel_finds_pottery_detail`
--
ALTER TABLE `newModel_finds_pottery_detail`
  ADD CONSTRAINT `dcbf5be20477b0280832f0d22467411e` FOREIGN KEY (`dc_finds_pottery_detail_id`) REFERENCES `newModel_dc_finds_pottery_detail` (`id`),
  ADD CONSTRAINT `newModel_finds_pottery_de_finds_id_20ea0170_fk_newModel_finds_id` FOREIGN KEY (`finds_id`) REFERENCES `newModel_finds` (`id`);

--
-- Constraints for table `newModel_finds_pottery_form`
--
ALTER TABLE `newModel_finds_pottery_form`
  ADD CONSTRAINT `D37c6d88e3756151f6568e5eaa99289a` FOREIGN KEY (`dc_finds_pottery_form_id`) REFERENCES `newModel_dc_finds_pottery_form` (`id`),
  ADD CONSTRAINT `newModel_finds_pottery_fo_finds_id_12bdbe6d_fk_newModel_finds_id` FOREIGN KEY (`finds_id`) REFERENCES `newModel_finds` (`id`);

--
-- Constraints for table `newModel_finds_reference`
--
ALTER TABLE `newModel_finds_reference`
  ADD CONSTRAINT `newModel_finds_reference_finds_id_68b96fb7_fk_newModel_finds_id` FOREIGN KEY (`finds_id`) REFERENCES `newModel_finds` (`id`),
  ADD CONSTRAINT `newModel_finds_re_reference_id_47f2ba56_fk_newModel_reference_id` FOREIGN KEY (`reference_id`) REFERENCES `newModel_reference` (`id`);

--
-- Constraints for table `newModel_finds_small_finds_type`
--
ALTER TABLE `newModel_finds_small_finds_type`
  ADD CONSTRAINT `D454d16301b122e2828f370cb22575e0` FOREIGN KEY (`dc_finds_small_finds_type_id`) REFERENCES `newModel_dc_finds_small_finds_type` (`id`),
  ADD CONSTRAINT `newModel_finds_small_finds_finds_id_5f2b740_fk_newModel_finds_id` FOREIGN KEY (`finds_id`) REFERENCES `newModel_finds` (`id`);

--
-- Constraints for table `newModel_interpretation_area`
--
ALTER TABLE `newModel_interpretation_area`
  ADD CONSTRAINT `newModel_interpretation_are_area_id_69b6b7d1_fk_newModel_area_id` FOREIGN KEY (`area_id`) REFERENCES `newModel_area` (`id`),
  ADD CONSTRAINT `newMode_interpretation_id_193abe8c_fk_newModel_interpretation_id` FOREIGN KEY (`interpretation_id`) REFERENCES `newModel_interpretation` (`id`);

--
-- Constraints for table `newModel_interpretation_finds`
--
ALTER TABLE `newModel_interpretation_finds`
  ADD CONSTRAINT `newModel_interpretation_f_finds_id_58d3c71f_fk_newModel_finds_id` FOREIGN KEY (`finds_id`) REFERENCES `newModel_finds` (`id`),
  ADD CONSTRAINT `newModel_interpretation_id_1b387c4_fk_newModel_interpretation_id` FOREIGN KEY (`interpretation_id`) REFERENCES `newModel_interpretation` (`id`);

--
-- Constraints for table `newModel_interpretation_production_type`
--
ALTER TABLE `newModel_interpretation_production_type`
  ADD CONSTRAINT `D882d0d99db74141ea875872b5b5c222` FOREIGN KEY (`dc_interpretation_productiontype_id`) REFERENCES `newModel_dc_interpretation_productiontype` (`id`),
  ADD CONSTRAINT `newMode_interpretation_id_2dbf2e32_fk_newModel_interpretation_id` FOREIGN KEY (`interpretation_id`) REFERENCES `newModel_interpretation` (`id`);

--
-- Constraints for table `newModel_interpretation_reference`
--
ALTER TABLE `newModel_interpretation_reference`
  ADD CONSTRAINT `newModel_interpret_reference_id_3446b25_fk_newModel_reference_id` FOREIGN KEY (`reference_id`) REFERENCES `newModel_reference` (`id`),
  ADD CONSTRAINT `newMode_interpretation_id_5d574089_fk_newModel_interpretation_id` FOREIGN KEY (`interpretation_id`) REFERENCES `newModel_interpretation` (`id`);

--
-- Constraints for table `newModel_interpretation_subsistence_type`
--
ALTER TABLE `newModel_interpretation_subsistence_type`
  ADD CONSTRAINT `a2694417ce02afe61e972bfc0784b646` FOREIGN KEY (`dc_interpretation_subsistencetype_id`) REFERENCES `newModel_dc_interpretation_subsistencetype` (`id`),
  ADD CONSTRAINT `newMode_interpretation_id_3f5f8192_fk_newModel_interpretation_id` FOREIGN KEY (`interpretation_id`) REFERENCES `newModel_interpretation` (`id`);

--
-- Constraints for table `newModel_period`
--
ALTER TABLE `newModel_period`
  ADD CONSTRAINT `newMod_system_id_52987bb1_fk_newModel_dc_chronological_system_id` FOREIGN KEY (`system_id`) REFERENCES `newModel_dc_chronological_system` (`id`);

--
-- Constraints for table `newModel_period_dated_by`
--
ALTER TABLE `newModel_period_dated_by`
  ADD CONSTRAINT `newModel_period_dated_by_period_id_d36b97f_fk_newModel_period_id` FOREIGN KEY (`period_id`) REFERENCES `newModel_period` (`id`),
  ADD CONSTRAINT `n_dc_period_datedby_id_4c63992a_fk_newModel_dc_period_datedby_id` FOREIGN KEY (`dc_period_datedby_id`) REFERENCES `newModel_dc_period_datedby` (`id`);

--
-- Constraints for table `newModel_period_dating_method`
--
ALTER TABLE `newModel_period_dating_method`
  ADD CONSTRAINT `cd390487ce41c46a7cc3aa5984bdb044` FOREIGN KEY (`dc_period_datingmethod_id`) REFERENCES `newModel_dc_period_datingmethod` (`id`),
  ADD CONSTRAINT `newModel_period_dating__period_id_47df4bab_fk_newModel_period_id` FOREIGN KEY (`period_id`) REFERENCES `newModel_period` (`id`);

--
-- Constraints for table `newModel_period_reference`
--
ALTER TABLE `newModel_period_reference`
  ADD CONSTRAINT `newModel_period_referen_period_id_6fc4f549_fk_newModel_period_id` FOREIGN KEY (`period_id`) REFERENCES `newModel_period` (`id`),
  ADD CONSTRAINT `newModel_period_ref_reference_id_59c954_fk_newModel_reference_id` FOREIGN KEY (`reference_id`) REFERENCES `newModel_reference` (`id`);

--
-- Constraints for table `newModel_reference`
--
ALTER TABLE `newModel_reference`
  ADD CONSTRAINT `newM_reference_type_id_53c24dd5_fk_newModel_dc_reference_type_id` FOREIGN KEY (`reference_type_id`) REFERENCES `newModel_dc_reference_type` (`id`);

--
-- Constraints for table `newModel_researchevent_institution`
--
ALTER TABLE `newModel_researchevent_institution`
  ADD CONSTRAINT `c3ee549ad5d6ab575638cd546de0ba4c` FOREIGN KEY (`dc_researchevent_institution_id`) REFERENCES `newModel_dc_researchevent_institution` (`id`),
  ADD CONSTRAINT `newModel__researchevent_id_543df842_fk_newModel_researchevent_id` FOREIGN KEY (`researchevent_id`) REFERENCES `newModel_researchevent` (`id`);

--
-- Constraints for table `newModel_researchevent_reference`
--
ALTER TABLE `newModel_researchevent_reference`
  ADD CONSTRAINT `newModel_researche_reference_id_6de0707_fk_newModel_reference_id` FOREIGN KEY (`reference_id`) REFERENCES `newModel_reference` (`id`),
  ADD CONSTRAINT `newModel__researchevent_id_6028e217_fk_newModel_researchevent_id` FOREIGN KEY (`researchevent_id`) REFERENCES `newModel_researchevent` (`id`);

--
-- Constraints for table `newModel_researchevent_research_type`
--
ALTER TABLE `newModel_researchevent_research_type`
  ADD CONSTRAINT `ccd1e7ac8d2ac2a1fddd85bd0e1fc35e` FOREIGN KEY (`dc_researchevent_researchtype_id`) REFERENCES `newModel_dc_researchevent_researchtype` (`id`),
  ADD CONSTRAINT `newModel__researchevent_id_7cc75280_fk_newModel_researchevent_id` FOREIGN KEY (`researchevent_id`) REFERENCES `newModel_researchevent` (`id`);

--
-- Constraints for table `newModel_researchevent_special_analysis`
--
ALTER TABLE `newModel_researchevent_special_analysis`
  ADD CONSTRAINT `D9cc0e4eb8a424dfaf7aa79c19fc6a7a` FOREIGN KEY (`dc_researchevent_special_analysis_id`) REFERENCES `newModel_dc_researchevent_special_analysis` (`id`),
  ADD CONSTRAINT `newModel__researchevent_id_3a3f5dcf_fk_newModel_researchevent_id` FOREIGN KEY (`researchevent_id`) REFERENCES `newModel_researchevent` (`id`);

--
-- Constraints for table `newModel_site`
--
ALTER TABLE `newModel_site`
  ADD CONSTRAINT `D185e0f3f8532029d9ed510bfb4f9645` FOREIGN KEY (`geographical_coordinate_reference_system_id`) REFERENCES `newModel_dc_site_geographicalreferencesystem` (`id`),
  ADD CONSTRAINT `newModel_site_province_id_63de6422_fk_newModel_dc_province_id` FOREIGN KEY (`province_id`) REFERENCES `newModel_dc_province` (`id`);

--
-- Constraints for table `newModel_site_reference_site`
--
ALTER TABLE `newModel_site_reference_site`
  ADD CONSTRAINT `newModel_site_reference_sit_site_id_6f7180fc_fk_newModel_site_id` FOREIGN KEY (`site_id`) REFERENCES `newModel_site` (`id`),
  ADD CONSTRAINT `newModel_site_refe_reference_id_bdd10ef_fk_newModel_reference_id` FOREIGN KEY (`reference_id`) REFERENCES `newModel_reference` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
