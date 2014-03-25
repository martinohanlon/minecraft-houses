#www.stuffaboutcode.com
#Raspberry Pi, Minecraft Snake

#import the minecraft.py module from the minecraft directory
import minecraft 
#import minecraft block module
import block 
#import time, so delays can be used
import time
#import random module to create random number
import random

def buildHouse(mc, x, y, z):

    HOUSEWIDTH=6
    HOUSEHEIGHT=2
    
    #draw floor
    mc.setBlocks(x,y-1,z,x+HOUSEWIDTH,y-1,z+HOUSEWIDTH,block.GRASS.id)
    
    #draw walls
    mc.setBlocks(x, y, z, x+HOUSEWIDTH, y+HOUSEHEIGHT, z, block.STONE.id)
    mc.setBlocks(x+HOUSEWIDTH, y, z, x+HOUSEWIDTH, y+HOUSEHEIGHT, z+HOUSEWIDTH, block.STONE.id)
    mc.setBlocks(x+HOUSEWIDTH, y, z+HOUSEWIDTH, x, y+HOUSEHEIGHT, z+HOUSEWIDTH, block.STONE.id)
    mc.setBlocks(x, y, z+HOUSEWIDTH, x, y+HOUSEHEIGHT, z, block.STONE.id)
    
    #draw windows
    mc.setBlocks(x+(HOUSEWIDTH/2)-2,y+1,z,x+(HOUSEWIDTH/2)-2,y+2,z,block.GLASS.id)
    mc.setBlocks(x+(HOUSEWIDTH/2)+2,y+1,z,x+(HOUSEWIDTH/2)+2,y+2,z,block.GLASS.id)

    #draw door
    #cobble arch
    mc.setBlocks(x+(HOUSEWIDTH/2)-1,y,z,x+(HOUSEWIDTH/2)+1,y+2,z,block.COBBLESTONE.id)
    # clear space for door
    mc.setBlocks(x+(HOUSEWIDTH/2),y,z,x+(HOUSEWIDTH/2),y+1,z,block.AIR.id)

    #draw torches
    mc.setBlock(x+(HOUSEWIDTH/2)-1,y+2,z-1,block.TORCH.id,1)
    mc.setBlock(x+(HOUSEWIDTH/2)+1,y+2,z-1,block.TORCH.id,1)
    
    #draw roof
    mc.setBlocks(x,y+HOUSEHEIGHT+1,z,x+HOUSEWIDTH,y+HOUSEHEIGHT+1,z+HOUSEWIDTH,block.WOOD_PLANKS.id)
    

#main program
if __name__ == "__main__":

    time.sleep(3)

    #Connect to minecraft by creating the minecraft object
    # - minecraft needs to be running and in a game
    mc = minecraft.Minecraft.create()

    #Post a message to the minecraft chat window 
    mc.postToChat("Why build when you can code")

    time.sleep(3)
    
    buildHouse(mc,0,mc.getHeight(0,0),0)
    mc.postToChat("Code yourself a house")

    time.sleep(10)

    buildHouse(mc,-10,mc.getHeight(-10,0),0)
    mc.postToChat("Run it again for a friend")

    time.sleep(10)

    mc.postToChat("Or create a whole town")
    for housesX in range(1,5):
        for housesZ in range(1,5):
            buildHouse(mc, housesX*10, mc.getHeight(housesX*10, housesZ*10), housesZ*10)
    
    mc.postToChat("www.stuffaboutcode.com")
    
