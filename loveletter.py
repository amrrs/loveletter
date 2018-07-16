'''

This is a Python implementation of Christopher Strachey's "Loveletters" program (1952).

A simple port from the PHP version @ https://github.com/gingerbeardman/loveletter

'''

from random import randint
from random import choice as rc

sals1 = ["Beloved", "Darling", "Dear", "Dearest", "Fanciful", "Honey"]

sals2 = ["Chickpea", "Dear", "Duck", "Jewel", "Love", "Moppet", "Sweetheart"]

adjs = ["affectionate", "amorous", "anxious", "avid", "beautiful", "breathless", "burning", "covetous", "craving", "curious", "eager", "fervent", "fondest", "loveable", "lovesick", "loving", "passionate", "precious", "seductive", "sweet", "sympathetic", "tender", "unsatisfied", "winning", "wistful"]

nouns = ["adoration", "affection", "ambition", "appetite", "ardour", "being", "burning", "charm", "craving", "desire", "devotion", "eagerness", "enchantment", "enthusiasm", "fancy", "fellow feeling", "fervour", "fondness", "heart", "hunger", "infatuation", "little liking", "longing", "love", "lust", "passion", "rapture", "sympathy", "thirst", "wish", "yearning"]

advs = ["affectionately", "ardently", "anxiously", "beautifully", "burningly", "covetously", "curiously", "eagerly", "fervently", "fondly", "impatiently", "keenly", "lovingly", "passionately", "seductively", "tenderly", "wistfully"]

verbs = ["adores", "attracts", "clings to", "holds dear", "hopes for", "hungers for", "likes", "longs for", "loves", "lusts after", "pants for", "pines for", "sighs for", "tempts", "thirsts for", "treasures", "yearns for", "woos"]

last = ""

def salutation():
    return(rc(sals1) + " " + rc(sals2) + ", \n\n")

def short_sentence():
    return("%s You are my %s %s" % (last, rc(adjs), rc(nouns)))

def long_sentence():
    opt_adj1 = "" if randint(0,9) < 5 else rc(adjs)
    opt_adj2 = "" if randint(0,9) < 5 else rc(adjs)
    opt_adv1 = "" if randint(0,9) < 5 else rc(advs)
    return("%s My %s %s %s %s your %s %s" % (last, opt_adj1, rc(nouns), opt_adv1 ,rc(verbs), opt_adj2 ,rc(nouns)))

def sign():
    return(".\n\n     Yours %s,\n     M.U.C.\n"  % (rc(advs)))
ll = salutation()
for i in range(0,5):
    if randint(0,9) < 5:
        ll += short_sentence()
    else:
        ll += long_sentence()
    last = ". "

ll += sign()

print(ll)

with open("loveletter.txt","w") as file:
    file.write(ll)
file.close()

