---
status: ongoing
priority:
goal: "[[]]"
deadline:
completed:
created: '2023-10-31'
modified: 2024-03-26 - 10:30 am
Erstellt am: Dienstag, 📅13. August 2024, 🕐23:10:27
Geändert am: Dienstag, 📅13. August 2024, 🕐23:19:05
---
---

# Overview

> [!SUMMARY]+ Project Overview and Outcomes 🙋
> %%OVERVIEW%%
> 
> **Outcome:** %%OUTCOME%%

> [!QUESTION]+ Tasks Completion 🚧
> 
> ```dataviewjs
> await dv.view('JavaScript/Dataview/views/progress-bar', {type: "completed-tasks"})
> ```

---

# Tasks

> [!TODO] Remaining Tasks ✔️
> 
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/tasks", {type: "remaining"})
> ```

```dataviewjs
await dv.view("JavaScript/Dataview/views/button", {command: "add-task", attachedPagePath: "00 - Para/01 - Projects/Syst.md" })
```

> [!SUCCESS]- Tasks Done ✅
> 
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/tasks", {type: "all-completed"})
> ```

> [!EXAMPLE] All Tasks 📝 <js-todo-callout></js-todo-callout>

- [ ] Do laundry [created:: 2024-08-13] [scheduled:: 2024-08-21] [due:: 2024-08-23]

---

# Notes & References

> [!NOTE] Links 🔗
> 
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/links", {type:"notes"})
> ```

```dataviewjs
await dv.view("JavaScript/Dataview/views/button", {command: "add-note", attachedPagePath: "00 - Para/01 - Projects/Syst.md" })
```
