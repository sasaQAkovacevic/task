## Bug Report

Below is a list of defects found during execution

---

### Bug-01 - Placing several bets regardless of insufficient balance

* **Severity:** Critical

#### 🐾 Reproduction Steps
1. Open the application in Chrome browser
2. Open Developer Tools (in browser), got to Network tab
2. Find an upcoming match
3. Choose the highest odd
4. Enter the highest stake - 100
5. Click on PLACE BET button
6. While the spinner is still on, click quickly on the same button several times, until success modal appears
7. In Network tab check the list of the place-bet API calls
8. Close all opened modals, check all successful bets that you managed to place
9. Reload the page and check the balance

#### 🔍 Expected vs. Actual Result
* **Expected Result:** Only one bet is placed, place-bet endpoint is locked after first placed bet, balance does not go to negative number.
* **Actual Result:** Several bets are placed, most of them are successful, and balance goes to negative number. 

#### 💼 Business Impact
* User can place several equal bets, without having enough money in balance, and balance can go into negative number which might be several time bigger than initial balance.
* This bug is reproduced only on UI, on API side (I was using Swagger page for that) everything works OK and it immediately returns 409. 

#### 📸 Evidence
* Screenshots: 
* 1. SeveralBetsPlacedByFastClickingOnPlaceBetButtonAfterFirstClick.png 
* 2. NewNegativeBalanceAfterReloadingThePage.png

---

### Bug-02 - Placing bets is possible on past matches

* **Severity:** Critical

#### 🐾 Reproduction Steps
1. Open the application in Chrome browser
2. Find a match that happed few days ago
3. Choose the highest odd
4. Enter the highest stake - 100
5. Click on PLACE BET button
6. Check the Bet Placed Successfully! modal

#### 🔍 Expected vs. Actual Result
* **Expected Result:** Past matches should not be visible on the page, and thus there should  not be an option to bet on them. 
* **Actual Result:** Past matches are visible on the page, and the bet is placed successfully. 

#### 💼 Business Impact
* The bug makes this application a betting heaven for a user - he can choose several past matches, choos the right odd, place the bet and collect the money at the end. 

#### 📸 Evidence
* Screenshots: 
* 1. SuccessfulBetOnPastMatch.png

---

### Bug-03 - Incorrect Potential Payout On Bet Placed Successfully Modal

* **Severity:** High

#### 🐾 Reproduction Steps
1. Open the application in Chrome browser
2. Find a match 
3. Choose the odd
4. Enter the stake
5. Check the Potential Payout amount on Bet Slip
5. Click on PLACE BET button
6. Check the Potential Payout amount on the Bet Placed Successfully modal

#### 🔍 Expected vs. Actual Result
* **Expected Result:** Potential Payout amount is correct and the same on both places 
* **Actual Result:**  Potential Payout amount is incorrect on the Bet Placed Successfully modal

#### 💼 Business Impact
* The bug causes confusion: user can be unsure  whether the system works correctly and how accurate is the Potential Payout

#### 📸 Evidence
* Screenshots: 
* 1. PotentialPayoutOkOnBetSlip.png
* 2. PotentialPayoutWrongOnBetPlacedSuccesfully.png

---

### Bug-04 - Closing Bet Placed Successfully Modal does not refresh the balance amount

* **Severity:** High

#### 🐾 Reproduction Steps
1. Open the application in Chrome browser
2. Find a match 
3. Choose the odd
4. Enter the stake
5. Check the current balance on the UI
6. Click on PLACE BET button
7. Close the modal
8. Check the current balance on the UI

#### 🔍 Expected vs. Actual Result
* **Expected Result:** After closing the modal the recalculated Balance is shown on the page
* **Actual Result:**  After closing the modal the previous Balance is shown on the page

#### 💼 Business Impact
* The bug causes confusion: user can be unsure about exact balance amount
* This is pure UI bug, after placing a bet, on API call the calculation is correctly done

#### 📸 Evidence
* Screenshots: 
* 1. StartingBalance.png
* 2. BetSlipStake10.png
* 3. BetPlacedBalanceRecalculatedInApiCall.png
* 4. UiAfterClosingTheModalBalanceNotRefreshed.png

--- 

### Bug-05 - Positions of the teams have been swapped on Bet Placed Successfully Modal

* **Severity:** High

#### 🐾 Reproduction Steps
1. Open the application in Chrome browser
2. Find a match 
3. Choose the odd
4. Enter the stake
5. Check match details (positions of two teams) on Bet Slip
6. Click on PLACE BET button
7. Check match details (positions of two teams) on Bet Placed Successfully modal

#### 🔍 Expected vs. Actual Result
* **Expected Result:** The positions are the same as on Bet Slip
* **Actual Result:**  The positions are swapped (home team is guest and vice versa)

#### 💼 Business Impact
* The bug causes confusion: user can be unsure about the home/away team and chosen odd
* This is pure UI bug, when placing a bet, the order of the teams is correct

#### 📸 Evidence
* Screenshots: 
* 1. OrderOfTeamsCorrectOnTheBetSlip.png
* 2. OrderOfTeamsSwappedtOnTheModal.png

--- 
### Other bugs found

Below is a list of defects found during exploration.

* 1. Although every amount on UI and API is given in euros, when placing a bet , the currency is USD
* 2. ODDS RANGE modal does not have neither Cancel nor Close button, because of this - if user selects new range ad change his mind and want to revert to previously selected range it is not possible
* 3. In ODDS RANGE modal it is possible to select impossible range: with sliders user can set following range: min: 6.2, max: 2.5
* 4. In Bet Slip, when user put some value higher than max (100), it is possible to add numbers there indefinitely (screenshot: HugeNumberAsStakeValueInBetSlip.png)
* 5. In Bet Placed Successfully Modal timestamp is not in correct format (it says: "Today, 18:34")