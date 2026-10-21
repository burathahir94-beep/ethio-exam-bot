import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# ==================== ⚙️ ማስተካከያ መረጃዎች (CONFIGURATIONS) ====================
BOT_TOKEN = "8867531175:AAHSaBuMVMB8MqJCVJ7d64W99-KKKlTGqVI"
ADMIN_USERNAME = "@birukthahir"
CHANNEL_URL = "https://t.me/shmelshabteschoolofficial"

# የክፍያ መረጃዎች
CBE_ACCOUNT = "1000576441324"
TELEBIRR_NUMBER = "0932027090"

# የ VIP ዋጋዎች
VIP_1_MONTH_PRICE = "300 ብር"
VIP_1_SEMESTER_PRICE = "1300 ብር"
# =========================================================================

# Logging ማስተካከያ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ----------------- 🔘 የሜኑ እና የቁልፎች ዝግጅት (MENUS) -----------------

def get_main_menu():
    """የቦቱን ዋና ገጽ ቁልፎች ይፈጥራል"""
    keyboard = [
        [InlineKeyboardButton("📚 የፈተና ጥያቄዎች", callback_data="menu_exams")],
        [InlineKeyboardButton("📄 የትምህርት ማስታወሻዎች", callback_data="menu_materials")],
        [InlineKeyboardButton("⭐ VIP / Premium Access", callback_data="menu_vip")],
        [InlineKeyboardButton("📢 ዋና ቻናላችን", url=CHANNEL_URL)],
        [
            InlineKeyboardButton("❓ እንዴት ልጠቀም?", callback_data="menu_guide"),
            InlineKeyboardButton("📞 አድሚን / ድጋፍ", callback_data="menu_support")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_grades_menu():
    """የክፍል ደረጃዎች መምረጫ ንዑስ ሜኑ"""
    keyboard = [
        [InlineKeyboardButton("🎓 Grade 9 Exams", callback_data="grade_9")],
        [InlineKeyboardButton("🎓 Grade 10 Exams", callback_data="grade_10")],
        [InlineKeyboardButton("🎓 Grade 11 Exams", callback_data="grade_11")],
        [InlineKeyboardButton("🎓 Grade 12 Exams", callback_data="grade_12")],
        [InlineKeyboardButton("🔙 ወደ ዋናው ሜኑ ተመለስ", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_g10_subjects_menu():
    """የ 10ኛ ክፍል ትምህርት አይነቶች ሜኑ"""
    keyboard = [
        [InlineKeyboardButton("📐 Mathematics", callback_data="g10_maths")],
        [InlineKeyboardButton("⚡ Physics", callback_data="g10_physics")],
        [InlineKeyboardButton("🧪 Chemistry", callback_data="g10_chemistry")],
        [InlineKeyboardButton("🔙 ወደ ክፍሎች ተመለስ", callback_data="menu_exams")]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_back_button(target="main_menu"):
    """ማንኛውንም ገጽ ወደ ኋላ ለመመለስ የሚረዳ ቁልፍ"""
    return InlineKeyboardMarkup([[InlineKeyboardButton("🔙 ተመለስ", callback_data=target)]])


# ----------------- 🛠️ መልእክት አስተናጋጆች (HANDLERS) -----------------

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ተጠቃሚው /start ሲሉ የሚሰጥ ሰላምታ"""
    welcome_text = (
        "እንኳን ወደ **Ethio Exam Prep VIP Bot** በደህና መጡ! 👋\n\n"
        "እባክዎን ከታች ካሉት አማራጮች የሚፈልጉትን ይምረጡ፦"
    )
    await update.message.reply_text(
        welcome_text,
        parse_mode="Markdown",
        reply_markup=get_main_menu()
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ተማሪዎች ቁልፎቹን ሲጫኑ ምላሽ የሚሰጥ ክፍል"""
    query = update.callback_query
    await query.answer()
    data = query.data

    # ዋና ሜኑ መመለሻ
    if data == "main_menu":
        await query.edit_message_text(
            "ዋና ሜኑ፦\nእባክዎን የሚፈልጉትን አገልግሎት ይምረጡ፦",
            reply_markup=get_main_menu()
        )

    # የፈተና ጥያቄዎች ገጽ
    elif data == "menu_exams":
        await query.edit_message_text(
            "📚 **የፈተና ጥያቄዎች**\n\nእባክዎን የክፍል ደረጃዎን ይምረጡ፦",
            parse_mode="Markdown",
            reply_markup=get_grades_menu()
        )

    # የትምህርት ማስታወሻዎች (PDF) ገጽ
    elif data == "menu_materials":
        await query.edit_message_text(
            "📄 **የትምህርት ማስታወሻዎች**\n\nየ PDF ማጠቃለያዎችን ለማግኘት የክፍል ደረጃዎን ይምረጡ፦",
            parse_mode="Markdown",
            reply_markup=get_grades_menu()
        )

    # የ VIP አባልነት ገጽ (የተስተካከለ መረጃ)
    elif data == "menu_vip":
        vip_text = (
            "⭐ **VIP / Premium Access**\n\n"
            "የሁሉንም ፈተናዎች ሙሉ ማብራሪያ እና አጫጭር PDF ማጠቃለያዎችን ያግኙ!\n\n"
            f"💰 **የአባልነት ታሪፍ፦**\n"
            f"• የ 1 ወር፦ **{VIP_1_MONTH_PRICE}**\n"
            f"• የ 1 ሴሚስተር፦ **{VIP_1_SEMESTER_PRICE}**\n\n"
            f"💳 **የክፍያ መንገዶች፦**\n"
            f"• የኢትዮጵያ ንግድ ባንክ (CBE): `{CBE_ACCOUNT}`\n"
            f"• Telebirr: `{TELEBIRR_NUMBER}`\n\n"
            f"📩 ክፍያ ከፈጸሙ በኋላ ደረሰኙን ለአድሚን ይላኩ፦ {ADMIN_USERNAME}"
        )
        await query.edit_message_text(
            vip_text,
            parse_mode="Markdown",
            reply_markup=get_back_button("main_menu")
        )

    # እንዴት መጠቀም እንደሚቻል
    elif data == "menu_guide":
        guide_text = (
            "❓ **ቦቱን እንዴት መጠቀም ይቻላል?**\n\n"
            "1️⃣ የክፍል ደረጃዎን እና የትምህርት አይነት ይምረጡ።\n"
            "2️⃣ የልምምድ ጥያቄዎችን እና PDFዎችን ያውርዱ።\n"
            "3️⃣ የፈተናዎችን ሙሉ ማብራሪያ ለማግኘት የ VIP አባል ይሁኑ።"
        )
        await query.edit_message_text(
            guide_text,
            parse_mode="Markdown",
            reply_markup=get_back_button("main_menu")
        )

    # የአድሚን ድጋፍ ገጽ
    elif data == "menu_support":
        support_text = (
            "📞 **የአድሚን ድጋፍ**\n\n"
            "ለማንኛውም ጥያቄ ወይም የ VIP አባልነት ክፍያ ማረጋገጫ፦\n"
            f"📩 Admin: {ADMIN_USERNAME}"
        )
        await query.edit_message_text(
            support_text,
            parse_mode="Markdown",
            reply_markup=get_back_button("main_menu")
        )

    # የ Grade 10 ንዑስ ክፍል
    elif data == "grade_10":
        await query.edit_message_text(
            "📚 **Grade 10 Exam Prep**\n\nየትምህርት አይነት ይምረጡ፦",
            parse_mode="Markdown",
            reply_markup=get_g10_subjects_menu()
        )

    # የ 10ኛ ክፍል Mathematics ይዘት
    elif data == "g10_maths":
        await query.edit_message_text(
            "📐 **Grade 10 Mathematics Resources:**\n\n"
            "• Chapter 1 Test [PDF]\n"
            "• Model Exam 2026\n"
            "• VIP Answer Explanations (Locked)",
            reply_markup=get_back_button("grade_10")
        )


# ----------------- 🚀 ቦቱን ማስነሻ ዋና ክፍል (MAIN) -----------------

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("ቦቱ በተሳካ ሁኔታ መስራት ጀምሯል! (Bot is running...)")
    app.run_polling()

if __name__ == "__main__":
    main()
