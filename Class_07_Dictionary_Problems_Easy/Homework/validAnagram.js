/**
 * Given two strings s and t, return true if t is an anagram of s, and false otherwise. Use a dictionary.
 * 
 * An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
 * typically using all the original letters exactly once.
 * 
 * Input: s = "anagram", t = "nagaram"
 * Output: true
 * 
 * Input: s = "rat", t = "car"
 * Output: false
 * 
 * Source: https://leetcode.com/problems/valid-anagram/
 */

let s = 'anagram'
let t = 'nagaram'

// brute force
function isAnagram(s, t) {
    let s_dict = {};
    let t_dict = {};

    for (i = 0; i < s.length; i++) {
        if (s_dict.hasOwnProperty(s[i])) {
            s_dict[s[i]] = s_dict[s[i]] + 1;
        } else {
            s_dict[s[i]] = 1;
        }
    }

    for (i = 0; i < t.length; i++) {
        if (!s_dict.hasOwnProperty(t[i])) {
            return false;
        }
        if (t_dict.hasOwnProperty(t[i])) {
            t_dict[t[i]] = t_dict[t[i]] + 1;
        } else {
            t_dict[t[i]] = 1;
        }
    }

    for (const letter in s_dict) {
        if (!t_dict.hasOwnProperty(letter) || s_dict[letter] != t_dict[letter]) {
            return false;
        }
    }

    for (const letter in t_dict) {
        if (!s_dict.hasOwnProperty(letter) || s_dict[letter] != t_dict[letter]) {
            return false;
        }
    }

    return true;
}

//optimized
function isAnagramopt(s, t) {
    let letter_counts = {};

    for (i = 0; i < s.length; i++) {
        if (letter_counts.hasOwnProperty(s[i])) {
            letter_counts[s[i]][0]++;
        } else {
            letter_counts[s[i]] = [1, 0];
        }
    }

    for (i = 0; i < t.length; i++) {
        if (!letter_counts.hasOwnProperty(t[i])) {
            return false;
        }
        letter_counts[t[i]][1]++;
    }  

    for (const letter in letter_counts) {
        if (letter_counts[letter][0] != letter_counts[letter][1]) {
            return false;
        }
    }
    return true;
}

//online solution
function online(s, t) {
    let letter_counts = {};

    for (l of s) {
        if (letter_counts[l] != undefined) {
            letter_counts[l]++;
        } else {
            letter_counts[l] = 1;
        }
    }

    for (l of t) {
        if (letter_counts[l] === undefined) {
            return false;
        }
        if (letter_counts[l] < 1) {
            return false;
        }
        letter_counts[l]--;
    }
    return true;
}

// console.log(isAnagram(s, t));
s = 'anagram'
t = 'naagrams'
console.log(online(s, t));