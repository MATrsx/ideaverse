---
created: '2023-10-31'
modified: 2024-05-12 - 05:24 pm
---

---

# Overview

> [!SUMMARY]+ Area Overview 🙋
> --- Overview of your area ---

---

# Tasks

> [!TODO] Remaining Tasks ✔️
>
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/tasks", {type: "remaining"})
> ```

> [!SUCCESS]- Tasks Done ✅
>
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/tasks", {type: "completed"})
> ```

> [!EXAMPLE] All Tasks 📝 <js-todo-callout></js-todo-callout>

---

# Linked Goals & Resources

> [!NOTE] Linked Goals 🎯
>
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/links", {type:"goals"})
> ```

```dataviewjs
await dv.view("JavaScript/Dataview/views/button", {command: "add-goal", attachedPagePath: "<% tp.file.path(true) %>" })
```

> [!NOTE] Linked Notes 🔗
>
> ```dataviewjs
> await dv.view("JavaScript/Dataview/views/links", {type:"notes"})
> ```

```dataviewjs
await dv.view("JavaScript/Dataview/views/button", {command: "add-note", attachedPagePath: "<% tp.file.path(true) %>" })
```
