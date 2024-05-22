## General
You will need to create the following files:
1. palette.txt
2. defaults.txt 

The default background color is #FFFFFF, and the default foreground and text colors are #000000.\

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

## Opacity Commands
* `o any any opacity any` - if each value is stacked on top of each other from left to right, and the opacity is applied to the middle "any", then it calculates the contrast ratio with the last "any". 
* `o any any any` - if each value is stacked on top of each other from left to right, then the required opacity for the middle "any" is calculated to meet 3.0:1 and 4.5:1 contrast ratios with the last "any".
* `o any -l level any` - given a bottom color, level in your palette, and top color, this finds the opacity required for all colors at this level in your palette to meeet contrast ratios with the top color.
* `o any -l level1 -l level2` - given a bottom color, level1 in your palette, and level2 in your palette, this finds the opacity between level1 and level2 at each color in your palette to meet contrast ratios. 

## Blend Commands
* `b any any opacity` - given a bottom color, a top color, and a top color opacity, it blends these colors together to give you the resulting hex value.