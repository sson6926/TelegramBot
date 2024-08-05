import json
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from module.static import messageXSMB
from utils.xsmb import getSXMB

async def xs(update: Update, context):
    result = await getSXMB()
    result_json = json.loads(result)
    await update.message.reply_text(messageXSMB.format(today = result_json['date'],
                                                       GDB =result_json['data']['giai_dac_biet'],
                                                       G1 = result_json['data']['giai_1'],
                                                       G2 = result_json['data']['giai_2'],
                                                       G3 = result_json['data']['giai_3'],
                                                       G4 = result_json['data']['giai_4'],
                                                       G5 = result_json['data']['giai_5'],
                                                       G6 = result_json['data']['giai_6'],
                                                       G7 = result_json['data']['giai_7']), parse_mode='HTML')