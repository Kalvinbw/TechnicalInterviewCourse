/* 
Given an integer array, give the maximum product of a triplet in an array.

Examples:
Input = [10, 3, 5, 6, 20]
Output = 1200 (product of 10, 6, and 20)

Input:  [-10, -3, -5, -6, -20]
Output: -90

Input:  [1, -4, 3, -6, 7, 0]
Output: 168

Source: https://www.geeksforgeeks.org/find-maximum-product-of-a-triplet-in-array/
*/

const factors1 = [10, 3, 5, 6, 20] // 1200
const factors2 = [-10, -3, -5, -6, -20] // -90
const factors3 = [1, -4, 3, -6, 7, 0] // 168

function merge_sort(array) {
    if (array.length > 1) {
        let mid = Math.floor(array.length / 2);
        let l = array.slice(0, mid);
        let r = array.slice(mid, array.length);
        merge_sort(l);
        merge_sort(r);
        let i = 0;
        let j = 0;
        let k = 0;
        while (i < l.length && j < r.length) {
            if (l[i] < r[j]) {
                array[k] = l[i];
                i++;
            } else {
                array[k] = r[j];
                j++;
            }
            k++;
        }
        while (i < l.length) {
            array[k] = l[i];
            i++;
            k++;
        }
        while (j < r.length) {
            array[k] = r[j];
            j++;
            k++;
        }
    }
}

function find_max_product(array) {
    merge_sort(array);
    let len = array.length;
    let top = array[len-1] * array[len-2] * array[len-3];
    let bottom_top = array[0] * array[1] * array[len-1];
    return top > bottom_top ? top : bottom_top;
}

console.log(find_max_product(factors1));
console.log(find_max_product(factors2));
console.log(find_max_product(factors3));