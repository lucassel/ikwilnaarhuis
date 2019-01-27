# ikwilnaarhuis

A Python CLI tool to help people who think 'IK WIL NAAR HUIS'.

![https://imgix.ttcdn.co/i/product/original/0/532772-51cb22d9b8f04f71bd347ed4b7fb07c4.jpeg?q=100&auto=format%2Ccompress&w=1000]

# Usage

``` $ ikwilnaarhuis ```

Default behaviour, starts your day at runtime of the script. 

Yes, you will be typing 'ikwilnaarhuis' in your terminal to start your workday.

``` $ ikwilnaarhuis -t 9 ```

Starts your day at 9 : 00 with a default lunchbreak of 60 minutes.

``` $ ikwilnaarhuis -t 9 15```

Starts your day at 9 : 15 with a default lunchbreak of 60 minutes.

``` $ ikwilnaarhuis 9 15 -l 90```

Starts your day at 9 : 15 with a custom lunchbreak of 90 minutes.

``` $ ikwilnaarhuis 9 15 --lunch 90```

Starts your day at 9 : 15, with a custom lunchbreak of 90 minutes.

# Deployment

Install using ```pip install ikwilnaarhuis```

Build using ```python setup.py sdist bdist_wheel```

Upload using ```twine upload dist/*```
