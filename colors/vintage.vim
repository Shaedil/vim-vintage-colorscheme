" Name:         Vintage
" Author:       Shaedil
" Maintainer:   Shaedil
" License:      MIT

if version > 580
	hi clear
	if exists("syntax_on")
		syntax reset
	endif
endif
let g:colors_name = "vintage"
set t_Co=256

"red = #a45444
"orange = #b59b51
"yellow = #DBBBA3
"green = #546424
"lightblue = #57a3c6
"grayblue = #94ABBE
"brown = #866234
"purple = #997069
"grey = #a9a79e
"black & background = #211E1A
"white = #FFFFFF

hi Normal guifg=#a9a79e guibg=#211e1a guisp=#211e1a gui=bold ctermfg=246 ctermbg=234 cterm=bold 
hi IncSearch guifg=#eb5e00 guibg=NONE guisp=NONE gui=NONE ctermfg=166 ctermbg=NONE cterm=NONE
hi WildMenu guifg=#073642 guibg=#eee8d5 guisp=#eee8d5 gui=NONE ctermfg=23 ctermbg=230 cterm=NONE
hi SignColumn guifg=#657b83 guibg=#bebebe guisp=#bebebe gui=NONE ctermfg=66 ctermbg=7 cterm=NONE
hi SpecialComment guifg=#64625d guibg=NONE guisp=NONE gui=NONE ctermfg=160 ctermbg=NONE cterm=NONE 
hi Typedef guifg=#b59b51 guibg=NONE guisp=NONE gui=NONE ctermfg=136 ctermbg=NONE cterm=NONE 
hi Title guifg=#94abbe guibg=NONE guisp=NONE gui=bold ctermfg=137 ctermbg=NONE cterm=bold
hi Folded guifg=#657b83 guibg=#eee8d5 guisp=#eee8d5 gui=bold ctermfg=66 ctermbg=230 cterm=bold
hi PreCondit guifg=#866234 guibg=NONE guisp=NONE gui=NONE ctermfg=166 ctermbg=NONE cterm=NONE
hi Include guifg=#cb4b16 guibg=NONE guisp=NONE gui=NONE ctermfg=166 ctermbg=NONE cterm=NONE
hi Float guifg=#57a3c6 guibg=NONE guisp=NONE gui=NONE ctermfg=37 ctermbg=NONE cterm=NONE
hi StatusLineNC guifg=#797979 guibg=#211e1a guisp=#211E1A gui=NONE ctermfg=66 ctermbg=235 cterm=NONE
hi CTagsMember guifg=#e2e4e5 guibg=NONE guisp=NONE gui=NONE ctermfg=254 ctermbg=NONE cterm=NONE
hi NonText guifg=#a9a79e guibg=NONE guisp=NONE gui=bold ctermfg=37 ctermbg=NONE cterm=bold
hi CTagsGlobalConstant guifg=#e2e4e5 guibg=NONE guisp=NONE gui=NONE ctermfg=254 ctermbg=NONE cterm=NONE
hi DiffText guifg=#57a3c6 guibg=NONE guisp=NONE gui=NONE ctermfg=73 ctermbg=NONE cterm=NONE
hi ErrorMsg guifg=#a45444 guibg=#211e1a guisp=#211e1a gui=NONE ctermfg=13 ctermbg=234 cterm=NONE
hi Ignore guifg=#ffffff guibg=NONE guisp=NONE gui=NONE ctermfg=15 ctermbg=NONE cterm=NONE
hi Debug guifg=#a45444 guibg=NONE guisp=NONE gui=NONE ctermfg=160 ctermbg=NONE cterm=NONE
hi PMenuSbar guifg=#a9a79e guibg=#7a7a7a guisp=#7a7a7a gui=NONE ctermfg=249 ctermbg=243 cterm=NONE
hi Identifier guifg=#57a3c6 guibg=NONE guisp=NONE gui=NONE ctermfg=103 ctermbg=NONE cterm=NONE
hi SpecialChar guifg=#a45444 guibg=NONE guisp=NONE gui=NONE ctermfg=160 ctermbg=NONE cterm=NONE
hi Conditional guifg=#a5bf73 guibg=NONE guisp=NONE gui=NONE ctermfg=72 ctermbg=NONE cterm=NONE
hi StorageClass guifg=#b59b51 guibg=NONE guisp=NONE gui=NONE ctermfg=136 ctermbg=NONE cterm=NONE 
hi Todo guifg=#997069 guibg=#211e1a guisp=#211e1a gui=bold ctermfg=161 ctermbg=234 cterm=bold
hi Special guifg=#a45444 guibg=NONE guisp=NONE gui=NONE ctermfg=167 ctermbg=NONE cterm=NONE
hi LineNr guifg=#585858 guibg=#211E1A guisp=#211E1A gui=NONE ctermfg=101 ctermbg=234 cterm=NONE
hi StatusLine guifg=#797979 guibg=#262422 guisp=#262422 gui=bold ctermfg=66 ctermbg=235 cterm=bold
hi Label guifg=#546424 guibg=NONE guisp=NONE gui=NONE ctermfg=106 ctermbg=NONE cterm=NONE
hi CTagsImport guifg=#B5B4AA guibg=NONE guisp=NONE gui=NONE ctermfg=254 ctermbg=NONE cterm=NONE
hi PMenuSel guifg=#ffffff guibg=#a9a79e guisp=#a9a79e gui=NONE ctermfg=15 ctermbg=245 cterm=NONE
hi Search guifg=#263238 guibg=#e6db74 guisp=#e6db74 gui=NONE ctermfg=1 ctermbg=236 cterm=NONE
hi CTagsGlobalVariable guifg=#a9a79e guibg=NONE guisp=NONE gui=NONE ctermfg=254 ctermbg=NONE cterm=NONE
hi Delimiter guifg=#a45444 guibg=NONE guisp=NONE gui=NONE ctermfg=160 ctermbg=NONE cterm=NONE
hi Statement guifg=#a5bf73 guibg=NONE guisp=NONE gui=NONE ctermfg=72 ctermbg=NONE cterm=NONE
hi SpellRare guifg=#a9a79e guibg=#ff40ff guisp=#ff40ff gui=NONE ctermfg=254 ctermbg=13 cterm=NONE
hi EnumerationValue guifg=#CFCFCE guibg=NONE guisp=NONE gui=NONE ctermfg=254 ctermbg=NONE cterm=NONE
hi Comment guifg=#64625d guibg=NONE guisp=NONE gui=italic ctermfg=241 ctermbg=NONE cterm=NONE
hi Character guifg=#57a3c6 guibg=NONE guisp=NONE gui=NONE ctermfg=37 ctermbg=NONE cterm=NONE
hi TabLineSel guifg=#a9a79e guibg=#211e1a guisp=#211e1a gui=bold ctermfg=251 ctermbg=234 cterm=bold
hi Number guifg=#94abbe guibg=NONE guisp=NONE gui=bold ctermfg=67 ctermbg=NONE cterm=bold
hi Boolean guifg=#94abbe guibg=NONE guisp=NONE gui=NONE ctermfg=37 ctermbg=NONE cterm=NONE
hi Operator guifg=#446682 guibg=NONE guisp=NONE gui=bold ctermfg=72 ctermbg=NONE cterm=bold
hi CursorLine guifg=NONE guibg=#232323 guisp=NONE gui=NONE ctermfg=NONE ctermbg=233 cterm=NONE
hi Union guifg=#a9a79e guibg=NONE guisp=NONE gui=NONE ctermfg=254 ctermbg=NONE cterm=NONE
hi TabLineFill guifg=#404046 guibg=#211e1a guisp=#211e1a gui=underline ctermfg=238 ctermbg=238 cterm=NONE
hi Question guifg=#57a3c6 guibg=NONE guisp=NONE gui=bold ctermfg=37 ctermbg=NONE cterm=bold
hi WarningMsg guifg=#a52927 guibg=NONE guisp=NONE gui=bold ctermfg=160 ctermbg=NONE cterm=bold
hi VisualNOS guifg=#e2e4e5 guibg=#eee8d5 guisp=#eee8d5 gui=bold ctermfg=254 ctermbg=230 cterm=bold
hi DiffDelete guifg=#a45444 guibg=#292629 guisp=#292629 gui=bold ctermfg=160 ctermbg=235 cterm=bold
hi ModeMsg guifg=#3a82b3 guibg=NONE guisp=NONE gui=bold ctermfg=67 ctermbg=NONE cterm=bold
hi CursorColumn guifg=NONE guibg=#232323 guisp=NONE gui=NONE ctermfg=NONE ctermbg=233 cterm=NONE
hi Define guifg=#ffea84 guibg=NONE guisp=NONE gui=NONE ctermfg=166 ctermbg=NONE cterm=NONE
hi Function guifg=#57a3c6 guibg=NONE guisp=NONE gui=NONE ctermfg=67 ctermbg=NONE cterm=NONE
hi FoldColumn guifg=#a9a79e guibg=#eee8d5 guisp=#eee8d5 gui=NONE ctermfg=66 ctermbg=230 cterm=NONE
hi PreProc guifg=#dbbba3 guibg=NONE guisp=NONE gui=NONE ctermfg=130 ctermbg=NONE cterm=NONE 
hi EnumerationName guifg=#a9a79e guibg=NONE guisp=NONE gui=NONE ctermfg=254 ctermbg=NONE cterm=NONE
hi Visual guifg=NONE guibg=#2e2e2e guisp=NONE gui=NONE ctermfg=NONE ctermbg=237 cterm=NONE
hi MoreMsg guifg=#57a3c6 guibg=NONE guisp=NONE gui=NONE ctermfg=32 ctermbg=NONE cterm=NONE
hi SpellCap guifg=#e2e4e5 guibg=#a45444 guisp=#a45444 gui=NONE ctermfg=254 ctermbg=9 cterm=NONE
hi VertSplit guifg=#755d3a guibg=#755d3a guisp=#755d3a gui=NONE ctermfg=237 ctermbg=234 cterm=NONE
hi Exception guifg=#a5bf73 guibg=NONE guisp=NONE gui=NONE ctermfg=71 ctermbg=NONE cterm=NONE
hi Keyword guifg=#a5bf73 guibg=NONE guisp=NONE gui=NONE ctermfg=142 ctermbg=NONE cterm=NONE
hi Type guifg=#b59b51 guibg=NONE guisp=NONE gui=NONE ctermfg=136 ctermbg=NONE cterm=NONE 
hi DiffChange guifg=#a3a3a3 guibg=#292629 guisp=#292629 gui=bold ctermfg=248 ctermbg=235 cterm=bold
hi Cursor guifg=#38332F guibg=#b8b8b8 guisp=#b8b8b8 gui=NONE ctermfg=144 ctermbg=250 cterm=NONE
hi SpellLocal guifg=#e2e4e5 guibg=#446682 guisp=#446682 gui=NONE ctermfg=254 ctermbg=11 cterm=NONE
hi Error guifg=#dc322f guibg=#8080ff guisp=#8080ff gui=bold ctermfg=160 ctermbg=12 cterm=bold
hi PMenu guifg=#a6a6a6 guibg=#3d3d3d guisp=#3d3d3d gui=NONE ctermfg=248 ctermbg=237 cterm=NONE
hi SpecialKey guifg=#839496 guibg=#eee8d5 guisp=#eee8d5 gui=bold ctermfg=66 ctermbg=230 cterm=bold
hi Constant guifg=#94abbe guibg=NONE guisp=NONE gui=NONE ctermfg=67 ctermbg=NONE cterm=NONE
hi DefinedName guifg=#e2e4e5 guibg=NONE guisp=NONE gui=NONE ctermfg=254 ctermbg=NONE cterm=NONE
hi Tag guifg=#dc322f guibg=NONE guisp=NONE gui=NONE ctermfg=160 ctermbg=NONE cterm=NONE
hi String guifg=#94abbe guibg=NONE guisp=NONE gui=NONE ctermfg=67 ctermbg=NONE cterm=bold
hi PMenuThumb guifg=#767676 guibg=#b3b3b3 guisp=#b3b3b3 gui=NONE ctermfg=243 ctermbg=249 cterm=NONE
hi MatchParen guifg=#dc322f guibg=#93a1a1 guisp=#93a1a1 gui=bold ctermfg=160 ctermbg=109 cterm=bold
hi LocalVariable guifg=#e2e4e5 guibg=NONE guisp=NONE gui=NONE ctermfg=254 ctermbg=NONE cterm=NONE
hi Repeat guifg=#a5bf73 guibg=NONE guisp=NONE gui=NONE ctermfg=106 ctermbg=NONE cterm=NONE
hi SpellBad guifg=#e2e4e5 guibg=#8080ff guisp=#8080ff gui=NONE ctermfg=254 ctermbg=12 cterm=NONE
hi CTagsClass guifg=#e2e4e5 guibg=NONE guisp=NONE gui=NONE ctermfg=254 ctermbg=NONE cterm=NONE
hi Directory guifg=#268bd2 guibg=NONE guisp=NONE gui=NONE ctermfg=32 ctermbg=NONE cterm=NONE
hi Structure guifg=#b58900 guibg=NONE guisp=NONE gui=NONE ctermfg=136 ctermbg=NONE cterm=NONE
hi Macro guifg=#b59b51 guibg=NONE guisp=NONE gui=NONE ctermfg=166 ctermbg=NONE cterm=NONE 
hi Underlined guifg=#6c71c4 guibg=NONE guisp=NONE gui=underline ctermfg=61 ctermbg=NONE cterm=underline
hi DiffAdd guifg=#b3b3b3 guibg=#333333 guisp=#333333 gui=bold ctermfg=249 ctermbg=236 cterm=bold
hi TabLine guifg=#a3a3a3 guibg=#404040 guisp=#404040 gui=underline ctermfg=248 ctermbg=238 cterm=underline
hi mbenormal guifg=#cfbfad guibg=#2e2e3f guisp=#2e2e3f gui=NONE ctermfg=187 ctermbg=237 cterm=NONE
hi perlspecialstring guifg=#c080d0 guibg=#404040 guisp=#404040 gui=NONE ctermfg=176 ctermbg=238 cterm=NONE
hi doxygenspecial guifg=#fdd090 guibg=NONE guisp=NONE gui=NONE ctermfg=222 ctermbg=NONE cterm=NONE
hi mbechanged guifg=#eeeeee guibg=#2e2e3f guisp=#2e2e3f gui=NONE ctermfg=255 ctermbg=237 cterm=NONE
hi mbevisiblechanged guifg=#eeeeee guibg=#4e4e8f guisp=#4e4e8f gui=NONE ctermfg=255 ctermbg=60 cterm=NONE
hi pythonbuiltin guifg=#446682 guibg=NONE guisp=NONE gui=NONE ctermfg=66 ctermbg=NONE cterm=NONE
hi phpstringdouble guifg=#e2e4e5 guibg=NONE guisp=NONE gui=NONE ctermfg=254 ctermbg=NONE cterm=NONE
hi doxygensmallspecial guifg=#fdd090 guibg=NONE guisp=NONE gui=NONE ctermfg=222 ctermbg=NONE cterm=NONE
hi doxygencomment guifg=#ad7b20 guibg=NONE guisp=NONE gui=NONE ctermfg=130 ctermbg=NONE cterm=NONE
hi doxygenprev guifg=#fdd090 guibg=NONE guisp=NONE gui=NONE ctermfg=222 ctermbg=NONE cterm=NONE
hi htmltagname guifg=#94abbe guibg=NONE guisp=NONE gui=NONE ctermfg=254 ctermbg=NONE cterm=NONE
hi perlspecialmatch guifg=#c080d0 guibg=#404040 guisp=#404040 gui=NONE ctermfg=176 ctermbg=238 cterm=NONE
hi javascriptstrings guifg=#a9a79e guibg=NONE guisp=NONE gui=NONE ctermfg=254 ctermbg=NONE cterm=NONE
hi cformat guifg=#c080d0 guibg=#404040 guisp=#404040 gui=NONE ctermfg=176 ctermbg=238 cterm=NONE
hi lcursor guifg=#FFFFFF guibg=NONE guisp=NONE gui=NONE ctermfg=238 ctermbg=120 cterm=NONE
hi htmlstring guifg=#e2e4e5 guibg=NONE guisp=NONE gui=NONE ctermfg=254 ctermbg=NONE cterm=NONE
hi cursorim guifg=#192224 guibg=#536991 guisp=#536991 gui=NONE ctermfg=235 ctermbg=60 cterm=NONE
hi user2 guifg=#7070a0 guibg=#3e3e5e guisp=#3e3e5e gui=NONE ctermfg=103 ctermbg=60 cterm=NONE
hi doxygenspecialmultilinedesc guifg=#ad600b guibg=NONE guisp=NONE gui=NONE ctermfg=130 ctermbg=NONE cterm=NONE
hi taglisttagname guifg=#808bed guibg=NONE guisp=NONE gui=NONE ctermfg=105 ctermbg=NONE cterm=NONE
hi phpstringsingle guifg=#e2e4e5 guibg=NONE guisp=NONE gui=NONE ctermfg=254 ctermbg=NONE cterm=NONE
hi doxygenbrief guifg=#fdab60 guibg=NONE guisp=NONE gui=NONE ctermfg=215 ctermbg=NONE cterm=NONE
hi mbevisiblenormal guifg=#cfcfcd guibg=#4e4e8f guisp=#4e4e8f gui=NONE ctermfg=252 ctermbg=60 cterm=NONE
hi user1 guifg=#00ff8b guibg=#3e3e5e guisp=#3e3e5e gui=NONE ctermfg=48 ctermbg=60 cterm=NONE
hi doxygenspecialonelinedesc guifg=#ad600b guibg=NONE guisp=NONE gui=NONE ctermfg=130 ctermbg=NONE cterm=NONE
hi cspecialcharacter guifg=#c080d0 guibg=#404040 guisp=#404040 gui=NONE ctermfg=176 ctermbg=238 cterm=NONE
hi doxygenparam guifg=#fdd090 guibg=NONE guisp=NONE gui=NONE ctermfg=222 ctermbg=NONE cterm=NONE
