You will need to create the following files:
1. palette.txt
2. defaults.txt 

The default background color is #FFFFFF\
A reference to `val` can either be a variable name or it can be a hex value.

## AA Accessibility
> <b>3.0:1</b> contrast ratio
* Text 18pt and above
* Bold text 14pt and above
* Icons and actionable graphics

> <b>4.5:1</b> contrast ratio
* Text 17pt and below
* Bold text 13pt and below


## Print/Set Commands
* `p bg` - print current background color
* `s bg #XXXXXX` - set current background color
* `p fg` - print the current foreground color
* `s fg #XXXXXX` - set the current foreground color
* `p text` - print the current text color
* `s text #XXXXXX` - set the current text color

## Contrast Ratio Commands
### Compare any two values
* `c val val` - compares two values

### Compare against background
* `c bg val` - gets the contrast ratio between the current background and another color
* `c bg` - gets the contrast ratio between every color in your palette and the current background
* `f bg var_name` - finds the values of var_name that gives you 3.0:1 and 4.5:1 contrast ratios with the current background color
* `f bg` - finds the values for each color in your palette that give you 3.0:1 and 4.5:1 contrast ratios with the current background color


### Compare against foreground
* `c fg val` - gets the contrast ratio between the current foreground and another color
* `c fg` - gets the contrast ratio between every color in your palette and the current background
* `f fg var_name` - finds the values of var_name that gives you 3.0:1 and 4.5:1 contrast ratios with the current foreground color
* `f fg` - finds the values for each color in your palette that give you 3.0:1 and 4.5:1 contrast ratios with the current foreground color

### Compare against text
* `c text val` - gets the contrast ratio between the current text and another color
* `c text` - gets the contrast ratio between every color in your palette and the current background
* `f text var_name` - finds the values of var_name that gives you 3.0:1 and 4.5:1 contrast ratios with the current text color
* `f text` - finds the values for each color in your palette that give you 3.0:1 and 4.5:1 contrast ratios with the current text color

### Multiple variable calculations
* `o bg text val` - calculates the opacity of "val" to create the proper 3.0:1 and 4.5:1 contrast ratios with the text. This assumes "val" is the layer above the background, and text is the layer above "val"
* `o bg fg val` - calculates the opacity of "val" to create the proper 3.0:1 and 4.5:1 contrast ratios with the foreground. This assumes "val" is the layer above the background, and foreground is the layer above "val"
* `o bg text -l level` - calculates the opacity of each color at "level" to create the proper 3.0:1 and 4.5:1 contrast ratio with the text color. This assumes the color at "level" is the layer above the background, and the text color is the layer above the color at "level"
* `o bg fg -l level` - calculates the opacity of each color at "level" to create the proper 3.0:1 and 4.5:1 contrast ratio with the foreground color. This assumes the color at "level" is the layer above the background, and the foreground color is the layer above the color at "level"