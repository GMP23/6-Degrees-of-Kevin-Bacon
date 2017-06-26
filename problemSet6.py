# file: problemSet6.py
# authors: Tom O'Boyle, Garret Patten
# date: March 21, 2016
# date modified: March 24, 2016
#
# Part 1
#
def makeFilmActorsDictionary():
  titledict = {}
  infile = open("mdb.txt", "r")
  masterlist = [nextline.strip() for nextline in infile]
  infile.close()
  j = 0
  while j < len(masterlist):
    title = masterlist[j]
    actor = masterlist[j + 1]
    if title in titledict:
      if not actor in titledict[title]:
        titledict[title].append(actor)
    else:
      titledict[title] = [actor]
    j = j + 2
  return titledict

a = makeFilmActorsDictionary()

#Question 1: Length of longest cast list
#
def largeCast():
  lrg = (None, 0)
  for film in a:
    cast = a[film]
    if len(cast) > lrg[1]:
      lrg = (film, len(cast))
  return lrg[1]


#Question 2: Film/films with largest cast
#
def largeFilm():
  lrgcast = largeCast()
  lrgfilms = []
  for film in a:
    cast = a[film]
    if len(cast) == lrgcast:
      lrgfilms.append(film)
  return lrgfilms

#Question 3: How many films in the database?
#
def numberFilms():
  n = 0
  films = []
  for film in a:
    if film not in films:
      films.append(film)
      n = n + 1
  return n

#Question 4: Smallest cast and film
#
def smallCast():
  sml = (None, largeFilm())
  for film in a:
    cast = a[film]
    if len(cast) < sml[1]:
      sml = (film, len(cast))
  return sml[1]

def smallFilm():
  smlcast = smallCast()
  smlfilms = []
  for film in a:
    cast = a[film]
    if len(cast) == smlcast:
      smlfilms.append(film)
  return smlfilms

#Question 5: Every movie with Owen Wilson
#
def owenWilsonFilms():
  films = []
  for film in a:
    cast = a[film]
    if 'Owen Wilson' in cast:
      films.append(film)
  return films

#Question 6: Actors in Silver Linings Playbook and American Hustle
#
def actorsInBoth():
  both = []
  silLinCast = a['Silver Linings Playbook']
  for actor in a['American Hustle']:
    if actor in silLinCast:
      both.append(actor)
  return both

# Step 2
#
def build_actor_dict():
  actorDict = {}
  infile = open("mdb.txt", "r")
  masterlist = [nextline.strip() for nextline in infile]
  infile.close()
  j = 0
  while j < len(masterlist):
    title = masterlist[j]
    actor = masterlist[j + 1]
    if actor in actorDict:
      if title not in actorDict[actor]:
        actorDict[actor].append(title)
    else:
      actorDict[actor] = [title]
    j = j + 2
  return actorDict

b = build_actor_dict()

# makeActorFilmsMap : string -> Map.t
#
def makeActorFilmsMap(actor):
  if actor in b:
    return actor, b[actor]
  else:
    return None

# Question 7: Movies in which Owen Wilson appears
#
def newWilsonFilms():
  return b["Owen Wilson"]

# Question 8: How many actors in database?
#
def howManyActors():
  return len(b)

# Question 9: Actor with most films
#
def mostFilms():
  filmNumberDict = []
  for actor in b:
    tally = (actor, len(b[actor]))
    filmNumberDict.append(tally)
    amounts = []
  for (key, value) in filmNumberDict:
    amounts.append(value)
  most = max(amounts)
  answerDict =[]
  for (key, value) in filmNumberDict:
    if value == most:
      answerDict.append(key)
  return answerDict

# member is a helper function of removeDuplicates
#
def member(x, xs):
    if xs == []:
        return False
    else:
        y = xs[0]
        ys = xs[1:]
        if x == y:
            return True
        else:
            return member(x, ys)

# removeDuplicates is a helper function of eastwoodFreeman
#
def removeDuplicates(xs):
    if xs == []:
        return []
    else:
        y = xs[0]
        ys = xs[1:]
        if member(y, ys):
            return removeDuplicates(ys)
        else:
            return [y] + removeDuplicates(ys)

# Question 10: All films with Clint Eastwood OR Morgan Freeman
#
def eastwoodFreeman():
  eastwood = b["Clint Eastwood"]
  freeman = b["Morgan Freeman"]
  eastwoodFreeman = eastwood + freeman
  return removeDuplicates(eastwoodFreeman)

# PART 3
#
# collaborationList : string -> dictionary
#

def collaborationDict():
  colbDict = {}
  for A in b:    
    for film in b[A]:
      for B in a[film]:          
        if A <> B and B not in colbDict:
          colbDict[B] = [A]
        elif A <> B and B in colbDict:
          colbDict[B].append(A)
  return colbDict

c = collaborationDict()
        
# Question 11: Which actor has the most collaborators
#
def mostCollaborators():
  most = (None, 0)
  for actor in c:
    clbtrs = len(c[actor])
    if most[1] < clbtrs:
      most = (actor, clbtrs)
  return most[0]
  #print "The actor with the most collaborator is " + str(most[0]) + " with " + str(most[1]) + " collaborators."

def leastCollaborators():
  least = (None, 1000)
  for actor in c:
    clbtrs = len(c[actor])
    if least[1] > clbtrs:
      least = (actor, clbtrs)
  return least[0]

  
