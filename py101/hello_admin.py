current_users = ['dave', 'ayman', 'rafiki', 'saint', 'jog', 'saint', 'amar', 'bhat']
new_users = ['ayman', 'rafiki', 'saint', 'frank', 'mario', 'burna', 'waiyaki']
for new_user in new_users:
    if new_user in current_users:
        print(f"Username already exists. Please enter a new username")
    else:
        print(f"Username available.")