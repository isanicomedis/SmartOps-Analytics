-- CRIANDO A TABELA

CREATE TABLE manutencao_industrial ( --criar uma tabela no banco de dados

    -- tipo da máquina
    machine_type VARCHAR(10), --texto até 10 caracteres

    -- temperatura do ar
    air_temperature FLOAT,

    -- temperatura do processo
    process_temperature FLOAT,

    -- torque da máquina
    torque FLOAT,

    -- velocidade de rotação
    rotational_speed INT,

    -- desgaste da ferramenta
    tool_wear INT,

    -- falha da máquina
    -- 0 = sem falha
    -- 1 = com falha
    machine_failure INT

);