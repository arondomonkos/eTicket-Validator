# eTicket Validator

This program processes and analyzes boarding data for a bus line equipped with electronic ticket validation. It checks passenger validity, generates statistics on ticket usage, and outputs alerts for soon-to-expire passes.

## Functionality

1. **Data loading** – Reads the `utasadat.txt` file and stores each boarding attempt.
2. **Passenger count** – Determines how many unique passengers attempted to board.
3. **Validation check** – Identifies how many passengers were denied boarding due to invalid tickets or expired passes.
4. **Busy stop** – Finds the stop with the most boarding attempts.
5. **Statistics** – Calculates how many passengers traveled with free or discounted passes.
6. **Expiration alert** – Outputs a list of passengers whose pass will expire within 3 days after their last boarding attempt.

## Input

- `passdata.txt`: Contains data in the following format per line:
  ```
  stop_number boarding_time card_id ticket_type validity
  ```

## Output

- Console messages for all answers.
- `warning.txt`: A file listing the card IDs and expiration dates of passes expiring soon.

---
Developed by Áron Domonkos, 2023.