# Question 12: Is Kate Winslet a collaborator of Cate Blanchett
#
def  kateAndCate():
  kateList = c["Kate Winslet"]
  if "Cate Blanchett" in kateList:
    return True
  else:
    return False
  
# Question 13: Is Kate Winslet a collaborator of a collaborator of Cate Blanchett
#
def doubleCollaborator():
  kateList = c["Kate Winslet"]
  cateList = c["Cate Blanchett"]
  for actor in kateList:
    if actor in cateList:
      return True, str(actor)
  else:
    return False


def BnotC():
  no = []
  for actor in b:
    if actor not in c:
      no.append(actor)
  return no

#PART 4
#
def make_bfs_tree(c, root):
   bfs = {}
   queue = [root]
   def repeat(queue):
     if queue <> []:
       new_queue = []
       for A in queue:
         for B in c[A]:
           if B not in bfs:
             bfs[B] = (A)
             new_queue.append(B)
       repeat(new_queue)  
   repeat(queue)
   bfs[root] = ""
   return bfs

tree = make_bfs_tree(c, "Dustin Hoffman")

#Question 14
#
def collabTree(actor):
  person = actor
  while person <> "":
    print person
    person = tree[person]

#Samuel L. Jackson
#
def samToDust():
  collabTree("Samuel L. Jackson")

#Kevin Bacon
#
def baconToDust():
  collabTree("Kevin Bacon")

#Mel Gibson
#
def melToDust():
  collabTree('Mel Gibson')

#Qustion 15
#
def actorsInTree():
  tree_actors = float(len(tree))
  total_actors = float(len(b))
  return str((tree_actors / total_actors) * 100) + "%"

#Question 16
#
def numbered_make_bfs_tree(c, root):
   bfs = {}
   queue = [root]
   n = 1
   def repeat(queue, n):
     if queue <> []:
       new_queue = []
       for A in queue:
         for B in c[A]:
           if B not in bfs:
             bfs[B] = (A, n)
             new_queue.append(B)
       repeat(new_queue, n + 1)  
   repeat(queue, n)
   bfs[root] = ("", 0)
   return bfs

number_tree = numbered_make_bfs_tree(c, "Dustin Hoffman")

def longestPath():
  lng = (None, 0)
  for A in number_tree:
    if lng[1] < number_tree[A][1]:
      lng = number_tree[A]
  return lng

#Question 17
#
def longPath():
  lng = (None, 0)
  for A in number_tree:
    if lng[1] < number_tree[A][1]:
      lng = number_tree[A]
  return collabTree(lng[0])


#STEP 5
#
def newCollaborationDict():
  colbDict = {}
  for A in b:    
    for film in b[A]:
      for B in a[film]:
        if A <> B and B not in colbDict:
          colbDict[B] = [(A, film)]
        elif A <> B and B in colbDict:
          colbDict[B].append((A, film))
  return colbDict

d = newCollaborationDict()

def better_bfs_tree(start, end):
   tree = make_bfs_tree(c, start)
   person1 = end
   print person1
   while person1 <>"":
     person2 = tree[person1]
     film = sharedMovie(person1, person2)
     if film <> None:
       print film
       print person2
       person1 = person2
     else:
       return ""

def sharedMovie(actor1, actor2):
  for (actor, movie) in d[actor1]:
       if actor == actor2:
         return movie

# masterFunction : string -> strings
#
def masterFunction(s):
  makeFilmActorsDictionary() # calls Film/Actors dictionary
  build_actor_dict() # calls Actor/Films dictionary
  # Step One
  print "1. The length of the longest cast list is " + str(largeCast())
  print "2. The film(s) with the largest cast is/are " + str(largeFilm())
  print "3. The number of films in the database is " + str(numberFilms())
  print "4. The film with the smallest cast is " + str(smallFilm())
  print "5. Owen Wilson has acted in the following films: " + str(owenWilsonFilms())
  print "6. The following actors have starred in both Silver Linings Playbook and American Hustle: " + str(actorsInBoth())
  # Step Two
  print "7. Movies in which Owen Wilson acts are: " + str(makeActorFilmsMap("Owen Wilson"))
  print "8. The number of actors in the database is " + str(howManyActors())
  print "9. The actor who has appeared in the most films is " + str(mostFilms())
  print "10. Films with either Clint Eastwood or Morgan Freeman are: " + str(eastwoodFreeman())
  # Step Three
  print "11. The actor with the most collaborators is " + str(mostCollaborators())
  print "12. Is Kate Winslet a collaborator of Cate Blanchett? " + str(kateAndCate())
  print "13. Is Kate Winlset a collaborator of a collaborator of Cate Blanchett? " + str(doubleCollaborator())
  # Step Four
  print "14. Collaboration Trees of Samuel L. Jackson, Kevin Bacon, and Mel Gibson"
  samToDust()
  baconToDust()
  melToDust()
  print "15. The percentage of the total number of actors in this tree is: " + str(actorsInTree())
  print "16. The length of the longest path of this tree is: " +str(longestPath())
  print "17. An instance of the longest path is " + str(longPath())
  # Step Five
  print "Improved Tree of Meryl Streep and Don Cheadle: " + str(better_bfs_tree("Meryl Streep", "Don Cheadle"))

masterFunction("mdb")
