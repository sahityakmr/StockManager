import ui.mainframe as mainframe
import babel.numbers

old_file = False

if __name__ == '__main__':
    if old_file:
        import ui.main
    else:
        mainframe.vp_start_gui()
