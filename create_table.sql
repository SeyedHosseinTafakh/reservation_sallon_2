use reserve;
drop table reservation;
create table reservation (
id int not null auto_increment,
str_rez datetime,
end_rez datetime,
customer_phone varchar(255),
worker_id varchar(255),
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY ( id ));

