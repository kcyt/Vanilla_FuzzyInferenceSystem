fis = newfis('expert_tipping_system');    % Initialise a new Fuzzy Inference System

fis = addvar(fis, 'input', 'service_rating', [0 10]); % Add in an Input Variable called 'service_rating' that has a range from 0 to 10.
fis = addvar(fis, 'input', 'food_rating', [0 10]); % Add in an Input Variable called 'food_rating' that has a range from 0 to 10.
fis = addvar(fis,'output','tip',[0 10]); % Add in an Output Variable called 'tip' which has a range from 0 to 10

% Set the MFs for 'service_rating'
fis = addmf(fis,'input',1,'poor','trapmf',[0 0 4 5]);    % The '1' indicates the Index of the Input Variable 'service_rating'
fis = addmf(fis,'input',1,'good','trapmf',[4 5 6 7]);
fis = addmf(fis,'input',1,'excellent','trapmf',[6 7 10 10]);

% Set the MFs for 'food_rating'
fis = addmf(fis,'input',2,'lousy','trapmf',[0 0 2 3]);   % The '2' indicates the Index of the Input Variable 'food_rating'
fis = addmf(fis,'input',2,'delicious','trapmf',[7 8 10 10]);

% Set the MFs for 'tip'
fis = addmf(fis,'output',1,'cheap','trapmf',[0 2 2 3]);     % The '1' indicates the Index of the Output Variable 'tip'
fis = addmf(fis,'output',1,'average','trapmf',[3 4 4 5]); 
fis = addmf(fis,'output',1,'generous','trapmf',[4 5 5 9]);

% Create a ruleList which will indicate the rules that we would add into
% our fis

% The ruleList encodes information as such:
% Each Row is a separate Rule
% Column 1 - Index of membership function for first input
% Column 2 - Index of membership function for second input
% Column 3 - Index of membership function for output
% Column 4 - Rule weight
% Column 5 - Fuzzy operator (1 for AND, 2 for OR)

% We will be encoding 4 Rules:
% R1: If service is poor then tip is cheap.
% R2: If service is excellent and food is delicious then tip is generous.
% R3: If food is lousy then tip cheap.
% R4: If service is good and food is delicious then tip is average. 

ruleList = [1 0 1 1 1;     % Use AND when 1 of the 2 inputs is not used 
            3 2 3 1 1;
            0 1 1 1 1;
            2 2 2 1 1];
        
fis = addrule(fis,ruleList);  % Add the Rules into our fis using our ruleList




% Evaluating our fis by sending in 3 different Input Pairs [1 Input Pair contains a value for service_rating and a value for food_rating]

inputs = [3 7;
          9 8;
          4.5 2.5];
      
evalfis(inputs,fis)





