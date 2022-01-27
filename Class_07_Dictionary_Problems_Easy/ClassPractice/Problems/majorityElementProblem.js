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

function majority(array) {
    let mid = Math.round(array.length / 2)

    let my_counts = {}

    for (let i=0; i < array.length; i++) {
        if (my_counts[array[i]] !== undefined) {
            my_counts[array[i]]++;
            if (my_counts[array[i]] >= mid) {
                return array[i];
            }
        } else {
            my_counts[array[i]] = 1;
        }
    }

    for (c of my_counts) {
        if (my_counts[c] >= mid) {
            return c
        }
    }
}

console.log(majority(arr1))