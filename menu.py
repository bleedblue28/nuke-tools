
#
#
#  Copyright (c) 2014, 2015, 2016, 2017 Psyop Media Company, LLC
#  See license.txt
#
#

import cryptomatte_utilities
cryptomatte_utilities.setup_cryptomatte_ui()






# pMask
import nuke

#nuke.pluginAddPath('./icons')

#m=toolbar.addMenu("AOVs", icon="3DIcon_01.png")
#m.addCommand("PMask", "nuke.createNode(\"PMask\")") 


#-------------------------------------------------------------------------------------------------------------------
#GONZO TOOLS
#------------------------------------------------------------------------------------------------------

nuke.pluginAddPath("gonzo_gizmos")
nuke.pluginAddPath("gonzo_icons")

gonzoToolBar = nuke.menu("Nodes").addMenu("Gonzo_Tools", icon = "gonzoicon25.png")

gonzoToolBar.addCommand("Filters/G_FineEdgeDetect", 'nuke.createNode("G_FineEdgeDetect")')
gonzoToolBar.addCommand("Filters/G_AngleEdgeDetect", 'nuke.createNode("G_AngleEdgeDetect")')
gonzoToolBar.addCommand("Filters/G_ChannelReBuild", 'nuke.createNode("G_ChannelReBuild")')
gonzoToolBar.addCommand("Keyers/G_ScreenXchange", 'nuke.createNode("G_ScreenXchange")')
gonzoToolBar.addCommand("CC/G_EdgeHammer", 'nuke.createNode("G_EdgeHammer")')
gonzoToolBar.addCommand("CC/G_Matchtone", 'nuke.createNode("G_Matchtone")')
gonzoToolBar.addCommand("Showreel/G_Breakdowner", 'nuke.createNode("G_Breakdowner")')
gonzoToolBar.addCommand("CC/G_WrappersDelight", 'nuke.createNode("G_WrappersDelight")')
gonzoToolBar.addCommand("Filters/G_Sharpen", 'nuke.createNode("G_Sharpen")')

#-----------------------------------------------------------------------------------------------------------------


import os
import sys
import nuke
import KnobScripter

import SearchReplacePanel

def addSRPanel():
        '''Run the panel script and add it as a tab into the pane it is called from'''
        myPanel = SearchReplacePanel.SearchReplacePanel()
        return myPanel.addToPane()
 
#THIS LINE WILL ADD THE NEW ENTRY TO THE PANE MENU
nuke.menu('Pane').addCommand('SearchReplace', addSRPanel)
 
#THIS LINE WILL REGISTER THE PANEL SO IT CAN BE RESTORED WITH LAYOUTS
nukescripts.registerPanel('com.ohufx.SearchReplace', addSRPanel)




# AP definitions

toolbar = nuke.menu('Nodes')
AMenu = toolbar.addMenu('AP', icon='AP.png')
AMenu.addCommand('A_ColorCorrectManager', 'nuke.createNode("A_ColorCorrectManager")', icon='AP.png')



#-------------------------------------------------------------------------------------------------------------------
#CG TOOLS
#------------------------------------------------------------------------------------------------------


nuke.pluginAddPath("CG_gizmos")
nuke.pluginAddPath("CG_icons")
nuke.pluginAddPath("CG_nk_files")

CGToolBar = nuke.menu("Nodes").addMenu("CG_Tools", icon = "3d-icon-0.png")

CGToolBar.addCommand("Camera/fl_VirtualLens", 'nuke.createNode("fl_VirtualLens")')
CGToolBar.addCommand("Camera/FocalMatch", 'nuke.createNode("FocalMatch")')
CGToolBar.addCommand("Masks/PMask", 'nuke.createNode("PMask")')
CGToolBar.addCommand("Camera/OpticalZDefocus", "nuke.nodePaste(C:/Users/Connor Adams/.nuke/CG_nk_files)")
#CGToolBar.addCommand('Camera/OpticalZDefocus', "nuke.nodePaste("/CG_nk_files/OpticalZDefocus.nk")"