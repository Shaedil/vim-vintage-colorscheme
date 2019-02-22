scriptencoding utf-8

let s:blck      = [ "#211e1a", 234 ] "black 211e1a
let s:gry0      = [ "#282520", 234 ] "A lighter shade of bg color
let s:gry1      = [ "#a9a79e", 248 ] "regular grey
let s:gry3      = [ "#a2A097", 246 ] "lighter grey
let s:red       = [ "#a45444", 124 ] 
let s:gren      = [ "#7e9736", 34  ]
let s:gryblu    = [ "#94ABBE", 18  ]
let s:blue      = [ "#57a3c6", 24  ] "skyblue
let s:oran      = [ "#baa118", 16  ] "orange b59b51
let s:purp      = [ "#414a99", 19  ] "purple
let s:brwn      = [ "#866234", 100 ] "brown
let s:whit      = [ "#f2f2f2", 242 ] "white

" Normal mode [guifg,    guibg,      ctermfg,    ctermbg,  ]
let s:N1 = [ s:gry0[0] , s:gry1[0] , s:gry0[1] , s:gry3[1] ] " A section
let s:N2 = [ s:gry0[0] , s:gren[0] , s:gry1[1] , s:gren[1] ] " B section
let s:N3 = [ s:gren[0] , s:gry0[0] , s:gry1[1] , s:gry0[1] ] " C section

" insert mode
let s:I1 = [ s:gry0[0]   , s:blue[0] , s:gry0[1] , s:blue[1] ] "black on blue
let s:I2 = [ s:gry0[0]   , s:gren[0]   , s:gry0[1] , s:gren[1]   ]
let s:I3 = [ s:blue[0] , s:gry0[0]   , s:gry3[1] , s:gry0[1]   ]

" visual mode
let s:V1 = [ s:gry0[0]   , s:oran[0]   , s:whit[1] , s:oran[1]   ] "black on yello
let s:V2 = [ s:gry0[0]   , s:gren[0]   , s:whit[1] , s:gren[1]   ]
let s:V3 = [ s:oran[0]   , s:gry0[0]   , s:oran[1] , s:gry0[1]   ]

" replace mode
let s:R1 = [ s:gry0[0]   , s:red[0]    , s:whit[1] , s:brwn[1]   ] "black on red
let s:R2 = [ s:whit[0]   , s:gren[0]   , s:whit[1] , s:brwn[1]   ] 
let s:R3 = [ s:red[0]    , s:gry0[0]   , s:red[1]  , s:gry0[1]   ]

let g:airline#themes#vintage#palette = {}

let g:airline#themes#vintage#palette.normal = airline#themes#generate_color_map(s:N1, s:N2, s:N3)

let g:airline#themes#vintage#palette.insert = airline#themes#generate_color_map(s:I1, s:I2, s:I3)

let g:airline#themes#vintage#palette.visual = airline#themes#generate_color_map(s:V1, s:V2, s:V3)

let g:airline#themes#vintage#palette.replace = airline#themes#generate_color_map(s:R1, s:R2, s:R3)

let s:IA = [ s:N1[0], s:N2[1], s:N3[2], s:N1[3], '' ]
let g:airline#themes#vintage#palette.inactive = airline#themes#generate_color_map(s:IA, s:IA, s:IA)
