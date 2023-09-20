from flask import Flask, request
import psycopg2
import json

app = Flask(__name__)

# Inisialisasi koneksi ke database
conn = psycopg2.connect(
    host='localhost',
    port=5432,
    user='my_user',
    password='my_password',
    database='my_database'
)

# Fungsi untuk membuat data baru
@app.route('/api/v1/create', methods=['POST'])
def create():
    # Dapatkan data dari request
    data = request.json

    # Simpan data ke database
    cur = conn.cursor()
    cur.execute("INSERT INTO my_table (name, age) VALUES (%s, %s)", (data['name'], data['age']))
    conn.commit()

    return 'Data berhasil dibuat!'

# Fungsi untuk membaca data
@app.route('/api/v1/read', methods=['GET'])
def read():
    # Dapatkan semua data dari database
    cur = conn.cursor()
    cur.execute("SELECT * FROM my_table")
    data = cur.fetchall()

    return data

# Fungsi untuk memperbarui data
@app.route('/api/v1/update', methods=['PUT'])
def update():
    # Dapatkan data dari request
    data = request.json

    # Perbarui data di database
    cur = conn.cursor()
    cur.execute("UPDATE my_table SET name=%s, age=%s WHERE id=%s", (data['name'], data['age'], data['id']))
    conn.commit()

    return 'Data berhasil diperbarui!'

# Fungsi untuk menghapus data
@app.route('/api/v1/delete', methods=['DELETE'])
def delete():
    # Dapatkan id data yang akan dihapus dari request
    id = request.json['id']

    # Hapus data dari database
    cur = conn.cursor()
    cur.execute("DELETE FROM my_table WHERE id=%s", (id,))
    conn.commit()

    return 'Data berhasil dihapus!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)