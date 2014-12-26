The most naive solution, generating all possible subarrays and reducing them to find their product, worked, but was way too slow. And it was wasteful -- though it already calculated the product of `[2, 3]`, it would have to do it again when calculating the product of `[2, 3, 4]`.

A less wasteful, still naive solution is to iterate the indices making up each subarray, and incrementally calculating the product, e.g.:

```python
for i, base in enumerate(A):
    product = base
    for num in A[i+1:]:
        product *= num
```

But even this is O(n^2/2), and I still think it wastes calculations.

For too long, I ignored my gut, which nagged me about positives/negatives being most important. I finally went down that road, and figured that for an array of integers where n > 0, the max product is simply the product of the array. If the array is |n| > 0, the biggest product is the longest string which is positive. 

To find that, I figured I'd calculate the product of the entire array. If that's positive, boom done. If it's negative, though, I'd start shaving off the rightmost number until the result is positive. Then I'd do the same with the leftmost number (starting over the the entire array's product). The highest of those two would be the max product.

That proved to be true. However, my assumption of |n| > 0 wasn't right. So, I figured the zeroes to be poisonous, and split the array into sections by the zeroes. The largest product of those sections (using the rules above) would be the max product. My one last slip-up on that was forgetting to include 0 in that max product judgment. For instance, the correct result of `[-2, 0, -1]` is `0`, not `-1`.

That was fun :D
