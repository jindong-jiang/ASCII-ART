function! AsciiPlayer()
    set nowrap
    set scrolloff=0
    set columns=80        
    set lines=26           
    normal gg
    let i = 1
    while i < 9000 
        execute "normal 23\<cr>zt"
        redraw
        let i = i + 1
        sleep 33m
    endwhile
endfunction
command! AsciiPlayer call AsciiPlayer()

