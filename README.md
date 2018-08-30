<table><tbody align="center">

<tr><td colspan='2'>
<img src="https://github.com/Shaedil/vim-vintage-colorscheme/raw/master/images/Banner.png" alt="Apollo and the Continents Asia  by Tiepolo, Giovanni Battista" />
<h4> <i>Feel the oils of the 1700's</i> </h4>
</td></tr>

<tr></tr>

<tr>
<td>
<br>
<img alt="screenshot of the vim-vintage color theme, light version" src="https://github.com/Shaedil/vim-vintage-colorscheme/raw/master/images/Vintage-light.png" width="430" />
<br>
</td>
<td>
<br>
<img alt="screenshot of the vim-vintage color theme, dark version" src="https://github.com/Shaedil/vim-vintage-colorscheme/raw/master/images/Vintage-dark.png" width="430" />
<br>
</td>
</tr>

<tr></tr>

<tr><td colspan='2'>
<br>
<p align="center">The Vim-Vintage colorscheme, also known as the Vi-Vintage colorscheme as I like to call it, was inspired by the <a hrel = "https://github.com/altercation/vim-colors-solarized">Solarized</a> colorscheme's subtleness. As well as the look and feel of oil pantings.</p>

</td></tr>

</tbody></table>

## Story
<p>    While I was listening to my Pandora and doing some vim, I came across a piece of beautiful playlist art. I looked from the art and to my vim screen and at once, I imagined the colors swirling like a toilet flush. I imagined my code onto that piece of art and the colors colliding into the text washing the entire screen with light colors. I scratched my nose, and I looked at more paintings that were similar, I found one in particular with more contrasting colors. At once, I imagined the painting filled black like the night, and the colors dancing and shooting across the screen like fireworks revealing text that were hidden. A day after (this was at night, mind you), I started to look into color compliments and accents and did more research... What you see before you is the result of that research.
<p>
    
## Installation
    
Installation is very simple, and I prefer to keep it simple. You can either use Tim Pope's [Pathogen](https://github.com/tpope/vim-pathogen) (recommended) or manually install it.

### Pathogen Installation 
1. Download and install Pathogen.
2. Clone my github repository using Git.

    a. **Cloning** 
    ```
    $ cd /.vim/bundle
    $ git clone git://github.com/Shaedil/vim-vintage-colorscheme.git
    ```
    
3. Then, move the vim-vintage-colorscheme directory into the .vim/bundles directory.  

    b. **Moving**
    In the parent directory of vim-vintage-colorscheme:
    ```
        mv vim-vintage-colorscheme /.vim/bundle/
    ```
    
4. (Optional) You can move the vim-vintage color file to your .vim/colors directory for those with less space

### Manual Installation
1. Download the zip file at the top right of the github repository
2. Extract into the .vim/bundles folder.
3. Move vintage.vim into the .vim/colors folder

## Configuration (Modify your .vimrc)
The commands are easy, because it's similar to other colorschemes:
    ```
    set background=dark
    colorscheme vim-vintage
    ```
Or, if you prefer using the light version try this:
    ```
    set background=dark
    colorscheme vim-vintage
    ```
If you have vim-airline or lightline, add that too.
    ```
     
    ```
**Important Note for Terminal Users** If your terminal is **not** compatible with my colorscheme please look to my temporary documentation for 16 color palette values. Thank you.

## License
    Please see my LICENSE.md file for more details on that.
