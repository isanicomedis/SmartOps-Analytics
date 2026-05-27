-- vizualizar todos os dados
SELECT *
FROM manutencao_industrial;

-- quantidade total de maquinas
SELECT COUNT(*) AS total_maquinas
FROM manutencao_industrial;

-- quantidade de falhas
SELECT COUNT(*) AS total_falhas
FROM manutencao_industrial
WHERE machine_failure = 1;

-- media de torque
SELECT AVG(torque) AS media_torque
FROM manutencao_industrial;

-- media da temperatura do processo
SELECT AVG(process_temperature) AS media_temperatura
FROM manutencao_industrial;

-- maior velocidade rotacional
SELECT MAX(rotational_speed) AS maior_velocidade
FROM manutencao_industrial;

-- menor velocidade rotacional
SELECT MIN(rotational_speed) AS menor_velocidade
FROM manutencao_industrial;

-- tipos de maquinas existentes 
SELECT DISTINCT machine_type
FROM manutencao_industrial;

-- QUANTIDADE DE MÁQUINAS POR TIPO
SELECT machine_type,
       COUNT(*) AS quantidade
FROM manutencao_industrial
GROUP BY machine_type;

-- MÁQUINAS COM FALHA
SELECT *
FROM manutencao_industrial
WHERE machine_failure = 1;