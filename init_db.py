import sqlite3

def inicializador_db():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()

        # Tabela de usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL,email TEXT UNIQUE NOT NULL,senha TEXT NOT NULL
        )
    ''')

    # Tabela de vagas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vagas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            empresa TEXT NOT NULL,
            area TEXT NOT NULL,
            descricao TEXT,
            usuario_id INTEGER,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        )
    ''')

    conn.commit()
    conn.close()

    if __name__ == '__main__':
        inicializador_db()