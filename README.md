# XKCD Password Generator

Flask application inspired by Web comic [XKCD 936](https://xkcd.com/936/ "xkcd's pass gen").

### Features:
 * *Number Substitution*
 * *Easy Typing*

#### Number Substitution

Number Substitution allows user to request that letters get swapped by number or
symbols. The dictionary below is used in implementation:
  * {"e":"3","s":"5","b":"8","o":"0","i":"!"}

#### Easy Typing
Easy typing rules are based on easiness keyboard strokes by having keys from both sides of
the keyboards "envenly" spread out with maximum deviation of ONE.
  * *Implementation:*
    * Keys on right side of keyboard receive the score of one.
    * Keys on left side of keyboard receive the score of minus one.
    * As the each password is read the program keeps track of overall score
      and return if score is *one, zero, or minus one.*

### XKCD Explained Best:
![alt text](static/img/password.png)
