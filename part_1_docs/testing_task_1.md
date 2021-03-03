### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

  # Class doesn't start with an def __init__(self): method.
  def check_for_ace(self, card):
    if card.value = 1: # possibly wrong should be card.value == 1:
      return True
    else # colon is missing 
      return False
   

 
 
  
  dif highest_card(self, card1 card2):  # Spelling error in the word 'dif' should be 'def'.
  if card1.value > card2.value: # There is an indent error.
    return card # typo needs to be card1.
  else:
    return card2
  


# Indent is off here as well.
def cards_total(self, cards):
  total # total does not have anything associated with it. Should be an = 0.
  for card in cards:
    total += card.value
    return "You have a total of" + total # return statement needs to be indented back.
  
```
