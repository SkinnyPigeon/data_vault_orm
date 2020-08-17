insert into patient (serums_id, name, age, address, postcode) values (1, 'Euan', 26, 'There', 'EH3');
insert into patient (serums_id, name, age, address, postcode) values (1, 'Euan', 36, 'Here', 'EH6');

insert into operations (serums_id, operation_id, description) values (1, 1, 'Knee op');
insert into operations (serums_id, operation_id, description) values (1, 2, 'Arm op');
insert into operations (serums_id, operation_id, description) values (1, 3, 'Head op');
insert into operations (serums_id, operation_id, description) values (1, 4, 'Back op');
insert into operations (serums_id, operation_id, description) values (1, 5, 'Chest op');

insert into patient_operations (serums_id, operations_id) values (1, 1);
insert into patient_operations (serums_id, operations_id) values (1, 2);
insert into patient_operations (serums_id, operations_id) values (2, 3);
insert into patient_operations (serums_id, operations_id) values (2, 4);
insert into patient_operations (serums_id, operations_id) values (2, 5);

