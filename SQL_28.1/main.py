import sqlite3

# 1️⃣ Připojení k databázi (vytvoří soubor, pokud neexistuje)
conn = sqlite3.connect("chat.db")
cursor = conn.cursor()

# 2️⃣ Vytvoření tabulek
cursor.executescript("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE IF NOT EXISTS rooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_id INTEGER,
    user_id INTEGER,
    message TEXT,
    FOREIGN KEY (room_id) REFERENCES rooms(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
""")

# 3️⃣ Vložení dat
cursor.executescript("""
INSERT INTO users (username, password) VALUES
('user1', 'password1'),
('user2', 'password2'),
('user3', 'password3');

INSERT INTO rooms (name) VALUES
('room1'),
('room2'),
('room3');

INSERT INTO messages (room_id, user_id, message) VALUES
(1, 1, 'Ahoj, ako sa máte?'),
(1, 1, 'Dobre ráno všetkým!'),
(1, 2, 'Dobré popoludnie!'),
(2, 3, 'Ahojte, čo sa deje?'),
(2, 1, 'Som tu!'),
(2, 2, 'Ahoj, ako sa máte?'),
(3, 3, 'Tento chat je skvelý!');
""")

# SQL dotaz: Najít uživatele, kteří poslali zprávy do místnosti 'room1'
dotaz_uzivatele_v_mistnosti = """
SELECT DISTINCT uzivatele.id, uzivatele.username
FROM users AS uzivatele
JOIN messages AS zpravy ON uzivatele.id = zpravy.user_id
JOIN rooms AS mistnosti ON zpravy.room_id = mistnosti.id
WHERE mistnosti.name = 'room1';
"""

# Úkol 2: Počet různých uživatelů, kteří poslali zprávy do jednotlivých místností
dotaz_pocet_uzivatelu_v_mistnostech = """
SELECT mistnosti.name AS nazev_mistnosti, COUNT(DISTINCT zpravy.user_id) AS pocet_unikatnich_uzivatelu
FROM messages AS zpravy
JOIN rooms AS mistnosti ON zpravy.room_id = mistnosti.id
GROUP BY mistnosti.name;
"""

# Úkol 3: Místnosti, do kterých poslal zprávy konkrétní uživatel (např. user2)
dotaz_mistnosti_uzivatele = """
SELECT DISTINCT mistnosti.name AS nazev_mistnosti
FROM messages AS zpravy
JOIN rooms AS mistnosti ON zpravy.room_id = mistnosti.id
JOIN users AS uzivatele ON zpravy.user_id = uzivatele.id
WHERE uzivatele.username = 'user2';
"""

# Úkol 4: Počet zpráv, které poslal každý uživatel
dotaz_pocet_zprav_uzivatelu = """
SELECT uzivatele.username AS jmeno_uzivatele, COUNT(zpravy.id) AS pocet_zprav
FROM messages AS zpravy
JOIN users AS uzivatele ON zpravy.user_id = uzivatele.id
GROUP BY uzivatele.username;
"""

# Úkol 5: Počet zpráv v místnostech od jednotlivých uživatelů
dotaz_pocet_zprav_v_mistnostech = """
SELECT mistnosti.name AS nazev_mistnosti, uzivatele.username AS jmeno_uzivatele, COUNT(zpravy.id) AS pocet_zprav
FROM messages AS zpravy
JOIN rooms AS mistnosti ON zpravy.room_id = mistnosti.id
JOIN users AS uzivatele ON zpravy.user_id = uzivatele.id
GROUP BY mistnosti.name, uzivatele.username
ORDER BY mistnosti.name, pocet_zprav DESC;
"""

# Seznam dotazů k vykonání
seznam_dotazu = [
    ("Počet unikátních uživatelů v místnostech", dotaz_pocet_uzivatelu_v_mistnostech),
    ("Místnosti, do kterých poslal zprávy uživatel 'user2'", dotaz_mistnosti_uzivatele),
    ("Počet zpráv, které poslal každý uživatel", dotaz_pocet_zprav_uzivatelu),
    ("Počet zpráv v místnostech od jednotlivých uživatelů", dotaz_pocet_zprav_v_mistnostech),
]

# Spuštění dotazů a výpis výsledků
for nazev_dotazu, dotaz in seznam_dotazu:
    cursor.execute(dotaz)
    vysledky = cursor.fetchall()

    print(f"\nVýsledky pro: {nazev_dotazu}")
    for radek in vysledky:
        print(radek)

# Uzavření spojení s databází
conn.close()