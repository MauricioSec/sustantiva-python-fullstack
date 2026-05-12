-- 1. Listar todos los pacientes en fase 2 o 3
SELECT * FROM pacientes_covid
WHERE fase IN (2, 3);

-- 2. Mostrar el promedio de edad de los pacientes en fase 1
SELECT AVG(edad) AS promedio_edad
FROM pacientes_covid
WHERE fase = 1;

-- 3. Mostrar la mayor cantidad de días enfermo que lleva un paciente en fase 3
SELECT MAX(dias_enfermo) AS max_dias_enfermo
FROM pacientes_covid
WHERE fase = 3;

-- 4. Mostrar el promedio de días enfermo de los pacientes en fase 2
SELECT AVG(dias_enfermo) AS promedio_dias_enfermo
FROM pacientes_covid
WHERE fase = 2;

-- 5. Mostrar los pacientes con edades entre 25 y 39 que estén en fase 1 o 3
SELECT * FROM pacientes_covid
WHERE edad BETWEEN 25 AND 39
  AND fase IN (1, 3);

-- 6. Mostrar todos los pacientes con rut terminado en número que estén en un hospital empezado en S
-- La función RIGHT extrae el último carácter del rut para validar que sea un dígito.
-- Esto asegura compatibilidad estándar sin depender exclusivamente de expresiones regulares complejas.
SELECT * FROM pacientes_covid
WHERE RIGHT(rut, 1) IN ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
  AND hospital LIKE 'S%';

-- 7. Mostrar el promedio de edad de pacientes mujeres
SELECT AVG(edad) AS promedio_edad_mujeres
FROM pacientes_covid
WHERE sexo = 'F';

-- 8. Mostrar la cantidad total de pacientes que están en fase 1 o 3
SELECT COUNT(*) AS total_pacientes
FROM pacientes_covid
WHERE fase IN (1, 3);