import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
table=[]
d_table=[]
your_card=(random.sample(cards, 2))
dealer=(random.sample(cards, 2))
#print(dealer)
your_card_sum=0
dealer_card_sum=0
for card in your_card:
    your_card_sum+=card
#print(your_card_sum)
for card in dealer:
    dealer_card_sum+=card
#print(dealer_card_sum)
print(f'Your cards :{your_card} , current score:{your_card_sum}')
print(f'Computer first card: {dealer[0]}')
rep=True
while rep==True:
    new_card=input("Y if new card and N if pass ").lower()
    if new_card=="y":
        table.append(random.choice(cards))
        #d_table.append(random.choice(cards))
        if 11 in table:
            if your_card_sum <= 10:
                your_card.append(11)
                your_card_sum+=table[0]
                print(f'Your cards :{your_card} , current score:{your_card_sum}')
                print(f'Computer first card: {dealer[0]}')
                table.clear()
            else:
                your_card.append(1)
                your_card_sum+=1
                print(f'Your cards :{your_card} , current score:{your_card_sum}')
                print(f'Computer first card: {dealer[0]}')
                table.clear()
        else:
            your_card.append(table[0])
            your_card_sum += table[0]
            print(f'Your cards :{your_card} , current score:{your_card_sum}')
            print(f'Computer first card: {dealer[0]}')
            table.clear()
            if your_card_sum>21:
                print("YOU LOSE")
                print(f'Your cards :{your_card} , current score:{your_card_sum}')
                print(f'Computer cards: {dealer},Computer score:{dealer_card_sum}')
                break
            else:
                pass
        d_table.append(random.choice(cards))
        if 11 in d_table:
            if dealer_card_sum <= 10:
                dealer.append(11)
                dealer_card_sum += d_table[0]
                d_table.clear()
                #print(dealer)
            else:
                dealer.append(1)
                dealer_card_sum += 1
                d_table.clear()
                #print(dealer)
        else:
            dealer.append(d_table[0])
            dealer_card_sum += d_table[0]
            d_table.clear()
            #print(dealer)
    else:
        print(f'Your cards :{your_card} , current score:{your_card_sum}')
        print(f'Computer cards: {dealer},Computer score:{dealer_card_sum}')
        if dealer_card_sum>your_card_sum:
            print("Computer has won")
        elif dealer_card_sum<your_card_sum:
            print("You won")
        else:
            pass
        rep=False
        break


