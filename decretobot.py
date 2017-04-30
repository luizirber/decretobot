#! /usr/bin/env python
# encoding: utf-8

import json
import logging
from random import sample
import os

from telegram.ext import Updater, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


template = """
18:00, horário de Brasília. Já pode:

{frases}

Decreto liberado. Cumpra-se.
"""

with open('frases.json', 'r') as f:
    frases = json.load(f)


def decretar(bot, update):
    update.message.reply_text(
        template.format(frases=" ".join(sample(frases, 5))))


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
