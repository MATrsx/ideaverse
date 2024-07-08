---
Erstellt am: 2024-07-03T21:01
Geändert am: 2024-07-08T17:20
tags:
  - map
cssclasses:
  - header-box
---

`[!!|ghb>release:1.2.1]` `[!!|ghb>issues:2]` `[!!|ghb>open issues:0]` `[!!|ghb>closed issues:2]` `[!!|ghb>contributors:3]` `[!!|ghb>license:MIT]` `[!!|ghs>checks:success]` `[!!|ghs>build:success]`

`ALT` + `A` -> Neues Callout erstellen
 
- & [&]
- ? [?]
- ! [!]
- ~ [~]
- @ [@]
- $ [$]
- % [%]
- " ["]
- tip [tip]
- url [url]
- file [file]
- pin [pin]

> [!Multi-column] 
> 
> > [!Sailboat]+ ## Boats 🚤
> > You probably made these notes in a rush. These [[BOAT notes]] are *lonely boats floating in an empty ocean*. All you need to do is tether them to other notes.
> > 
> > ```dataview
> > LIST
> > FROM #note/boat🚤 
> > SORT file.cday desc
> > LIMIT 10
> > ```
> > This sorts up to the most recent `10`.
> > 
> 
> > [!Leaf]+ ## Develop 🍃
> > You can develop these notes by making remarks, clarifying, and critiquing. Add your opinion and if needed cite your sources.
> > 
> > ```dataview
> > LIST
> > FROM #note/develop🍃 
> > SORT file.cday desc
> > LIMIT 10
> > ```
> > This sorts up to the most recent `10`.


## Zeitstrahl
---
- Punkt 1
	- Unterpunkt 1
		- Unter-Unterpunk 1
	- Unterpunkt 2 
- Punkt 2
	
- Punkt 3

- Test 
- Test 2
hfghfghfghhfghfghfghfghfghhgfhfghfghgfhfghgfhgfhfghgf Hallo mein Name ist Milan
## Multi-Column Icons 
> [!multi-column|center-fixed-small]
>
>> [!blank|center]
>> [![lightbulb icon|80](https://img.icons8.com/ios/250/FFFFFF/light-on.png) <br/> Interests](target%20note.md)
>>
>> [![macbook icon|80](https://img.icons8.com/ios/250/FFFFFF/macbook.png) <br/> Technology](target%20note.md)
>
>> [!blank|center]
>> [![brain icon|80](https://img.icons8.com/ios/250/FFFFFF/brain.png) <br/> Life & Wisdom](target%20note.md)
>>
>> [![briefcase icon|80](https://img.icons8.com/ios/250/FFFFFF/business.png) <br/> Work](target%20note.md)
>
>> [!blank|center]
>> [![running icon|80](https://img.icons8.com/ios/250/FFFFFF/sports-mode.png) <br/> Health](target%20note.md)
>>
>> [![home icon|80](https://img.icons8.com/ios/250/FFFFFF/house-with-a-garden.png) <br/> Family](target%20note.md)

## Column List
---
> [!blank-container] 
> - list item 1 #mcl/list-column
> - list item 2
> - list item 3
> -  sub list 3-1
> -  sub list 3-2
> - list item 4
> - list item 5
> -  sub list 5-1
> - list item 6

## Grid List
---
> [!blank-container]
> - #### Frontmatter CSS #mcl/list-grid 
> 	- `two-column-grid-list`
> 	- `three-column-grid-list`
> - #### Hashtag
> 	- `#mcl/list-grid`
> 	- `#mcl/list-grid-wide`
> - #### Warnung
>  >[!warning]+ Warnung
>  >Wenn die CSS-Klassen im Frontmatter/Properties festgelegt werden,  beeinflusst dies das Styling **aller** ungeordneten Listen im aktuellen Dokument.

**Neon Text{ class=" neon-purple text-big " }**

## Card List
---
> [!blank-container]
> - #### Core Work #mcl/list-card
>     - [[00 Home|Main Goal 1]]
>     - [[00 Home|Main Goal 1]]
>     - [[00 Home|Main Goal 1]]
>         - Collaboration with Jane
>     - [[00 Home|Main Goal 1]]
> - #### Learning & System
>     - [[00 Home|Learning Goal 1]]
>     - [[00 Home|Initiative 1]]
>     - [[00 Home|Initiative 2]]
> - #### Personal
>     - [[00 Home|Personal Goal 1]]
>     - [[00 Home|Personal Goal 2]]

>[!comment-r]
> Lorem ipsum dolor imun de d d fsdg gbfjsd fsdjhfsd sdfsdfs


## Floating Images
---
 ![[lyt-mode-graphic-1.jpg|float-right|350]]
>[!no-icon] ### Callout Title
---
Hier kann eine Beschreibung des Bildes vorgenommen werden, sodass der Platz optimal genutzt werden  kann.  Dadurch können Bilder einfacher und schöner in die Struktur der Datei eingebunden werden, machen das Lesen einfacher und erhöhen die Benutzererfahrung.
## When is the best to ski in Switzerland?
> [!info|float-right-medium green] Average Temperatures and Rainfall
> ![[flow-map.png]]
>> Switzerland’s weather in January is dominated by cold temperatures and snowfall.

- ### The best months to ski in Switzerland are December, January, and February with **January would be the best month** to ski in Switzerland of all three.
	- Most tourists who intend to ski tend to visit **between Christmas and New Year**. Lots of locals go skiing during this period as well.
	- **January** is the best month to ski in my opinion. Snow conditions are often good, there are fewer crowds and hotel prices are not as high.
	- During **February**, it is common for locals to take ski vacations. If you go during this time, expect more crowds and higher hotel prices.


## Infobox
> [!infobox|float-right]
> ## Title
> ![[robert-mccall-black-hole-concept-art-bottom.jpg]]
> ## Info
> A|  B |
> ---|---|
> Text| ([Links](https://en.wikipedia.org/wiki/Frank_Herbert)) |

Diese Infobox soll im Wikipedia-Stil die wichtigsten Informationen am rechten (oder linken) Rand anzeigen.  Dort können Tabellen, Bilder und Admonitions eingefügt werden. Die Syntax ist dieselbe wie die der Callouts. Also `|float-right`, damit die Infobox rechts  und `float-left` damit sie links erscheint. Außerdem können folgende Größen ausgewählt werden:
- `small`
- `medium`
- `large`
Diese Größen können mit einem `-` angehängt werden. Also zum Beispiel `|float-right-medium`.


## Zusätzliches

Hier werden zusätzliche Dateien und Funktionen gelistet: