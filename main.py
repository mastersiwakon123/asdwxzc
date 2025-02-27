import discord
from discord.ext import commands
import datetime
import os
from myserver import server_on
from dotenv import load_dotenv

# โหลดข้อมูลจากไฟล์ .env
load_dotenv()

# รับค่า Token จาก environment variable
TOKEN = os.getenv('TOKEN')

# ตรวจสอบว่า TOKEN มีค่าไหม
if not TOKEN:
    print("Token not found! Please make sure to set the TOKEN environment variable.")
    exit()

intents = discord.Intents.default()
intents.message_content = True

# สร้างคลาส bot
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} is online!")

    # สร้าง Rich Presence
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

    # ตั้งค่าภาพใหญ่และเล็ก
    await client.change_presence(activity=r)

    # เพิ่มปุ่ม (จำกัดได้ 2 ปุ่ม)
    # Discord ไม่รองรับการเพิ่มปุ่มแบบ JS แต่สามารถใส่ลิ้งค์ใน Rich Presence ได้
    # ปุ่ม Discord
    # ปุ่มใน Python API ไม่รองรับ แต่สามารถเพิ่มปุ่มเพิ่มเติมผ่านการแสดงสถานะอื่นๆ
    # กรณีนี้เราจะใช้การแสดงผลใน Rich Presence แทนการเพิ่มปุ่มจริงๆ

    # ปุ่มที่ 1: เปิดร้าน
    activity = discord.Activity(
        type=discord.ActivityType.streaming,
        name="Meoaw Hub",
        details="เปิดร้าน",
        state="คลิกเพื่อเริ่ม!",
        start=datetime.datetime.utcnow(),
        url="https://www.youtube.com/watch?v=g88A3mmF3A0"
    )
    await client.change_presence(activity=activity)

    server_on()

# เริ่มบอทด้วย Token ที่ได้จาก .env
client.run(TOKEN)
