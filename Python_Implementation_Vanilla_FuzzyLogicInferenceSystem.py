

# Take in crisp inputs and return a crisp output
def fuzzy_infer(serviceRating, foodRating):

    fuzzified_service = fuzzify_serviceRating(serviceRating)
    fuzzified_food = fuzzify_foodRating(foodRating)

    service_poor = fuzzified_service[0]
    service_good = fuzzified_service[1]
    service_excellent = fuzzified_service[2]
    
    food_lousy = fuzzified_food[0]
    food_delicious = fuzzified_food[1]


    # Rule base
    # We have 4 Rules:
    # R1: If service is poor then tip is cheap.
    # R2: If service is excellent and food is delicious then tip is generous.
    # R3: If food is lousy then tip cheap.
    # R4: If service is good and food is delicious then tip is average. 

    
    # R1 and R3 [Because they have the exact same consequent]:
    single_value_from_antecedent = max(service_poor, food_lousy)

    # Computing the Area of the Final Output MF from R1 and R3 [So as to compute the Centroid later]
    if single_value_from_antecedent != 0:
        x1 = single_value_from_antecedent*2
        x2 = -1*(single_value_from_antecedent - 3)
        centroid_R1_R3, area_R1_R3 = find_centroid_x_val(0,x1,x2,3, single_value_from_antecedent)
    else:
        centroid_R1_R3 = 0
        area_R1_R3 = 0
       
    
    # R2
    single_value_from_antecedent = min(service_excellent,food_delicious)

    # Computing the Area of the Final Output MF from R2 [So as to compute the Centroid later]
    if single_value_from_antecedent != 0:
        x1 = single_value_from_antecedent+4
        x2 = (single_value_from_antecedent - 2.25)/(-0.25)
        centroid_R2, area_R2 = find_centroid_x_val(4,x1,x2,9, single_value_from_antecedent)
    else:
        centroid_R2 = 0
        area_R2 = 0


    # R4
    single_value_from_antecedent = min(service_good,food_delicious)

    # Computing the Area of the Final Output MF from R4 [So as to compute the Centroid later]
    if single_value_from_antecedent != 0: 
        x1 = single_value_from_antecedent+3
        x2 = -1*(single_value_from_antecedent - 5)
        centroid_R4, area_R4 = find_centroid_x_val(3,x1,x2,5, single_value_from_antecedent)
    else:
        centroid_R4 = 0
        area_R4 = 0



    # Compute the final, average Centroid/ Centre of Mass [which gives us the output_tip]:
    output_tip = (centroid_R1_R3 + centroid_R2 + centroid_R4) / (area_R1_R3 + area_R2 + area_R4)
    return output_tip






# Fuzzify the crisp input 'serviceRating'
# There are 3 MFs - 1. 'poor' 2. 'good' 3. 'excellent'
def fuzzify_serviceRating(serviceRating):
    result = []
    
    # Get the Membership Grade for 'poor' [ 'trapezoidal(0 0 4 5) ]:
    if serviceRating >=5:
        poor = 0
    elif serviceRating <=4:
        poor = 1
    else:
        poor = 1 - (serviceRating-4)  # Plot out and See the Trapezoidal MF to understand this.

    
    # Get the Membership Grade for 'good' [ 'trapezoidal(4 5 6 7) ]:
    if serviceRating >=7:
        good = 0
    elif serviceRating <=4:
        good = 0
    elif serviceRating <5:
        good = serviceRating - 4   # Plot out and See the Trapezoidal MF to understand this.
    elif serviceRating >6:
        good = 1 - (serviceRating-6)
    else:
        good = 1


    # Get the Membership Grade for 'excellent' [ 'trapezoidal(6 7 10 10) ]:
    if serviceRating >=7:
        excellent = 1
    elif serviceRating <=6:
        excellent = 0
    else:
        excellent = serviceRating -6  # Plot out and See the Trapezoidal MF to understand this.

    result.append(poor)
    result.append(good)
    result.append(excellent)
    return result
    


# Fuzzify the crisp input 'foodRating'
# There are 2 MFs - 1. 'lousy' 2. 'delicious'
def fuzzify_foodRating(foodRating):
    result = []
    
    # Get the Membership Grade for 'lousy' [ 'trapezoidal(0 0 2 3) ]:
    if foodRating >=3:
        lousy = 0
    elif foodRating <=2:
        lousy = 1
    else:
        lousy = 1- (foodRating-2)  # Plot out and See the Trapezoidal MF to understand this.

    
    # Get the Membership Grade for 'delicious' [ 'trapezoidal(7 8 10 10) ]:
    if foodRating >=8:
        delicious = 1
    elif foodRating <=7:
        delicious = 0
    else:
        delicious = foodRating-7  # Plot out and See the Trapezoidal MF to understand this.

    result.append(lousy)
    result.append(delicious)
    return result


