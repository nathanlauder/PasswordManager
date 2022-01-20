#![allow(non_snake_case)]

use std::env;
mod actions;

fn main() {
    let cliArgs: Vec<String> = env::args().collect();
    
    let service: &str = &cliArgs[2];
    let action: &str = &cliArgs[1];
    match action {
        "create" => actions::create(service),
        "find" => actions::get(service),
        "update" => actions::update(service),
        "delete" => actions::delete(service),
        _ => println!("No action matching {:?}", action)
    }
}
