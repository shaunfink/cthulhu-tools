# TODO: This stuff should really be in a database

# List of Stats
stats_list = ["strength" , "constitution", "dexterity", "appearance", "power", "size", "intelligence", "education"]

# Stats and Rolls
rolls = {
    "strength": "3d6*5",
    "constitution": "3d6*5",
    "dexterity": "3d6*5",
    "appearance": "3d6*5",
    "power": "3d6*5",
    "size": "2d6*5",
    "intelligence": "2d6*5",
    "education": "2d6*5",
    "luck": "3d6*5",
    "percentile": "d100",
    "improvement": "d10"
}

# rolls_flat = {"strength": "3d6*5", "constitution": "3d6*5", "dexterity": "3d6*5", "appearance": "3d6*5", "power": "3d6*5", "luck": "3d6*5", "size": "2d6*5", "intelligence": "2d6*5", "education": "2d6*5"}

# Stats and Rolls
rolls_v2 = {
    "strength": {"quantity": "3", "die": "d6", "modifier": "multiply", "value": "5"},
    "constitution": {"quantity": "3", "die": "d6", "modifier": "multiply", "value": "5"},
    "dexterity": {"quantity": "3", "die": "d6", "modifier": "multiply", "value": "5"},
    "appearance": {"quantity": "3", "die": "d6", "modifier": "multiply", "value": "5"},
    "power": {"quantity": "3", "die": "d6", "modifier": "multiply", "value": "5"},
    "luck": {"quantity": "3", "die": "d6", "modifier": "multiply", "value": "5"},
    "size": {"quantity": "2", "die": "d6", "modifier": "multiply", "value": "5"},
    "intelligence": {"quantity": "2", "die": "d6", "modifier": "multiply", "value": "5"},
    "education": {"quantity": "2", "die": "d6", "modifier": "multiply", "value": "5"}
}

# rolls_v2_flat = {"strength": {"quantity": "3", "die": "d6", "modifier": "multiply", "value": "5"}, "constitution": {"quantity": "3", "die": "d6", "modifier": "multiply", "value": "5"}, "dexterity": {"quantity": "3", "die": "d6", "modifier": "multiply", "value": "5"}, "appearance": {"quantity": "3", "die": "d6", "modifier": "multiply", "value": "5"}, "power": {"quantity": "3", "die": "d6", "modifier": "multiply", "value": "5"}, "luck": {"quantity": "3", "die": "d6", "modifier": "multiply", "value": "5"}, "size": {"quantity": "2", "die": "d6", "modifier": "multiply", "value": "5"}, "intelligence": {"quantity": "2", "die": "d6", "modifier": "multiply", "value": "5"}, "education": {"quantity": "2", "die": "d6", "modifier": "multiply", "value": "5"}}

