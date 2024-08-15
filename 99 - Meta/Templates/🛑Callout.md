<%*

const callouts = {

    note:       '🔵 ✏ Note', 
    info:       '🔵 ℹ️ Info',  
    todo:       '🔵 🔳 Todo', 
    tip:        '🌐 🔥 Tip / Hint / Important',   
    abstract:   '🌐 📋 Abstract / Summary / TLDR',    
    question:   '🟡 ❓ Question / Help / FAQ',    
    quote:      '🔘 💬 Quote / Cite', 
    example:    '🟣 📑 Example',  
    success:    '🟢 ✅ Success / Check / Done',   
    warning:    '🟠 ⚠️ Warning / Caution / Attention',    
    failure:    '🔴 ❌ Failure / Fail / Missing', 
    danger:     '🔴 ⚡ Danger / Error',   
    bug:        '🔴 🐞 Bug',
    calendar:   '🟣 📅 Calendar / Month',
    globe:      '🟣 🌐 Globe / Earth / World',
    industry:   '🟣 🏭 Industry / Company / Factory',
    network:    '🟣 🛜 Network / Wifi',
    orbit:      '🟣 🛰️ Orbit / Satelite',
    video:      '🟣 🎞️ Video',
    blocks:     '🌐 🗒️ Block',
    map :       '🌐 🗺️ Map',
    radar :     '🌐 🔭 Radar',
    rocket:     '🌐 🚀 Rocket / Start',
    planet:     '🌐 🌍 Planet / Earth',
    user:       '🌐 👤 User / Person',
    book:       '🟠 📖 Book',
    boxes:      '🟠 📦 Boxes',
    castleo:    '🟠 🏰 Castleo',
    compass:    '🟠 🧭 Compass',
    shell :     '🟠 🧑‍💻 Shell / Input',
    combine:    '🟡 ➕ Combine',
    connect:    '🟡 ➿ Connect',
    puzzle:     '🟡 🧩 Puzzle',
    sparkles:   '🟡 ✨ Sparkles',
    sun:        '🟡 ☀️ Sun',
    box:        '🔘 📦 Box',
    command:    '🔘 〰️ Command',
    cross:      '🔘 ❌ Cross / X',
    link:       '🔘 🔗 Link',
    notes:      '🔘 🗒️ Notes',
    script:     '🔘 📒 Script',
    activity:   '🩷 📈 Activity',
    joystick:   '🩷 🕹️ Joystick / Gaming',
    milestone:  '🩷 #️⃣ Milestone',
    rainbow:    '🩷 🌈 Rainbow',
    tower:      '🩷 🗼Tower',
    camera:     '🩵 📷 Camera',
    castle:     '🩵 🏰 Castle',
    combo:      '🩵 💥Combo',
    play:       '🩵 ▶️ Play / Start / Resume',
    recycle:    '🩵 ♻️ Recycle',
    bike:       '🟢 🚲 Bike',
    contact:    '🟢 💬 Contact / Chat',
    leaf:       '🟢 🍂 Leaf',
    sprout:     '🟢 🌴 Sprout',
    train:      '🟢 🚄 Train',
    training:   '🟢 🎯 Training',
    trees:      '🟢 🌳 Trees / Forest',
    anchor:     '🔵 ⚓ Anchor',
    locate:     '🔵 📍 Locate / Marker / Pin',
    parking:    '🔵 🅿️ Parking',
    sailboat:   '🔵 ⛵ Sailboat',
    ship:       '🔵 🚢 Boat',
    shipwheel:  '🔵 🔆 Shipwheel',
    snowflake:  '🔵 ❄️ Snowflake',
    award:      '🔴 🏆 Award',
    cone:       '🔴 ⚠️ Pylone',
    fingerprint:'🔴 🐾 Fingerprint',
    watch:      '🔴 ⌚ Watch'
};

const type = await tp.system.suggester(Object.values(callouts), Object.keys(callouts), true, 'Select callout type.');

const fold = await tp.system.suggester(['None', 'Expanded', 'Collapsed'], ['', '+', '-'], true, 'Select callout fold option.');

let floating = await tp.system.suggester(['None', '👈Float left', '👉Float right'], ['', 'float-left', 'float-right'], true, 'Select floating option:');

if (floating) {
	floating += await tp.system.suggester(['Fit content (default)', '⬛⬛◼️◽⬜⬜⬜⬜⬜⬜⬜ 25%', '⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜ 40%', '⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜ 50%', '⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜ 60%', '⬛⬛⬛⬛⬛⬛⬛◼️◽⬜⬜ 75%'], ['', '-25', '-40', '-50', '-60', '-75'], true, 'Select Callout size option:');
}

const title = await tp.system.prompt('Title:', '', true);

let content = await tp.system.prompt('Content (New line -> Shift + Enter):', '', true, true);

content = content.split('\n').map(line => `> ${line}`).join('\n')

const calloutHead = `> [!${type}|${floating}]${fold} ${title}\n`;

tR += calloutHead + content

-%>