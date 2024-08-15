---
created: '<% tp.file.title %>'
modified: 2024-06-11 - 06:58 pm
---

⏮️<% tp.user.dailyZoomOutRibbon(tp.file.title) %>⏭️
 
⬅️<% tp.user.dailyNextPrevRibbon(tp.file.title) %>➡️

---

<% tp.user.dailyDateInfo(tp.file.title) %>

****

# 1. Take Actions

## Tasks

> [!MISSING] Overdue Tasks 🚨
> 
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/tasks", {type: "overdue", onDate: "<% tp.file.title %> " , scope: "all"})
> ```

> [!CAUTION] Due Tasks for Today 🧨
> 
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/tasks", {type: "due", onDate: "<% tp.file.title %> " , scope: "all"})
> ```

> [!TIP] Scheduled Tasks for Today 🔥
> 
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/tasks", {type: "scheduled", onDate: "<% tp.file.title %> " , scope: "all"})
> ```

> [!TODO] Ongoing Tasks 🏃‍♂️
> 
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/tasks", {type: "ongoing", onDate:"<% tp.file.title %> ", scope: "all"})
> ```

> [!EXAMPLE]- Due Tasks (This week) 📅
> 
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/tasks", {type: "due", onDate: "<% tp.file.title %> ", forceFormat: "isoWeek", scope: "all"})
> ```

---

# 2. Reflect

> [!SUMMARY]+ Keep track of your end goals 🎯
> - Don't forget the objectives you have set for yourself, the goals that need to be accomplished, and the projects that need to be completed.

## 1. What Did I Accomplish Today?

- 

## 2. What Am I Grateful for Today?

- 

## 3. What Was Challenging Today?

- 

## 4. What Am I Most Nervous about Tomorrow?

-

## 5. What Am I Most Excited about Tomorrow?

- 

## Goals

> [!TIP] Ongoing Goals 📅
> 
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/goals", {type: "ongoing"})
> ```

## Projects

> [!TIP] Ongoing Projects 📅
> 
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/projects", {type: "ongoing"})
> ```

## Tasks

> [!EXAMPLE]- Upcoming Tasks (3 days) 🗓️
> 
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/tasks", {type: "upcoming", onDate: "<% tp.file.title %> " , scope: "all"})
> ```

> [!SUCCESS]- Tasks Done ✅
> 
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/tasks", {type: "completed", onDate: "<% tp.file.title %> ", scope: "all"})
> ```

---

# 3. Quick Capture

> [!NOTE] Notes created today 🔗
> 
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/links", {type:"notes"})
> ```

> [!NOTE] Notes updated today ✏️
> 
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/links", {type:"notes-updated", onDate: "<% tp.file.title %> "})
> ```