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

HOUSEWIDTH=6
HOUSEHEIGHT=2

def buildHouse(mc, x, y, z):
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

def clearHouse(mc, x, y, z):
    mc.setBlocks(x,y-1,z,x+HOUSEWIDTH,y+HOUSEHEIGHT+1,z+HOUSEWIDTH,block.AIR.id)
    

#main program
if __name__ == "__main__":

    time.sleep(3)

    #Connect to minecraft by creating the minecraft object
    # - minecraft needs to be running and in a game
    mc = minecraft.Minecraft.create()

    playersPath = []
    lastPlayerPos = mc.player.getTilePos()
    playersPath.append(lastPlayerPos)

    lastHousePos = None

    while(True):
        playerPos = mc.player.getTilePos()
        if playerPos != lastPlayerPos:
            playersPath.append(playerPos)
        lastPlayerPos = playerPos

        #when a player has moved 15 blocks, moved their house and reset the path
        if len(playersPath) == 15:

            #clear the old house (if there was one)
            if lastHousePos is not None:
                clearHouse(mc, lastHousePos.x, lastHousePos.y, lastHousePos.z)
            
            #create house 10 blocks back, we dont want the house on top of us!
            lastHousePos = playersPath[5]
            lastHousePos.y = mc.getHeight(lastHousePos.x,lastHousePos.z)
            buildHouse(mc,lastHousePos.x, lastHousePos.y, lastHousePos.z)
            
            #clear list
            playersPath[:] = []
            
        
