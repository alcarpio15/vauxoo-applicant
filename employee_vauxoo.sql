-- "employee_vauxoo.sql" por Pedro A. Carpio
--
--
--Contacteme a traves del Telefono: (416)434-7903,
--	
-- 
-- NOTA: Por favor, no agregue comandos para crear bases de datos en este archivo.
--       Puede crear base de datos localmente para probarlo.
--       Considere agregar ';' al comando final.

-- Creo las Tablas: 'employee' se define de ultimo porque deseo establecer
-- 					sus relaciones foraneas con otras tablas a la hora de
--					su creacion.

CREATE TABLE employee_department (
	id INT NOT NULL,
	name VARCHAR(64) NOT NULL,
	description VARCHAR(256),
	PRIMARY KEY(id)
);

CREATE TABLE employee_hobby (
);

CREATE TABLE employee (
	id INT NOT NULL,
	first_name VARCHAR(32) NOT NULL,
	last_name VARCHAR(32) NOT NULL,
	department_id INT  NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(department_id) REFERENCES employee_department(id)
	ON DELETE CASCADE
);

CREATE TABLE has_as_hobby (
);


-- Insertamos Departamentos y Empleados para el Ejercicio sql1

INSERT INTO employee_department (id, name, description) VALUES (1, 'Produccion', ' ');
INSERT INTO employee_department (id, name, description) VALUES (2, 'Ventas', ' ');
INSERT INTO employee_department (id, name, description) VALUES (3, 'Soporte Técnico', ' ');
INSERT INTO employee_department (id, name, description) VALUES (4, 'Contaduria', ' ');
INSERT INTO employee_department (id, name, description) VALUES (5, 'Recursos Humanos', ' ');
INSERT INTO employee_department (id, name, description) VALUES (6, 'Comite Directivo', ' ');

--Nombres al Azar, cortesia de BehindTheName.com. Apellidos escogidos por otros métodos.
INSERT INTO employee (id, first_name, last_name, department_id) VALUES(1, 'Felipe Aurelio', 'Gonzalez', 6);
INSERT INTO employee (id, first_name, last_name, department_id) VALUES(2, 'Eladio Geronimo', 'Villa', 3);
INSERT INTO employee (id, first_name, last_name, department_id) VALUES(3, 'Adela', 'Alvarez Arevalo', 2);
INSERT INTO employee (id, first_name, last_name, department_id) VALUES(4, 'Maritza Nuria', 'Ortiz Quevedo', 5);


