from ib_insync import *
util.startLoop()

ib = IB()
ib.connect('127.0.0.1', 4002, clientId=10)
#print(ib.positions())

contract = Option('SPY', '20220701', 413, 'C', 'SMART')

print(ib.reqContractDetails(contract))

ib.disconnect()
