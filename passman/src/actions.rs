use rand::Rng; // random functionality

pub fn create(service: &str, length: i32) {
    println!("Creating {} password of len: {}", service, length);
    let password: String = generatePassword(length);
    println!("{}: {}", service, password);
}

pub fn get(service: &str) {
    println!("Getting: {:?}", service);
}

pub fn update(service: &str) {
    println!("Updating: {:?}", service);
}

pub fn delete(service: &str) {
    println!("Deleting: {:?}", service);
}

fn generatePassword(length: i32) -> String {
    let mut rng = rand::thread_rng();
    let possibleChars: String = String::from("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*");
    let mut result: String = String::from("");
    for _i in 0..length {
      let index: usize = rng.gen_range(0..possibleChars.len());
      let character: String = possibleChars.chars().nth(index).unwrap().to_string(); 
      result.push_str(&character);
    }
    result
}