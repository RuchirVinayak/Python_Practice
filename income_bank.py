income=int(input("Enter your salary :"))
save=int(input("How much do you want to save this month ? :"))
to_spend=income-save
transactions={"utilities":0,"shopping":0,"food":0}
u=int(input("Enter the amount spent this month on utilities :"))
s=int(input("Enter the amount spent this month on shopping :"))
f=int(input("Enter the amount spent this month on food :"))
transactions["utilities"]=u
transactions["shopping"]=s
transactions["food"]=f
total_spent=sum(transactions.values())
remaining_balance=to_spend-total_spent
print("Utilities:",transactions["utilities"])
print("Shopping:",transactions["shopping"])
print("Food:",transactions["food"])
print("Your remaining balance is:", remaining_balance)
print("Amount in savings account: ",save)