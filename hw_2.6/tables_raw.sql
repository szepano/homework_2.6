DROP TABLE IF EXISTS students;
CREATE TABLE students (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(30)
);

DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	students VARCHAR(50),
	FOREIGN KEY (students) REFERENCES students (id)
);

DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	teacher VARCHAR(30)
);

DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	subject VARCHAR(20),
	teaches INT,
	FOREIGN KEY (teaches) REFERENCES teachers (id)
);
	
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
	stud_id INT,
	grade TINYINT,
	subj VARCHAR(20),
	given_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (stud_id) REFERENCES students (id),
	FOREIGN KEY (subj) REFERENCES subjects (subject)
);