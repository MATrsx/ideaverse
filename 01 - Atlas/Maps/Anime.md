---
Erstellt am: 2024-07-30T21:20
Geändert am: 2024-07-30T21:50
up:
  - "[[Sources Map]]"
---

If a note has a `tag` property that says `source/anime` or has the `type` Property `Anime`, it will show up below.

> [!map]+ Top 10 Anime
> ```dataview
> TABLE WITHOUT ID 
> file.link AS "Name/Titel", genre, rank
> 
> FROM #source/anime 
> 
> SORT rank desc
> 
> LIMIT 10
> ```