skills = [
    {"name": "Accounting", "base": "05", "link": "", "groups": ""},
    {"name": "Acting", "base": "05", "link": "Arts and Crafts", "groups": ""},
    {"name": "Animal Handling", "base": "05", "link": "", "groups": "Uncommon"},
    {"name": "Anthropology", "base": "01", "link": "", "groups": ""},
    {"name": "Appraise", "base": "05", "link": "", "groups": ""},
    {"name": "Archaeology", "base": "01", "link": "", "groups": ""},
    {"name": "Arts and Crafts", "base": "05", "link": "", "groups": "Specializations"},
    {"name": "Artillery", "base": "01", "link": "", "groups": "Uncommon"},
    {"name": "Astronomy", "base": "01", "link": "Science", "groups": ""},
    {"name": "Axe", "base": "15", "link": "Fighting", "groups": ""},
    {"name": "Biology", "base": "01", "link": "Science", "groups": ""},
    {"name": "Botany", "base": "01", "link": "Science", "groups": ""},
    {"name": "Bow", "base": "15", "link": "Firearms", "groups": ""},
    {"name": "Brawl", "base": "25", "link": "Fighting", "groups": ""},
    {"name": "Chainsaw", "base": "10", "link": "Fighting", "groups": ""},
    {"name": "Charm", "base": "15", "link": "", "groups": ""},
    {"name": "Chemistry", "base": "01", "link": "Science", "groups": ""},
    {"name": "Climb", "base": "20", "link": "", "groups": ""},
    {"name": "Computer Use", "base": "05", "link": "", "groups": "Modern"},
    {"name": "Credit Rating", "base": "00", "link": "", "groups": ""},
    {"name": "Cryptography", "base": "01", "link": "Science", "groups": ""},
    {"name": "Cthulhu Mythos", "base": "00", "link": "", "groups": ""},
    {"name": "Demolitions", "base": "01", "link": "", "groups": "Uncommon"},
    {"name": "Disguise", "base": "05", "link": "", "groups": ""},
    {"name": "Diving", "base": "01", "link": "", "groups": "Uncommon"},
    {"name": "Dodge", "base": "half DEX", "link": "", "groups": ""},
    {"name": "Drive Auto", "base": "20", "link": "", "groups": ""},
    {"name": "Electrical Repair", "base": "10", "link": "", "groups": ""},
    {"name": "Electronics", "base": "01", "link": "", "groups": "Modern"},
    {"name": "Engineering", "base": "01", "link": "Science", "groups": ""},
    {"name": "Fast Talk", "base": "05", "link": "", "groups": ""},
    {"name": "Fighting", "base": "varies", "link": "", "groups": "Specializations"},
    {"name": "Fine Art", "base": "05", "link": "Arts and Crafts", "groups": ""},
    {"name": "Firearms", "base": "varies", "link": "", "groups": "Specializations"},
    {"name": "First Aid", "base": "30", "link": "", "groups": ""},
    {"name": "Flail", "base": "10", "link": "Fighting", "groups": ""},
    {"name": "Flamethrower", "base": "10", "link": "Firearms", "groups": ""},
    {"name": "Forensics", "base": "05", "link": "Science", "groups": ""},
    {"name": "Forgery", "base": "01", "link": "Arts and Crafts", "groups": ""},
    {"name": "Garrote", "base": "15", "link": "Fighting", "groups": ""},
    {"name": "Geology", "base": "01", "link": "Science", "groups": ""},
    {"name": "Handgun", "base": "20", "link": "Firearms", "groups": ""},
    {"name": "Heavy Weapons", "base": "10", "link": "Firearms", "groups": ""},
    {"name": "History", "base": "05", "link": "", "groups": ""},
    {"name": "Hypnosis", "base": "01", "link": "", "groups": "Uncommon"},
    {"name": "Intimidate", "base": "15", "link": "", "groups": ""},
    {"name": "Jump", "base": "20", "link": "", "groups": ""},
    {"name": "Language (Other)", "base": "01", "link": "", "groups": "Specializations"},
    {"name": "Language (Own)", "base": "EDU", "link": "", "groups": ""},
    {"name": "Law", "base": "05", "link": "", "groups": ""},
    {"name": "Library Use", "base": "20", "link": "", "groups": ""},
    {"name": "Listen", "base": "20", "link": "", "groups": ""},
    {"name": "Locksmith", "base": "01", "link": "", "groups": ""},
    {"name": "Lore", "base": "01", "link": "", "groups": "Uncommon, Specializations"},
    {"name": "Machine Gun", "base": "10", "link": "Firearms", "groups": ""},
    {"name": "Mathematics", "base": "10", "link": "Science", "groups": ""},
    {"name": "Mechanical Repair", "base": "10", "link": "", "groups": ""},
    {"name": "Medicine", "base": "01", "link": "", "groups": ""},
    {"name": "Meteorology", "base": "01", "link": "Science", "groups": ""},
    {"name": "Natural World", "base": "10", "link": "", "groups": ""},
    {"name": "Navigate", "base": "10", "link": "", "groups": ""},
    {"name": "Occult", "base": "05", "link": "", "groups": ""},
    {"name": "Operate Heavy Machinery", "base": "01", "link": "", "groups": ""},
    {"name": "Persuade", "base": "10", "link": "", "groups": ""},
    {"name": "Pharmacy", "base": "01", "link": "Science", "groups": ""},
    {"name": "Photography", "base": "05", "link": "Arts and Crafts", "groups": ""},
    {"name": "Physics", "base": "01", "link": "Science", "groups": ""},
    {"name": "Pilot", "base": "01", "link": "", "groups": "Specializations"},
    {"name": "Psychoanalysis", "base": "01", "link": "", "groups": ""},
    {"name": "Psychology", "base": "10", "link": "", "groups": ""},
    {"name": "Read Lips", "base": "01", "link": "", "groups": "Uncommon"},
    {"name": "Ride", "base": "05", "link": "", "groups": ""},
    {"name": "Rifle", "base": "25", "link": "Firearms", "groups": ""},
    {"name": "Science", "base": "01", "link": "", "groups": "Specializations"},
    {"name": "Shotgun", "base": "25", "link": "Firearms (Rifle/Shotgun)", "groups": ""},
    {"name": "Sleight of Hand", "base": "10", "link": "", "groups": ""},
    {"name": "Spear", "base": "20", "link": "Fighting (or Throw)", "groups": ""},
    {"name": "Spot Hidden", "base": "25", "link": "", "groups": ""},
    {"name": "Stealth", "base": "20", "link": "", "groups": ""},
    {"name": "Submachine Gun", "base": "15", "link": "Firearms", "groups": ""},
    {"name": "Survival", "base": "10", "link": "", "groups": "Specializations"},
    {"name": "Sword", "base": "20", "link": "Fighting", "groups": ""},
    {"name": "Swim", "base": "20", "link": "", "groups": ""},
    {"name": "Throw", "base": "20", "link": "", "groups": ""},
    {"name": "Track", "base": "10", "link": "", "groups": ""},
    {"name": "Whip", "base": "05", "link": "Fighting", "groups": ""},
    {"name": "Zoology", "base": "01", "link": "Science", "groups": ""}
]

