---
status: ongoing
priority:
goal: "[[]]"
deadline:
completed:
created: '2023-10-31'
modified: 2024-03-26 - 10:30 am
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
await dv.view("JavaScript/Dataview/views/button", {command: "add-task", attachedPagePath: "<% tp.file.path(true) %>" })
```

> [!SUCCESS]- Tasks Done ✅
>
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/tasks", {type: "all-completed"})
> ```

> [!EXAMPLE] All Tasks 📝 <js-todo-callout></js-todo-callout>

---

# Notes & References

> [!NOTE] Links 🔗
>
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/links", {type:"notes"})
> ```

```dataviewjs
await dv.view("JavaScript/Dataview/views/button", {command: "add-note", attachedPagePath: "<% tp.file.path(true) %>" })
```
