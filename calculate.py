import datetime

#This is a script to calculate the amount of time it will take to lose 
#a certain amount of pounds

Current_weight = int(input("Current weight in pounds:"))
goal_weight = int(input("Desired weight in pounds:"))
avg_lbs_week = 1.5

start_date = datetime.date.today()
end_date = start_date

while Current_weight > goal_weight:

	#7 days have gone by 
	end_date += datetime.timedelta(days=7)
	#and this is our current wight
	Current_weight -= avg_lbs_week


print(f'you will reach goal on {end_date} if you lose {avg_lbs_week} pounds per week')
print(f'Reached Goal in {(end_date - start_date).days // 7} weeks')
