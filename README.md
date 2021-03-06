# XKCD Password Generator :closed_lock_with_key:

* Flask application inspired by Web comic [XKCD 936](#xkcd-explained-best).
* Hosted on:
  * [Python Anywhere](http://tortellinibroseghini.pythonanywhere.com/) -> *Not Active*
  * [Heroku](https://xkcd-pass-gen.herokuapp.com/) -> *Not Active*

## Features:
 * *Number Substitution*
 * *Easy Typing*

## Number Substitution

Number Substitution allows user to request that letters get swapped by numbers/
symbols. The python dictionary below is used for number substitution:
  ```python
  number_substitute = {"e":"3", "s":"5", "b":"8", "o":"0", "i":"!"}
  ```

## Easy Typing
Easy typing rules are based on easiness keyboard strokes by having keys from both sides of
the keyboards "evenly" spread out with maximum deviation of ONE.
  * *Implementation:*
    * Keys on right side of keyboard receive the score of one.
    * Keys on left side of keyboard receive the score of minus one.
    * As each password is read the program keeps track of overall score
      and returns it if score is *one, zero, or minus one.*

## Language Support:
  * *English* :uk:
  * *French* :fr:
  * *Italian* :it:
  * *Spanish* :es:
  * *Portuguese* 🇧🇷
  * *Multilingual* :uk: :fr: :it: :es: 🇧🇷
  * *Star Wars* :space_invader:

## Install & Usage
* *From the command line:*
* `git clone git@github.com:RafaelBroseghini/XKCD-password-generator.git`
* `cd XKCD-password-generator`
* `python3 app.py`

## Modifications :hammer:
  * Modify password.py as desired to implement new password features or improve current ones.

## Future Work/Current Mods
  * Copy to clipboard plugin. (Current) -> [Check it out](https://github.com/RafaelBroseghini/XKCD-password-generator/tree/clipboard_plugin)

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :+1:

# XKCD Explained Best:
![alt text](static/img/password.png)
