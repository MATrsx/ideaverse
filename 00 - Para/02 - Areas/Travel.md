---
created: '2024-04-01'
modified: 2024-06-15 - 03:13 pm
---

---

# Overview

> [!SUMMARY]+ Area Overview 🙋
> Everything related to my past and future travels.

---

# Tasks

> [!TODO] Remaining Tasks ✔️
> 
> ```dataviewjs
> await dv.view("scripts/dataview/views/tasks", {type: "remaining"})
> ```

> [!EXAMPLE] All Tasks 📝 <js-todo-callout></js-todo-callout>

---

# Linked Goals & Resources

> [!NOTE] Linked Goals 🎯
> 
> ```dataviewjs
> await dv.view("scripts/dataview/views/links", {type:"goals"})
> ```

> [!NOTE] Linked Notes 🔗
> 
> ```dataviewjs
> await dv.view("scripts/dataview/views/links", {type:"notes"})
> ```

```dataviewjs
await dv.view("scripts/dataview/views/button", {command: "add-goal"})
```