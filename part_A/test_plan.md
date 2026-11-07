## Test Plan

Below is a list of defects found during execution and exploration.

---
Maximum stake is €100.00
### Requirements review

The following are discrepancies between the requirements and the actual state of the application:
 - 2.1 - point 1 is not satisfied (Display upcoming football matches)
 - 2.2 - point 3 is not satisfied (available balance - it is shown only in bet slip’s empty state)
 - 2.3 - point 3 is not satisfied (stake is deducted - it is not visible on the success modal)
 - 2.3 - point 4 is actual naming is slightly different (retry option is REBET button)
 - 2.4 - point 2 is satisfied but order of teams is switched
 - 2.4 - point 3 is not satisfied (selection is not shown)
 - 2.6 - point 2 is not satisfied (by using slider buttons you can make this range: min: 6.5, max: 2.5)
 - 3 - rule Event type is not satisfied (matches from the past are shown and you can place a bet on them)
 - 3 - rule Currency is not satisfied (although on UI all is shown in Euros, in API call /place-bet currency is USD)
 - 4.1 - rule Stake minimum is not satisfied (through API call you can put 1.00 there and the call will be succesfull)
 - 5 - reset balance API call shows 125.5 as a balance, and on UI it is 120  

Duplicate in requirements:
 - 2.1 - points 3 and 5 points to the same behavior

#### 🐾 Test scenarios

#### Pre-conditions:

* Open the application in Chrome browser

---

### TS-01 - Placing bet on upcoming match - happy path

#### 🐾 Priority: 
* Critical 

#### 🐾 Risk Rationale: 
* This is a key, revenue-generating user case; if this flow is disrupted, the application cannot be considered functional.

#### 🐾 Steps

1. Check the balance amount 
2. Find an upcoming match 
3. Choose the highest odd
4. Enter the highest stake (100)
5. Click on PLACE BET button
6. Check the Bet Placed Successfully! modal
7. Close the modal.
8. Check the balance amount 

#### 🔍 Expected Result

1. Balance amount is positive
2. An upcoming match is found
3. Bet Slip populates with match details and highest odd is selected
4. Stake is accepted as valid
5. Button change name to PLACING, with loader
6. The Bet Placed Successfully! modal appeared with the bet details
7. Modal is closed 
8. Balance amount is recalculated 

---

### TS-02 - Validate Bet Placed Successfully Modal

#### 🐾 Priority: 
* High 

#### 🐾 Risk Rationale: 
* The modal window is the final point in the application where bet details can be viewed; therefore, it is crucial that these details are entirely accurate to avoid any user confusion.

#### 🐾 Steps

1. Find a match 
2. Choose the odd
3. Enter the stake
4. Click on PLACE BET button
5. Check the following on Bet Placed Successfully Modal:
   * "Bet Placed Successfully!" message
   * Bet ID number
   * match details - teams
   * stake value
   * odds value
   * Potential Payment value
   * Bet timestamp
   * Close button
   * X button

#### 🔍 Expected Result

1. Match is found
2. Bet Slip is populated with match details
3. Stake is populated
4. Button change name to PLACING, with loader
5. Bet Placed Successfully modal appears with following content:
   * "Bet Placed Successfully!" message
   * Bet ID number
   * match details - teams are in correct order
   * correct stake value
   * correct odds value
   * correct Potential Payment value (odds * stake)
   * correct and complete Bet timestamp
   * Close button
   * X button

---

### TS-03 - Validate Potential Payout on Bet Slip

#### 🐾 Priority: 
* Critical 

#### 🐾 Risk Rationale: 
* The Potential Payout feature is important in the sense that it should further motivate the user to place a bet.

#### 🐾 Steps

1. Find a match 
2. Choose the odd
3. Enter the stake
4. Check the Potential Payout amount on Bet Slip
5. Choose the other odd
6. Check the Potential Payout amount on Bet Slip
7. Enter the other stake
8. Check the Potential Payout amount on Bet Slip


#### 🔍 Expected Result

1. Match is found 
2. Bet Slip is populated with match details
3. Stake is populated
4. Potential Payout amount on Bet Slip is calculated (odds * stake)
5. Odd value is changed
6. Potential Payout amount on Bet Slip is recalculated (new odds * stake)
7. Stake value is changed
8. Potential Payout amount on Bet Slip is recalculated (odds * new stake)

---

### TS-04 - Validate stake under balance - validation scenario

#### 🐾 Priority: 
* High

#### 🐾 Risk Rationale: 
* It is important that the stake always remains within the limits of the existing balance; this ensures that a user cannot end up with a negative balance when placing a bet.

#### 🐾 Steps

1. Place few bets until balance drop below €100.00
2. Find a match 
3. Choose the odd
4. Enter the stake - €100
5. Check the validation message on Bet Slip
6. Place a bet with stake equal as current balance 
7. Find another match 
8. Choose the odd
9. Enter the other stake - €10
10. Check the validation message on Bet Slip


#### 🔍 Expected Result

1. Balance is below €100.00 
2. Match is found 
3. Bet Slip is populated with match details
4. Stake is populated
5. There is validation error: "Insufficient balance"
6. Balance is €0.00 
7. Match is found 
8. Bet Slip is populated with match details
9. Stake is populated
10. There is validation error: "Insufficient balance"

---

### TS-05 - Validate min and nax stake values - boundary conditions

#### 🐾 Priority: 
* Critical 

#### 🐾 Risk Rationale: 
* From a business perspective, it is important to have strict validation for the minimum and maximum stake values. This ensures that any stake entered into our application always falls within the specified range.

#### 🐾 Steps

1. Find a match 
2. Choose the odd
3. Check the validation messages on Bet Slip - while entering following stakes: 
4. Enter the stake - €0.09
5. Enter the stake - €1.00
6. Enter the stake - €1.01
7. Enter the stake - €99.09
8. Enter the stake - €100.00
9. Enter the stake - €100.01

#### 🔍 Expected Result

1. Match is found 
2. Bet Slip is populated with match details
3. Stake is populated
4. There is validation error: "Minimum stake is €1.00"
5. There is no validation error 
6. There is no validation error  
7. There is no validation error 
8. There is no validation error 
9. There is validation error: "Maximum stake is €100.00"

---

#### Post-condition:

* Close the application in Chrome browser

---