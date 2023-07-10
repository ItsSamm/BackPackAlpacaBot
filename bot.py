from distutils.log import error
from email import message
from random import randrange
import hikari
import discord
import Extra
import numpy as np



import asyncio
import random
import time
from PIL import Image
CanvasSize = [10, 10]
playerpos = [0, 0]
goalposition = [9,random.randint(2, 8)]
imppos = [5, 2, 5, 9]
Extra.currentnum = 0
def colorfromname(cname):
    if cname == "black":
        return (0, 0, 0)
    if cname == "blue":
        return (56, 126, 224)
    if cname == "brown":
        return (125, 96, 66)
    if cname == "cyan":
        return (107, 255, 250)
    if cname == "darkblue":
        return (107, 255, 250)
    if cname == "green":
        return (20, 245, 57)
    if cname == "grey":
        return (66, 66, 66)
    if cname == "lightgrey":
        return (163, 163, 163)
    if cname == "magenta":
        return (205, 100, 209)
    if cname == "lime":
        return (108, 212, 118)
    if cname == "orange":
        return (219, 106, 61)
    if cname == "pink":
        return (247, 109, 243)
    if cname == "purple":
        return (142, 64, 245)
    if cname == "red":
        return (245, 64, 64)
    if cname == "white":
        return (255, 255, 255)
    if cname == "yellow":
        return (245, 227, 64)
    return (0, 0, 0)
    
def setupscale():
    basewidth = 1000
    grid = Image.open('E:/@backpackalpaca/alpaca bot/PythonBot/Grid.png')
    orgimg = Image.open('E:/@backpackalpaca/alpaca bot/PythonBot/canvas.png')
    orgimg = orgimg.resize((1000, 1000), resample=Image.NEAREST)  
    orgimg = orgimg .transpose(Image.FLIP_TOP_BOTTOM)
    # Calculate width to be at the center
    width = (orgimg.width - grid.width) // 2
  
# Calculate height to be at the center
    height = (orgimg.height - grid.height) // 2
  
# Paste the frontImage at (width, height)
    orgimg.paste(grid, (width, height), grid)
    orgimg.save('E:/@backpackalpaca/alpaca bot/PythonBot/upscale.png')
def setpixel(x, y, color):
    img = Image.open('E:/@backpackalpaca/alpaca bot/PythonBot/canvas.png')
    pixels = img.load()
    pixels[x ,y] = color
    img.save('E:/@backpackalpaca/alpaca bot/PythonBot/canvas.png')

def bensays():
    rnd = random.randint(1, 4)
    #yes
    if rnd == 1:
        return 'https://cdn.discordapp.com/attachments/976644950194266145/976694205881671710/YES.png'
            #no
    if rnd == 2:
        return 'https://cdn.discordapp.com/attachments/976644950194266145/976693917430988840/YES.png'
            #hangup
    if rnd == 3:
        return 'https://cdn.discordapp.com/attachments/976644950194266145/976694001031839764/HANGUPS.png'
            #HMMM
    if rnd == 4:
        return 'https://cdn.discordapp.com/attachments/976644950194266145/976694042966511626/HMMMM.png'
def coinflip():
    rand = random.randint(1,2)
    if rand == 1:
        return "Heads!"
    else:
        return "Tails!"
def reset():
    CanvasSize[0] = 10
    CanvasSize[1] = 10
    playerpos[0] = 0
    playerpos[1] = 0
    goalposition[0] = 9
    goalposition[1] = random.randint(2, 8)
    imppos[0] = 5
    imppos[1] = 2
    imppos[2] = 5
    imppos[3] = 9
def helpmessage(key):
    
    if Extra.currentnum==11:
        return "```How to use:\n .game will demonstrate how to play the game.\n Type .Ben for talking Ben to reply to any question.\n Use .flip to flip a coin.\n Type .color to learn how to draw with friends. ```"
    else:
        if key == False:
            return "ERROR"
        if key == True:
            return "```How to use:\n .game will demonstrate how to play the game.\n Type .Ben for talking Ben to reply to any question.\n Use .flip to flip a coin.\n Type .color to learn how to draw with friends. ```"
        
def moveimp():
    rnd = random.randint(1,2)
    if rnd == 1:
        if playerpos[0]>imppos[0]:
            imppos[0]+=1
        if playerpos[0]<imppos[0]:
            imppos[0]-=1
    if rnd == 2:
        if playerpos[1]>imppos[1]:
            imppos[1]+=1
        if playerpos[1]<imppos[1]:
            imppos[1]-=1
    rnd = random.randint(1,2)
    if rnd == 1:
        if playerpos[0]>imppos[2]:
            imppos[2]+=1
        if playerpos[0]<imppos[2]:
            imppos[2]-=1
    if rnd == 2:
        if playerpos[1]>imppos[3]:
            imppos[3]+=1
        if playerpos[1]<imppos[3]:
            imppos[3]-=1
