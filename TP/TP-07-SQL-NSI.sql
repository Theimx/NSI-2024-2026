DROP TABLE IF EXISTS coordonnees;
DROP TABLE IF EXISTS options;
DROP TABLE IF EXISTS seconde;
DROP TABLE IF EXISTS eleve;

CREATE TABLE eleve (
    num_eleve INT PRIMARY KEY,
    nom TEXT,
    prenom TEXT,
    datenaissance TEXT);

INSERT INTO eleve (num_eleve,nom,prenom,datenaissance) 
VALUES (807158,"WENGER","Alexandre","15/04/2007");

CREATE TABLE seconde (
    num_eleve INT PRIMARY KEY 
    REFERENCES eleve(num_eleve),
    langue1 TEXT,
    langue2 TEXT, 
    classe TEXT);

INSERT INTO seconde (num_eleve,langue1,langue2,classe) 
VALUES (807158,"Anglais","Espagnol","2D");

CREATE TABLE options (
    num_eleve INT PRIMARY KEY 
    REFERENCES eleve(num_eleve),
    options TEXT);

INSERT INTO options (num_eleve,options) 
VALUES (807158,"cinéma");

CREATE TABLE coordonnees (
    num_eleve INT PRIMARY KEY 
    REFERENCES eleve(num_eleve),
    adresse TEXT,
    codepostal INT,
    ville TEXT,
    courriel TEXT);

INSERT INTO coordonnees (num_eleve,adresse,codepostal,ville,courriel) 
VALUES (807158,"15 avenue Léon Blum",8800,"Epinal","Alxandre@gmail.com");