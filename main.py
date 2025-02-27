import discord
from discord.ext import commands
import datetime
import os
from dotenv import load_dotenv  # ใช้ dotenv เพื่อโหลดโทเค็นจากไฟล์ .env

# โหลดโทเค็นจากไฟล์ .env
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} is online!")

    # Rich Presence
    activity = discord.Activity(
        type=discord.ActivityType.streaming,
        name="Meoaw Hub",  # เปลี่ยนได้
        url="https://www.youtube.com/watch?v=g88A3mmF3A0",  # เปลี่ยนได้
        details="Meoaw Hub",  # เปลี่ยนได้
        state="สถานะ: :zaved: เปิดร้าน !",  # เปลี่ยนได้
        start=datetime.datetime.utcnow(),
    )
    await client.change_presence(activity=activity)

    # Rich Presence Assets (รูปภาพใหญ่และเล็ก)
    large_image_url = "https://media.discordapp.net/attachments/1297932056562761869/1339236820344377516/2797.gif_wh300.gif?ex=67c071fb&is=67bf207b&hm=0c6926815b756b8c67e8057a5b70a08eba69e82b2d73c3d97252f323d69f6785&="
    small_image_url = "https://media.discordapp.net/attachments/1297932056562761869/1339237230115295334/476486213_563757063486648_2416448072645905892_n.gif?ex=67c0725d&is=67bf20dd&hm=caa5d24955d1940115edd186ddb40bda1003826ed6ff7ddfe7ee0b4bb0ad0de3&=&width=550&height=194"

    # ใช้ Discord Rich Presence Asset
    r = discord.Activity(
        type=discord.ActivityType.streaming,
        name="Meoaw Hub",
        details="Meoaw Hub",
        state="สถานะ: :zaved: เปิดร้าน !",  # เปลี่ยนได้
        start=datetime.datetime.utcnow(),
        url="https://www.youtube.com/watch?v=g88A3mmF3A0",
    )

    await client.change_presence(activity=r)

    # ปุ่ม "เริ่ม" สำหรับการเริ่มการทำงาน
    class MyView(discord.ui.View):
        @discord.ui.button(label="เริ่ม", style=discord.ButtonStyle.primary)  # ใช้ primary แทน blue
        async def start_button(self, interaction: discord.Interaction, button: discord.ui.Button):
            # ใช้ interaction เพื่อส่งข้อความ
            await interaction.response.send_message("เริ่มการทำงานแล้ว!")

    # สร้าง view และส่งปุ่มไปที่ Discord
    await client.get_channel(1297932056562761869).send("กดปุ่มเริ่ม:", view=MyView())

client.run(os.getenv('TOKEN'))  # ใช้โทเค็นจากไฟล์ .env
