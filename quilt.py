import numpy as np
import random

print("Welcome to the Quilt program.\n")
height = int(input("Enter height for quilt:\n"))
width = int(input("Enter width for quilt:\n"))
colors = int(input("Enter number of colors for quilt:\n"))

def create_quilt(height, width, colors):
    
    #create a randomized quilt
    quilt = np.random.randint(1, colors, size=(height,width))

    #iterate through each row
    for i in range(0, quilt.shape[0]):
        
        #iterate through each col
        for j in range(0, quilt.shape[1]):
            current_block = quilt[i, j]
            all_colors = [color for color in range(1, colors+1)]
            neighboring_blocks = []
            
            #try pulling previous block
            try:
                neighboring_blocks.append(quilt[i, j-1])
            except:
                pass

            #try pulling top left diagonal block
            try:
                neighboring_blocks.append(quilt[i-1, j-1])
            except:
                pass
                
            #try pulling block above
            try:
                neighboring_blocks.append(quilt[i-1, j])
            except:
                pass
                
            #try pulling top right diagonal block
            try:
                neighboring_blocks.append(quilt[i-1, j+1])
            except:
                pass
            
            #try pulling next block
            try:
                neighboring_blocks.append(quilt[i, j+1])
            except:
                pass

            #try pulling bottom left diagonal block
            try:
                neighboring_blocks.append(quilt[i+1, j-1])
            except:
                pass
                
            #try pulling block below
            try:
                neighboring_blocks.append(quilt[i+1, j])
            except:
                pass
                
            #try pulling botttom right diagonal block
            try:
                neighboring_blocks.append(quilt[i+1, j+1])
            except:
                pass

            #if current block is the same as neighboring blocks
            if current_block in neighboring_blocks:
                
                #update possible colors list
                useable_colors = [color for color in all_colors if color not in neighboring_blocks]
                
                #check to see if you have enough colors
                if not useable_colors:
                    try:
                        #prompt user to add more colors to quilt
                        print("We need to add more colors to your quilt.")
                        colors = int(input("Enter a new number of colors for quilt:\n"))
                        create_quilt(height, width, colors)
                    except:
                        #return zero matrix if not enough colors in quilt
                        print("An unknown error has occured")
                        return np.zeros((height, width))
                
                #if you have enough colors, update the current block
                else:
                    #update current block
                    quilt[i, j] = random.choice(useable_colors)
    
    return quilt

q = create_quilt(height, width, colors)
print("Here is your Quilt Pattern \n")
print("-------"*q.shape[1])
print('\n\n\n'.join(['\t'.join([str(cell) for cell in row]) for row in q]))
