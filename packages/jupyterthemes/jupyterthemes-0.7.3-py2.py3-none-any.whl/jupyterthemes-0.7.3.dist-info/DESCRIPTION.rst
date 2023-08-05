## Theme-ify your Jupyter Notebooks!

### Oceans16
![image](https://github.com/dunovank/jupyter-themes/blob/master/screens/oceans16_nb.png?raw=true)

### Grade3
![image](https://github.com/dunovank/jupyter-themes/blob/master/screens/grade3_nb.png?raw=true)

### Install jupyterthemes w/ pip (officially)
```sh
pip install jupyterthemes
```

### How to...
```sh
# can call with "jupyter-themes" or "jt" interchangeably
# list available themes
# oceans16 | grade3 | spacelegos | chesterish (New!) | onedark (New!)
jt -l

# install a theme...
jt -t grade3

# ...with toolbar (-T) enabled
jt -T -t grade3

# ...and adjust cell width [default=950 (pixels)]
jt -t grade3 -cw 850

# ...with alternate markdown/text-cell layout
jt -t grade3 -altmd

# set font (-f) and font-size (-fs) (defaults are Hack and 11)
jt -t grade3 -f Source-Code-Pro -fs 10

# set notebook (-ff) & textcell fontfamily (-tcff) (both default to sans)
jt -t grade3 -ff serif -tcff serif

# restore (-r) default theme
jt -r
```

#### mmmm so theme-y...


