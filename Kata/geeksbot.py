import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Activar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def start(update, context):
    """Envia un mensaje cuando se emita el comando /start."""
    update.message.reply_text('Hola, Geeks!')


def help(update, context):
    """Envia un mensaje cuando se emita el comando /help."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Repite el mensaje del usuario."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Envia los errores por consola"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def pizza(update, context):
    if(update.message.text.upper().find("MANZANAS VERDES") > 0):
        update.message.reply_text("Prefiero comer pizza")

def sumar(update,context):
    try:
        numero1 = int(context.args[0])
        numero2 = int(context.args[1])

        suma = numero1 + numero2

        update.message.reply_text("La suma es "+str(suma))

    except (ValueError):
        update.message.reply_text("por favor utilice dos numeros")

def main():
    """Inicio del Bot"""

    #Colocamos el Token creado por FatherBot
    updater = Updater("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", use_context=True)

    # Es el Registro de Comandos
    dp = updater.dispatcher

    # Añadimos a la lista de Registro todos los comandos con su función
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("sumar", sumar))

    # Este comando es un Trigger.
    dp.add_handler(MessageHandler(Filters.text, pizza))

    # Y este espera al error
    dp.add_error_handler(error)

    # Lanzamos el Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()