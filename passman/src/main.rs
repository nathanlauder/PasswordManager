#![allow(non_snake_case)]

use std::env;
mod actions;

fn main() {
    let cliArgs: Vec<String> = env::args().collect();
    
    let service:String = cliArgs[2].to_string();
    let action:&str = cliArgs[1].as_str();
    match action {
        "create" => actions::create(service),
        "find" => actions::get(service),
        "update" => actions::update(service),
        "delete" => actions::delete(service),
        _ => println!("No action matching {:?}", action)
    }
}
