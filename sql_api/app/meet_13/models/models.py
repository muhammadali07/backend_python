import sqlalchemy as sa
meta = sa.MetaData()


students = sa.Table("students", 
                    meta, 
                    sa.Column("id_siswa", sa.Integer, primary_key=True), 
                    sa.Column("nama", sa.String), 
                    sa.Column("id_kelas", sa.Integer), 
                    sa.Column("tahun_masuk", sa.Integer),
                    sa.Column("jenis_kelas", sa.String),
                    sa.Column("update_date", sa.TIMESTAMP),
                    sa.Column("create_date", sa.TIMESTAMP)
                )