occupations = [
    "Accountant",
    "Acrobat",
    "Actor",
    "Agency Detective",
    "Alienist [Classic]",
    "Animal Trainer",
    "Antiquarian [Lovecraftian]",
    "Antique Dealer",
    "Archaeologist [Lovecraftian]",
    "Architect",
    "Artist",
    "Asylum Attendant",
    "Assassin – see Criminal",
    "Athlete",
    "Author [Lovecraftian]",
    "Aviator [Classic] – see Pilot",
    "Bank Robber – see Criminal",
    "Bartender",
    "Big Game Hunter",
    "Book Dealer",
    "Bootlegger – see Criminal",
    "Bounty Hunter",
    "Boxer/Wrestler",
    "Burglar – see Criminal",
    "Butler/Valet/Maid",
    "Chaufeur – see Driver",
    "Clergy, Member of the",
    "Computer Programmer/Technician/Hacker [Modern]",
    "Conman – see Criminal",
    "Cowboy/girl",
    "Craftsperson",
    "Criminal – also Gangster",
    "Cult Leader",
    "Deprogrammer [Modern]",
    "Designer",
    "Dilettante [Lovecraftian]",
    "Diver",
    "Doctor of Medicine [Lovecraftian] – also see Psychiatrist",
    "Drifter",
    "Driver",
    "Editor",
    "Elected Official",
    "Engineer",
    "Entertainer",
    "Explorer [Classic]",
    "Farmer",
    "Federal Agent",
    "Fence – see Criminal",
    "Fire Fighter",
    "Foreign Correspondent",
    "Forensic Surgeon",
    "Forger/Counterfeiter – see Criminal",
    "Gambler",
    "Gangster",
    "Gun Moll [Classic] – see Criminal",
    "Gentleman/Lady",
    "Hacker – see Computer Programmer",
    "Hobo",
    "Hospital Orderly",
    "Journalist [Lovecraftian]",
    "Judge",
    "Laboratory Assistant",
    "Laborer",
    "Lawyer",
    "Librarian [Lovecraftian]",
    "Lumberjack – see Laborer",
    "Maid – see Butler",
    "Mechanic (and Skilled Trades)",
    "Military Officer",
    "Miner – see Laborer",
    "Missionary",
    "Mountain Climber",
    "Museum Curator",
    "Musician",
    "Nurse",
    "Occultist [Lovecraftian]",
    "Outdoorsman/Outdoorswoman",
    "Parapsychologist",
    "Pharmacist",
    "Photographer",
    "Photojournalist – see Photographer",
    "Pilot – also see Aviator",
    "Police Detective/Officer [Lovecraftian]",
    "Private Investigator",
    "Professor [Lovecraftian]",
    "Prospector",
    "Prostitute",
    "Psychiatrist",
    "Psychologist/Psychoanalyst",
    "Reporter – see Journalist",
    "Researcher",
    "Sailor",
    "Salesperson",
    "Scientist",
    "Secretary",
    "Shopkeeper",
    "Smuggler – see Criminal",
    "Soldier/Marine",
    "Spy",
    "Street Punk – see Criminal",
    "Student/Intern",
    "Stuntman",
    "Taxi Driver – see Driver",
    "Thug – see Criminal",
    "Tribe Member",
    "Undertaker",
    "Union Activist",
    "Valet – see Butler",
    "Waitress/Waiter",
    "White-collar Worker",
    "Zealot",
    "Zookeeper"
]

