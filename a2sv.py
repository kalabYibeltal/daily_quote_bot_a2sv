import asyncio
import logging
import sys
import requests
import io
from aiogram.types import InputFile

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
# from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6834075119:AAGK8MOU0AV2coWz61rFwasipeSf2R2NfSI"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

async def fetch_Quote(bot: Bot):
    
    response =  requests.get('https://zenquotes.io/api/today')
    val = response.json()
    
    quote = val[0]["q"]
    author = val[0]["a"]
    message = f"{quote}\n\n{'by ' + author:>100}"
    
    await bot.send_message(chat_id='-1002007018861', text=message, message_thread_id=8)
    


# async def fetch_Image():
        
#     url = "https://quotes.rest/qod?language=en"

#     # Define headers (if needed)
#     headers = {
#         "accept": "application/json",
#         "Authorization": "Bearer XAHHYHPNs2ZE2rZQnHpOz4Jq5CKVirtuQEx8vi3m"
#     }

#     # Send GET request
#     response = requests.get(url, headers=headers)

#     # Check if request was successful (status code 200)
#     if response.status_code == 200:
#         # Parse JSON response
#         data = response.json()
#         # Extract image URL
#         image_url = data['contents']['quotes'][0]['background']
        
#         # Now you have the image URL, you can use it as needed
#         return image_url

#         # Perform further actions such as downloading the image or overlaying text on it
#     else:
#         print("Error:", response.status_code)
#         return ''

# async def overlay_text_on_image(image_url, text,bot ):
    # Load the image from URL
    response = requests.get(image_url)
    my_image = Image.open(BytesIO(response.content))
    # my_image = Image.open("image.jpg")

    title_font = ImageFont.truetype("Arial.ttf", 400)
    image_drawer = ImageDraw.Draw(my_image)

    tw, th = image_drawer.textsize("THIS IS text", font=title_font)

    iw, ih = my_image.size
    x = (iw - tw) // 2
    y = (ih - th) // 2
    image_drawer.text((x, y), "Text goes here",
                    (237, 0, 0), font=title_font)

    my_image.save("image-text.jpg")

    # # Initialize drawing context
    # draw = ImageDraw.Draw(image)

    # # Define font size and font type
    # font_size = 40
    # font = ImageFont.truetype("arial.ttf", font_size)

    # # Calculate text size and position
    # text_width, text_height = draw.textsize(text, font=font)
    # image_width, image_height = image.size
    # text_x = (image_width - text_width) // 2
    # text_y = image_height - text_height - 20  # Adjust Y position as needed

    # # Overlay text on the image
    # draw.text((text_x, text_y), text, fill="white", font=font)

    # Save the modified image
    # image.save("image-text.jpg")
    
    bio = io.BytesIO()
    Image.save(bio, 'JPEG')
    bio.seek(0)

    photo = types.InputFile(bio, filename='photo.jpg')

    # Create an InputFile from the BytesIO object
    
    await bot.send_photo(chat_id='-1002007018861',photo=photo, message_thread_id=8)
  


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}! {message.chat.id}")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    
    # Send a message to the group every 5 seconds
    # This is a demonstration of how to use asyncio with aiogram
    
    # Specify the topic ID in the chat_id parameter
   
    # And then run events dispatching
    
    
    # ImageUrl = "https://theysaidso.com/assets/images/qod/qod-inspire.jpg"
    # ImageUrl = await fetch_Image()
    # Image =  await overlay_text_on_image(ImageUrl, message,bot)

    # Format the message    
    
    
    
    while True:
        await fetch_Quote(bot)
        await asyncio.sleep(86400)  # 24 hours    
    
    


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main()) 