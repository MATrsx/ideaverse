<%*
const title = await tp.system.prompt('Title:', '', true);
let content = await tp.system.prompt('Content (New line -> Shift + Enter):', '', true, true);
const fold = await tp.system.suggester(['open', 'closed'], ['open', ''], true, 'Select Dropdown fold option.');
-%>

<details <%* tR += fold %>>
<summary><%* tR += title %></summary>
<br>
<%* tR += content %>
</details>