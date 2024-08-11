---
created: '🛑Callout'
modified: 2024-06-11 - 06:58 pm
---

⏮️[[0-plan/5-yearly/Invalid date|Yearly]] > [[0-plan/4-quarterly/Invalid date|Quarterly]] > [[0-plan/3-monthly/Invalid date|Monthly]] > [[0-plan/2-weekly/Invalid date|Weekly]]⏭️
 
⬅️[[Invalid date|Invalid date]] < Invalid date > [[Invalid date|Invalid date]]➡️

---

**Invalid date of Week NaN, Invalid date**

****

# 1. Take Actions

## Tasks

> [!MISSING] Overdue Tasks 🚨
> 
> ```dataviewjs
> await dv.view("scripts/dataview/views/tasks", {type: "overdue", onDate: "🛑Callout " , scope: "all"})
> ```

> [!CAUTION] Due Tasks for Today 🧨
> 
> ```dataviewjs
> await dv.view("scripts/dataview/views/tasks", {type: "due", onDate: "🛑Callout " , scope: "all"})
> ```

> [!TIP] Scheduled Tasks for Today 🔥
> 
> ```dataviewjs
> await dv.view("scripts/dataview/views/tasks", {type: "scheduled", onDate: "🛑Callout " , scope: "all"})
> ```

> [!TODO] Ongoing Tasks 🏃‍♂️
> 
> ```dataviewjs
> await dv.view("scripts/dataview/views/tasks", {type: "ongoing", onDate:"🛑Callout ", scope: "all"})
> ```

> [!EXAMPLE]- Due Tasks (This week) 📅
> 
> ```dataviewjs
> await dv.view("scripts/dataview/views/tasks", {type: "due", onDate: "🛑Callout ", forceFormat: "isoWeek", scope: "all"})
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
> await dv.view("scripts/dataview/views/goals", {type: "ongoing"})
> ```

## Projects

> [!TIP] Ongoing Projects 📅
> 
> ```dataviewjs
> await dv.view("scripts/dataview/views/projects", {type: "ongoing"})
> ```

## Tasks

> [!EXAMPLE]- Upcoming Tasks (3 days) 🗓️
> 
> ```dataviewjs
> await dv.view("scripts/dataview/views/tasks", {type: "upcoming", onDate: "🛑Callout " , scope: "all"})
> ```

> [!SUCCESS]- Tasks Done ✅
> 
> ```dataviewjs
> await dv.view("scripts/dataview/views/tasks", {type: "completed", onDate: "🛑Callout ", scope: "all"})
> ```

---

# 3. Quick Capture

> [!NOTE] Notes created today 🔗
> 
> ```dataviewjs
> await dv.view("scripts/dataview/views/links", {type:"notes"})
> ```

> [!NOTE] Notes updated today ✏️
> 
> ```dataviewjs
> await dv.view("scripts/dataview/views/links", {type:"notes-updated", onDate: "🛑Callout "})
> ```