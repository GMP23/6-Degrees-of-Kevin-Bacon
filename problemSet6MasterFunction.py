########################################################
# masterFunction : string -> answers
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
  


  
  
