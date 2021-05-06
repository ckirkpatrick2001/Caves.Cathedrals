# ----------------------------------------------------------
# --------             Caves to Cathedrals Final              ---------
# ----------------------------------------------------------
# This game a chose your own adventure game where you can chose different paths
# and try to survive to the end
# ----------------------------------------------------------
# Name:Chase Kirkpatrick
# ----------------------------------------------------------

print('''INTRUCTIONS: When prompted to enter something [this/that], make sure that you enter it exactly as it is displayed onscreen.
If you get to the end of a bubble of text and the game does not prompt you to enter anything, simply press enter and the game will continue. Good Luck!\n''')

username = input("What is your name: ")

print("\nWelcome, " + username + ''', to a chose your own adventure game. This game will allow you to travel down a
series of paths while exploring different outcomes based on your choices. Many of the choices and events that you will encounter
are based on true events that wehave either learned about in class or are similar.\n''')

direction0 = input("The Medieval ages were difficult and dangerous times. Are you ready to begin? [yes/no] ")
if direction0 == "yes" :
    print("\nLet us begin.")
if direction0 == "no" :
    print("\nIf you are not ready, why are you here? Although I must say, it is already to late. Let us begin.\n")

print('''\nThe year is 1134 and you are a simple man living in medieval England. Canterbury to be exact. During you time
growing up there,a religious figure named Thomas Becket has risen to power. He served as the Royal Chancellor and was
now the Archbishop of Canterbury. One day you are walking towards the cathedral in town and someone calls out, "The kings knights
are coming". You have no reason to suspect anything is wrong so you continue on your way to the cathedral.\n''')
input()
print('''As you are standing in the cathedral, the knights arrive at the door demanding Thomas Becket to come out. They
claim that he is a traitor to the king. It is well known that you cannot be arrested on religious grounds so these knights
have no juristiction here.''')

#The Murder of Thomas Becket
direction1 = input("Do you stand by your religious beliefs and prevent the knights from going in, or do you stand aside? [fight/run] ")
if direction1 == "run":
    print('''\nYou step aside to let the knights run past. You aren't sure what is happening so you follow them at a safe distance.
You hear Becket screaming up ahead and see him holding on to one of the pillars. The knights try to pry him off but he refuses to get go.
The three knights then all raise their swords and bring them down on him. He is dead within seconds and his blood stains their swords
and the floor of the cathedral.''')
    input()
    print('''When you get home, you decide that Canterbury is no longer where you want to live. You hear rumors of a great cathedral
being built in France. "There will be jobs there," you think to yourself. While you are no builder, you have always been able to scrape together
enough money to get by. So you pack up your limited belongings and begin on your way. It is a long journey that will take many months, so you plan to make stops along the way.''')
    input()
    print('''\nOn your way there you encounter a group of people planning to make a trek to the Holy Land. They say that they are going on a crusade to
protect their religion as well as become rich. They say that you should join them as you are a christian yourself and it is your duty to protect and fight for your religion.
You realize that you are low on money and that the idea of becoming rich doesnt seem like a terrible option. However, you're not entirely sure if you want to go.''')
#Crusade
    direction2 = input("Do you decide to join these crusaders on their jounrey or do you continue south to France? [Crusade/France] ")
    if direction2 == "Crusade":
            print('''\nWe are excited to have you on our journey, one of the men proclaims. The men provide you with a horse and armour and then you are on your way.
You travel east towards Constantinople. A couple months later you arrive. Your army begins the takeover of the city. Many of the other soldiers loot, destroy, and
ransack much of the city.You decide to take part too.''')
            input()
            print('''You aquire many treasure and gold. You discover that many of the religious places of worship contain priceless artifacts. As a result, you steal as many as you can.
Many ancient Greek and Roman artifacts are taken as well. You finish  conquering the city and decide that it is time to head back home with your newly found wealth.\n''')
#Cathedral
    print('''\nYou arrive in France and seee the new Beauvais Cathedral being built. It is nothing like you have seen before: it was much higher and grander than any building.
There were supports on the outside of the building, a peculiar addition that must have been newly invented. You decide to go inside and your breath is taken away. There are stained
glass windows with light pouring in. The columns supporting the weight of the ceiling were so thin. And the ceilings had pointed arches as well. This was certainly a technological
marvel. With you're newly aquired wealth, you decide to settle down here for a while.''')
    input()
    print('''A couple days later, you hear of a ceremony happening at the cathedral. It has only been a couple of days since you arrived in town and you are quite tired from your journey.
Yet the cathedral has such capitivating beauty that you want to see it any oppertunity that you get. Still, you feel like something is wrong and you shouldn't go.''')
    direction3 = input("Do you listen to your gut and stay home or do you go to the ceremony? [stay/go] ")
    if direction3 == "stay" :
        print('''\nYou decide to stay home and notice that there is a storm brewing outside.You shut the windows and doors and start making yourself a cup of tea and a warm meal.
As you are sitting at the table eating, you feel the floor underneath your feet shake. You wonder what it could be since there is no thunder outside. However, you aren't given much
time to think as soon you begin hearing cries coming from outside. You walk outside and everyone is running towards the cathedral.You stop someone to ask what happened and they exclaim,
“The Cathedral. It collapsed”. You then run towards the other side of town to the cathedral. The ceiling collapsed. People aren't sure why it happened but some are saying that the high
winds caused the high parts of the cathedral to sway and crack.''')
        input()
        print('''You realize that there was something from stopping you from going to the cathedral today. One of the other people says, “thank God”, and quite frankly you agree
with them.  Maybe God was trying to send you a message. Maybe staying here isn't what God wants for you. You come to the decision that you need to become closer with God, as he has saved
you once again. You remember back to when the crusaders mentioned that there was a pilgrimage that he was planning on doing called the Santiago De Compostela. The crusader mentioned that
the pilgrimage purifies the soul and shows your devotion to God as a christian.\n''')
        direction3 = input("Do you begin this long walk to the city of Santiago De Compostela? [yes/no] ")
