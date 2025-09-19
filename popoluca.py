import yaml
import re

# Forzar listas en línea
class FlowListDumper(yaml.SafeDumper):
    def represent_list(self, data):
        return yaml.representer.SafeRepresenter.represent_sequence(
            self, 'tag:yaml.org,2002:seq', data, flow_style=True
        )

def represent_str(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='')

FlowListDumper.add_representer(str, represent_str)

def parse_popoluca_entry(entry_text):
    entries_dict = {}

    # Separar encabezado (antes del primer punto)
    header_match = re.match(r"^\s*(\S+)\s+(\S+)\.\s+([^.]+)\.", entry_text)
    if not header_match:
        print("No se pudo analizar el encabezado.")
        return {}

    entry, pos, es_translation = header_match.groups()
    es_translation = es_translation.strip()

    # Extraer oraciones + traducciones
    examples = re.findall(r"\.?\s*([^‘’]+?)\.?\s*‘([^’]+)’", entry_text)

    sense_list = [{"es_translation": es_translation}]
    for idx, (example, translation) in enumerate(examples, 1):
        sense_list.append({
            "example": example.strip(),
            "soundFile": f"http://localhost:8000/audio/POPOLUCA/{entry.lower()}" + (".mp3" if idx == 1 else f"{idx}.mp3"),
            "es_exampleTranslation": translation.strip()
        })

    entries_dict[entry] = {
        "audio": f"http://localhost:8000/audio/POPOLUCA/{entry.lower()}.mp3",
        "PartOfSpeech": pos,
        "sense": sense_list
    }

    return entries_dict

def generate_popoluca_yaml(text):
    entries_dict = parse_popoluca_entry(text)
    with open("C:/Users/personal/Desktop/Diccionarios/popoluca_output.yaml", "w", encoding="utf-8") as file:
        yaml.dump(entries_dict, file, allow_unicode=True, sort_keys=False, Dumper=FlowListDumper)

# Entrada de ejemplo
entrada_popoluca = """aañi   st.   Tortilla. Yɨ’p aañi agi pijpa. ‘Esta tortilla está muy caliente’; Soonaayɨ yɨ’p aañi jem yooya ikudyiñ. ‘Remójale estas tortillas al puerco para que se las coma’."""

generate_popoluca_yaml(entrada_popoluca)




#C:/Users/personal/Desktop/Diccionarios/popoluca_output.yaml
