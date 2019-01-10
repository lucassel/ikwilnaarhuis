# ikwilnaarhuis

A Python CLI tool to help people who think 'IK WIL NAAR HUIS'.

# Usage

``` $ ikwilnaarhuis ```

Default behaviour, starts your day at runtime of the script. Yes, you will be typing 'ikwilnaarhuis' in your terminal to start your workday.

``` $ ikwilnaarhuis 9 ```

Starts your day at 9 o clock.

``` $ ikwilnaarhuis 9 15```

Starts your day at 9 : 15.

``` $ ikwilnaarhuis 9 15 -l 90```

Starts your day at 9 : 15, with a lunchbreak of 90 minutes.

``` $ ikwilnaarhuis 9 15 --lunch 90```

Starts your day at 9 : 15, with a lunchbreak of 90 minutes.

# Deployment

Install using ```pip install ikwilnaarhuis```

Build using ```python setup.py sdist bdist_wheel```

Upload using ```twine upload dist/*```
