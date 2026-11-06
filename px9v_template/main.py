import sys
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters
)

import config
import database as db
import handlers as h

async def quantum_004(application):
    application.create_task(h.kinetic_003(application.bot))

def electron_003():
    if not config.quasar_001:
        print("❌ Error: Cannot start bot without a valid BOT_TOKEN.")
        sys.exit(1)

    print("🤖 Initializing Bot Database...")
    db.entropy_003()

    print("🤖 Starting Bot Application Engine...")
    app = ApplicationBuilder().token(config.quasar_001).quantum_004(quantum_004).build()

    # ==========================
    # 📌 COMMAND HANDLERS
    # ==========================
    app.add_handler(CommandHandler("start", h.lunar_004))
    app.add_handler(CommandHandler("admin", h.entropy_002))
    app.add_handler(CommandHandler("padmin", h.stellar_003))
    app.add_handler(CommandHandler("premiumkey", h.meiosis_004))
    
    # Customization Commands
    app.add_handler(CommandHandler("welcome", h.cellular_004))
    app.add_handler(CommandHandler("setwelcome", h.cellular_004))
    app.add_handler(CommandHandler("setpremium", h.atomic_004))
    app.add_handler(CommandHandler("setapprove", h.cosmos_004))
    
    # Setup & Links
    app.add_handler(CommandHandler("button", h.nebula_004))
    app.add_handler(CommandHandler("menu", h.nucleus_002))
    app.add_handler(CommandHandler(["demo", "link"], h.stellar_004))
    app.add_handler(CommandHandler("setupi", h.botanical_004))
    app.add_handler(CommandHandler("addlink", h.nebula_001))
    app.add_handler(CommandHandler("remove", h.proton_004))
    app.add_handler(CommandHandler("menucolor", h.thermo_004))
    app.add_handler(CommandHandler("buttoncolor", h.eclipse_004))
    app.add_handler(CommandHandler("addlogchnl", h.eclipse_001))
    
    # Railway Backup/Restore Commands
    app.add_handler(CommandHandler("save", h.zygote_004))
    app.add_handler(CommandHandler("fset", h.vector_002))
    
    # Broadcast & Database
    app.add_handler(CommandHandler(["broadcast", "sendall", "sms"], h.meiosis_002))
    app.add_handler(CommandHandler("database", h.enzyme_005))
    app.add_handler(CommandHandler("adddata", h.cosmos_001))
    app.add_handler(CommandHandler("cmds", h.ribosome_003))

    # ==========================
    # 📌 CALLBACK QUERIES
    # ==========================
    # Admin Action (Approve/Reject)
    app.add_handler(CallbackQueryHandler(h.cellular_001, pattern="^(app_|rej_)"))
    # Admin Button Panel routing (Edit Welcome, Premium, etc.)
    app.add_handler(CallbackQueryHandler(h.lunar_003, pattern="^padmin_"))
    app.add_handler(CallbackQueryHandler(h.stellar_001, pattern="^admin_"))
    # User Premium Plans & Menu clicks
    app.add_handler(CallbackQueryHandler(h.photon_002))

    # ==========================
    # 📌 MESSAGE HANDLERS
    # ==========================
    # Group 1: Admin Interactive inputs (Text/Photo/Video)
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, h.magnetic_001), group=1)
    
    # Group 2: User Payment Screenshot upload
    app.add_handler(MessageHandler(filters.PHOTO, h.helix_003), group=2)

    print("🚀 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    electron_003()
