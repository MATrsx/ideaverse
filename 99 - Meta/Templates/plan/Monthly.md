---
created: '2024-08-11'
modified: 2024-04-11 - 01:51 pm
---
⏮️ [[0-plan/5-yearly/Invalid date|Yearly]] > [[0-plan/4-quarterly/Invalid date|Quarterly]] ⏭️

⬅️ [[Invalid date|Invalid date]] < Invalid date > [[Invalid date|Invalid date]] ➡️

---

# 1. Close Last Month

## Collect

> [!SUMMARY]+ Declutter Your Space 🧘
> - Compile any data you have from tracking apps
> - Tidy up your desk, file away documents, and organize office supplies
> - Review finances and keep track of spending/incomes
> - Review bookmarked websites and see if I find some irrelevant
> - Close your weekly review

## Process

> [!SUMMARY]+ Process Unfinished Things 🔁
> - Extract any key points or actions from this past month

---

# 2. Reflect and Review

> [!SUMMARY]+ Reflect on this past month 👁️‍🗨️
> - Look at everything you have achieved this month (completed goals, projects, and more). 
> - Review each area of your life.
> - With all of that in mind, answer the questions below.

> [!SUCCESS] Goals Done (This Month) 🎯
> 
> ```dataviewjs
> await dv.view("scripts/dataview/views/goals", {type: "completed", onDate: "🛑Callout ", scope: "all"})
> ```

> [!SUCCESS] Projects Done (This Month) 💼
> 
> ```dataviewjs
> await dv.view("scripts/dataview/views/projects", {type: "completed", onDate: "🛑Callout ", scope: "all"})
> ```

## 1. Review Each Area of Your Life

> [!LIST] All Areas 📥
> 
> ```dataviewjs
> dv.view("scripts/dataview/views/areas", {type:"all"})
> ```

## 1. What New Skills Did You Acquire or Which Existing Skills Did You Enhance?
-   
## 2. What Prevented You from Accomplishing Certain Tasks or Goals?
- 
## 3. Was there Any Wastage that Could Be Reduced next Time? 
- 
## 4. Think about the Activities that Recharged You and Those that Drained You:
- 

---

# 3. Plan

> [!SUMMARY]+ Time to plan your next moves for your goals and projects 👀
> - Plan and update goals you must accomplish this upcoming month in accordance with your quarterly and yearly goals.
> - Review on hold goals if needed.
> - According to your new goals for the upcoming month, plan and update projects.

## Goals

> [!TIP] Ongoing Goals 📅
> 
> ```dataviewjs
> await dv.view("scripts/dataview/views/goals", {type: "ongoing", onDate: "🛑Callout "})
> ```

> [!SUMMARY] On hold Goals 📅
> 
> ```dataviewjs
> await dv.view("scripts/dataview/views/goals", {type: "on-hold", onDate: "🛑Callout "})
> ```

```dataviewjs
await dv.view("scripts/dataview/views/button", {command: "add-goal"})
```

## Projects

> [!TIP] Ongoing Projects 📅
> 
> ```dataviewjs
> await dv.view("scripts/dataview/views/projects", {type: "ongoing"})
> ```

```dataviewjs
await dv.view("scripts/dataview/views/button", {command: "add-project"})
```