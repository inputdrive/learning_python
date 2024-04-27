# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Write your code below: 
def f_to_c():
    f_temp = 100
    c_temp = (f_temp - 32) * 5/9
    return c_temp
    print(c_temp)
# step 2    
f100_in_celsius = round(f_to_c(),2)
print(f100_in_celsius)

# step 3
def c_to_f():
    c_temp = 0
    f_temp = c_temp * (9/5) + 32
    return f_temp
    print(f_temp)

# step 4
c0_in_fahrenheit = round(c_to_f(),2)
print(c0_in_fahrenheit)

# step 5

def get_force(mass, acceleration):
    return mass * acceleration  
    print(get_force)    
# step 6
train_force = get_force(train_mass, train_acceleration)
print(train_force)

# step 7
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# step 8
def get_energy(mass, c=3*10**8):
    return mass * c**2
    print(get_energy)
# step 9, 10
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies" , bomb_energy , "Joules.")

# step 11
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance
    print(get_work)

# step 12,13
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
