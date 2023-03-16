import os
import sys
import json
import pandas as pd
import numpy as np
from dotenv import load_dotenv
sys.path.append('/Users/amitairuskin/Desktop/redefine/redefine-backend/')
from common.utilities.web3_bundle import Web3Bundle
from common.utilities.globals import ChainIDS 
from common.wrappers.mongodb_wrapper import MongoDBWrapper
from common.wrappers.bitquery_wrapper import BitqueryWrapper

sys.path.append('/Users/amitairuskin/Desktop/redefine/redefine-backend/scripts/research/pool_compliance_v2')
load_dotenv()
chain_id = 1
web3 = Web3Bundle(ChainIDS(chain_id))
bit_query = BitqueryWrapper()
path = '/Users/amitairuskin/Desktop/redefine/redefine-backend/scripts/research/pool_compliance_v2/'
df = pd.read_csv(path + 'project_creator_info.csv')
def get_contracts(creator):
    creator_lower = creator.lower()
    try:
        res = bit_query.get_contract_creations_by_address(network='ethereum',
                                                    creator_address=creator_lower,
                                                    max_results=100,
                                                    days_back=300)
        contracts = res['data']['ethereum']['smartContractCalls']
        print(contracts)
        return contracts
    except Exception as e:
        print(e)
        return None
df['other_contracts'] = df.loc[:,'token_creator'].apply(lambda x: get_contracts(x))
print(df)
df.to_csv(path + 'ariel_project_data.csv')