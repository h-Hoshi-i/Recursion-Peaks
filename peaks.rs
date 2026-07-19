fn find_a_peak(a: &[i32])->Option<&i32>{
    if a.len() <= 2{
        let n = a.len();
        if n == 2{
            if a[0] >= a[1]{
                return Some(&a[0]);
            } else{
                return Some(&a[1]);
            }
        } else if n == 1{
            return Some(&a[0]);
        } else{
            return None;
        }
    }

    let n = a.len() / 2;
    if a[n-1] >= a[n]{
        return find_a_peak(&a[..n]);
    } else if a[n+1] >= a[n]{
        return find_a_peak(&a[n+1..]);
    } else{
        return Some(&a[n]);
    }

}

fn main(){
    let a = [0,1,2,3,4,5,6,7,8,9];
    match find_a_peak(&a) {
        Some(value) => println!("{}", value),
        None => println!("No peak found"),
    };

}