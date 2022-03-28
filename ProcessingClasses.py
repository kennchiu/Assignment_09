#------------------------------------------#
# Title: Processing Classes
# Desc: A Module for processing Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# KChiu, 2022-Mar-27, Added codes to complete ProcessingClasses module
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """function to add CD info in CDinfo to the inventory table.


        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """

        cdId, title, artist = CDInfo        
        while True:
            try:
                cdId = int(cdId)
                row = DC.CD(cdId, title, artist)
                table.append(row)
                break
            except ValueError:
                print('CD not added! ID must be an Integer!\n')
                break
            except Exception as e:
                print(e)
                break

    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """selects a CD object out of table that has the ID cd_idx

        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return

        Raises:
            Exception: If id is not in list.

        Returns:
            row (DC.CD): CD object that matches cd_idx

        """
        # TODone add code as required
        while True:
            try:
                cd_idx = int(cd_idx)
            except ValueError:
                print('CD ID should be an Integer!\n')
                break
            try:
                cd = None
                for row in table:
                    if row.cd_id == cd_idx:
                        cd = row
                if cd == None:# display an error if user chooses an invalid CD ID
                    raise Exception('CD ID doesn\'t exist! Try again!\n')
                else:
                    return cd
            except Exception as e:
                print(e)
                break
            
    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """adds a Track object with attributes in track_info to cd


        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (DC.CD): cd object the tarck gets added to.

        Raises:
            Exception: DESCraised in case position is not an integer.

        Returns:
            None: DESCRIPTION.

        """

        # TODone add code as required
        # set Track variables based on input
        position, title, length = track_info
        while True:
            try:
                position = int(position)
            except ValueError:
                print('Track not added! Track Position must be an Integer!')
                break
            except Exception as e:
                print(e)
                break
            # instantiates a new Track object
            row = DC.Track(position, title, length)
            # add the new Track object to associated CD.
            cd.add_track(row)
            break


