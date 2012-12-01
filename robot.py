import curses
import time
import random
stdscr = curses.initscr()
stdscr=curses.newwin(39,138,0,0)
stdscr.border(0)
curses.start_color()
curses.cbreak()
curses.noecho()
stdscr.keypad(1)
curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)

win1=curses.newwin(18,110,12,15)
win1.border(0)

win1.refresh()
win1.addstr(2,45,"DEFUSE THE BOMB!",curses.A_STANDOUT)
win1.addstr(4,3," 1.This game consists of 5 levels.",curses.color_pair(2))
win1.addstr(5,3," 2.A robot moves in the field and cannot go outside the field",curses.color_pair(2))
win1.addstr(6,3," 3.The field has a bomb which you have to defuse.",curses.color_pair(2))
win1.addstr(7,3," 4.In order to defuse a bomb, the robot must have 6 defuse codes. ",curses.color_pair(2))
win1.addstr(8,3," 5.The user should move the robot around in order to collect 6 defuse codes.",curses.color_pair(2))
win1.addstr(9,3," 6.Once the bomb is successfully defused,you move to next level.",curses.color_pair(2))
win1.addstr(12,3,"                       Best of Luck!!",curses.color_pair(3))
win1.addstr(15,3,"                Press any key to continue",curses.A_BOLD)
win1.addstr(4,90,"    @@@   ",curses.color_pair(1))
win1.addstr(5,90,"  @@@@@@@  ",curses.color_pair(1))
win1.addstr(6,90,"  | < <  |",curses.color_pair(1))
win1.addstr(7,90,"  |__V___|",curses.color_pair(1))
win1.addstr(8,90," {        } ",curses.color_pair(1))
win1.addstr(9,90," /{      }\ ",curses.color_pair(1))
win1.addstr(10,90,"  ||||||| ",curses.color_pair(1))
win1.addstr(11,90,"   ^   ^ ",curses.color_pair(1))
win1.addstr(12,90,"  /\   /\   ",curses.color_pair(1))
win1.addstr(13,90," &&&& &&&&    ",curses.color_pair(1))
win1.getch()
win1.refresh()

class ROBOT:
 pass

def SECURE_ROBOT(a,b,c,d,e,i1,i2,i3,i4,j,flag):
 robot=ROBOT()
 robot.a=a
 robot.b=b
 robot.c=c
 robot.d=d
 robot.color=e
 robot.i1=i1
 robot.i2=i2
 robot.i3=i3
 robot.i4=i4
 robot.j=j
 robot.flag=flag
 def show_i1():
	   return robot.i1
 def show_i2():
	   return robot.i2
 def show_i3():
	   return robot.i3
 def show_i4():
	   return robot.i4
 def show_j():
	   return robot.j
 def erase():
	   stdscr.addstr(robot.i1,robot.j,"        ")
	   stdscr.addstr(robot.i2,robot.j,"        ")
	   stdscr.addstr(robot.i3,robot.j,"        ")
	   stdscr.addstr(robot.i4,robot.j,"        ")
 def append():
	   stdscr.addstr(robot.i1,robot.j,robot.a,curses.color_pair(robot.color))
	   stdscr.addstr(robot.i2,robot.j,robot.b,curses.color_pair(robot.color))
	   stdscr.addstr(robot.i3,robot.j,robot.c,curses.color_pair(robot.color))
	   stdscr.addstr(robot.i4,robot.j,robot.d,curses.color_pair(robot.color))
 append()
 def movright():
	   erase()
	   if robot.j==130 and robot.flag==1:
	    robot.j=0
	   robot.j=robot.j+1
	   append()
 def movup():
	   erase()
	   if robot.i1==0 and robot.flag==1:
	    robot.i1=33
	    robot.i2=34
	    robot.i3=35
	    robot.i4=36
	   robot.i1=robot.i1-1
	   robot.i2=robot.i2-1
	   robot.i3=robot.i3-1
	   robot.i4=robot.i4-1
	   append()
 def movleft():
	   erase()
	   if robot.j==0 and robot.flag==1:
	    robot.j=130
	   robot.j=robot.j-1
	   append()
 def movdown():
	   erase()
	   if robot.i4==37 and robot.flag==1:
	    robot.i1=1
	    robot.i2=2
	    robot.i3=3
	    robot.i4=4
	   robot.i1=robot.i1+1
	   robot.i2=robot.i2+1
	   robot.i3=robot.i3+1
	   robot.i4=robot.i4+1
	   append()
 robo2=ROBOT()
 robo2.movup=movup
 robo2.movleft=movleft
 robo2.movright=movright
 robo2.movdown=movdown
 robo2.i1=show_i1
 robo2.i2=show_i2
 robo2.i3=show_i3
 robo2.i4=show_i4
 robo2.j=show_j
 return robo2

