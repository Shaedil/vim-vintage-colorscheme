" Name:         Vim-Vintage
" Author:       Shaedil
" Maintainer:   Shaedil
" License:      MIT

" Set an error message if the user's terminal has < 256 colors.
if !(has('termguicolors') && &termguicolors) && !has('gui_running')
        \ && (!exists('&t_Co') || &t_Co < 256)
    echoerr '[Vim-Vintage] There are not enough colors'
    finish
endif

" Clear any default/user settings for syntax highlighting 
hi clear
if exists('syntax_on')
    Syntax reset
endif

" Set the colorscheme name to Vim-Vintage
let g:colors_name = 'vim-vintage'

" If the user picked 'dark' background:
if &background ==# 'dark'
    hi
    hi
    hi
    hi
    hi
    ...
    finish
endif

"else, use the light colorscheme
