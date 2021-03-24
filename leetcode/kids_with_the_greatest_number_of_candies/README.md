# 1431. Kids With the Greatest Number of Candies
> Easy

Given the array `candies` and the integer `extraCandies`, where `candies[i]` represents the number of candies that the **ith** kid has.

For each kid check if there is a way to distribute `extraCandies` among the kids such that he or she can have the **greatest** number of candies among them. Notice that multiple kids can have the **greatest** number of candies.


**Example 1:**
<pre>
<b>Input:</b> candies = [2,3,5,1,3], extraCandies = 3
<b>Output:</b> [true, true, true, false, true] 
<b>Explanation:</b> 
Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies --- the greatest number of candies among the kids. 
Kid 2 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 
Kid 3 has 5 candies and this is already the greatest number of candies among the kids. 
Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies. 
Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 
</pre>


**Example 2:**

<pre>
<b>Input:</b> candies = [4,2,1,1,2], extraCandies = 1
<b>Output:</b> [true,false,false,false,false] 
<b>Explanation:</b> There is only 1 extra candy, therefore only kid 1 will have the greatest number of candies among the kids regardless of who takes the extra candy.
</pre>

**Example 3:**

<pre>
<b>Input:</b> candies = [12,1,12], extraCandies = 10
<b>Output:</b> [true,false,true]
</pre>

#### Constraints:

- `2 <= candies.length <= 100`
- `1 <= candies[i] <= 100`
- `1 <= extraCandies <= 50`

# Submission Detail
**103 / 103** test cases passed.  
Status: ***Accepted***  
Runtime: **24 ms**, faster than **76.37%** of Python online submissions for Kids With the Greatest Number of Candies.  
Memory Usage: **13.4 MB**, less than **43.36%** of Python online submissions for Kids With the Greatest Number of Candies.