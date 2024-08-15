---
created: '<% tp.file.creation_date("YYYY-MM-DD") %>'
modified: 2024-05-30 - 11:04 am
---

⏮️ <% tp.user.weeklyZoomOutRibbon(tp.file.title) %> ⏭️

⬅️ <% tp.user.weeklyNextPrevRibbon(tp.file.title) %> ➡️

---

<% tp.user.weeklyDateInfo(tp.file.title) %>

---

# 1. Close Past Week

## Tidy Up

> [!SUMMARY]+ Declutter Your Space 🧘
> - Clear all notifications
> - Close all browsers tabs
> - Empty mail box
> - review calendar
> - Clean Desktop and Downloads
> —
> - Breath
> —
> - Have a look at your overdue and remaining tasks for this week. Why did you not finish them? What is blocking you?
> - Plan as many "unscheduled" tasks as possible so you can keep track of what you are doing and maintain a low level of chaos.

> [!MISSING] Remaining & Overdue Tasks (This Week) 🧨
> 
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/tasks", {type: "remaining", onDate: "<% tp.file.title %> " , scope: "all"})
> ```

> [!EXAMPLE] Clean Unplanned Actions 📨
> 
> ```dataviewjs
> dv.view("JavaScript/Dataview/views/tasks", {type: "unplanned", onDate: "<% tp.file.title %> ", scope: "all"})
> ``` 

## Process

> [!SUMMARY]+ Process Unfinished Things 🔁
> It's time to sort all your unassigned weekly notes (notes without a linked page), take a closer look, and clean or archive them if not needed.

> [!SUMMARY] Sort Captured Notes 📝
> 
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/notes", {type: "unsorted"})
> ```

---

# 2. Reflect and Review

> [!SUMMARY]+ Reflect on this past week 👁️‍🗨️
> - Look at everything you have achieved this week (completed goals, projects, and more) and with all of that in mind, answer the questions below.

> [!SUCCESS] Goals Done (This Week) 🎯
> 
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/goals", {type: "completed", onDate: "<% tp.file.title %> "})
> ```

> [!SUCCESS] Projects Done (This Week) 💼
> 
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/projects", {type: "completed", onDate: "<% tp.file.title %> "})
> ```

> [!SUCCESS]- Tasks Done (This Week) ✅
> 
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/tasks", {type: "completed", onDate: "<% tp.file.title %> ", scope: "all"})
> ```

## 1. What More Did I Accomplish This Week?

- 

## 2. What Am I Grateful for This Week?

-  

## 3. What Did Not Go Well This Week?

- 

## 4. How Can I Improve Next Week?

- 

## 5. How Can I Get out of My Comfort Zone Next Week?

- 

---

# 3. Plan

> [!SUMMARY]+ Time to plan your next moves for your goals and projects 👀
> - Plan and update goals you must accomplish this upcoming week in accordance with your monthly goals.
> - According to your new goals for the upcoming week, plan and update projects, create new tasks.

## Goals

> [!TIP] Ongoing Goals 📅
> 
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/goals", {type: "ongoing", onDate: "<% tp.file.title %> "})
> ```

```dataviewjs
await dv.view("JavaScript/Dataview/views/button", {command: "add-goal"})
```

## Projects

> [!TIP] Ongoing Projects 📅
> 
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/projects", {type: "ongoing"})
> ```

```dataviewjs
await dv.view("JavaScript/Dataview/views/button", {command: "add-project"})
```

## Tasks

> [!DANGER] Due Tasks (Next Week) ✔️
> 
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/tasks", {type: "due", onDate: "<% tp.user.dateUtils({date: tp.file.title, action: "get-next-week"}) %> " , scope: "all"})
> ```

> [!TODO] Ongoing Tasks 🏃‍♂️
> 
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/tasks", {type: "ongoing", onDate: "<% tp.file.title %> ", scope: "all"})
> ```

```dataviewjs
await dv.view("JavaScript/Dataview/views/button", {command: "add-task"})
```