class Defuse:
 ht=35
 wt=135
 def __init__(self):
	  self.i=int(random.uniform(2,35))
	  self.j=int(random.uniform(2,135))
	  stdscr.addstr(int(self.i),int(self.j),"$",curses.color_pair(1))

 def show_progress(self,c):
 	win = curses.newwin(3,40,1,1)
 	win.border(0)
 	win.addstr(1,1,"Codes defused ",curses.color_pair(2))
 	pos = 17
 	for i in range(15):
       		  win.addstr(1,pos,".",curses.color_pair(2))
       		  win.refresh()
        	  time.sleep(0.01)
       		  pos += 1
 	win.addstr(1,35,str(c),curses.color_pair(2))
 	win.refresh()
 	time.sleep(0.5)
        win=curses.newwin(3,40,1,1)
	win.refresh()

 def stop(self):
 	curses.flash()
 	win = curses.newwin(5,75,18,35)
 	win.border()
 	win.addstr(2,1,"       You have enough codes to defuse the bomb...!!",curses.color_pair(1))
 	win.refresh()
 	time.sleep(1)
 	win=curses.newwin(5,75,18,35)
 	win.refresh()

class Bomb:
 p=11
 q=24
 def __init__(self):
	  stdscr.addstr(11,24,"B",curses.color_pair(4))

 def endgame_lose(self):
 	global endflag
 	endflag=1
 	curses.flash()
 	win = curses.newwin(5,75,18,35)
 	win.border()
        win.addstr(2,1,"    SORRY",curses.color_pair(3))
 	pos = 17
 	for i in range(15):
       		  win.addstr(2,pos,".",curses.color_pair(2))
 		  win.refresh()
       		  time.sleep(0.05)
       		  pos += 1
 	win.addstr(2,35,"YOU LOSE :-( !!",curses.color_pair(2))
 	win.refresh()
 	time.sleep(1)	  


 def endgame_win(self):
 	curses.flash()
 	win = curses.newwin(5,75,18,35)
 	win.border()
 	win.addstr(2,1,"    BOMB DEFUSED",curses.color_pair(3))
 	pos = 17
 	for i in range(15):
       	  	win.addstr(2,pos,".",curses.color_pair(2))
       	        win.refresh()
       	  	time.sleep(0.05)
       	  	pos += 1
 	if winflag==0:
 		win.addstr(2,35,"YOU PROCEED TO NEXT LEVEL !!",curses.color_pair(2))
 	if winflag==1:
		win.addstr(2,35,"YOU WIN THE GAME !!",curses.color_pair(2))
 	win.refresh()
 	time.sleep(1)	

class Wall:
 begin=10
 end=30
 def __init__(self,j):
	 self.j=j
	 k=0
	 for i in range(10,30):
		 stdscr.addstr(i,j,"X",curses.color_pair(k))
		 k=k+1
		 if k==4:
		  k=1

def out_of_game():
 	global endflag
 	endflag=1
 	curses.flash()
 	win = curses.newwin(5,75,18,35)
 	win.border()
        win.addstr(2,1,"    SORRY",curses.color_pair(3))
 	pos = 17
 	for i in range(15):
       		  win.addstr(2,pos,".",curses.color_pair(2))
 		  win.refresh()
       		  time.sleep(0.05)
       		  pos += 1
 	win.addstr(2,35,"YOU ARE OUT OF THIS GAME..!!",curses.color_pair(2))
 	win.refresh()
 	time.sleep(1)	  


 
