/*-------------------------------------------------------
 CHAPITRE 5 : TRAVAIL PRATIQUE SUR LES BASES DE DONNEES
-------------------------------------------------------*/


DROP TABLE IF EXISTS coordonnees;
DROP TABLE IF EXISTS options;
DROP TABLE IF EXISTS seconde;
DROP TABLE IF EXISTS eleve;

CREATE TABLE eleve (
    num_eleve INT PRIMARY KEY,
    nom TEXT,
    prenom TEXT,
    datenaissance TEXT);

INSERT INTO eleve 
    (num_eleve,nom,prenom,datenaissance) 
VALUES 
    (133310,'ACHIR','Mussa','01/01/2005'),
    (156929,'ALTMEYER','Yohan','05/05/2005'),
	(500633,'BELEY','Thibaut','05/05/2005'),
	(911887,'BELEY','Marie','05/05/2005'),
	(906089,'BELEY','Manon','10/01/2005'),
	(488697,'CAILLE','Marie','30/03/2004'),
	(193514,'CHARPENTIER','Jules','26/12/2005'),
	(321188,'CLAUDEL','Benjamin','09/09/2005'),
	(081282,'EISEN','Carla','23/06/2004'),
	(026946,'EL AYAR','Amir','11/09/2005'),
	(108303,'GEHIN','Arthur','26/02/2005'),
	(057934,'GROSJEAN','Alexandre','09/11/2005'),
	(571113,'HENRY','Paul','12/03/2005'),
	(488820,'JACQUEY','Marc','13/11/2005'),
	(024810,'JULIANO','Alberto','21/04/2005'),
	(249992,'KLEIBER','Gusti','20/02/2005'),
	(492698,'LACOUR','Julie','06/04/2005'),
	(026454,'LARBI','Nourdine','14/07/2004'),
	(309341,'LEFZA','Yasmina','26/11/2005'),
	(076725,'MARTIN','Victor','13/03/2005'),
	(815183,'NGUYEN','Ngong','16/03/2005'),
	(094002,'PELTIER','Romane','14/06/2005'),
	(311262,'RENAULT','Zoé','06/08/2005'),
	(075421,'ROTH','Ursule','03/01/2005'),
	(121001,'SERHANI','Sabrina','01/09/2005'),
	(538965,'TUDJANE','Yourk','31/01/2005'),
	(389873,'VIALET','Priscile','28/02/2005'),
	(980306,'WADE','Marcelin','03/05/2005'),
	(807158,'WENGER','Alexandre','20/08/2005'),
	(666702,'YAMAN','Elamine','23/04/2005');

CREATE TABLE seconde (
    num_eleve INT PRIMARY KEY 
    REFERENCES eleve(num_eleve),
    langue1 TEXT,
    langue2 TEXT, 
    classe TEXT);

INSERT INTO seconde 
    (num_eleve,langue1,langue2,classe) 
VALUES 
    (133310,'anglais','espagnol','2A'),
	(156929,'allemand','anglais','2D'), 
	(500633,'anglais','espagnol','2A'),
	(911887,'anglais','espagnol','2A'),
	(906089,'anglais','allemand','2E'),
	(488697,'italien','anglais','2D'),
	(193514,'espagnol','anglais','2C'),
	(321188,'espagnol','anglais','2E'),
	(081282,'anglais','allemand','2A'), 
	(026946,'anglais','arabe','2D'),
	(108303,'allemand','anglais','2D'),
	(057934,'anglais','espagnol','2C'),
	(571113,'allemand','anglais','2E'),
	(488820,'anglais','italien','2D'),
	(024810,'anglais','espagnol','2D'),
	(249992,'anglais','espagnol','2E'),
	(492698,'italien','anglais','2D'),
	(026454,'espagnol','anglais','2C'),
	(309341,'espagnol','anglais','2E'),
	(076725,'anglais','espagnol','2A'),
	(815183,'anglais','espagnol','2D'),
	(094002,'allemand','anglais','2D'),
	(311262,'anglais','espagnol','2E'),
	(075421,'anglais','allemand','2A'),
	(121001,'italien','anglais','2D'),
	(538965,'espagnol','anglais','2D'),
	(389873,'espagnol','anglais','2C'),
	(980306,'allemand','anglais','2E'),
	(807158,'allemand','anglais','2A'),
	(666702,'anglais','arabe','2D');

CREATE TABLE options (
    num_eleve INT PRIMARY KEY 
    REFERENCES eleve(num_eleve),
    options TEXT);

INSERT INTO options 
    (num_eleve,options) 
VALUES 
    (156929,'théâtre'),
	(026946,'cinéma'),
	(249992,'cinéma'),
	(311262,'latin');

CREATE TABLE coordonnees (
    num_eleve INT PRIMARY KEY 
    REFERENCES eleve(num_eleve),
    adresse TEXT,
    codepostal INT,
    ville TEXT,
    courriel TEXT);

-- INSERT INTO coordonnees (num_eleve,adresse,codepostal,ville,courriel) 
-- VALUES (807158,"15 avenue Léon Blum",9200,"Paris","Alxandre@gmail.com");

