<%*

const numColumns = await tp.system.prompt("Wie viele Spalten soll die Tabelle haben?");

let tableHeader = "| ";

let tableSeparator = "| ";

let tableRows = "";

let columnNames = [];

for (let i = 0; i < numColumns; i++) {

        const columnName = await tp.system.prompt(`Name der Spalte ${i + 1}:`);

        columnNames.push(columnName);

        tableHeader += `${columnName} | `;

        tableSeparator += "--- | ";

}

const numRows = await tp.system.prompt("Wie viele Zeilen soll die Tabelle haben?");

let skipAll = false;

for (let i = 0; i < numRows; i++) {

        if (skipAll) {

                break;

        }

        const skipRow = await tp.system.prompt(`Zeile ${i + 1} überspringen? (y/n/all)`);

        if (skipRow.toLowerCase() === "y") {

                continue;

        }

        if (skipRow.toLowerCase() === "all") {

                skipAll = true;

                break;

        }

        let row = "| ";

        for (let j = 0; j < numColumns; j++) {

                const cellContent = await tp.system.prompt(`Inhalt für Zeile ${i + 1} (${columnNames[j]}):`);

                row += `${cellContent} | `;

        }

        tableRows += `${row}\n`;

}

const table = `${tableHeader}\n${tableSeparator}\n${tableRows}`;

tR += table;

%>