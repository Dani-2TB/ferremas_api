create database ferremas_dev;
use ferremas_dev;
create user dev_admin@localhost identified by "Testing4321";
grant all on ferremas_dev.* to dev_admin@localhost;