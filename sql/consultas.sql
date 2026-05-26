-- =========================================
-- SMARTOPS ANALYTICS
-- consultas.sql
-- Consultas para análise dos dados
-- =========================================


-- -----------------------------------------
-- VISUALIZAR TODOS OS DADOS
-- -----------------------------------------

SELECT *
FROM manutencao_industrial;


-- -----------------------------------------
-- QUANTIDADE TOTAL DE MÁQUINAS
-- -----------------------------------------

SELECT COUNT(*) AS total_maquinas
FROM manutencao_industrial;


-- -----------------------------------------
-- QUANTIDADE DE FALHAS
-- -----------------------------------------

SELECT COUNT(*) AS total_falhas
FROM manutencao_industrial
WHERE machine_failure = 1;


-- -----------------------------------------
-- MÉDIA DE TORQUE
-- -----------------------------------------

SELECT AVG(torque) AS media_torque
FROM manutencao_industrial;


-- -----------------------------------------
-- MÉDIA DA TEMPERATURA DO PROCESSO
-- -----------------------------------------

SELECT AVG(process_temperature) AS media_temperatura
FROM manutencao_industrial;


-- -----------------------------------------
-- MAIOR VELOCIDADE ROTACIONAL
-- -----------------------------------------

SELECT MAX(rotational_speed) AS maior_velocidade
FROM manutencao_industrial;


-- -----------------------------------------
-- MENOR VELOCIDADE ROTACIONAL
-- -----------------------------------------

SELECT MIN(rotational_speed) AS menor_velocidade
FROM manutencao_industrial;


-- -----------------------------------------
-- TIPOS DE MÁQUINAS EXISTENTES
-- -----------------------------------------

SELECT DISTINCT machine_type
FROM manutencao_industrial;


-- -----------------------------------------
-- QUANTIDADE DE MÁQUINAS POR TIPO
-- -----------------------------------------

SELECT machine_type,
       COUNT(*) AS quantidade
FROM manutencao_industrial
GROUP BY machine_type;


-- -----------------------------------------
-- MÁQUINAS COM FALHA
-- -----------------------------------------

SELECT *
FROM manutencao_industrial
WHERE machine_failure = 1;