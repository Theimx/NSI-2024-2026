-- Question 7 page 23
SELECT DISTINCT langue1 FROM seconde;

-- page 24
SELECT eleve.nom, eleve.prenom, seconde.classe
FROM eleve
JOIN seconde ON eleve.num_eleve=seconde.num_eleve