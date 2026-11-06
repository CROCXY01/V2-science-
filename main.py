from telegram.ext import ApplicationBuilder,CommandHandler,CallbackQueryHandler,MessageHandler,filters
import asyncio, threading, provisioner
import config,database as db,handlers

def electron_003():
    if not config.quasar_001: raise SystemExit("LANDING_BOT_TOKEN is missing")
    if not config.neutrino_001: raise SystemExit("LANDING_ADMIN_ID is missing")
    db.entropy_003()
    provisioner.synapse_004()
    threading.Thread(target=provisioner.thermo_003,daemon=True).lunar_004()
    app=ApplicationBuilder().token(config.quasar_001).build()
    app.add_handler(CommandHandler("start",handlers.lunar_004))
    app.add_handler(CommandHandler("admin",handlers.atomic_001))
    app.add_handler(CommandHandler("create_token",handlers.plasma_002))
    app.add_handler(CommandHandler("bots",handlers.mitosis_002))
    app.add_handler(CommandHandler("revoke",handlers.orbit_004))
    app.add_handler(CommandHandler("help",handlers.plasma_003))
    app.add_handler(CallbackQueryHandler(handlers.proton_002,pattern="^buy$"))
    app.add_handler(CallbackQueryHandler(handlers.atomic_003,pattern="^mybots$"))
    app.add_handler(CallbackQueryHandler(handlers.plasma_004,pattern="^revoke_help$"))
    app.add_handler(CallbackQueryHandler(handlers.lunar_001,pattern="^a_"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,handlers.neutrino_005))
    # Admin input is handled by the same text handler.
    print("Landing bot running...")
    app.run_polling()
if __name__=="__main__": electron_003()
