create database Asset_Management;
use Asset_Management;
/* 
 employees table:
 employee_id (Primary Key)
 name
 department
 email
 password
 */
create table employees(
    employee_id varchar(10) primary key not null,
    name varchar(120),
    department varchar(20),
    email varchar(130),
    password varchar(80)
);
/*
 assets table:
 asset_id (Primary Key): Unique identifier for each asset
 name
 type: Type of the asset (e.g., laptop, vehicle, equipment).
 serial_number: Serial number or unique identifier of the asset.
 purchase_date.
 location: Current location of the asset.
 status: Status of the asset (e.g., in use, decommissioned, under maintenance).
 owner_id: (Foreign Key): References the employee who owns the asset.
 */
create table assets(
    asset_id varchar(10) primary key not null,
    name varchar(100),
    type varchar(70),
    serial_number varchar(60) not null unique,
    purchase_date date,
    location varchar(80),
    status varchar(30),
    owner_id varchar(10),
    foreign key (owner_id) references employees(employee_id)
);
/*
 maintenance_records table:
 maintenance_id (Primary Key): Unique identifier for each maintenance record.
 asset_id (Foreign Key): References the asset for which maintenance was performed.
 maintenance_date.
 description: Description of the maintenance activity.
 cost: Cost associated with the maintenance.
 */
create table maintenanceRecords(
    maintenance_id varchar(10) primary key not null,
    asset_id varchar(10),
    maintenance_date date,
    description varchar(150),
    cost decimal(6, 2),
    foreign key (asset_id) references assets(asset_id)
);
/*
 asset_allocation table:
 allocation_id (Primary Key): Unique identifier for each asset allocation.
 asset_id (Foreign Key): References the asset that is allocated.
 employee_id (Foreign Key): References the employee to whom the asset is allocated.
 allocation_date: Date when the asset was allocated.
 return_date: Date when the asset was returned (if applicable).
 */
create table assetAllocation(
    allocation_id varchar(10) primary key not null,
    asset_id varchar(10),
    employee_id varchar(10),
    allocation_date date,
    return_date date,
    foreign key (asset_id) references assets(asset_id),
    foreign key (employee_id) references employees(employee_id)
);
/*
 reservations table(to store order details):
 reservation_id (Primary Key): Unique identifier for each reservation.
 asset_id (Foreign Key): References the asset that is being reserved.
 employee_id (Foreign Key): References the employee who made the reservation.
 reservation_date: Date when the reservation was made.
 start_date: Date when the reserved asset is needed.
 end_date: Date when the reservation ends.
 status: Status of the reservation (e.g., pending, approved, canceled).
 */
create table reservations(
    reservation_id varchar(10) primary key not null,
    asset_id varchar(10),
    employee_id varchar(10),
    reservation_date date,
    start_date date,
    end_date date,
    status varchar(15),
    foreign key (employee_id) references employees(employee_id),
    foreign key (asset_id) references assets(asset_id)
);

insert into employees (employee_id, name, department, email, password)
values (
        'E001',
        'John Doe',
        'IT',
        'john.doe@gmail.com',
        'password123'
    ),
    (
        'E002',
        'Jane Smith',
        'HR',
        'jane.smith@gmail.com',
        'password456'
    ),
    (
        'E003',
        'Alice Johnson',
        'Finance',
        'alice.johnson@gmail.com',
        'password789'
    ),
    (
        'E004',
        'Bob Brown',
        'Marketing',
        'bob.brown@gmail.com',
        'password101'
    ),
    (
        'E005',
        'Charlie Davis',
        'Operations',
        'charlie.davis@gmail.com',
        'password202'
    );
insert into assets (
        asset_id,
        name,
        type,
        serial_number,
        purchase_date,
        location,
        status,
        owner_id
    )
values (
        'A001',
        'Laptop',
        'Electronics',
        'SN123456',
        '2028-01-15',
        'Office',
        'in use',
        'E001'
    ),
    (
        'A002',
        'Projector',
        'Electronics',
        'SN654321',
        '2028-02-20',
        'Conference Room',
        'under maintenance',
        'E002'
    ),
    (
        'A003',
        'Office Chair',
        'Furniture',
        'SN789012',
        '2028-03-05',
        'Office',
        'in use',
        'E003'
    ),
    (
        'A004',
        'Desk',
        'Furniture',
        'SN345678',
        '2028-04-10',
        'Office',
        'available',
        'E004'
    ),
    (
        'A005',
        'Company Car',
        'Vehicle',
        'SN901234',
        '2028-05-15',
        'Parking Lot',
        'in use',
        'E005'
    );
insert into maintenanceRecords (
        maintenance_id,
        asset_id,
        maintenance_date,
        description,
        cost
    )
values (
        'M001',
        'A002',
        '2028-03-01',
        'Replaced bulb',
        150.00
    ),
    (
        'M002',
        'A001',
        '2028-02-10',
        'Software update',
        75.00
    ),
    (
        'M003',
        'A003',
        '2028-04-15',
        'Repaired armrest',
        50.00
    ),
    ('M004', 'A004', '2028-05-01', 'Assembly', 30.00),
    (
        'M005',
        'A005',
        '2028-06-10',
        'Oil change',
        100.00
    );
insert into assetAllocation (
        allocation_id,
        asset_id,
        employee_id,
        allocation_date,
        return_date
    )
values ('AL001', 'A001', 'E001', '2028-01-16', NULL),
    ('AL002', 'A002', 'E002', '2028-02-21', NULL),
    ('AL003', 'A003', 'E003', '2028-03-06', NULL),
    ('AL004', 'A004', 'E004', '2028-04-11', NULL),
    ('AL005', 'A005', 'E005', '2028-05-16', NULL);
insert into reservations (
        reservation_id,
        asset_id,
        employee_id,
        reservation_date,
        start_date,
        end_date,
        status
    )
values (
        'R001',
        'A002',
        'E001',
        '2028-03-01',
        '2028-03-05',
        '2028-03-10',
        'approved'
    ),
    (
        'R002',
        'A003',
        'E002',
        '2028-04-01',
        '2028-04-05',
        '2028-04-10',
        'pending'
    ),
    (
        'R003',
        'A004',
        'E003',
        '2028-05-01',
        '2028-05-05',
        '2028-05-10',
        'canceled'
    ),
    (
        'R004',
        'A005',
        'E004',
        '2028-06-01',
        '2028-06-05',
        '2028-06-10',
        'approved'
    ),
    (
        'R005',
        'A001',
        'E005',
        '2028-07-01',
        '2028-07-05',
        '2028-07-10',
        'pending'
    );

select *
from employees;
select *
from assets;
select *
from maintenanceRecords;
select *
from assetAllocation;
select *
from reservations;