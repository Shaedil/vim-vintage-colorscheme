" Name:         Vintage Airline theme
" Description:  A 'cool', dark airline theme 
" Author:       Shaedil Dider <shaedildider@gmail.com>
" Maintainer:   Shaedil Dider <shaedildider@gmail.com>
" Website:      https://github.com/Shaedil/vim-vintage-colorscheme
" License:      Vim License (see `:help license`)
" Last Updated: Tue 23 Jul 2019 11:06:35 PM EST

scriptencoding utf-8

let s:blck      = [ "#211e1a", 234 ] "bg color
let s:gry0      = [ "#282520", 234 ] "lighter bg color
let s:gry1      = [ "#a9a79e", 248 ] "regular grey
let s:gry3      = [ "#a2a097", 246 ] "light grey
let s:red       = [ "#a45444", 124 ] "crimson red
let s:gren      = [ "#7e9736", 34  ] "pale green
let s:gryblu    = [ "#94ABBE", 18  ] "Steel blue
let s:blue      = [ "#57a3c6", 24  ] "dark cyan
let s:oran      = [ "#baa118", 16  ] "dark gold brass
let s:purp      = [ "#414a99", 19  ] "almost indigo
let s:brwn      = [ "#866234", 100 ] "pale dirt brown
let s:whit      = [ "#f2f2f2", 255 ] "teeth white

" Normal mode [guifg,   , guibg,    , ctermfg,  , ctermbg,  ]
let s:N1 = [ s:gry0[0]  , s:whit[0] , 234 , 255 ] " A section
let s:N2 = [ s:whit[0]  , '#0087af' , 188 , 31  ] " B section
let s:N3 = [ s:whit[0]  , s:blck[0] , 188 , 234 ] " C section

" Insert mode
let s:I1 = [ s:gry0[0]  , s:whit[0] , 234 , 255 ] 
let s:I2 = [ s:whit[0]  , '#47AF00' , 255 , 70  ]
let s:I3 = [ s:whit[0]  , '#2E8700' , 255 , 28  ]

" Visual mode
let s:V1 = [ s:gry0[0]  , s:whit[0] , 234 , 255 ] 
let s:V2 = [ s:whit[0]  , '#B0AE00' , 255 , 184 ]
let s:V3 = [ s:whit[0]  , '#918F00' , 255 , 142 ]

" Replace mode
let s:R1 = [ s:gry0[0]  , s:whit[0] , 234 , 255 ] 
let s:R2 = [ s:whit[0]  , '#AF2800' , 255 , 124 ] 
let s:R3 = [ s:whit[0]  , '#872800' , 255 , 88  ]

let g:airline#themes#vintage#palette = {}

" Modified
let g:airline#themes#vintage#palette.normal_modified  = {
   \ 'airline_a': [ '#0087AF', s:whit[0], 31  , 255 , '' ] ,
   \ }
let g:airline#themes#vintage#palette.insert_modified  = {
   \ 'airline_a': [ '#47AF00', s:whit[0], 70  , 255 , '' ] ,
   \ }
let g:airline#themes#vintage#palette.visual_modified  = {
   \ 'airline_a': [ '#B0AE00', s:whit[0], 184 , 255 , '' ] ,
   \ }
let g:airline#themes#vintage#palette.replace_modified = {
   \ 'airline_a': [ '#AF2800', s:whit[0], 124 , 255 , '' ] ,
   \ } 

" Inactive
let s:IA = [ s:N2[0], s:N3[1]  , s:N2[2], s:N3[3], '' ] "inactive mode airline_a
let s:IB = [ s:N2[0], '#444444', s:N2[2], s:N1[3], '' ] "inactive mode airline_b
let s:IC = [ s:N3[1], s:N1[1]  , s:N3[3], s:N1[3], '' ] "inactive mode airline_c

let g:airline#themes#vintage#palette.normal   = airline#themes#generate_color_map(s:N1, s:N2, s:N3)
let g:airline#themes#vintage#palette.insert   = airline#themes#generate_color_map(s:I1, s:I2, s:I3)
let g:airline#themes#vintage#palette.visual   = airline#themes#generate_color_map(s:V1, s:V2, s:V3)
let g:airline#themes#vintage#palette.replace  = airline#themes#generate_color_map(s:R1, s:R2, s:R3)
let g:airline#themes#vintage#palette.inactive = airline#themes#generate_color_map(s:IC, s:IB, s:IA)
