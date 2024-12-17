# Proiectarea-Translatoarelor-Proiect

## Proiect: Programarea Translatoarelor

### Descriere Proiect

Acest proiect este o aplicație Python care analizează **fișiere de log-uri** și extrage informații utile folosind **expresii regulate (regex)**. Aplicația permite utilizatorului să interacționeze prin **meniul interactiv** în linia de comandă și oferă opțiuni variate pentru filtrarea și extragerea datelor relevante.

---

## Arhitectura Proiectului

Structura fișierelor este următoarea:

```plaintext
Proiect-Translatoare/
│
├── README.md               # Documentația proiectului
├── requirements.txt        # Lista de dependențe
├── logs/                   # Folder ce conține fișierele de log
│   └── app.log             # Exemplu de fișier de log pentru analiză
├── src/                    # Codul sursă al aplicației
│   ├── main.py             # Punctul principal de intrare al aplicației
│   ├── config.py           # Configurația aplicației (căi către fișiere, etc.)
│   ├── utils/              # Utilitare diverse
│   │   ├── file_utils.py   # Funcții pentru citirea fișierelor
│   │   └── regex_utils.py  # Funcții pentru aplicarea regex-urilor
│   └── processors/         # Procesare log-uri
│       └── log_parser.py   # Clasa pentru parsarea și manipularea log-urilor
└── output/                 # Opțional, rezultate salvate (dacă aplicația exportă ceva)
```

### Modul de Funcționare

1. **Fișierul principal:** `src/main.py` conține meniul interactiv care oferă utilizatorului opțiuni pentru analiza log-urilor.
2. **Regex-uri implementate:** Sunt folosite expresii regulate pentru a extrage date precum:
   - Identificatori de cerere (`reqId`);
   - Nivelul de log (`level`);
   - Adresele IP (`remoteAddr`);
   - Mesaje (`message`);
   - `userAgent` și URL-uri.
3. **Modularitate:** Codul este împărțit pe fișiere, fiecare cu o responsabilitate clară:
   - `file_utils.py` - Citirea fișierelor log.
   - `regex_utils.py` - Funcții pentru regex.
   - `log_parser.py` - Procesarea și filtrarea log-urilor.

---

## Instrucțiuni de Instalare

### 1. Instalarea Python
Asigură-te că ai instalat **Python 3.8+** pe sistemul tău. Verifică versiunea cu comanda:
```bash
python --version
```

### 2. Clonarea Proiectului
Clonează repository-ul folosind `git` sau descarcă fișierele manual:
```bash
git clone https://github.com/utilizator/Proiect-Translatoare.git
cd Proiect-Translatoare
```

### 3. Structura Fișierelor de Log
Creează sau încarcă fișierele de log în folderul `logs/`. Exemplu de fișier de log valid:
```json
{"reqId":"96LuQQeekORu1qdgtsoG","level":3,"time":"2024-12-11T01:49:08+00:00","remoteAddr":"192.168.100.49","message":"could not enable apps"}
{"reqId":"z4rlVEo3pYPBbRcxjg1K","level":2,"time":"2024-12-11T02:21:46+00:00","remoteAddr":"5.14.162.225","message":"Login failed: Lorand (Remote IP: 5.14.162.225)"}
```

### 4. Rularea Aplicației
Accesează directorul `src/` și rulează programul principal:
```bash
python main.py
```

---

## Bonus: Edge Cases

Aplicația tratează următoarele edge cases:  
- Intrări incomplete sau corupte în log-uri (de exemplu, lipsa câmpului `remoteAddr`);  
- Mesaje cu caractere speciale sau text neconvențional;  
- Fișiere goale sau lipsă – utilizatorul va fi notificat corespunzător.

---

## Licență

Proiectul este public și poate fi utilizat pentru scopuri educaționale.