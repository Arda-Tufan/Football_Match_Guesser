import configparser
import config


print("Hello fellow user! I see that you want to bid on a team or you are just curious about this project (Probably the first one)!")
print("This is a script that will look into;\n a team's attack power,\n a team's defence weakness,\n and finally check whether they are the home team or not.")
print("You will be asked to input a team name in the prompt. Currently, there is 20 teams from Süperlig they are:\nFenerbahce\nBesiktas\nGalatasaray\nTrabzonspor\nMedipol-Başakşehir\nKaragumruk\nAlanyaspor\nCaykur-Rizespor\nAdana-Demirspor\nSivasspor\nGaziantep\nGöztepe\nKasımpaşa\nAntalyaspor\nKayserispor\nKonyaspor\nHatayspor\nYeni-Malatya\nAltayspor\nGiresunspor")
print("---!---WARNING---!---\nTHIS SCRIPT IS NOT 100% ACCURATE. IT IS BASED ON THE PREVIOUS YEAR'S STATS! DO NOT BET TRUSTING THIS SCRIPT! USER DISCREATION ADVISED!")
print("Finally please enter the team names according to the list or else it won't be accepted as an anwser!")








#Read the home teams section in config file and look to the data of the home team's attack and defence weakness

config = configparser.RawConfigParser()

while True:
 try:
  home_team = input("Enter the home team (Match will be played in this team's stadium): ")

  away_team = input("Enter the away team (This team will play match in the other team's stadium): ")

  config.read('TEAM_STATS.ini', encoding="utf8")
  home_stats_dict = dict(config.items(home_team.upper()))
  home_team_atck_pwr = list(home_stats_dict.items())[0][1]
  home_team_defence_wkns = list(home_stats_dict.items())[1][1]

  away_stats_dict = dict(config.items(away_team.upper()))
  away_team_atck_pwr = list(home_stats_dict.items())[0][1]
  away_team_defence_wkns = list(away_stats_dict.items())[1][1]
  break
 except configparser.NoSectionError:
     print("please enter one of the team names from the list above or add your own! Make sure there are no typos when entering the team name! If you added a new team, the list won't show it however it will be eligable for calculations.".upper())

#Read the away teams section in config file and look to the data of the away team's attack and defence weakness



#Variables for average scored goals for away and home team

avrg_home_team_score = 1.51

avrg_away_team_score = 1.21



#Do the requried calculations
home_team_score_prob = float(float(home_team_atck_pwr) * float(avrg_home_team_score) * float(away_team_defence_wkns))

away_team_score_prob = float(float(away_team_atck_pwr) * float(avrg_away_team_score) * float(home_team_defence_wkns))


print("The home team will end up scoring (READ THE DOCS IN GITHUB TO BETTER UNDERSTAND THE MEANING OF THE NUMBER PRINTED!): " + str(home_team_score_prob) + " goals")
if str(round(home_team_score_prob)) != str(home_team_score_prob)[0]:
 
 print(home_team.lower() + " will much likely end up scoring " + str(round(home_team_score_prob)) + "goals or with less chance, will end up scoring " + str(int(home_team_score_prob)) + " goals")
else:
 print(home_team.lower() + " will very likely end up scoring " + str(round(home_team_score_prob)) + " goals")

print("The away team will end up scoring (READ THE DOCS IN GITHUB TO BETTER UNDERSTAND THE MEANING OF THE NUMBER PRINTED!): " + str(away_team_score_prob) + " goals")

if str(round(away_team_score_prob)) != str(away_team_score_prob)[0]:
 
 print(away_team.lower() + " will much likely end up scoring " + str(round(away_team_score_prob)) + " goals or with less chance, will end up scoring " + str(int(away_team_score_prob)) + " goals")
else:
 print(away_team.lower() + " will very likely end up scoring " + str(round(away_team_score_prob)) + " goals")





