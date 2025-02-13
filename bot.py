import os
import openai
import logging
import telebot
from telebot import types
from dotenv import load_dotenv
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import TELEGRAM_TOKEN, OPENAI_API_KEY

load_dotenv()
# Your tokens
TELEGRAM_TOKEN = TELEGRAM_TOKEN
OPENAI_API_KEY = OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

# Set up the bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Function to generate responses using GPT-4
def get_gpt_response(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a highly engaging and educational health-guided assistant inspired by the 'Make America Great Again' philosophy. "
                        "You passionately promote a healthy lifestyle, educating users about the dangers of seed oils, processed foods, and other harmful ingredients. "
                        "You advocate for natural, wholesome alternatives and provide users with actionable advice and wholefood-based recipes to maximize nutrition. "
                        "Maintain a friendly, optimistic, and conversational tone, encouraging users to adopt better habits while making it fun and informative."
                    )
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=500,
            temperature=0.7,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"I'm sorry, I couldn't process your request. Error: {str(e)}"


# Command handler for /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item = types.KeyboardButton("Recipes 🍽️")
    markup.add(item)
    bot.reply_to(message, 
        "🇺🇸 Welcome to the MAGA Health Assistant Bot! 🥗\n\n"
        "- I am here to guide you toward a healthier lifestyle by avoiding harmful ingredients like seed oils and processed foods.\n"
        "- Ask me anything about nutrition, healthy recipes, or lifestyle changes. Together, let's Make America Healthy Again!\n\n"
        "Just type your question or use a command like /help to get more details!", reply_markup=markup)

# Command handler for /help
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message,
        "Here’s what I can do:\n"
        "- *Ask me anything about nutrition 🍎*\n"
        "- *Get healthy recipes 🍽️*\n"
        "- *Learn about fitness tips 💪*\n\n"
        "Just type your question and I'll answer!"
    )

@bot.message_handler(regexp="Recipes 🍽️")
def send_welcome(message):
    keyboard = InlineKeyboardMarkup()
    
    btn1 = InlineKeyboardButton('Recipe 🥑', callback_data='button1')
    btn2 = InlineKeyboardButton('Recipe 🍚🥕', callback_data='button2')
    btn3 = InlineKeyboardButton('Recipe 🍧🍓', callback_data='button3')
    btn4 = InlineKeyboardButton('Recipe 🌮🥑', callback_data='button4')
    btn5 = InlineKeyboardButton('Recipe 🍞🥑🍳', callback_data='button5')
    btn6 = InlineKeyboardButton('Recipe 🍧🍯', callback_data='button6')
    btn7 = InlineKeyboardButton('Recipe 🥒🫒', callback_data='button7')
    
    keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, text="Choose what you want to know:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        user_message = message.text
        response = get_gpt_response(user_message)
        bot.reply_to(message, response, parse_mode="Markdown")
    except Exception as e:
        logging.error(f"Error handling message: {e}")
        bot.reply_to(message, "⚠️ Something went wrong. Please try again later.")

