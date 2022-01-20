#![allow(non_snake_case)]

use std::env;
mod actions;

fn main() {
    let cliArgs: Vec<String> = env::args().collect();
    
    let service: &str = if cliArgs.len() > 2 { &cliArgs[2] } else { "None" };
    let action: &str = &cliArgs[1];
    let passwordLength: i32 = if cliArgs.len() > 3 { cliArgs[3].parse().unwrap() } else { 10 };
    if passwordLength < 8 { 
      println!("Seriously? Less than 8 characters? Absolutely not.");
      panic!(); 
    }
    match action {
        "create" => actions::create(service, passwordLength),
        "find" => actions::get(service),
        "update" => actions::update(service),
        "delete" => actions::delete(service),
        "help" => displayHelp(),
        _ => println!("No action matching {:?}", action)
    }
}

fn displayHelp() {
  println!("Welcome to PassMan 🔑");
  println!("Rules are pretty simple around here.  There are four actions:\n - create a password\n - update a password\n - delete a password\n - get a password\n");
  println!("Each action has its own set of arguments:\n - create: cargo run create <Service> <PasswordLength(optional >= 8, default=10)>");
  println!(" - update: cargo run update <Service> <PasswordLength(optional >= 8, default=10)>");
  println!(" - find: cargo run find <Service>");
  println!(" - delete: cargo run delete <Service>\n");
  println!("Everything does exactly what it sounds like, and stores the encrypted password in Mongo");
  println!("You will need your own Mongo Cluster because I am not going to hold your passwords.\nUse at your own risk.\n\nHappy hacking :)");
}