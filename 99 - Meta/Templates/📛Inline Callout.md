<%*

const callouts = {
    'FlQuestion':       '🔵 ❓ Question', 
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

const type = await tp.system.suggester(Object.values(callouts), Object.keys(callouts), true, 'Select callout type.');

const markdown = `- :${type}: `;

tR += markdown 

-%>