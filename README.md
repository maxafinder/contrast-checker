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


## Property Commands

### Print
* `p bg` - print current background color
* `p fg` - print the current foreground color
* `p text` - print the current text color

### Set
* `s bg #XXXXXX` - set current background color
* `s fg #XXXXXX` - set the current foreground color
* `s text #XXXXXX` - set the current text color

### Swap
* `swap bg fg` and `swap fg bg` - swap the background and foreground colors.
* `swap bg text` and `swap text bg` - swap the background and text colors.
* `swap fg text` and `swap text fg` - swap the foreground and text colors.

## Contrast Ratio Commands
References to "any" refer to bg, fg, text, or any variable/value (either in your palette or a hex value).
* `c any any` - gets the contrast ratio between these two colors.
* `c any -c color` - gets the contrast ratio between the color specified by "any" and every level of "color". 
* `c any` - gets the contrast ratio between this color and every color in your palette. 

## Find Commands
* `f any color` - finds the levels of the specified color that give you 3.0:1 and 4.5:1 contrast ratios with the color referenced by "any".
* `f any` - finds the levels of all colors in your palette that give you 3.0:1 and 4.5:1 contrast ratios with the color referenced by "any".

## Opacity Commands

# Old


### Multiple variable calculations
* `o bg text val` - calculates the opacity of "val" to create the proper 3.0:1 and 4.5:1 contrast ratios with the text. This assumes "val" is the layer above the background, and text is the layer above "val"
* `o bg fg val` - calculates the opacity of "val" to create the proper 3.0:1 and 4.5:1 contrast ratios with the foreground. This assumes "val" is the layer above the background, and foreground is the layer above "val"
* `o bg text -l level` - calculates the opacity of each color at "level" to create the proper 3.0:1 and 4.5:1 contrast ratio with the text color. This assumes the color at "level" is the layer above the background, and the text color is the layer above the color at "level"
* `o bg fg -l level` - calculates the opacity of each color at "level" to create the proper 3.0:1 and 4.5:1 contrast ratio with the foreground color. This assumes the color at "level" is the layer above the background, and the foreground color is the layer above the color at "level"