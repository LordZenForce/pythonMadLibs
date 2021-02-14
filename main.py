from tkinter import * 

root = TK()
root.geometry ('300x300')
root.title ('Python Mad Libs Generator')
Label (root, text = 'Mad Libs Generator, enjoy!', font= 'arial 15 bold') .pack()
Label (root, text = 'Click One!', font= 'arial 15 bold') .place (x=40, y=80)

def madlib():

  animals= input('enter a animal name: ')
  pottery= input('enter a type of pottery: ')
  profession= input('enter a type of profession: ')
  name= input('enter a name: ')
  place= input ('enter a place: ')
  verb= input ('enter a verb: ')
  food= input ('enter the name of a food: ')
  
  print( 'Oh wow, its a ' + animal + '! I cant believe I was foolish enough to leave out my ' + pottery + '. The ' + profession + ' said before yelling ' + name + ' go to ' + place + ' and ' + verb + ' so we can chase the animal away with ' + food + '.')
  
  Button (root, text= 'A Tragedy!', font= 'Helvetica 10', command= madlib(), bg= 'ghost white').place (x=80, y=240)
  
  root.mainloop()
  
