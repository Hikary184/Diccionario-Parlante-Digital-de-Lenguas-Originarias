import yaml

def parse_entry(entry_text):
    entries = []
    lines = entry_text.strip().split('\n')
    
    for line in lines:
        # Separamos la línea por el símbolo "|"
        parts = [p.strip() for p in line.split('|')]
        head_part = parts[0]
        additional_data = parts[1:]  # Se espera que sean: [traducción ejemplo ES, traducción ejemplo EN]
        
        # Separamos el primer bloque por espacios
        tokens = head_part.split()
        # Suponiendo el siguiente orden:
        # token0: headword
        # token1: primer pronunciación (ej. [awáʔ])
        # token2: segunda pronunciación (ej. [ʔawáʔ])
        # token3: PartOfSpeech (ej. part.)
        # token4: es_translation (ej. sí.)
        # token5: en_translation (ej. yes.)
        # token6+: texto de ejemplo (ej. Awa, llsedla'be' di'llwrall)
        headword = tokens[0]
        pronunciations = tokens[1:3]
        part_of_speech = tokens[3]
        es_translation = tokens[4]  
        en_translation = tokens[5]
        example_text = " ".join(tokens[6:])  # el resto es el ejemplo
        
        entry = {
            "entry": headword,
            "pronunciation": [{"label": pron} for pron in pronunciations],
            "audio": "link de audio",
            "PartOfSpeech": part_of_speech,
            "sense": [],  
            "sense2": []
        }
        
        # Primer bloque sense: traducciones
        sense_translation = {
            "es_translation": es_translation,
            "en_translation": en_translation
        }
        # Segundo bloque sense: ejemplo
        sense_example = {
            "example": example_text,
            "es_exampleTranslation": additional_data[0] if len(additional_data) > 0 else "",
            "en_exampleTranslation": additional_data[1] if len(additional_data) > 1 else ""
        }
        
        entry["sense"].append(sense_translation)
        entry["sense2"].append(sense_example)
        
        entries.append(entry)
    
    return entries

def generate_yaml(text):
    entries = parse_entry(text)
    with open("C:/Users/personal/Desktop/output.yaml", "w", encoding="utf-8") as file:
        yaml.dump(entries, file, allow_unicode=True, default_flow_style=False, sort_keys=False)

# Ejemplo de entrada de texto
entrada = """bày [bàj] [bàj] s. pañuelo. handkerchief. xhpaya' | mi pañuelo | my handkerchief. 

"""

generate_yaml(entrada)
