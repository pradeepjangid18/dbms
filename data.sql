CREATE TABLE customer_database(
	Name varchar(16) NOT NULL,
	Email varchar(32) NOT NULL,
	Mobile_No varchar(10),
	Address varchar(256),
	password varchar(256) NOT NULL,
	PRIMARY KEY (Mobile_No)
);

CREATE TABLE appointment_database(
	appoint_id int auto_increment,
	Mobile_No varchar(10),
	Working_Address varchar(64),
	Meeting_Address varchar(64),
	Date varchar(16),
	Discription varchar(128),
	status varchar(16),
	PRIMARY KEY (appoint_id),
	FOREIGN KEY (Mobile_No) REFERENCES customer_database(Mobile_No)
);

CREATE TABLE site_database(
	site_id int,
	location varchar(64),
	work_to_do varchar(128),
	deadline varchar(16),
	PRIMARY KEY (site_id),
	FOREIGN KEY (site_id) REFERENCES appointment_database(appoint_id)
);

CREATE TABLE site_payment(
	payment_id int,
	site_no int,
	money_taken int,
	date_of_taken varchar(16),
	PRIMARY KEY (payment_id),
	FOREIGN KEY (site_no) REFERENCES site_database(site_id) ON DELETE CASCADE
);

CREATE TABLE raw_materials(
	product_id int auto_increment,
	product_name varchar(32),
	date_of_supply varchar(16),
	quantity int,
	image LONGBLOB,
	bill_amount int,
	site_no int,
	PRIMARY KEY (product_id),
	FOREIGN KEY (site_no) REFERENCES site_database(site_id) ON DELETE CASCADE
);



CREATE TABLE employee(
	Name varchar(32) NOT NULL,
	Mobile_No varchar(10),
	Address varchar(64),
	salary int,
	work_location int,
	account_no int,
	bank_name varchar(32) NOT NULL,
	ifsc_code varchar(32) NOT NULL,
	password varchar(16) NOT NULL,
	PRIMARY KEY (Mobile_No),
	FOREIGN KEY (work_location) REFERENCES site_database(site_id) ON DELETE SET NULL
);

CREATE TABLE employee_site_history(
	site_id int,
	Mobile_No varchar(10),
	date_of_start varchar(16),
	date_of_end varchar(16),
	PRIMARY KEY(site_id,Mobile_No,date_of_start),
	FOREIGN KEY (site_id) REFERENCES site_database(site_id) ON DELETE CASCADE,
	FOREIGN KEY (Mobile_No) REFERENCES employee(Mobile_No) ON DELETE CASCADE
);

CREATE TABLE employee_payment(
	payment_no int auto_increment,
	money_given int,
	date_of_given varchar(16),
	Mobile_No varchar(10),
	PRIMARY KEY (payment_no),
	FOREIGN KEY (Mobile_No) REFERENCES employee(Mobile_No) ON DELETE CASCADE
);


CREATE TABLE customer_query(
	query_id int auto_increment,
	Mobile_No varchar(10),
	query varchar(128),
	PRIMARY KEY (query_id),
	FOREIGN KEY (Mobile_No) REFERENCES customer_database(Mobile_No) ON DELETE CASCADE
);

CREATE TABLE employee_query(
	query_id int auto_increment,
	Mobile_No varchar(10),
	query varchar(128),
	PRIMARY KEY (query_id),
	FOREIGN KEY (Mobile_No) REFERENCES employee(Mobile_No) ON DELETE CASCADE
);

CREATE TABLE catalog(
	image_id int NOT NULL auto_increment,
	image_type varchar(32),
	image LONGBLOB,
	PRIMARY KEY (image_id)
);

