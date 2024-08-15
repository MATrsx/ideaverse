import os
import re
import uuid

def make_ids_unique(svg_content):
    # Regex zum Finden von ID-Definitionen und ID-Verweisen
    id_pattern = r'id="([^"]+)"'
    url_pattern = r'url\(#([^"]+)\)'
    xlink_pattern = r'xlink:href="#([^"]+)"'
    
    # Finden aller IDs
    ids = re.findall(id_pattern, svg_content)
    
    # Dictionary für alte zu neuen IDs
    id_mapping = {}

    for old_id in ids:
        # Generiere eine neue, eindeutige ID
        new_id = f'{uuid.uuid4()}'
        id_mapping[old_id] = new_id
    
    # Ersetzen der alten IDs mit den neuen in ID, URL und xlink:href
    for old_id, new_id in id_mapping.items():
        svg_content = re.sub(f'id="{old_id}"', f'id="{new_id}"', svg_content)
        svg_content = re.sub(f'url\\(#{old_id}\\)', f'url(#{new_id})', svg_content)
        svg_content = re.sub(f'xlink:href="#{old_id}"', f'xlink:href="#{new_id}"', svg_content)
    
    return svg_content

def process_svg_files_in_folder(folder_path):
    # Durchlaufe alle Dateien im angegebenen Ordner
    for filename in os.listdir(folder_path):
        # Überprüfe, ob es sich um eine SVG-Datei handelt
        if filename.lower().endswith(".svg"):
            svg_file_path = os.path.join(folder_path, filename)
            
            # Lade den Inhalt der SVG-Datei
            with open(svg_file_path, 'r', encoding='utf-8') as file:
                svg_content = file.read()

            # IDs einzigartig machen
            new_svg_content = make_ids_unique(svg_content)

            # Neuen Dateinamen generieren, um mögliche Konflikte zu vermeiden
            new_filename = f"{os.path.splitext(filename)[0].lower()}.svg"
            output_file_path = os.path.join(folder_path, new_filename)
            
            # Die bearbeitete SVG-Datei speichern
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(new_svg_content)
            
            print(f'Datei {filename} wurde bearbeitet und als {output_file_path} gespeichert.')

def rename_svgs():
    for filename in os.listdir(folder_path):
        # Überprüfen, ob die Datei eine SVG-Datei ist
        if filename.endswith('.svg'):
            # Neuer Dateiname in Kleinbuchstaben
            new_filename = filename.lower()
            # Vollständige Pfade für die Umbenennung
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_filename)
            # Datei umbenennen
            os.rename(old_file, new_file)

# Beispiel für die Verwendung des Skripts
folder_path = 'C:/Users/milan/Documents/Obsidian Vaults/Ideaverse/.obsidian/icons/save'  # Gebe hier den Pfad zu deinem Ordner an

# Alle SVG-Dateien im Ordner bearbeiten
process_svg_files_in_folder(folder_path)
rename_svgs()
