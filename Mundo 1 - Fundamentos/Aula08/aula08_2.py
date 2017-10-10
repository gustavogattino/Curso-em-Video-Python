import random
import emoji
num = random.randint(0,42)
print('Seu número random é {} {}'.format(num, emoji.emojize(':joy:', use_aliases=True)))
