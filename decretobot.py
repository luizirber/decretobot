#! /usr/bin/env python
# encoding: utf-8

import logging
from random import sample
import os

from telegram.ext import Updater, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


template = """
18:08, horário de Brasília. Já pode:

{frases}

Decreto liberado. Cumpra-se.
"""

permitido = [
"Beber sidra da semana anterior.",
"Emendar com um barril de chope que sobrou porque alguém quis calcular as quantidades da festa com base no próprio consumo.",
"Corote.",
"Catuaba selvagem.",
'Lavar o Landau ao som de "Sessenta dias apaixonado - Chitãozinho e Xororó".',
"Mandar “Deu Onda” pro crush.",
"Reunir as pontas restantes do Réveillon.",
"Pedir e pendurar um quibe de procedência duvidosa como o almoço de sábado.",
"Conversar com o bot do sci-hub em situação de ebriedade.",
"Chegar em casa às 23:39h do domingo e chegar em casa com um corte de cabelo novo que não lembra quando fez."
]


def decretar(bot, update):
    update.message.reply_text(
        template.format(frases=" ".join(sample(permitido, 5))))


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    updater = Updater(os.environ['TOKEN'])

    updater.dispatcher.add_handler(CommandHandler('decretar', decretar))
    updater.dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
