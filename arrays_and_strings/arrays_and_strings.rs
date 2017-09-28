/*
    1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures?
*/
use std::collections::HashSet;

fn all_unique(string: &str) -> bool {
    let mut characters = HashSet::new();
    for character in string.chars() {
        if characters.contains(&character) {
            return false
        }
        characters.insert(character);
    }
    return true;
}

fn all_unique_(string: &str) -> bool {
    return true;
}

fn main() {
    let string = "aaaa";
    println!("Is unique {}? {}", string, all_unique(string));


    let other_string = "abc";
    println!("Is unique {}? {}", other_string, all_unique(other_string));
}