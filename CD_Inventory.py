#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# KChiu, 2022-Mar-27, Added codes to complete CD_Inventory program
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()
    
    if strChoice == 'x':# exit the program
        break
    if strChoice == 'l':# load CD inventory from files
        # confirm that existing CD inventory table will be replaced
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'a':# add a new CD to invenotry
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'd':# display current CD inventory
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c':# choose a CD for more options
        # TODone add code to handle tracks on an individual CD        
        cd = None
        while cd == None:# continue to asking for CD ID until a valid ID is selected.
            IO.ScreenIO.show_inventory(lstOfCDObjects)
            cd_idx = input('Select the CD / Album index: ')
            cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
            continue
        while True:
            IO.ScreenIO.print_CD_menu()
            strChoice = IO.ScreenIO.menu_CD_choice()
            if strChoice == 'x':# exit and return to main menu
                break
            if strChoice == 'a':# add a new track to selected CD
                tplTrkInfo = IO.ScreenIO.get_track_info()
                PC.DataProcessor.add_track(tplTrkInfo, cd)
            elif strChoice == 'd': # display all track saved in selected CD
                IO.ScreenIO.show_tracks(cd)
            elif strChoice == 'r':
                while True:# remove a track to from selected CD
                    IO.ScreenIO.show_tracks(cd)
                    # display error if chosen CD has no track for deletion
                    if len(cd.cd_tracks) < 1:
                        print('Can\'n perform this task, no tracks saved for this Album!\n')
                        break
                    trk_idx = input('Select the Track index: ')
                    try:
                        cd.rmv_track(trk_idx)
                        break
                    except:
                        continue
            else:
                print('General Error')
    elif strChoice == 's':# save current CD invenotry table to files
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        # confirm existing files will be ssaved over
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')