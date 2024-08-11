---
created: '2024-08-11'
modified: 2024-04-11 - 01:51 pm
---
⏮️ [[0-plan/5-yearly/Invalid date|Yearly]] ⏭️

⬅️ [[Invalid date|Invalid date]] < Invalid date > [[Invalid date|Invalid date]] ➡️

---

**(undefined NaN ~ undefined NaN)**

---

# 1. Close This Quarter

## Collect

> [!SUMMARY]+ Collect Last Bits 📦
> - Check any new habits acquired
> - Clean up, save or archive your "Read It Later"
> - Close your monthly and weekly review

## Process

> [!SUMMARY]+ Process Last Chunks 📬
> - Set any new habits that should be acquired or strengthened
> - Think about next holidays and plan if needed

---

# 2. Reflect and Review

> [!SUMMARY]+ Reflect on this past quarter 👁️‍🗨️
> - Look at everything you have achieved this quarter (completed goals, projects, and more) and with all of that in mind, answer the questions below.

> [!SUCCESS] Goals Done (This Quarter) 🎯
> 
> ```dataviewjs
> await dv.view("scripts/dataview/views/goals", {type: "completed", onDate: "🛑Callout " , scope: "all"})
> ```

> [!SUCCESS] Projects Done (This Quarter) 💼
> 
> ```dataviewjs
> await dv.view("scripts/dataview/views/projects", {type: "completed", onDate: "🛑Callout " , scope: "all"})
> ```

## 1. How Have Your Long-term Goals or Vision Shifted Based on This Quarter's Insights?

- 

## 2. How Has Your Network or Relationship Grown or Evolved This Quarter?

- 

## 3. What Lessons Have You Learned This Quarter that Could Influence Future Decision-Making?

- 

## 4. How Consistently Have You Applied Your Productivity and Organization Systems This Quarter?

- 

## 5. What Are the Emerging Trends or Opportunities that You Could Capitalize On? (Business-wise)

- 

---

# 3. Plan

> [!SUMMARY]+ Time to plan your next moves for your goals and projects 👀
> - Plan and update your goals according to your yearly goals.
> - Review on hold goals if needed.
> - According to your new goals for the upcoming quarter, plan and update projects.

## Goals

> [!TIP] Ongoing Goals 📅
> 
> ```dataviewjs
> await dv.view("scripts/dataview/views/goals", {type: "ongoing"})
> ```

> [!SUMMARY] On hold Goals 📅
> 
> ```dataviewjs
> await dv.view("scripts/dataview/views/goals", {type: "on-hold"})
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

> [!SUMMARY] On Hold Projects 📅
> 
> ```dataviewjs
> await dv.view("scripts/dataview/views/projects", {type: "on-hold"})
> ```

```dataviewjs
await dv.view("scripts/dataview/views/button", {command: "add-project"})
```