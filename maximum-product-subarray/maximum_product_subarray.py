class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        # First, split into sections by 0
        sections = []
        section_begin = 0
        products = []
        for i, num in enumerate(A):
            if num == 0:
                sections.append(A[section_begin:i])
                section_begin = i + 1
                # If we find a 0, it's possible it may be the largest product,
                # if the rest are all negatives. Let's not forget that.
                products.append(0)
        sections.append(A[section_begin:])

        # Remove any empty sections
        sections = filter(None, sections)

        # If no sections remain, our array was full of zeroes. Return 0.
        if not sections:
            return 0

        # Find the max product for each section
        for section in sections:
            # If the total product of a section is positive, it's the largest
            product = reduce(lambda a, b: a * b, section)
            if product >= 0:
                products.append(product)
                continue

            # If not, try shaving from the left until it's positive
            left_product = product
            for num in section[:len(section) - 1]:
                left_product /= num
                if left_product > 0:
                    break

            # And the same from the right
            right_product = product
            for num in section[:0:-1]:
                right_product /= num
                if right_product > 0:
                    break

            # The largest of these two is the max product for the section
            products.append(max([left_product, right_product]))

        # The largest product of all the sections is the max product
        return max(products)