def main(speed,level):
  height,width = stdscr.getmaxyx()
  num = min(height,width)
  code=Defuse()
  count=0
  bomb=Bomb()
  stdscr.refresh()
  key=stdscr.getch()
  pos=16
  c1=0
  c2=0 
  c3=0
  c4=0
  
  while 1:
   global winflag
   global score
   stdscr.addstr(1,126,"Score : ")
   stdscr.addstr(1,135,str(score))
   bomb=Bomb()
   if level==3:
    stdscr.addstr(26,pos,".",curses.color_pair(0))
   if level==4:
    num=int(random.uniform(0,100))
    if num>=0 and num<25 and c2==0 and c3==0 and c4==0:
               enemy.movup()
	       c1=c1+1
	       if c1==6:
	        c1=0
    elif num>25 and num<=50 and c1==0 and c3==0 and c4==0:
               enemy.movright()
	       c2=c2+1
	       if c2==6:
	         c2=0
    elif num>50 and num<=75 and  c1==0 and c2==0 and c4==0:
               enemy.movleft() 
	       c3=c3+1
	       if c3==6:
	        c3=0
    elif num>75 and c1==0 and c2==0 and c3==0:
               enemy.movdown()
	       c4=c4+1
	       if c4==6:
	        c4=0
   if key==curses.KEY_UP:
               if level==4 or level==3:
	        if robo.i1()==enemy.i4()-2 and [x for x in range(robo.j(),robo.j()+7) if x in range(enemy.j(),enemy.j()+7)]:
			out_of_game()
	                break
               if robo.i1()==26 and pos>=robo.j() and pos<robo.j()+len(c) and level==3:
                        out_of_game()
	                break

	       if level==2 :
		 if robo.i1()==w1.end:
		  if w1.j in range(robo.j(),robo.j()+9) or w2.j in range(robo.j(),robo.j()+9) or w3.j in range(robo.j(),robo.j()+9):
                        out_of_game()
	                break
               if code.i==robo.i1() and code.j>=robo.j() and code.j<robo.j()+len(c) and count<=5:
			count=count+1
			score=score+1
                	code.show_progress(count)
	                if count<=5:
	        	 code=Defuse()
	                else:
			 code.stop()
	       if bomb.p==robo.i1() and bomb.q>=robo.j() and bomb.q<robo.j()+len(c) and count>5:
	                if level==4:
	                	winflag=1
	        	bomb.endgame_win()
	                break
	       elif bomb.p==robo.i1() and bomb.q>=robo.j() and bomb.q<robo.j()+len(c) and count<=5:
	        	bomb.endgame_lose()
	                break
	       robo.movup()
	       stdscr.timeout(speed)
               getkey=stdscr.getch()
	       if getkey==-1:
	       		key=key
	       else:
	       		key=getkey
               stdscr.refresh()

   if key==curses.KEY_RIGHT:
               if level==4 or level==3:
	        if robo.j()+8==enemy.j() and [x for x in range(robo.i1(),robo.i4()+1) if x in range(enemy.i1(),enemy.i4()+1)]:
			out_of_game()
	                break
               if 26>=robo.i1() and 26<=robo.i4() and pos>=robo.j() and pos<robo.j() +len(c) and level==3:
		        out_of_game()
	                break
	       if level==2:
	        if robo.i4()<=w1.end+3 and robo.i1()>=w1.begin-3:
	         if robo.j()==w1.j-8 or robo.j()==w2.j-8 or robo.j()==w3.j-8:
	                out_of_game()
	                break
	       if code.i>=robo.i1() and code.i<=robo.i4() and code.j>=robo.j()+1 and code.j==robo.j()+len(c)-1 and count<=5:
		 	count=count+1
			score=score+1
                 	code.show_progress(count)
	                if count<=5:
	         	 code=Defuse()
	                else:
			 code.stop()
               if bomb.p>=robo.i1() and bomb.p<=robo.i4() and bomb.q>=robo.j() and bomb.q<robo.j() +len(c) and count>5:
	                if level==4:
	                	winflag=1
	         	bomb.endgame_win()
	                break
               elif bomb.p>=robo.i1() and bomb.p<=robo.i4() and bomb.q>=robo.j() and bomb.q<robo.j() +len(c) and count<=5:
                 	bomb.endgame_lose()
	                break
	       robo.movright()
	       stdscr.timeout(speed)
	       getkey=stdscr.getch()
	       if getkey==-1:
	                 key=key
	       else:
	                 key=getkey
               stdscr.refresh()
   

   if key==curses.KEY_DOWN:
              if level==4 or level==3:
	       if robo.i4()==enemy.i1() and [x for x in range(robo.j(),robo.j()+7) if x in range(enemy.j(),enemy.j()+7)]:
	       		out_of_game()
	                break
              if 26==robo.i4() and pos>=robo.j() and pos<robo.j()+len(c) and level==3:
		       out_of_game()
	               break
	      if level==2 :
		 if robo.i4()==w1.begin:
		  if w1.j in range(robo.j(),robo.j()+9) or w2.j in range(robo.j(),robo.j()+9) or w3.j in range(robo.j(),robo.j()+9):
                        out_of_game()
			break
              if code.i==robo.i4() and code.j>=robo.j() and code.j<robo.j()+len(c) and count<=5:
		       count=count+1
		       score=score+1
                       code.show_progress(count)
	               if count<=5:
	                code=Defuse()
		       else: 
			code.stop()
              if bomb.p==robo.i4() and bomb.q>=robo.j() and bomb.q<robo.j()+len(c) and count>5:
	               if level==4:
	                	winflag=1
		       bomb.endgame_win()
		       break
              elif bomb.p==robo.i4() and bomb.q>=robo.j() and bomb.q<robo.j()+len(c) and count<=5:
                       bomb.endgame_lose()
	               break
	      robo.movdown()
	      stdscr.timeout(speed)
              getkey=stdscr.getch()
              if getkey==-1:
                       key=key
              else:
                       key=getkey
              stdscr.refresh()

   if key==curses.KEY_LEFT:
              if level==4 or level==3:
	        if robo.j()==enemy.j()+7 and [x for x in range(robo.i1(),robo.i4()+1) if x in range(enemy.i1(),enemy.i4()+1)]:
			out_of_game()
	                break
              if 26>=robo.i1() and 26<=robo.i4() and pos==robo.j() and level==3:
	             out_of_game()
	             break
	      if level==2:
	        if robo.i4()<=w1.end+3 and robo.i1()>=w1.begin-3:
	         if robo.j()==w1.j or robo.j()==w2.j or robo.j()==w3.j:
	                out_of_game()
	                break
	      if code.i>=robo.i1() and code.i<=robo.i4() and code.j==robo.j()+1 and count<=5:
		     count=count+1
		     score=score+1
                     code.show_progress(count)
	             if count<=5:
	              code=Defuse()
	             else:
		      code.stop()
              if bomb.p>=robo.i1() and bomb.p<=robo.i4() and bomb.q==robo.j() and count>5:
	             if level==4:
	                	winflag=1
                     bomb.endgame_win()
	             break
              elif bomb.p>=robo.i1() and bomb.p<=robo.i4() and bomb.q==robo.j() and count<=5:
                     bomb.endgame_lose()
	             break
              robo.movleft()
              stdscr.timeout(speed)
              getkey=stdscr.getch()
              if getkey==-1:
                      key=key
              else:
                      key=getkey
              stdscr.refresh()
   if level==3:
    stdscr.addstr(26,pos," ")
    pos=pos+1
    if pos==138:
     pos=16
   if key==curses.KEY_UP or key==curses.KEY_LEFT or key==curses.KEY_RIGHT or key==curses.KEY_DOWN:
    continue
   else:
    break

