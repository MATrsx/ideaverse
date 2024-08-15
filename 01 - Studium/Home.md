---
Erstellt am: Dienstag, 📅13. August 2024, 🕐23:19:04
Geändert am: Donnerstag, 📅15. August 2024, 🕐18:25:21
---

Dateien:
	`$=dv.pages('"01 - Studium"').length`

Dateien
: fdsfsdfsd

# Recents

## Last Opened

```dataviewjs
dv.list(app.workspace.recentFileTracker.lastOpenFiles.map(x=>dv.fileLink(x)).slice(0, 7))
```

---

## Last Modified

```dataview
LIST
FROM ""
SORT file.mtime DESC
LIMIT 7
```