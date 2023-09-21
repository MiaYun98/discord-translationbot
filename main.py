import discord
from google import Google_Translator
from datetime import datetime

TOKEN = ''
CHANNEL_ID = ''
 
 
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await self.change_presence(status=discord.Status.online, activity=discord.Game("대기중"))
 
    async def on_message(self, message):
        if message.author == self.user:
            return
 
        if message.content == 'ping':
            await message.channel.send('pong {0.author.mention}'.format(message))
        else:
            answer = self.get_answer(message.content)
            await message.channel.send(answer)
 
    def get_day_of_week(self):
        weekday_list = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
 
        weekday = weekday_list[datetime.today().weekday()]
        date = datetime.today().strftime("%Y년 %m월 %d일")
        result = '{}({})'.format(date, weekday)
        return result
 
    def get_time(self):
        return datetime.today().strftime("%H시 %M분 %S초")
 
    def get_answer(self, text):
        trim_text = text.replace(" ", "")
 
        answer_dict = {
            '안녕': '안녕하세요. 먀룽입니다.',
            '요일': ':calendar: 오늘은 {}입니다'.format(self.get_day_of_week()),
            '시간': ':clock9: 현재 시간은 {}입니다.'.format(self.get_time()),
        }
 
        if trim_text in answer_dict.keys():
            return answer_dict[trim_text]
        else:
            if __name__ == '__main__':
                translator = Google_Translator()

                # Select the option you want to use

                input_text = text


                result = translator.translate(input_text, "ko")

                print('[{}] -> [{}]'.format(result['src_lang'], result['tgt_lang']))
                print('=' * 50)
                print('Source Text : {}'.format(result['src_text']))
                print('Target Text : {}'.format(result['tgt_text']))

                return result['tgt_text']


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)
