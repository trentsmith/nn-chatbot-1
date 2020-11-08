import sqlite3
conn = sqlite3.connect('Talk.db')
c = conn.cursor()
def create_table():
  c.execute('CREATE TABLE IF NOT EXISTS Talk(Keywords TEXT, Response TEXT, User TEXT)')
def insert_value_into_table(user,keywords,response):
  c.execute('INSERT INTO Talk(Keywords,Response,User)VALUES(?,?,?)',(keywords,response,user))
  str1= " "
  keywords = str1.join(keywords)
  print(keywords)
  conn.commit()
def select_from_table(user):
  c.execute('Select * from Talk where user = '+user)
create_table()
#insert_value_into_table("admin",["good","bad"],"Test")
class node:
  def __init__(self,value=None):
    self.value = value
    self.word = []
    self.wordnode =[]
class binary_search_tree:
  def __init__(self):
    self.root=None

  def insert(self,value):
    if self.root==None:
      self.root=node(value)
    else:
      self._insert(value,self.root)  

  def _insert(self,value,cur_node,words):
    flag = False
    keywords = []
    while len(words)!=0:
        for i in words:
            if i in cur_node.word:
                cur_node= self.wordnode[cur_node.word.index(i)]
                words.remove(i)
                keywords.append(i)
                if len(words)==0:
                       break
            elif flag:
                cur_node.word.append(i)
                cur_node.wordnode.append(node(value))
                words.remove(i)
                keywords.append(i)
                if len(words)==0:
                  #insert_value_into_table()             
                  break
            if i == words[len(words)-1]:
                flag = True
                break
  def find(self,value):
    if self.root!=None:
        return self._find(value,self.root)
    else:
        return None

  def _find(self,words,cur_node):
    flag = False
    final = ""
    while len(words) != 0:
        for i in words:
            if i in cur_node.word:
                words.remove(i)
                cur_node= cur_node.wordnode[cur_node.word.index(i)]
                flag=False
                final = cur_node.value
        if flag:
            break
        flag=True
    return final

print("hello how are you")
#response = raw_input()
#print(response)
a = binary_search_tree()
a.insert("Hello")
a._insert("Test",a.root,["good","Hello"])
a._find(["good","Hello"],a.root)
print(a.root.wordnode[0].value)
#a._insert(7,a.root)
#print(a.root.right_child.value)

# List of string 
print(a.root.value)
while True:
  x =input()
  x=x.split(" ")
  answer = a._find(x,a.root)
  print("answer is "+answer)
  if answer == None or answer =="":
    print("unfamiliar what to say what should I say?")
    y = input()
    a._insert(y,a.root,x)