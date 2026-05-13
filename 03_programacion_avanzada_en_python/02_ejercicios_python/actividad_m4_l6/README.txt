=========================================================
ENTREGABLE: LECTURA Y ESCRITURA DE ARCHIVOS
=========================================================

1. ¿Qué diferencia notaste entre write() y append()?
La diferencia radica en la manipulación del puntero y la integridad de los datos previos. El modo escritura ('w') sobrescribe el archivo; trunca la información existente a cero bytes antes de inyectar el nuevo contenido. El modo adición ('a' o append) posiciona el puntero al final del documento, preservando la información histórica y permitiendo concatenar los nuevos registros.

2. ¿Qué ventaja tiene usar with open(...) frente a abrir y cerrar manualmente?
El uso de la instrucción 'with' activa el protocolo de Administradores de Contexto de Python. Su ventaja estructural es que garantiza la liberación automática del archivo en memoria una vez finalizado el bloque de código indentado, incluso si el proceso sufre un colapso (excepción) inesperado durante la lectura o escritura. Esto elimina el riesgo de secuestro de recursos y la fuga de memoria asociada al olvido humano del método .close() en operaciones manuales.