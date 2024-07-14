from openai import OpenAI
import aiogram


client = OpenAI(api_key='api_key')
TOKEN_API = "token_api"


bot = aiogram.Bot(TOKEN_API)
dp = aiogram.Dispatcher(bot)

code_phrase = 'PUD'


@dp.message_handler(commands=['image'])
async def send_image(message: aiogram.types.Message):
    try:
      description = message.text.replace('/image', '').strip()
      image = await generate_image(description)
      await bot.send_photo(chat_id=message.chat.id, photo=image)
    except Exception as e:
        await message.reply(['image_error'] + str(e))


async def generate_image(prompt):
    response = client.images.generate(
        prompt=prompt,
        n=1,
        size='1024x1024',
        quality= 'hd',
        style = 'vivid',
    )
    image_url = response.data[0].url
    return image_url 

messages=[
  {"role": "system", "content": "PROMPT"},
  {"role": "user", "content": "PROMPT"}
]

@dp.message_handler()
async def echo_answer(message: aiogram.types.Message):
      if message.text.startswith(code_phrase):
          messages.append({"role": "user", "content": message.text})
          completion = client.chat.completions.create(
        model="gpt-3.5-turbo", messages = messages)
          reply = completion.choices[0].message.content
          await message.reply(text=reply)
          messages.append({"role": "assistant", "content": reply})
          print(len(messages))
          x = len(messages)
          if x > 25:
               messages.pop(1,2,3,4,5,6,7,8,9,10)
      else:
          pass


if __name__ == '__main__':
    aiogram.executor.start_polling(dp)