# Pokemon_GUI_Game
A GUI game where you're rewarded for attending Focusmate sessions. When done so, you can catch Pokemon and upload them to a gallery. 

## Built With
Tkinter
Selenium
	Chromedriver

## Getting Started
### Without APIs
If you're content with having the pokemon in your computer gallery, run the file: Pokemon_GUI_Without_APIs.py.
### With APIs: [With_APIs_Instructions.md](https://github.com/jlpython65/Pokemon_GUI_Game1/blob/main/With_API_Instructions)
If you so happen to use Focusmate, Beeminder, and Notion in your productivity workflow, this section will prove useful. 

First you need to get the following credentials listed in the config.ini file and assign them to their respective variable.

##### Beeminder: 
First you must create a goal that's integrated with Focusmate.
https://www.beeminder.com/home

Note: I haven't found a way for pymider to find a goal with a specific integration (this case being Focusmate) and assign it to the goal variable. For now, you can just change the the index of goals[] until you get the right goal.

Click on your icon in the upper right > Account Settings >Apps & API 
You will find your token in the API section.

For simple integration, use the Pyminder (https://github.com/narthur/pyminder) import. If not installed, run this line in the terminal.
pip install pyminder

##### Imgur
Create an imgur account by following the prompts
https://help.imgur.com/hc/en-us/articles/210076633-Create-an-Account
Afterwards apply for an API to get your client ID and secret
https://api.imgur.com/oauth2/addclient
Note: 
- Select "OAuth 2 authorization without a callback URL" for authorization type
- Same case for Beeminder, change the index in album_id[] until the code selects the right album.

##### Notion
Click "View my Integrations" on the upper right > New integration. You only need to assign a name, and the workspace you use. Otherwise you can keep everything in default and submit. There you can copy your token. Now you need to connect this integration to a table.

###### In Notion Workspace
Open your table as a page
Click the 3 dots on the upper right
Click "Add connections" and in the search bar, type the name of the integration you just made
Select integration
Confirm the connection

As for the database ID, look at the URL
![[Pasted image 20220909153907.png]]
the numbers and letters after v= is your database id. Copy and paste that into your config.ini

