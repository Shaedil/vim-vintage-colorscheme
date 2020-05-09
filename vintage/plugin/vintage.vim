scriptencoding utf-8
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" vintage.vim - Switch your colors to one based on a painting, image, etc
" Version: 0.1.0
" Author: Shaedil Dider <shaedildider@gmail.com>
" Maintainer: Shaedil Dider <shaedildider@gmail.com>
" License: This script is released under the Vim License.
" Last modified: 05/07/2020
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" check if script is already loaded
if !exists("g:loaded_vintage")
    finish
endif let g:loaded_vintage = 1
 
let s:global_cpo = &cpo " vi compatible mode in local var
set cpo&vim             " go into nocompatible-mode

let s:path = '~/.vim/plugged/vim-vintage/'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Commands
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

command! VintageSwitch :execute ':call vintage#SearchIntemediaryFile("'. input("filename: ") . '")'
command! VintageGenerate :execute ':call vintage#GenerateIntemediaryFile("'. input("filename: ") . '")'

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Functions
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Search files function using fzf or grep or something and display options
function! vintage#SearchIntemediaryFile(file)
    l:file
endfunction

" If image/painting does not have an intermediary file, run python3 script
function! vintage#GenerateIntemediaryFile(file)
    execute 'python3 ' . s:path . "sortcolors.py" . l:file
endfunction

" Create the colorfile
function! vintage#GenerateColorFile()
    execute "e " . s:path . "template.vim"
    execute "%s/g:black/" . s:black 
    execute "%s/g:gray/"  . s:gray 
    execute "%s/g:gray2/" . s:gray2 
    execute "%s/g:red/"   . s:red 
    execute "%s/g:green/" . s:green 
    execute "%s/g:yellow/". s:yellow 
    execute "%s/g:white/" . s:white 
    execute ":so template.vim"
endfunction
