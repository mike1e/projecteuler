// Michael Le
// Problem 2
// Even Fibonacci numbers
/*
Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
*/
function evenFib() {
  let sum = 0;
  let temp = 0;
  let prev = 1;
  let next = 2;
  const MAX = 4000000;

  while (next < MAX) {
    if (next % 2 == 0) sum += next;
    temp = next;
    next = prev + next;
    prev = temp;
  }
  return sum;
}

const result = evenFib();
console.log(result);