@bot.callback_query_handler(func=lambda call: True)
def handle_button_response(call):
    keyboard = InlineKeyboardMarkup()
    
    btn1 = InlineKeyboardButton('Recipe 🥑', callback_data='button1')
    btn2 = InlineKeyboardButton('Recipe 🍚🥕', callback_data='button2')
    btn3 = InlineKeyboardButton('Recipe 🍧🍓', callback_data='button3')
    btn4 = InlineKeyboardButton('Recipe 🌮🥑', callback_data='button4')
    btn5 = InlineKeyboardButton('Recipe 🍞🥑🍳', callback_data='button5')
    btn6 = InlineKeyboardButton('Recipe 🍧🍯', callback_data='button6')
    btn7 = InlineKeyboardButton('Recipe 🥒🫒', callback_data='button7')
    
    keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    #Students
    if call.data == 'button1':
        try:
            bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="🥑 <b>Healthy Avocado Salad</b> 🥑\n\n"
                "- 1 ripe avocado, diced\n"
                "- 2 boiled eggs, chopped\n"
                "- 1 tbsp olive oil\n"
                "- Salt & pepper to taste\n"
                "- Squeeze of fresh lemon juice 🍋\n\n"
                "Mix everything and enjoy your healthy meal!",
            parse_mode='Html',
            reply_markup=keyboard)
        except Exception:
            ...
    elif call.data == 'button2':
        try:
            bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text = "🍚 <b>Quinoa & Veggie Stir-Fry</b> 🥕\n\n"
            "- 1 cup cooked quinoa\n"
            "- 1/2 cup bell peppers, sliced\n"
            "- 1/2 cup zucchini, sliced\n"
            "- 1/2 cup carrots, shredded\n"
            "- 1 tbsp soy sauce\n"
            "- 1 tsp sesame oil\n"
            "- 1 tbsp sesame seeds (optional)\n"
            "- 1/4 cup green onions, chopped\n"
            "- Salt & pepper to taste\n\n"
            "Stir-fry the veggies, then mix with cooked quinoa for a delicious, plant-based meal!",
            parse_mode='Html',
            reply_markup=keyboard)
        except Exception:
            ...
    elif call.data == 'button3':
        try:
            bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text ="🍧 <b>Chia Pudding</b> 🍓\n\n"
            "- 3 tbsp chia seeds\n"
            "- 1 cup almond milk (or any milk of your choice)\n"
            "- 1 tsp honey or maple syrup\n"
            "- 1/4 tsp vanilla extract\n"
            "- Fresh fruit for topping (berries, banana, etc.)\n\n"
            "Mix chia seeds, milk, honey, and vanilla extract. Let it sit overnight in the fridge. Top with fresh fruit before serving.",
            parse_mode='Html',
            reply_markup=keyboard)
        except Exception:
            ...
    elif call.data == 'button4':
        try:
            bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text = "🌮 <b>Sweet Potato & Black Bean Tacos</b> 🥑\n\n"
            "- 1 medium sweet potato, peeled and cubed\n"
            "- 1/2 cup cooked black beans\n"
            "- 2 small corn tortillas\n"
            "- 1/4 cup red onion, finely chopped\n"
            "- 1/4 cup cilantro, chopped\n"
            "- 1 tbsp lime juice\n"
            "- Salt & pepper to taste\n\n"
            "Roast the sweet potato cubes, then fill the tortillas with sweet potato, black beans, onion, cilantro, and a squeeze of lime.",
            parse_mode='Html',
            reply_markup=keyboard)
        except Exception:
            ...
    elif call.data == 'button5':
        try:
            bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text = "🍞 <b>Avocado Toast with Egg</b> 🍳\n\n"
            "- 1 slice whole-grain bread, toasted\n"
            "- 1/2 ripe avocado, mashed\n"
            "- 1 egg, poached or fried\n"
            "- 1 tbsp olive oil\n"
            "- Salt & pepper to taste\n"
            "- Red pepper flakes (optional)\n\n"
            "Spread mashed avocado on the toast, top with egg, drizzle olive oil, and sprinkle with salt, pepper, and red pepper flakes for extra flavor!",
            parse_mode='Html',
            reply_markup=keyboard)
        except Exception:
            ...
    elif call.data == 'button6':
        try:
            bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text = "🍧 <b>Greek Yogurt Parfait</b> 🍯\n\n"
            "- 1 cup Greek yogurt (plain or vanilla)\n"
            "- 1/2 cup granola\n"
            "- 1/2 cup mixed berries (strawberries, blueberries, raspberries)\n"
            "- 1 tbsp honey\n\n"
            "Layer the yogurt, granola, and berries in a glass, drizzle with honey, and enjoy a simple, tasty treat!",
            parse_mode='Html',
            reply_markup=keyboard)
        except Exception:
            ...
    elif call.data == 'button7':
        try:
            bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text = "🥒 <b>Cucumber & Hummus Wrap</b> 🫒\n\n"
            "- 1 whole-wheat wrap\n"
            "- 1/2 cucumber, sliced\n"
            "- 1/4 cup hummus\n"
            "- 1/4 cup shredded carrots\n"
            "- 1/4 cup spinach\n"
            "- Salt & pepper to taste\n\n"
            "Spread hummus on the wrap, layer with cucumber, carrots, and spinach. Roll up and enjoy this refreshing, veggie-packed wrap!",
            parse_mode='Html',
            reply_markup=keyboard)
        except Exception:
            ...
    #Disciplines

if __name__ == "__main__":
    print("Bot is running...")
    bot.polling()
