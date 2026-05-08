# ADBIS HORISTONTAL

## Krav

- Python 3.10 eller nyere
- Flask

## Kør lokalt på localhost

1. Åbn et terminalvindue i projektmappen.
2. Opret og aktivér et virtuelt miljø, hvis du ikke allerede har et:

**Windows:**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Installer Flask:

```
pip install flask
```



4. Start applikationen:
```
python app.py
```


5. Åbn browseren og gå til:

```text
http://127.0.0.1:5000/index
```

## Tilgængelige sider

- `/index`
- `/kalender`
- `/kurser`
- `/bookinger`
- `/kursusdetaljer`
- `/medarbejdere`
- `/booking`
