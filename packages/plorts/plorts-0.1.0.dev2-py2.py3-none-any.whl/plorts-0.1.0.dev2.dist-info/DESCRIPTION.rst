# Plorts - Niceish python plots

Like seaborn but with less stuff and also it starts faster

## Example Code

```python
import plorts
import matplotlib
import matplotlib.pyplot as plt

# make it look nice and plorty
plorts.set_style()
plorts.set_color_palette(plorts.palettes.colorblind)
plorts.set_context(scaling=1.2, font_base=16)

# plot some stuff
plt.plot([0,2,3], [1,2,10], label="1")
plt.plot([0,2,3], [3,2,1], label="2")
plt.plot([0,2,3], [2,2,2], label="3")
plt.legend(loc='best')
plt.axis(xmin=0, ymin=0)

# creates the directories and everything!
plorts.savefig('output/test.png)

plt.tight_layout()
plt.show()
```

## Example output

![](output/test.png)


