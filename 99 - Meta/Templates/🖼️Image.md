<%*
const vaultImages = app.vault.getFiles().filter(file => file.extension === 'png' || file.extension === 'jpg');
const imageNames = vaultImages.map(file => file.name);

const selectedImage = await tp.system.suggester((item) => item, imageNames, true, 'Select image from Vault:');

const callout = await tp.system.suggester(['🔳Embed in Callout', '🔲No embed'], ['active', ''], true, 'Select Callout:');
const float = await tp.system.suggester(['None', '👉Float right', '👈Float left'], ['', 'float-right', 'float-left'], true, 'Select Float:');
const width = await tp.system.prompt('Enter width (leave empty for default):');
const height = await tp.system.prompt('Enter height (leave empty for default):');

let imageMarkdown = `![[${selectedImage}`;
let calloutHead = `> [!image`;

if (float !== '') {
	imageMarkdown += `|${float}`
	calloutHead += `|${float}`
}
if (width !== '') {
    imageMarkdown += `|${width}`;
}

if (height !== '') {
	if (width !== '') {
	    imageMarkdown += `x`;
	}
    imageMarkdown += `${height}`;
}

imageMarkdown += ']]';

if (callout !== '') {
	calloutHead += `]+ Image - ${selectedImage} \n`;
} else {
	calloutHead = ''
}

tR += calloutHead + imageMarkdown;
%>
