from db import *

def ActuaConfig(): #Actualizar nombre y base del server
    NombreServer = input("Nombre del server: ")
    NombreBase = input("Nombre de la base: ")
    actualizar_config(NombreServer, NombreBase)  # Funcion para actualizar el config

ActuaConfig() #Llama a la función donde se ingresan los datos, a esta función debería apuntar el front, así el front nunca tiene conexión con el verdadero back
conn=conexion() #Función para verificar que todo funciona
