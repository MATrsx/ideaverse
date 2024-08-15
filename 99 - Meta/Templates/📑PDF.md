<%*
const vaultPDFs = app.vault.getFiles().filter(file => file.extension === 'pdf');
const pdfNames = vaultPDFs.map(file => file.name);

const selectedPDF = await tp.system.suggester((item) => item, pdfNames, true, 'Select PDF File from Vault:');

const callout = await tp.system.suggester(['🔳Embed in Callout', '🔲No embed'], ['active', ''], true, 'Select Callout:');
const float = await tp.system.suggester(['None', '👉Float right', '👈Float left'], ['', 'float-right', 'float-left'], true, 'Select Float:');
const width = await tp.system.suggester(['Fit Content (default)', '🔲Small (300px)', '🔲Medium (400px)', '🔲Large (600px)'], ['', '-small', '-medium', '-large'], true, 'Select Callout:');
const height = await tp.system.prompt('Enter height (leave empty for default):');

let pdfMarkdown = `![[${selectedPDF}`;
let pdfMarkdown_float = "";
let calloutHead = `> [!text-file`;

if (float !== '') {
	pdfMarkdown_float = `|${float}`
	calloutHead += `|${float}`
}
if (width !== '') {
    calloutHead += `${width}`;
}

if (height !== '') {
    pdfMarkdown += `#height=${height}`;
}

pdfMarkdown += pdfMarkdown_float +']]';

if (callout !== '') {
	calloutHead += `]+ Image - ${selectedPDF} \n`;
} else {
	calloutHead = ''
}

tR += calloutHead + pdfMarkdown;
%>