try:
 a="  i  i   "
 b=" [@  @]  "
 c="/|____|\ "
 d=" d    b  "
 endflag=0
 score=0
 winflag=0
 level1=2
 robo=SECURE_ROBOT(a,b,c,d,2,4,5,6,7,4,0)
 main(100,1)
 time1=75
 curses.nocbreak()
 curses.echo()
 curses.endwin()
 if endflag==1:
  quit()
 while level1<5:
  stdscr=curses.initscr()
  l="       "
  m="  @ @  "
  n="[[** ]]"
  o=" /   \ "
  stdscr=curses.newwin(39,138,0,0)
  stdscr.border(0)
  curses.start_color()
  curses.cbreak()
  curses.noecho()
  stdscr.keypad(1)
  curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
  curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
  curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
  curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
  robo=SECURE_ROBOT(a,b,c,d,2,4,5,6,7,4,0)
  if level1==2:
   w1=Wall(40)
   w2=Wall(65)
   w3=Wall(90)
  if level1==3 or level1==4:
   enemy=SECURE_ROBOT(l,m,n,o,4,24,25,26,27,4,1)
  #if level1==3:
  main(time1,level1)
  time1=time1-25
  stdscr.refresh()
  time.sleep(1)
  curses.endwin()
  level1=level1+1
  if endflag==1:
   quit()

except:
 error=[0]
finally:
  curses.endwin()
  stdscr=curses.newwin(39,138,0,0)
  stdscr.border(0)
  curses.start_color()
  curses.cbreak()
  curses.noecho()
  stdscr.keypad(1)
  curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
  curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
  curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
  curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
  if endflag==0 and score == 24:
   stdscr.addstr(10,50,"     YOU WIN!!                ",curses.color_pair(2)) 
   stdscr.addstr(11,50,"       /\                       ",curses.color_pair(2)) 
   stdscr.addstr(12,50,"      /**\        "           ,curses.color_pair(2)) 
   stdscr.addstr(13,50,"     {____}            ",curses.color_pair(2)) 
   stdscr.addstr(14,50,"     /    \             ",curses.color_pair(2)) 
   stdscr.addstr(15,50," [[ /******\ ]]         ",curses.color_pair(2)) 
   stdscr.addstr(16,50,"[[ {00000000} ]]        ",curses.color_pair(2)) 
   stdscr.addstr(17,50," [[ \******/ ]]     ",curses.color_pair(2)) 
   stdscr.addstr(18,50,"     \    /    ",curses.color_pair(2)) 
   stdscr.addstr(19,50,"      ||||     ",curses.color_pair(2)) 
   stdscr.addstr(20,50,"     /____\   ",curses.color_pair(2)) 
  else:
   stdscr.addstr(17,40,"        YOU LOSE THE GAME!!  ",curses.color_pair(2)) 
   stdscr.addstr(18,40,"      BETTER TRY NEXT TIME..!   ",curses.color_pair(2)) 
  stdscr.addstr(22,45,"Your final score is " +str(score),curses.A_BOLD) 
  stdscr.refresh()
  time.sleep(1) 
  curses.endwin()
  print "Your final score is %d" %(score)

