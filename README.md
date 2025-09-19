# Diccionario-Parlante-Digital-de-Lenguas-Originarias
Repositorio complementario a la tesis de maestría sobre el desarrollo de un diccionario parlante digital para lenguas originarias (Zapoteco, Iskonawa, Popoluca). Incluye scripts, datos de ejemplo y documentación

🎯 Objetivos

Diseñar y validar un prototipo de diccionario digital que integre texto y audio.

Implementar un flujo metodológico replicable con herramientas accesibles (Lexonomy, Python, YAML/XML).

Explorar criterios de ergonomía digital aplicados a diccionarios electrónicos.

Contribuir a la preservación y revitalización de lenguas originarias mediante recursos tecnológicos.

🏗️ Metodología

El proyecto siguió una secuencia metodológica en cinco fases principales:

Revisión documental: análisis de diccionarios impresos y digitales.

Exploración tecnológica: comparación de plataformas (Lexonomy, TLex, Living Dictionaries, entre otras).

Diseño estructural: definición de entradas léxicas, campos y etiquetas.

Automatización: desarrollo de scripts en Python para transformar datos (XML → YAML).

Integración sonora: vinculación de audios a cada entrada.

Los diagramas metodológicos y figuras están disponibles en la carpeta docs/.

📂 Contenido del repositorio
├── README.md                # Descripción general del proyecto
├── LICENSE                  # Licencia del código
├── LICENSE_data.md          # Licencia específica para datos lingüísticos
├── LICENSE_audio.md         # Licencia de audios (consentimiento comunitario)
│
├── tesis/                   # Documentos asociados a la investigación
│   ├── resumen.pdf
│   └── referencias.txt
│
├── data/                    # Datos lingüísticos
│   ├── zapoteco/
│   │   ├── entradas.yaml
│   │   └── ejemplos.xml
│   ├── popoluca/
│   └── iskonawa/
│
├── audio/                   # Archivos de audio (si están autorizados)
│   ├── zapoteco/
│   ├── popoluca/
│   └── iskonawa/
│
├── scripts/                 # Scripts en Python
│   ├── parser_xml_yaml.py
│   ├── carga_lexonomy.py
│   └── validacion.py
│
├── docs/                    # Diagramas y esquemas
│   ├── metodologia.png
│   ├── estructura_entrada_lexica.pdf
│   └── mapa_mental_lexonomy.png
│
└── examples/                # Ejemplos de uso
    ├── entrada_zapoteco.md
    └── consulta.gif

⚖️ Licencias

Código: MIT License

Datos lingüísticos: CC BY-SA 4.0

Audios: CC BY-NC-SA 4.0
 o licencias comunitarias específicas.

🚀 Cómo reproducir el proyecto

Clonar este repositorio:

git clone https://github.com/usuario/diccionario-parlante-lenguas-originarias.git
cd diccionario-parlante-lenguas-originarias


Instalar dependencias en Python (ejemplo con requirements.txt si lo generas).

Ejecutar scripts de transformación:

python scripts/parser_xml_yaml.py
python scripts/carga_lexonomy.py


Revisar resultados en data/ y cargar en Lexonomy.
