<%*
const language = await tp.system.suggester([
'Python', 
'C#', 
'JavaScript', 
'CSS', 
'HTML'], 
['python', 'c#', 'js', 'css', 'html'], true, 
'Select language for Syntaxhighlighting.');

const title = await tp.system.prompt('Titel:', '', true);
const hl = await tp.system.prompt('Highlight Lines:', '', true);
const ln = await tp.system.prompt('Linenumbers:', '', true);
const code = await tp.system.prompt('Code (New line -> Shift + Enter):', '', true, true);
-%>

```<%* tR += language %> title="<%* tR += title %>" {<%* tR += hl %>} ln:<%* tR += ln %>
<%* tR += code %>
```


