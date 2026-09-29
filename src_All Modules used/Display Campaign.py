# Display Campaign
def view_campaign():
  print("\n---Upcoming Healthcare Campaign---")

  for i, Campaign in enumerate(campaign,start=1):

     print("\nCampaign",i)
     print("Name:",Campaign["Name"])
     print("Date:",Campaign["Date"])
     print("Time:",Campaign["Time"])
     print("Venue:",Campaign["Venue"])