# "occupations_detailed" = [
#     {
#         "name": "accountant",
#         "skill-points": "EDU x 4",
#         "credit-rating": "30-70",
#         "suggested-contacts": [
#             "Business Associates",
#             "Legal Professionals",
#             "Financial Sector (Bankers, Other Accountants)"
#         ],
#         "skills": [
#             "Accounting",
#             "Law",
#             "Library Use",
#             "Listen",
#             "Persuade",
#             "Spot Hidden",
#             "Any two other skills as personal or era specialities (eg. Computer Use)"
#         ]
#     },
#     {
#         "name": "Acrobat",
#         "skill-points": "EDU × 2 + DEX × 2",
#         "credit-rating": "9–20",
#         "suggested-contacts": [
#             "Amateur Athletic Circles",
#             "Sports Writers", 
#             "Circuses", 
#             "Carnivals"
#         ],
#         "skills": [
#             "Climb",
#             "Dodge",
#             "Jump",
#             "Row",
#             "Spot Hidden",
#             "Swim",
#             "Any two other skills as personal or era specialties"
#         ]
#     },
#     {
#         "name": "Stage Actor",
#         "skill-points": "EDU × 2 + APP × 2",
#         "credit-rating": "9–40",
#         "suggested-contacts": [
#             "Theatre industry",
#             "Newspaper arts critics",
#             "Aactor’s guild or union"
#         ],
#         "skills": [
#             "Art/Craft (Acting)",
#             "Disguise",
#             "Fighting",
#             "History",
#             "Two interpersonal skills (Charm, Fast Talk, Intimidate, or Persuade)",
#             "Psychology",
#             "Any one other skill as a personal or era specialty"
#         ]
#     },
#     {
#         "name": "Film Star",
#         "skill-points": "EDU × 2 + APP × 2",
#         "credit-rating": "20-90",
#         "suggested-contacts": [
#             "Film industry",
#             "Media Critics",
#             "Writers"
#         ],
#         "skills": [
#             "Art/Craft (Acting)",
#             "Disguise",
#             "Drive Auto",
#             "Two interpersonal skills (Charm, Fast Talk, Intimidate, or Persuade)",
#             "Psychology",
#             "Any two other skills as personal or era specialties (e.g. Ride or Fighting)"
#         ]
#     }
# ]