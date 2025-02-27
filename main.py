import discord
from discord.ext import commands
from discord.ui import Button, View, TextInput
from discord import Interaction
import os
from dotenv import load_dotenv
import datetime

# โหลดโทเค็นจากไฟล์ .env
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)

# ฟังก์ชันจัดการปุ่มกรอกข้อมูลต่างๆ
class MyView(View):
    def __init__(self):
        super().__init__(timeout=180)  # ตั้งเวลาให้หมดอายุหลัง 180 วินาที

    # ปุ่มกรอกโทเค็น
    @discord.ui.button(label="กรอกโทเค็น", style=discord.ButtonStyle.primary)  # เปลี่ยนเป็น primary
    async def token_button(self, interaction: Interaction, button: discord.ui.Button):
        # แสดงฟอร์มกรอกโทเค็น
        await interaction.response.send_message("กรุณากรอกโทเค็นของคุณ:", ephemeral=True)

        # สร้าง TextInput ให้กรอกโทเค็น
        token_input = TextInput(label="กรุณากรอกโทเค็น", placeholder="ใส่โทเค็นที่นี่")
        modal = discord.ui.Modal(title="กรอกโทเค็น", custom_id="token_modal")
        modal.add_item(token_input)

        # รอรับการกรอกข้อมูล
        await interaction.response.send_modal(modal)

    # ปุ่มกรอกรูปลิ้งค์
    @discord.ui.button(label="กรอกรูปลิ้งค์", style=discord.ButtonStyle.success)  # เปลี่ยนเป็น success
    async def link_button(self, interaction: Interaction, button: discord.ui.Button):
        # แสดงฟอร์มกรอกรูปลิ้งค์
        await interaction.response.send_message("กรุณากรอกลิ้งค์รูปภาพของคุณ:", ephemeral=True)

        # สร้าง TextInput ให้กรอกลิ้งค์รูปภาพ
        link_input = TextInput(label="กรุณากรอกลิ้งค์รูป", placeholder="ใส่ลิ้งค์รูปที่นี่")
        modal = discord.ui.Modal(title="กรอกรูปลิ้งค์", custom_id="link_modal")
        modal.add_item(link_input)

        # รอรับการกรอกข้อมูล
        await interaction.response.send_modal(modal)

    # ปุ่มเริ่มการทำงาน
    @discord.ui.button(label="เริ่มการทำงาน", style=discord.ButtonStyle.primary)
    async def start_button(self, interaction: Interaction, button: discord.ui.Button):
        # ส่งข้อความยืนยันการเริ่มทำงาน
        await interaction.response.send_message("เริ่มการทำงานแล้ว!")

# คำสั่ง !start เพื่อเริ่มการทำงาน
@client.command()
async def start(ctx):
    view = MyView()
    await ctx.send("กรุณากรอกข้อมูลโทเค็นหรือกรอกรูปลิ้งค์", view=view)

@client.event
async def on_ready():
    print(f"{client.user} is online!")

    # Rich Presence
    activity = discord.Activity(
        type=discord.ActivityType.streaming,
        name="Meoaw Hub",  # เปลี่ยนได้
        url="https://www.youtube.com/watch?v=g88A3mmF3A0",  # เปลี่ยนได้
        details="Meoaw Hub",  # เปลี่ยนได้
        state="สถานะ: :green_circle: เปิดร้าน !",  # เปลี่ยนได้
        start=datetime.datetime.utcnow(),
    )
    await client.change_presence(activity=activity)

    # Rich Presence Assets (รูปภาพใหญ่และเล็ก)
    large_image_url = "https://media.discordapp.net/attachments/1297932056562761869/1339232056562761869/2797.gif_wh300.gif?ex=67c071fb&is=67bf207b&hm=0c6926815b756b8c67e8057a5b70a08eba69e82b2d73c3d97252f323d69f6785&="
    small_image_url = "https://media.discordapp.net/attachments/1297932056562761869/1339237230115295334/476486213_563757063486648_2416448072645905892_n.gif?ex=67c0725d&is=67bf20dd&hm=caa5d24955d1940115edd186ddb40bda1003826ed6ff7ddfe7ee0b4bb0ad0de3&=&width=550&height=194"

    # ใช้ Discord Rich Presence Asset
    r = discord.Activity(
        type=discord.ActivityType.streaming,
        name="Meoaw Hub",
        details="Meoaw Hub",
        state="สถานะ: :green_circle: เปิดร้าน !",  # เปลี่ยนได้
        start=datetime.datetime.utcnow(),
        url="https://www.youtube.com/watch?v=g88A3mmF3A0",
    )

    await client.change_presence(activity=r)

client.run(os.getenv('TOKEN'))  # ใช้โทเค็นจากไฟล์ .env
