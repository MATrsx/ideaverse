<%*
let numTabs;
while (true) {
  const numTabsInput = await tp.system.prompt("Wie viele Tabs möchten Sie erstellen?");
  numTabs = parseInt(numTabsInput);

  if (!isNaN(numTabs)) {
    break;
  } else {
    new Notice("Fehler: Bitte geben Sie eine gültige Zahl ein.");
  }
}

let tabsContent = "~~~tabs\n";

for (let i = 1; i <= numTabs; i++) {
  const tabLabel = await tp.system.prompt(`Geben Sie den Titel für Tab ${i} ein:`);
  const tabContent = await tp.system.prompt(`Geben Sie den Inhalt für Tab ${i} ein:`);
  tabsContent += `---tab ${tabLabel}\n${tabContent}\n`;
}

tabsContent += "~~~";
tR += tabsContent;
%>