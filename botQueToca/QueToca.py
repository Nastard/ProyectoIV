#!/usr/bin/python
# -*- coding: utf-8 -*-

import telebot
import os
from QueTocaBBDD import Horario

API_TOKEN = os.environ["TOKEN"]
bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hola, soy un bot que te dice tu horario.')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Comandos disponibles:')

@bot.message_handler(commands=['horario'])
def send_activity(message):
	cid = message.chat.id
	horario = Horario()
	info = horario.LeerHorario("D1")
	bot.send_message(cid, info)

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.polling()