def changepositon(amount):
    moveimp()
    playerpos[0]+=amount[0]
    playerpos[1]+=amount[1]
    if playerpos[0]>=CanvasSize[0]-1:
        playerpos[0] = CanvasSize[0]-1
    if playerpos[1]>=CanvasSize[1]-1:
        playerpos[1] = CanvasSize[1]-1
    if playerpos[0]<=0:
        playerpos[0] = 0
    if playerpos[1]<=0:
        playerpos[1] = 0

def RenderData():
    
    output = ""
    for y in range(CanvasSize[1]):
        output+="\n"
        for x in range(CanvasSize[0]):
            isplayer = False
            isgoal = False
            isimp = False
            if x == playerpos[0]:
                if y==playerpos[1]:
                    output+=":llama:"
                    isplayer = True
            if x == goalposition[0]:
                if y==goalposition[1]:
                    if isplayer == True:
                        output = "**YOU WIN!!** \n *(Move to restart)*"
                        reset()
                    else:
                        output+=":tada:"
                        isgoal = True
            if isgoal == False:
                    if x==imppos[0]:
                        if y == imppos[1]:
                            if isplayer == False:
                                output+=":rage:"
                                isimp = True
                            else:
                                output = "**YOU DIED** \n *(Move to restart)*"
                                reset()
            if isimp == False:
                if isgoal == False:
                    if x==imppos[2]:
                        if y == imppos[3]:
                            if isplayer == False:
                                output+=":rage:"
                                isimp = True
                            else:
                                output = "**YOU DIED** \n *(Move to restart)*"
                                reset()
            
                
                
            if isplayer == False:
                if isgoal == False:
                    if isimp == False:
                        output+=":green_square:"
                    
                
            
        
    
    return output
#dbot = discord.GatewayBot(token = '*DELETED')

bot = hikari.GatewayBot(token = '*DELETED')
bot.request_guild_members
@bot.listen(hikari.GuildMessageCreateEvent)

async def print_message(event):
    print(event.content)
    #GAME
    if event.content.strip() == ".right":
        changepositon(amount=[1,0])
        await event.message.respond(
            
            f''+RenderData()
        )
    if event.content.strip() == ".left":
        changepositon(amount=[-1,0])
        await event.message.respond(
            
            f''+RenderData()
        )
    if event.content.strip() == ".down":
        changepositon(amount=[0,1])
        await event.message.respond(
            
            f''+RenderData()
        )
    if event.content.strip() == ".up":
        changepositon(amount=[0,-1])
        await event.message.respond(
            
            f''+RenderData()
        )
    #other
    if event.content.strip() == ".flip":
        await event.message.respond(
            
            f''+coinflip()
        )
    if event.content.strip() == ".Ben":
        await event.message.respond(
            f''+ bensays()
            )
    if event.content.strip() == ".ben":
        await event.message.respond(
            f''+ bensays()
            )
    if event.content.strip() == ".help":
        await event.message.respond(
                helpmessage(key = True)
            )
    if event.content.strip() == ".game":
        await event.message.respond(
            f'```The game is played buy using the commands .right .left .up .down to move. Just type it in for the game to start!```'
            )
    if event.content.strip() == ".color":
        await event.message.respond(
            f'```Type, color (Color type) then cordinantes, for example: color blue 5 5```'
            )
    if event.content.strip() == "refresh":
        f = hikari.File('E:/@backpackalpaca/alpaca bot/PythonBot/upscale.png')

        await event.message.respond(f)
    if event.content!= "":
        print("NOTNULL")
        Extra.currentnum+=1
    if Extra.currentnum>20:
        f = helpmessage(key = False)
        if f != "ERROR":
            await event.message.respond(f)
        Extra.currentnum = 0
    
    splitcontent = event.content.split(" ")
    if splitcontent[0] == "color" or splitcontent[0] == "Color":
        if len(splitcontent)==4:
            x = int(splitcontent[2])-1
            y = int(splitcontent[3])-1
            
            setpixel(x=x, y=y, color = colorfromname(splitcontent[1]))
            setupscale()
            f = hikari.File('E:/@backpackalpaca/alpaca bot/PythonBot/upscale.png')

            await event.message.respond(f)
        

#https://www.youtube.com/watch?v=cCiqcu2NP8I

#https://www.youtube.com/watch?v=C55VphHxGKY


bot.run()