import nbformat as nbf
def generate_filename(title):
    # Replace spaces with hyphens and remove other special characters
    filename = title.replace(' ', '-').replace('.', '').replace(':', '').replace('"', '').replace("'", '').replace('?', '').replace('!', '').replace(',', '').replace('(', '').replace(')', '').replace('&', '').replace(';', '').replace('[', '').replace(']', '').replace('{', '').replace('}', '').replace('/', '')

    # Add the ".ipynb" extension
    filename += '.ipynb'

    return filename

# # Example usage:
# title = "80. Remove Duplicates from Sorted Array II"
# filename = generate_filename(title)
# print(filename)  # Output: "80-Remove-Duplicates-from-Sorted-Array-II.ipynb"

def create_and_save_notebook(title, code_content="",md_content=""):
    # Generate the filename
    filename = generate_filename(title)

    # Create a new Jupyter Notebook
    notebook = nbf.v4.new_notebook()

    if md_content:
        notebook.cells.append(nbf.v4.new_markdown_cell(md_content))
    # Add a cell with the provided content (optional)
    if code_content:
        notebook.cells.append(nbf.v4.new_code_cell(code_content))


    # Write the notebook to the file
    with open(filename, 'w', encoding='utf-8') as file:
        nbf.write(notebook, file)

    print(f"Notebook '{filename}' created and saved.")

# Example usage:
title = "122. Best Time to Buy and Sell Stock II"
md_content = """\
# Maximize Stock Trading Profit Algorithm

- Time complexity: `O(n)` - We iterate through the array of prices only once.
- Space complexity: `O(1)` - No additional space is needed; calculations are done using a few variables.

## Algo:
- The algorithm aims to maximize the profit from stock price changes by simulating continuous buying and selling.
- Steps:
    1. **Initialization**: Set `left` to 0 to represent the buy day, and `right` to 1 to represent the sell day.
    2. Loop while `right` is less than the length of `prices`.
        - Calculate `curr` profit or loss by subtracting the price at `left` from the price at `right`.
        - If `curr` is positive (profit), add it to `total`.
        - Move `left` to `right`, and increment `right` to move to the next day.
    3. **Termination**: When `right` reaches the end of `prices`, the loop ends.
    4. The `total` variable represents the accumulated profit from all transactions.

## Example:
- Given `prices = [7, 1, 5, 3, 6, 4]`, the method would calculate the profits as `4` (buy at `1`, sell at `5`), `3` (buy at `3`, sell at `6`), for a total profit of `7`.

## Implementation Details:
- The `maxProfit` method is a member of the `Solution` class.
- It simulates buying and selling on each rising edge to maximize profit.
- The total profit is calculated by summing up the profits from each transaction.
- Edge cases like an array of length 1 are handled at the beginning, returning `0` as no profit is possible.

## Code:
```Java
class Solution {
    public int maxProfit(int[] prices) {
        /*
        Prev solution:
        Initialization:
            left = 0 
            right = 1
        Loop:
            curr = nums[left] - nums[right]

            (Note seems that there are no duplicate prices)
            curr < 0 -> found a smaller min @ right, set min to be nums[right]

            otherwise, update max profit
        Termination:
            Will terminate when there are no prices to iterate over anymore
            Will leave maxProfit as the max of all maxprofits
         */
        /*
        New Solution:
        Why not just buy and sell on the max day before a new min is found?
        Why not just constantly buy and sell every time you can?
        Proof:
            Let's graph the problem as a hailstone problem
            To maximize profit, need to capitalize on every single rising edge.
            So total profit = sum(risingEdge)
            Proof left to the reader. 
            Hint: 
                Supposed there are no falling edges, then total profit = the single rising edge
                If there are falling edges, adding all the rising edges = if there were no rising edges + mag of all falling edges (assuming an increasing graph)
        */
        
        // Case 1: b < a: a := b
        // Case 2: a < b: profit += b-a; a:= b

        if (prices.length == 1){
            return 0;
        }
        int left = 0;
        int right = 1;
        int total = 0;
        int curr = 0;
        while (right < prices.length) {
            curr = prices[right] - prices[left];
            if (curr > 0) total += curr;
            left = right++;
        }
        return total;
    }
}

```
"""
code_content = """\
"""

create_and_save_notebook(title, code_content, md_content)
