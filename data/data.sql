insert into patient (id, serums_id, name, age, address, postcode) values (1, 1, 'Euan', 26, 'There', 'EH3');
insert into patient (id, serums_id, name, age, address, postcode) values (2, 1, 'Euan', 36, 'Here', 'EH6');

insert into operations (id, serums_id, operation_id, description) values (1, 1, 1, 'Knee op');
insert into operations (id, serums_id, operation_id, description) values (2, 1, 2, 'Arm op');
insert into operations (id, serums_id, operation_id, description) values (3, 1, 3, 'Head op');
insert into operations (id, serums_id, operation_id, description) values (4, 1, 4, 'Back op');
insert into operations (id, serums_id, operation_id, description) values (5, 1, 5, 'Chest op');

insert into patient_operations (patient_id, operations_id) values (1, 1);
insert into patient_operations (patient_id, operations_id) values (1, 2);
insert into patient_operations (patient_id, operations_id) values (2, 3);
insert into patient_operations (patient_id, operations_id) values (2, 4);
insert into patient_operations (patient_id, operations_id) values (2, 5);

insert into doctors (doctor_id, name) values (1, 'Jeff');
insert into doctors (doctor_id, name) values (2, 'Steve');
insert into doctors (doctor_id, name) values (3, 'Dave');

