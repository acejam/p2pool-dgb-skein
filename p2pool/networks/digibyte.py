from p2pool.bitcoin import networks

PARENT=networks.nets['digibyte']
SHARE_PERIOD=15
CHAIN_LENGTH=24*60*60//10
REAL_CHAIN_LENGTH=24*60*60//10
TARGET_LOOKBEHIND=50
SPREAD=30
IDENTIFIER='1bfe02342d4ae9b9'.decode('hex')
PREFIX='1bfe02342de3803a'.decode('hex')
P2P_PORT=5028
MIN_TARGET=0
MAX_TARGET=2**256//2**20 - 1
PERSIST=False
WORKER_PORT=5029
BOOTSTRAP_ADDRS='crypto.office-on-the.net'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-dgb-skein'
VERSION_CHECK=lambda v: True
VERSION_WARNING=lambda v: 'Upgrade DigiByte >=6.14.2!' if v < 70015 else None
