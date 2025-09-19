import yaml

def generar_yaml(entrada):
    # Separar la entrada en partes: palabra y definiciones
    partes = entrada.split('  ')
    palabra = partes[0].strip()
    definiciones = partes[1].split('. ')

    # Asegurarnos de que las definiciones estén bien estructuradas
    if len(definiciones) == 4:
        part_of_speech = definiciones[0].strip()
        es_translation = definiciones[1].strip()
        part_of_speech2 = definiciones[2].strip()
        en_translation = definiciones[3].strip()

        # Datos para el archivo YAML
        data = {
            'entry': palabra,
            'audio': f'http://localhost:8000/audio/ISKONAWA/{palabra}.wav',
            'PartOfSpeech': part_of_speech,
            'sense': {
                'es_translation': es_translation,
                
                'en_translation': en_translation
            }
        }
        
        # Ruta del archivo YAML
        ruta = "C:/Users/personal/Desktop/Diccionarios/iskonawa_output.yaml"
        
        # Crear el archivo YAML
        with open(ruta, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True, default_flow_style=False)
    else:
        print("Error: la entrada no está correctamente formateada.")

# Ejemplo de uso
entrada = "batan nochi  n. ají dulce de tamaño grande. n. sweet pepper of a large size."
generar_yaml(entrada)




#C:/Users/personal/Desktop/Diccionarios/iskonawa_output.yaml