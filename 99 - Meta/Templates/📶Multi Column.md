<%*
const types = {
    'callout':          '🔵 ❓ Callout', 
    'FlInfo':           '🔵 ℹ️ Info',  
    'FlBookmark':       '🔵 🔖 Bookmark', 
    'FlTranslate':      '🌐 💬 Language',       
    'FlBulb':           '🟡 💡 Idea / Tip',
    'FlAdvertising':    '🟡 📢 Shoutout',
    'FlFavourites':     '🟡 ⭐ Favourite',   
    'FlLocation':       '🔴 📍 Location', 
    'FlWarning':        '🔴 ⚠️ Danger / Error',   
    'FlHashtag':        '🔴 #️⃣ Topic / Tag',
    'Fl3dFire':         '🔴 🔥 Hot / Important',
    'FlPaperClip':      '🟣 📎 File / Attachment',
    'FlLink':           '🟣 🔗 Link / Website',
};

const numColumns = await tp.system.prompt("Wie viele Spalten sollen erstellt werden?");

const type = await tp.system.suggester(Object.values(types), Object.keys(types), true, 'Select callout type.');

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