# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:27:32 2023

@author: User
"""

def checksum(data):
    """
    Calcula la suma de verificación (checksum) de un conjunto de bytes.
    """
    checksum_value = 0
    for byte in data:
        checksum_value += byte
    return checksum_value & 0xFF  # Asegura que el resultado esté en el rango 0-255 (8 bits).

# Ejemplo de uso:
data = [0x10, 0x20, 0x30, 0x40, 0x50]  # Datos de ejemplo representados como bytes.
result = checksum(data)
print(f"Checksum: {result}")
#Este código toma una lista de bytes como entrada y calcula la suma de verificación como la suma de todos los bytes en el conjunto de datos. Luego, se aplica una máscara para asegurarse de que el resultado esté limitado a 8 bits (0-255).

#Ten en cuenta que este es un ejemplo simple de checksum y no es adecuado para aplicaciones críticas de seguridad, ya que es bastante vulnerable a errores y modificaciones maliciosas. Para aplicaciones más robustas, se suelen utilizar algoritmos de suma de verificación más complejos, como CRC (Cyclic Redundancy Check) o algoritmos de hash criptográficos, como SHA-256.





 