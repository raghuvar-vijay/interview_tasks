import os
from substrateinterface.contracts import ContractCode, ContractInstance
from substrateinterface import SubstrateInterface, Keypair

substrate = SubstrateInterface(
    url="ws://127.0.0.1:33105",
    type_registry_preset='canvas'
)

keypair = Keypair.create_from_uri('//Alice')



# Deploy contract
code = ContractCode.create_from_contract_files(
    metadata_file=os.path.join(os.path.dirname(__file__), 'target','ink' , 'metadata.json'),
    wasm_file=os.path.join(os.path.dirname(__file__), 'target','ink' , 'gs.wasm'),
    substrate=substrate
)

energy=int(float(input("Enter Energy(in kWh): ")))
price=int(float(input("Enter Price(in cents): ")))
from_add=input("Enter address of sender: ")
to_add=input("Enter address of receiver: ")

contract = code.deploy(
    keypair=keypair,
    endowment=10 ** 15,
    gas_limit=1000000000000,
    constructor="new",
    args={'_energy':energy,'_price': price, 'from':from_add, 'to':to_add},
    upload_code=True
)



print(f' Deployed @ {contract.contract_address}')
