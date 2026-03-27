##fortune_cookie.py

import random;
##rand int for lucky number
lucky_number = random.randint(1,50);
### rand int between 1-5 for phrase assignment
sentence_number= random.randint(1,5)

##5 phrases that sound like they would come from a fortune cookie
if sentence_number == 1:
    printed_phrase= "Bamboo sprouts so fast and so tall, only to fall to the humble panda."

if sentence_number == 2:
    printed_phrase= "Many small droplets of water will eventually carve stone."

if sentence_number ==3:
    printed_phrase = "A small risk today will open a big door tomorrow."

if sentence_number == 4:
    printed_phrase= "Forbidden fruits create the best jams."

if sentence_number == 5: 
    printed_phrase = "To cultivate a perfect bonsai, one must have much patience"

print(f"{printed_phrase}");
print(f"Your lucky number on this fine day is: {lucky_number}");