#Pilgrimage
        if direction3 == "yes":
            print('''\nAs you travel the way of Saint James, you get to see much of northern Spain. You meet many others doing the same pilgrimage as you. Along the way, you stop at
many small towns that have churches with religious relics. After a long day of hiking, you come to the town where you will be spending the night. It is late so all the places to eat are closed.
As a result, you head into the church hoping that they will have some food to feed you. You walk in and realize that it is completely empty except for you and another figure dressed in robes.
You walk around the church examining the beautiful sculptures and architecture. When you approach the front of the church, you get a more clear site of this man in robes.He is carefully taking
the relic out of the case. “Suspicious” you think to yourself.''')
            input()
            print('''You ask him, “what are you doing with that?”, to which he responds with, \n\n“I am a monk here.I am simply cleaning the relic for our good God so he may continue to
bless us with miracles.”\n\nYou take a good look at the relic and continue on your way to bed.''')
            input()
            print('''The next morning the talk of the town is that the relic has been stolen! People have many theories as to what happened but you yourself are quote sure that it was
the monk that stole it. You decide to go to the church to talk to the bishop. You find him sitting in his office and exclaim to him, “I saw the monk take the relic last night”.\n “Nonsense” the
bishop adds. “The relic was never stolen. Go look for yourself.” You head back down to the main area and see that the relic is there. Yet something looks off about it. You take a closer look and
realize that this is not the same relic that was there last night! The bishop must be aware that this is a fake.  He sees it every day!''')
            print('''\nYou can’t believe that a bishop would willingly put a fake relic in a church. \n\n“The people must know about this,” you think to yourself."''')
            direction4 = input("\nDo you announce that the relic is fake to the townspeople or do you keep it to yourself? [announce/self] ")
#Stolen Relic
            if direction4 == "self":
                print('''\nThe next morning, you decide to get out of town and continue on your pilgrimage. Nothing good ever comes of staying in a place where people you are supposed to be able
to trust are corrupt. You continue walking towards the coast of Spain.''')
                input()
                print('''Finally, after months of walking and seeing various towns and churches, you reach Santiago de Compostela. The cathedral stands tall in the center of the town,
towering over everything. You go inside and pay your respects to Saint James. As you sit in the church, you reflect on your journey here. It all started the day that you left Canterbury. You
thank God for taking you on this journey and finally realize that this is exactly where you want to be.\n\n[GAME OVER, CONGRATULATIONS]''')
            else:
                print('''\nYou decide to head to the townsquare to let everyone know that the relic is fake. The people must know that the church is lying to them. You get to the center green
and start yelling that the relic is fake. Soon enough, you have a large group of people surrounding you listening. Yet no one seems to be doing anything. hen you hear a voice yell
out, “arrest this man.” It’s the bishop. “He is spreading dangerous lies. That relic is obviously real.” You try to explain that you saw a monk take it last night but to no avail.\n''')
                input()
                print('''\nYou are taken to the jail where you sit there. You think about why the Bishop would lie and what he gains from it. You realize that without the relic, the whole
town would collapse. No one would come visit, and as a result the economy would collapse. People would never stop on their pilgrimage. Yet you have no one to tell this too as you sit in the jail
cell. The Bishop knows if you ever get out, it would be the death of the town.\n\n[GAME OVER]''')
        else:
            print('''\nYou decide not to go in this pilgrimage and stay home. You settle down and find work but you can't shake the feeling that you are missing something in your life.
Maybe in another life, you'll take another path.\n\n[GAME OVER]''')
    else:
        print('''\nYou cross the town and head through the streets towards the cathedral. You feel a strong gust of wind and realize that there is a storm brewing. You quickly hurry
to the cathedral. You take a seat in the pews and listen to the beautiful hymns being sung. As you listen, you look around that this modern marvel. You look up at the ceiling and realize that it's
moving. "That's not possible," you think to yourself. Yet it was possible. Becuase the cathedral was so tall, the building was more susceptible to the forces of wind. As the song finishes,
a large burst of thunder cracks overhead. Dust begins to fall from the ceilings and cracks form. Then, within seconds, the ceiling collapses. You try to run out to safety, but you are not quick
enough.\n\n[GAME OVER]''')
else:
    print('''\nYou say to the knights, "You cannot enter and arrest this man. He is on Holy ground". Yet before you can finish your sentence
a knight draws his sword and stabs you straight in the chest. As you fall to the ground, the last thing you see is the knights
going into the cathedral dragging their bloody swords, on their way to kill Thomas Becket.\n\n[GAME OVER]''')

