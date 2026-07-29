from ouigo import Ouigo
from telegram_bot import enviar_mensaje

print("Iniciando bot...")

o = Ouigo()

try:
    o.abrir()
    print("✓ Web abierta")

    o.seleccionar_origen_destino()
    print("✓ Origen y destino seleccionados")

    o.abrir_calendario()
    print("✓ Calendario abierto")

    o.captura()
    print("✓ Captura realizada")

    enviar_mensaje("✅ El bot de OUIGO está funcionando correctamente.")

finally:
    o.cerrar()
