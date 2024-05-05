CREATE TABLE teachers(
	teacher_id SERIAL PRIMARY KEY,
	first_name VARCHAR(150) NOT NULL,
	last_name VARCHAR(1050) NOT NULL,
	homeroom_number smallint,
	department VARCHAR(100) NOT NULL,
	email VARCHAR(250) UNIQUE ,
	phone VARCHAR(100) UNIQUE 
);

CREATE TABLE students(
	student_id SERIAL PRIMARY KEY,
	first_name VARCHAR(150) NOT NULL,
	last_name VARCHAR(150) NOT NULL, 
	homeroom_number smallint, 
	phone VARCHAR(100) UNIQUE NOT NULL,
	email VARCHAR(250) UNIQUE, 
	graduation_year INTEGER
	
);

INSERT INTO teachers(first_name ,last_name ,homeroom_number ,department, email ,phone)
VALUES
('Jonas', 'Salk', '5', 'Biology','jsalk@school.org','777-555-4321');

INSERT INTO students(first_name,last_name, homeroom_number, phone,graduation_year)
VALUES
('Mark','Watney','5', '777-555-1234','2035' )