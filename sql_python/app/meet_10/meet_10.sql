CREATE Table students(
    id_siswa int primary key auto_increment,
    nama VARCHAR(50) not null,
    id_kelas int not null,
    tahun_masuk VARCHAR(50) not null,
    jenis_kelas VARCHAR(100) not null,
    update_date timestamp,
    create_date timestamp
)

INSERT INTO students (nama, id_kelas, tahun_masuk, jenis_kelas, create_date)
VALUES
    ('anwar', 1, 2023, 'backend', NOW()),
    ('dwija', 1, 2023, 'backend', NOW()),
    ('rida', 1, 2023, 'backend', NOW()),
    ('kinanti', 1, 2023, 'backend', NOW()),
    ('touya', 2, 2023,  'flutter', NOW()),
    ('kanami', 2, 2023, 'flutter', NOW()),
    ('tsubasa', 3, 2023, 'laravel', NOW())

 INSERT INTO students (nama, id_kelas, tahun_masuk, jenis_kelas, create_date) VALUES (%s,%s,%s,%s,NOW())