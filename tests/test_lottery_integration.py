from brownie import network
import pytest
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    fund_with_link,
)
from scripts.deploy import deploy_lottery
import time


def test_can_pick_winner():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    lottery = deploy_lottery()
    account = get_account()
    lottery.startLottery({"from": account})
    lottery.enter({"from": account, "value": lottery.getEntranceFee() + 100000}) #can add a bit of WEI at the end if you run into an issue
    lottery.enter({"from": account, "value": lottery.getEntranceFee() + 100000}) #can add a bit of WEI at the end if you run into an issue
    fund_with_link(lottery)
    time.sleep(180)
    lottery.endLottery({"from": account})
    assert lottery.recentWinner() == account
    assert lottery.balance() == 0