# Fuzzify the crisp output 'tip'
# There are 3 MFs - 1. 'cheap' 2. 'average' 3. 'generous'
def fuzzify_tip(crisp_tip):
    result = []

    # Get the Membership Grade for 'cheap' [ 'trapezoidal(0 2 2 3) ]:
    if crisp_tip >=3:
        cheap = 0
    elif crisp_tip <=2:
        cheap = 0.5*crisp_tip  # Plot out and See the Trapezoidal MF to understand this.
    else:
        cheap = 1 - (crisp_tip-2)   # Plot out and See the Trapezoidal MF to understand this.

    
    # Get the Membership Grade for 'average' [ 'trapezoidal(3 4 4 5) ]:
    if crisp_tip >=5:
        average = 0
    elif crisp_tip <=3:
        average = 0
    elif crisp_tip <=4:
        average = crisp_tip - 3   # Plot out and See the Trapezoidal MF to understand this.
    else:
        average = 1 - (crisp_tip-4)  # Plot out and See the Trapezoidal MF to understand this.


    # Get the Membership Grade for 'generous' [ 'trapezoidal(4 5 5 9) ]:
    if crisp_tip >=9:
        generous = 0
    elif crisp_tip <=4:
        generous = 0
    elif crisp_tip <=5:
        generous = crisp_tip - 4   # Plot out and See the Trapezoidal MF to understand this.
    else:
        generous = 1 - (0.25* (crisp_tip-5)  ) # Plot out and See the Trapezoidal MF to understand this.

    result.append(cheap)
    result.append(average)
    result.append(generous)
    return result



# Models a Trapezium function;
# Given x-value, it returns the y-value of the trapezium;
# It expects Parameters of a Trapezium defined using (a,b,c,d), the height of the Trapezium,
# and the x-value
def trapezium(a,b,c,d, height, x):
    if x <= b:
        y = ((x-a)/(b-a))*height
    elif x <=c:
        y = height
    else:
        y = ((d-x)/(d-c))*height
    return y


# Find and Return the x-value of the Centroid; It is given a Trapezium with the same Parameters as 'trapezium()' but without the x-value
# It takes a number of samples (x-values) of that Trapezium, then it computes the Weighted Sum of these samples. The corresponding weight for each sample is that sample's area [see below].
def find_centroid_x_val(a,b,c,d, height):
    x_list = []
    
    for i in range(int(d-a)): # Compute the number of intervals (x-values) of that trapezium that we want to sample.
        x_list.append(i+0.5+a)
  
    centroid_x_val = 0  # to be used later as the weighted sum of the samples
    total_area = 0
    for x in x_list:
        x1 = x-0.5
        x2 = x+0.5
        if (b>x1 and b<x2):  # if b is between x1 and x2
            y1 = trapezium(a,b,c,d, height, x1)  # compute the y-value for a value that is 0.5 unit left of our x
            y2 = trapezium(a,b,c,d, height, b)  # compute the y-value for b
            y3 = trapezium(a,b,c,d, height, x2)  # compute the y-value for a value that is 0.5 unit right of our x
            area = (y1+y2)*(0.5)*(b-x1) + (y2+y3)*(0.5)*(x2-b)  # is the area under x-0.5 and x+0.5
                
        elif (c>x1 and c<x2): # if c is between x1 and x2
            y1 = trapezium(a,b,c,d, height, x1)  # compute the y-value for a value that is 0.5 unit left of our x
            y2 = trapezium(a,b,c,d, height, c)  # compute the y-value for c
            y3 = trapezium(a,b,c,d, height, x2)  # compute the y-value for a value that is 0.5 unit right of our x
            area = (y1+y2)*(0.5)*(c-x1) + (y2+y3)*(0.5)*(x2-c)            

        else:         # Neither b nor c is between x1 and x2
            y1 = trapezium(a,b,c,d, height, x1)  # compute the y-value for a value that is 0.5 unit left of our x
            y2 = trapezium(a,b,c,d, height, x2)  # compute the y-value for a value that is 0.5 unit right of our x
            area = (y1+y2)*(0.5)*(1)    # Compute the area using the general trapezium area formula [this area formula works for triangles and rectangles too]

        total_area = total_area + area
        centroid_x_val = centroid_x_val + area*x    # centroid_x_val will be a weighted sum of all the sampled x-values whereby the area represent the weights

    return (centroid_x_val, total_area)  # to return the total_area as well so as to later compute the averaged centroid_x_val among all the samples
    



# Main

# Set your Service Rating and Food Rating:
serviceRating = 4.5
foodRating = 2.5
tip = fuzzy_infer(serviceRating, foodRating)
print("Your Tip is: ")
print(tip)
