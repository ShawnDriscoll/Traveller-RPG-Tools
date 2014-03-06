@echo off
call pyuic4 -x skillcheck.ui -o ui_skillcheck.py
call pyuic4 -x about_dialog.ui -o ui_about_dialog.py
call pyrcc4 skillcheck.qrc -o skillcheck_rc.py