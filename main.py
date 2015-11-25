# Hey Gus, here's stub kinda outlining the
# gist of what I think you're getting at. 
#
# I'm essentially thinking that what you
# want is a data-driven simulation, meaning
# you have these defined qualities of a 'world'
# and the player's aims is to manipulate
# the systems in the simulation towards a 
# winning outcome (biggest city, low crime, etc.)
#
# By data-driven, we mean the simulations
# systems rely on a set of data which they
# use to figure out how they react to the
# players influence (via implementing 
# 'policies' in this case)
#
# SO I've written a basic stub of a program
# which takes some arbitrary data I've chosen
# and executes some 'policies' which are just
# sets of rules against this data, and we get
# to watch the outcome. This is what a 
# 'simulation' game is all about. 
#
# ENOUGH JABBERING, LETS HAVE A LOOK AT SOME CODE


# ==================
# Functions
# ==================
#
# A function is like an oven, which
# takes ingredients and produces a 
# cooked dish. 
#
# Below are some functions we're going to
# use in our baby simulation
# to help us play with some ideas about
# these policies

# This takes a policy and determines
# how it would perform within a given
# community
def applyPolicy(policy, community):
  
  # Make specific variables for each part of the community data
  # so that it's easier to read what we're doing later on
  comm_name   = community["name"]
  comm_budget = community["per_capita_income"] * community["population"]
  comm_crime  = community["crime"]
  comm_area   = community["area"]

  # Do the same for the policy
  pol_name = policy["name"]
  pol_cost = policy["cost"]
  pol_area = policy["area"]
  pol_safety = policy["safety"]

  # Now lets do some tests of the policy against the community
  if pol_cost > comm_budget: 
    print pol_name + " is too expensive for " + comm_name
  else:
    print pol_name + " is affordable for " + comm_name

  if pol_area > comm_area:
    print pol_name + " is too big for " + comm_name
  else: 
    print pol_name + " will fit within " + comm_name

  if comm_crime > pol_safety:
    print comm_name + " is to dangerous for " + pol_name
  else: 
    print pol_name + " is safe in " + comm_name

# =========
# Main 
# =========
#
# In many programming languages there is this
# idea of a 'main' function which is a function
# just like any other EXCEPT it is the first one
# executed by the program (python in this case) 
# so this is where everything gets started
def main():
  
  #
  # What we're doing right below is saying "The variable named
  # communities is a list of objects with certain properties"
  #
  # We know it's a list because we have those square brackets [] 
  # surrounding things RIGHT after the equals (=) sign. TO MAKE IT
  # EASIER TO READ I MOVE THE FIRST ELEMENT OF THE LIST ONTO A NEW 
  # LINE. 
  #
  # The square brackets are surrounding things with curly brackets {}, 
  # these are objects which have arbitrary attributes. Each attribute 
  # has a NAME and a VALUE. So the object below
  # {"first_name": "Tom"} 
  # Is just a piece of data which says "first_name" equals "Tome". In 
  # the communities variable, you see that we've defined three of these 
  # objects with sets of attributes about them. These are what I'm calling
  # communities, and kinda define the environment we're working in. 
  #
  # Reading each of the objects attributes, it becomes clear I'm 
  # defining a really basic set of data about three communities. 
  
  # This is a variable named communties
  communities = [ # <== This bracket means we're starting a list
    { # <== This means that we're defining an object (which is part of the list)
      "name" : "La Pine", # <== This means the object has a "name" which is "La Pine"
      "population": 1708, # And a "population" of 1708
      "per_capita_income":14680,  
      "biome" : "high_desert",
      "area": 18080707, # in square meters
      "crime": 50 # use arbitrary numbers to make it easier to compare
    }, # <== This is the end of the object definition, and the comma means we have another element we're adding to the list
    {
      "name" : "Bend",
      "population": 82000,
      "per_capita_income":28261,  
      "biome" : "high_desert",
      "area": 86170000, # in square meters
      "crime": 10
    },
    {
      "name" : "Cresent",
      "population": 715,
      "per_capita_income":23133,  
      "biome" : "high_desert",
      "area": 100000, # in square meters
      "crime": 70
    }
  ] # <== And that's the end of the list of communities
  
  # Policies is ANOTHER list, with more objects. These objects are each 
  # a definition of a policy, and each attribute defines a bit of data about the
  # policy, which will be used to determine how the policy does in the community. 
  policies = [
    {
      "name": "High School Auditorium",
      "cost": 3700000,
      "area": 669, # in square meters
      "zoning": "school",
      "safety": 60
    },
    {
      "name": "Tesla Factory",
      "cost": 20000000,
      "area": 10000, # in square meters
      "zoning": "commercial",
      "safety": 30
    },
    {
      "name": "Military Base",
      "cost": 500000,
      "area": 100000, # in square meters
      "zoning": "commerical",
      "safety": 100
    },
    {
      "name": "NASA Launch Facility",
      "cost": 500000000,
      "area": 10000000, # in square meters
      "zoning": "commerical",
      "safety": 5
    },
  ]

  # So now let's go through the list of policies and list of 
  # communities and actually see how they do. 
  
  for policy in policies: # Loop over the policies
    for community in communities: # Now loop over each community for the current policy
      # The \n just means put a newline space between the last thing printed on the screen
      # when this runs. 
      print "\n === Applying policy " + policy["name"] + " to " + community["name"] + " === "
      applyPolicy(policy, community) # Here we CALL the function we defined way back up in the beginning. 
                                     # CALLING means to execute, so we're actually using the applyPolicy code
                                     # when we do this. The applyPolicy function needs a policy and a community to 
                                     # work, so inside the parenthesis, we're giving it a policy (from the list of policies we're looping over)
                                     # and a community (from the list of communities we're looping over as well)
                                     


# ===============
# START
#================
#
# WHEW! After all that jabbering we haven't actually executed ANYTHING till right below
# this comment. So what happened above is we DEFINED what main() actually is (A function which
# has some community and policy lists and calls applyPolicy on all the possible pairs of the
# communities and policies). Here is where we call main(), executing it's logic. 
main()
