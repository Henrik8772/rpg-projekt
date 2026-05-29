I started by building up the foundation of tkinter.

when that was done I continued with design for some god damn reason.

I made a TO DO list to know what I have done and what I want to do.

I have finished the fight system but I will fix it so that you take damage from the monster too

I have now started building a stat menu in the battle system so the player can see their hop and heals if they have any, and I am also trying to find a good way to hide decimals that end up in, for example, the gold part in the game menu.

I have fixed the stats and battle system as well as the decimal overflow my goal with this project was precisely the battle system and now it is finished so now I will build on other things such as shop and inventory and such.

Changed the encounters to "classes" so that only monsters with the same id as the location id can be randomly selected, so that for example Bats can only "spawn" in the Cavern and so on.

i want to fix more features such as inventory and items and shops that reset with random items and stuff.

Adding stuff for a pressure system to make the battles more random and harder.

Fixed the pressure system but now i am dying on the inside while trying to make a boss fight based on that u drop a boss spawn item that then goes into your inventory and from there the system checks if u have it if u do then a boss button will appear in the encounter screen and so on.

I have started to build the boss battle system so it will be done soon if everything goes well.

I have finished building the boss battle system, i fixed some small issues with the drop system and i have also fixed som ui problems.
This took some time but is now done.'

I have added some small fixes so that the bosses attacks work properly and that rapid smash scales with hits and all attacks scale with accuracy as well





Everything should work as intended the things that doesnt do anything would be the shop button, the credits button, only goblins in the forest area drops loot, the item drop Goblin Kings Fury doesnt give any stat increase when droped, player crit rate doesn't do anything, there is only one boss and it is the Goblin King.

The battle system uses two main features first it gives you a randomized monster with a randomized pressure lvl, it uses an identification system comprised of ID that looks at if the place id aka the button u click, forest, mountains, cavern it checks if the mosnters in the pool has an id that matches with the place id, it picks a random monster with said id and then gives a random number from 1 to 100 and if it is above/under or equal to a certain number range it will set a pressure lvl. The hp is also randomized between two numbers.

Secondly the battle system it self aka the attacks and stuff, they make use of a combobox to select magic/skills that have a set dmg, we then use a button to link the choice together with an action, so if u dont select a spell or skill and click confirm it just returns u to the selection. 

The spells also take mana so the player has a set mana at 100 which cant be increased since i didnt fix anything like that, when u dont have mana to use a spell it will give a warning message and return u to the selection. You may see i have added a skill called DEBUGGER well that is bc i used it to test out stuff since it 1 taps anything even the boss which wont be killed normally bc i forgot to scale stuff propperly if i have time after this i might add a quick lvl system to fix the scaling.

This game is a rouge like rpg so if u die well then it is game over and u need to restart for the begining again. One of the main features of this program is that we have an inventory where drops from mobs go, this is also how the boss fight works, so by dropping an item called Kings Idol when it goes into ur inventory then the next time you get to the explore screen again you will find a new button called CHALLANGE GOBLIN KING, clicking this button will result in a boss fight, which you cant use the run away button in since it is a boss fight, when you defeat the boss you are rewarded with a good sum of gold and after that the boss item gets removed from your inventory.

Every pressure lvl of a goblin can drop the item tho it is easier to get from lvl 4 and is garantied from lvl 5 mobs. Every lvl drops basic drops, while only normal monsters aka pressure lvl 0 monsters only drops basic drops. 

There are 5 loot tiers, the normal one being basic loot, the one from lvl 1 to lvl 3 pressure monsters being monster loot, the one from lvl 4 being rare loot, the lvl 5 one being elite loot and lastly the universal one being granted loot aka garantied drops which only lvl 5 monsters drop so far.

The pressure lvls isnt just drops and for the monsters to feel unik no no it also makes the monsters harder to beat by increasing there hp and decreasing your chance of escape when using the run away button.

I would say i really am happy with what i was able to finish with in this time, there are so many things i could do better such as focus on one thing at a time and find ways to make the code more structured, i hade some problems while making this such as numbers displaying decimals and monstes and drops becoming infinite loops of the same thing over and over. When i look back at the code i still dont understand how i managed to have the problems i had when the solutions seemed so simple, i have used help from webbsites such as geeksforgeeks and python docs, i have also taken my time at home looking stuff up so that i know where to look when something goes wrong and idk how to fix it, a great place for me to find solutions to certain problems was asking people that i talk to who have used python more then me, i did tell them it was for a school assignment so they dont give me the codes and shit.  But most of my help was found in stack overflow forum where i looked up certain problems and looked at what people had suggested others, i then looked up the specific commands used to get a better understanding on what actually happened and how the commands work.

I strongly recommend taking help from others if you dont understand stuff or you have gotten stuck, that doesn't mean ask AI for the awnser, if you use AI then use it properly like asking for advice on what could be done to the code but always remeber to specify that you dont want them to write the code and rather want AI to explain stuff you dont understand or give you a little push such as asking you what would happen or what do you think would happen, maybe even get it to give you a report on what the error message means, AI is a really good tool if used correctly, if you use AI to explain something or to help you in a guided learning way it is a really good tool but if you use it to write code then you wont learn anything.

But the best advice would be to ask your teacher for help or try and google the problem and check if someone has had the same issue and see how they solved it, dont take their code instead de construct the code step by step and learn from the help, this will help you understand the problem and maybe find a different solution to the issue.

I took great help from others when i didnt know what to do, even just looking up a list of commands for certain stuff in your code is enough to get you on the right track so that you can hopefully solve the issue. I mean look at how i solved the decimal issues, i thought it would take so long to fix but after looking it up and getting an explanation to how you can fix it and learning how it works. I mean all i did was add :.0f after the things that needed decimals removed / hidden and it worked, all that :.0f does is hide every number after the decimal point, for example :.1f hides every number but the first one after the decimal point.

I really liked this assignment since we get to write code for something we want to write code for so yeah it was fun but also a hell since when i got stuck or something didnt work it took some time to find a solution even with help some of the problems took longer then others.


