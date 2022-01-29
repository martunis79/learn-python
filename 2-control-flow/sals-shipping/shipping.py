# @martunis79
# Outputs error message if weight isn't bigger than 0 lb.
# Outputs the all the costs and which one is the cheapest method

weight = 8

print("Weight of Package: ", weight, "lb")
# Checks if the weight is a valid value (> 0 lb)
if weight > 0:
  # Ground Shipping
  if weight <= 2:
    cost_ground = weight * 1.5
  elif weight <= 6:
    cost_ground = weight * 3
  elif weight <= 10:
    cost_ground = weight * 4
  else:
    cost_ground = weight * 4.75
  cost_ground += 20 # Add Ground Shipping Flat charge
  print("Ground shipping: $", cost_ground)

  # Ground Shipping Premium
  cost_premium = 125
  print("Ground shipping Premium: $", cost_premium)

  #Drone Shipping
  if weight <= 2:
    cost_drone = weight * 4.5
  elif weight <= 6:
    cost_drone = weight * 9
  elif weight <= 10:
    cost_drone = weight * 12
  else:
    cost_drone = weight * 14.25
  print("Drone shipping: $", cost_drone)

  # Output the cheapest method
  if cost_premium < cost_ground and cost_premium < cost_drone:
    print("The cheapest method is Ground Shipping Premium $", cost_premium)
  else:
    if cost_drone < cost_ground:
      print("The cheapest method is Drone Shipping $", cost_drone)
    else:
      print("The cheapest method is Ground Shipping $", cost_ground)
else:
  print("ERROR: Incorrect weight")