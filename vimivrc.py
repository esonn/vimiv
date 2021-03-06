# Configuration file for the vimiv image viewer

# General settings #############################################################
start_fullscreen = False
start_slideshow = False
slideshow_delay = 2
shuffle = False
display_bar = True
thumbsize = (128, 128)
geometry = "800x600"  # Only used when tiling_wm is False
recursive = False  # Search directories recursively for images
rescale_svg = True

# Library settings #############################################################
show_library = False
library_width = 300
expand_lib = True
border_width = 0
border_color = "#000000"
show_hidden = False

# Keybindings ##################################################################
# Modifiers: Shift (through uppercase) Ctrl (through ^), Alt (through Alt+)
key_quit = "q"

key_fullscreen_toggle = "f"
key_statusbar_toggle = "b"
key_slideshow_toggle = "s"
key_thumbnail_toggle = "t"
key_library_toggle = "o"
key_library_toggle_focus= "O"
key_animation_toggle = "space"  # Toggle animation of Gifs
key_rescale_toggle = "r"
key_hidden_toggle = "t"
key_move_up = "u"

key_slideshow_inc = "period"  # Increase slideshow delay
key_slideshow_dec = "comma"  # Decrease slideshow delay

key_scroll_left = "h"
key_scroll_down = "j"
key_scroll_up = "k"
key_scroll_right = "l"

key_scroll_left_page = "H"
key_scroll_down_page = "J"
key_scroll_up_page = "K"
key_scroll_right_page = "L"

key_zoom_in = "plus"
key_zoom_out = "minus"
key_fit = "w"
key_center = "W"
key_fit_horiz = "e"
key_fit_vert = "E"

key_next_image = "n"
key_prev_image = "p"
key_first_image = "g"
key_last_image = "G"

key_mark = "m"
key_mark_toggle = "M"

key_rotate_clock = "greater"
key_rotate_cclock = "less"
key_rotate_auto = "a"
key_fliph = "y"
key_flipv = "Y"
key_delete = "x"
key_edit = "c"

key_cmd_history_up = "^k"
key_cmd_history_down = "^j"
