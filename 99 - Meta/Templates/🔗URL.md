<%*
const title = await tp.system.prompt("Gib den Titel des Links ein:");
const url = await tp.system.prompt("Gib die URL ein:");

const markdown = `[${title}](${url})`;
-%>
<% markdown %>