<%*
const numColumns = await tp.system.prompt("Wie viele Karten sollen dargestellt werden?");

let header = `> [!multi-column|left-fixed]\n>\n`;

for (let i = 0; i < numColumns; i++) {

        const heading = await tp.system.prompt(`Überschrift der Karte ${i + 1}:`);
        
	    const vaultImages = app.vault.getFiles().filter(file => file.extension === 'png' || file.extension === 'jpg' || file.extension === 'svg');
		const imageNames = vaultImages.map(file => file.name);
		const selectedImage = await tp.system.suggester((item) => item, imageNames, true, 'Select image from Vault:');

        header += `> > - #### ${heading} #mcl/list-card\n> > ![[${selectedImage}]]\n> >\n`;
}

tR += header;
%>