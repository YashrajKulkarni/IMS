use IMS;
show tables;
select * from policy_payment;
select * from policy_data;
select members_id,bank_name from life_insurance;
select * from health_insurance;
select * from home_insurance;
select * from life_insurance;
select * from vehicle_insurance;
select * from members_data ;


ALTER TABLE policy_payment ADD total_premium_outstanding bigint;


ALTER TABLE vehicle_insurance MODIFY COLUMN vehicle_no varchar(25);
ALTER TABLE life_insurance ADD column ac_no bigint,add column ifsc varchar(15),add column bank_name varchar(25),add columnnominee_name varchar(15),add columnnominee_aadhar bigint,add column nominee_relation varchar(15);
create table life_insurance(policy_no bigint primary key not null,members_id varchar(15),medical_history varchar(255),occupation varchar(25),sum_assured int,premium int,city_living varchar(35),period int,policy_commencement date,status varchar(10),plan_name varchar(25), premium_type varchar(15),agent_id varchar(15),bonus int);
show tables;
select column_name,ordinal_position,is_nullable,column_type,column_key from information_schema.columns where table_schema = 'IMS' and table_name = 'vehicle_insurance';