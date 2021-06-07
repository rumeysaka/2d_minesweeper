import random
import sys
ground = [0,0,0,0,0,0,0,0,0,0]
print(len(ground))
numOfMines = int(input('How many mines you like to plant?:'))
found=False
mine_set=[]

def plant_mines():
    for i in range (0,(numOfMines)):
        mine_index=random.randint(0,9)

        while mine_index in mine_set:
            mine_index=random.randint(0,9)

        if mine_index not in mine_set:
            mine_set.append(mine_index)
            ground[mine_index] = 1


    print(mine_set)
    print(ground)

def dig_hole(found=False):
    used_indexes=[]
    index=int(input('Pick your desired location:'))

    while True:
        if ground[index]==1:
            for i in range (len(ground)):
                if i in (used_indexes):
                    print('0',end=' ')
                    continue
                if ground[i]==1:
                    print("*",end =' ')
                    continue
                print('_', end=' ')
            print()
            print('GAME OVER')
            found=True
            break

        elif ground[index]==0:
            used_indexes.append(index)
            print(used_indexes)
            if ground[max(0,index-1)]==1 or ground[min(index+1,9)]==1:
                print('you have neighboring bombs')
            for i in range(len(ground)):
                if i in (used_indexes):
                    print('0',end=' ')
                    continue
                print('_',end=' ')
            #print(bomb_list)
            # for i in range (len(ground)):
            #     if i==index:
            #         print('0',end=' ')
        #     #     print('_',end =' ')
        # elif len(used_indexes)==len(ground)-(numOfMines):
        #     print('You win...')


    #sys.exit()


        print()
        safe_locs= (len(ground) - numOfMines) - len(used_indexes)
        print('You have ',safe_locs,' locations left... ')

        if safe_locs==0 and found==False:
            print('You win...')
            for i in range (len(ground)):
                if i in (used_indexes):
                    print('0',end=' ')
                    continue
                if ground[i]==1:
                    print("*",end =' ')
                    continue
                print('_', end=' ')

            break

        index=int(input('Pick your next location:'))
        if index>9:
                print('Please pick a location in required range:')

    #print(ground[index])



plant_mines()
dig_hole()