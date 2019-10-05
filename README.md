# Proyecto: Consumo de alcohol en Europa (2014)
Frecuencia de consumo de alcohol por sexo, edad y país europeo en 2014.

## Descripción:
En este proyecto se trata con un dataset que contiene la frecuencia de consumo de alcohol en los diferentes países de Europa (2014), desglosados por frecuencia (diaria, semanal y mensual), sexo, edad y país.

Frecuencia de consumo de alcohol: distribución de la población ligada la frecuencia de consumo de alcohol.

## Fuente:
Los datos estadísticos reportadas en este proyecto provienen de la segunda ola de encuestas de  European Health Interview Survey (EHIS), realizada entre 2013 y 2015, y que abarca a personas de 15 años o más.

Enlace: https://ec.europa.eu/eurostat/cache/metadata/en/hlth_det_esms.htm

## Limitaciones:
De acuerdo con las especificaciones descritas por European Health Interview Survey (EHIS, segunda ola de encuestas):
"Manual metodológico, se supone que una bebida estándar contiene 10gr de alcohol. Sin embargo, cada país tiene su propia definición de bebida estándar que se adhiere a las normas emitidas por el gobierno y, por lo tanto, esto varía. Los datos se estandarizan para lograr la comparabilidad entre países."

## Leyenda:
Sex:
- F: Female
- M: Male

Age:
- Y15-24: Entre 15 y 24 años
- Y25-34: Entre 25 y 34 años
- Y35-44: Entre 35 y 44 años
- Y45-64: Entre 45 y 64 años
- Y65-74: Entre 65 y 74 años
- Y75+: Más de 75 años

## Etiquetas*:
Códigos que señalan casuísticas específicas de un dato estadístico, se utilizan con fines aclaratorios:
- "u": Low reliability
- "e": Estimated

*Estas han sido borradas en el csv tratado (BBDD.csv).

# Archivos del repositorio:
- Input/alcohol_consumption.tsv: csv original
- Output/BBDD.csv: csv tratado y usado en Tableau
- JupyterNotebook.ipynb: código
- README.md : Descripción del proyecto
