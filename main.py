from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

import os

# Token salvo como variável de ambiente
TOKEN = os.getenv("TELEGRAM_TOKEN")

respostas = {
    "horário": "Atendemos 24h por dia, 7 dias por semana! 🕐",
    "endereço": "Estamos na Rua XYZ 165, Ariquemes 🏗️",
    "telefone": "Você pode ligar ou chamar no WhatsApp: (69) 89999-9999 📞",
    "material": "Temos de tudo para sua obra! Telhas, cimento, areia, brita, pisos, torneiras e muito mais! 🧱🛠️",
}

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()

    for chave in respostas:
        if chave in texto:
            await update.message.reply_text(respostas[chave])
            return

    await update.message.reply_text(
        "Olá! 👷‍♂️ Sou o bot da Cavalcante Materiais para Construção!\nMe diga como posso te ajudar hoje? 💬"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

app.run_polling()
