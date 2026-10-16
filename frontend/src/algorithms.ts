export type Algorithm = {
  id: string
  name: string
  video: string
  complexity: string
  description: string
}

export const algorithms: Algorithm[] = [
  {
    id: 'linear-search',
    name: 'Linear Search',
    video: 'videos/LinearSearch.mp4',
    complexity: 'O(n)',
    description: 'Checks each element in order until the target is found.',
  },
  {
    id: 'binary-search',
    name: 'Binary Search',
    video: 'videos/BinarySearch.mp4',
    complexity: 'O(log n)',
    description: 'Halves a sorted array each step by comparing against the middle.',
  },
  {
    id: 'bubble-sort',
    name: 'Bubble Sort',
    video: 'videos/BubbleSort.mp4',
    complexity: 'O(n²)',
    description: 'Repeatedly swaps adjacent out-of-order pairs so the largest values bubble to the end.',
  },
  {
    id: 'linked-list-traversal',
    name: 'Linked List Traversal',
    video: 'videos/LinkedListTraversal.mp4',
    complexity: 'O(n)',
    description: 'Follows each node\'s next pointer from the head until it reaches NULL.',
  },
  {
    id: 'linked-list-insertion',
    name: 'Linked List Insertion',
    video: 'videos/LinkedListInsertion.mp4',
    complexity: 'O(n) to find, O(1) to link',
    description: 'Links the new node forward first, then points the previous node at it, so no part of the list is lost.',
  },
  {
    id: 'stack-push',
    name: 'Stack Push',
    video: 'videos/StackPush.mp4',
    complexity: 'O(1)',
    description: 'Adds a value on top of the stack; the most recently pushed value is always the first one out.',
  },
  {
    id: 'stack-pop',
    name: 'Stack Pop',
    video: 'videos/StackPop.mp4',
    complexity: 'O(1)',
    description: 'Removes and returns the top value, so values come back in the reverse of the order they went in.',
  },
  {
    id: 'valid-parentheses',
    name: 'Valid Parentheses',
    video: 'videos/ValidParentheses.mp4',
    complexity: 'O(n) time, O(n) space',
    description: 'Pushes every opening bracket and pops on each closing one; the string is valid if every pair matches and the stack ends empty.',
  },
  {
    id: 'invalid-parentheses',
    name: 'Invalid Parentheses',
    video: 'videos/InvalidParentheses.mp4',
    complexity: 'O(n) time, O(n) space',
    description: 'The same scan on "([)]": the closing bracket meets the wrong opener on top of the stack, so the string is rejected.',
  },
]
