Get something moving on the screen

=================================================================================
Lesson
=================================================================================
1. Import global variables and global function from another file
	There are essentially two way to import code from another file in the same directory
		1. import as a whole module
		2. import specific global variable or function directly
	Check them out in the importExample foler

2. Separate program in multiple parts and files
	In a team work, it is a very good practice to keep different part of your game in different file.
	So it is easier for one person to work on the game logic while another person produces nice graphics.
	
	Our pygame program contains three parts:
		Main.py (I/O)
			It contains the big main loop, a very structured loop that is run for each frame
			Besides what we have in the previous level, to make the interactive, it needs:
				1. event loop, which handles user input
				2. game logic, which update the game state
				3. graphics block, which draw components to the screen
				4. display on the screen and wait for a interval
			In this example, part 2 and 3 are just calling a function in GameLogic.py

		GameLogic.py
			It only has two simple functions:
				updateGame()		all the complex logic of the game is here.
				draw(screen)		all the drawing is happened here

		GraphicsUtil.py
			All the pre-drawn surfaces of sprites should be here.
			GameLogic can then import these sprites for draw(screen)


4. How to process user input
	Pygame catpure all sort of actions of user as the form of events.
	To make your game interactive, you should handle those events in an event loop:
		1. Aquire a list of events that pygame recieved												eventList = pygame.event.get()
		2. Write a for loop to process each of them													for event in eventList:
			The variable "event" represent an event instance stored in list "eventList" in each iteration
		3. When processing each event, check for its event type.
			All the events have an attribute called "type", which matches one of pygame event types
				You can look up all the event types on http://www.pygame.org/docs/ref/event.html
						QUIT             none
						ACTIVEEVENT      gain, state
						KEYDOWN          unicode, key, mod
						KEYUP            key, mod
						MOUSEMOTION      pos, rel, buttons
						MOUSEBUTTONUP    pos, button
						MOUSEBUTTONDOWN  pos, button
						JOYAXISMOTION    joy, axis, value
						JOYBALLMOTION    joy, ball, rel
						JOYHATMOTION     joy, hat, value
						JOYBUTTONUP      joy, button
						JOYBUTTONDOWN    joy, button
						VIDEORESIZE      size, w, h
						VIDEOEXPOSE      none
						USEREVENT        code
			The first row shows the name of event type.
			The second row shows what extra attribute this event contains.
				If you are not sure what those properties actually mean, print them out and experiment with it
			
			Both KEYDOWN and KEYUP has attribute called key, which encodes a key on your keyboard.
				You can look them up on http://www.pygame.org/docs/ref/key.html
			


=================================================================================
Challenge
=================================================================================
1. Create a circle around your mouse.
2. Right click makes it larger, and left click makes it smaller.
3. Print out some message like "Game ending ..." when you quit the game