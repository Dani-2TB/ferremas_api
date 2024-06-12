DROP TABLE marca CASCADE;
DROP TABLE categoria CASCADE;

CREATE TABLE marca(
	nombre varchar(60) NOT NULL
);

CREATE TABLE categoria(
	nombre varchar(60) NOT NULL
);

CREATE TABLE producto(
	nombre varchar(60) NOT NULL,
    descripcion varchar(300),
    precio decimal(10,2)
);