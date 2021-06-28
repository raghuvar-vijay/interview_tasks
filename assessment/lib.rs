
#![cfg_attr(not(feature = "std"), no_std)]

use ink_lang as ink;


#[ink::contract]
mod ls {

    #[ink(storage)]
    pub struct Ls {

        en: ink_storage::collections::HashMap<(AccountId,AccountId),(i32,i32)>,
    }




    impl Ls{
        #[ink(constructor)]
        pub fn new(_energy: i32, _price: i32, from:AccountId, to:AccountId) -> Self {

                let mut en= ink_storage::collections::HashMap::new();
                en.insert((from,to), (_price,_price));
                        Self {
                            en
                            }
        }

        #[ink(constructor)]
        pub fn default() -> Self {
            Self {
                en: Default::default(),


            }
        }


        #[ink(message)]
        pub fn inc(&mut self, init_energy: i32, init_price: i32, _from:AccountId, _to:AccountId) {

    }

    
}

