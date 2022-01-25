/*
Given an array nums of size n, return the majority element. 
The majority element is an element that appears more than [n/2] times. 
You may assume that the majority element always exists in the array.

Input = [3, 2, 3]
Output = 3

Input = [2, 2, 1, 1, 1, 2, 2]
Output = 2

Source: https://leetcode.com/problems/majority-element/
*/

const arr1 = [3, 2, 3] // 3
const arr2 = [2, 2, 1, 1, 1, 2, 2] // 2

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
            if (l[i] < r[i]) {
                array[k] = l[i];
                i++;
            } else {
                array[k] = r[j]
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

function find_maj(array) {
    merge_sort(array);
    mid = Math.floor(array.length / 2);
    return array[mid];
}


console.log(find_maj(arr1));