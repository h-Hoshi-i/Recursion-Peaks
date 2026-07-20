# TODO: Make sure two_d_peak always returns the same type.
# Right now it sometimes returns a value, sometimes (index, value),
# and sometimes a string.

# TODO: Fix the m == 1 case.
# my_max(a[0]) finds the max of the first ROW, not the only COLUMN.

# TODO: Handle [[]] (a matrix with an empty row).
# Currently this will cause my_max() to access col[0] and crash.

# TODO: Decide whether my_max() should support empty lists.
# If not, document that assumption or raise a clearer exception.

# TODO: When recursing to the right with row[j:],
# remember that column indices are shifted.
# If returning coordinates later, adjust the column index.

# TODO: Verify that slicing the matrix during recursion
# does not lose information needed for the final answer.

# TODO: Remove debugging print() statements before submission.

# TODO: Check whether the assignment wants the peak VALUE,
# the (row, column) location, or both.

# TODO: Verify the base cases (1, 2, and 3 columns)
# are consistent with the recursive algorithm.

# TODO: Test matrices containing duplicate values.
# Equal neighboring values should still count as a valid peak
# if using the "no neighbor is greater" definition.

# TODO: Test matrices containing negative numbers.

# TODO: Test a matrix with only one row.

# TODO: Test a matrix with only one column.

# TODO: Test an empty matrix.

# TODO: Test a matrix where the peak is already in the middle column.

# TODO: Test cases that force recursion to the left.

# TODO: Test cases that force recursion to the right.

# TODO: Test both even and odd numbers of columns.

# TODO: Consider replacing the custom error strings with
# exceptions or a consistent return value.

#=================================================================
#=================================================================

# BUG: m == 1 searches the first row instead of the only column.

# BUG: Right-side recursion changes column numbering after slicing.
# This matters if the function is expected to return coordinates.
