''' sanity_check.py
    By Zack Johnson

    do some simple math with huge numbers to check that my ssh keys have the right properties.
'''

import math

def main():
    p = int('00d542fd844bb4e4aa0f9a48abb2843637cfc35107a2b3ca1be6836465885931d4436e9e1aff6829c2f7c16efa73b67f647be456b6873b6ce662d97c92e15c38e26a96b18b812d9fc4c68ca57e60b2b8e557d0bd80546e288bc9eff7391307f04c89ab2fd256115b4aa2afddf8d248bb962a85c29ce14fb7c74f6db8906c0ebef630edfd42aedbe30c102c3723575ed611cdc250f3ad9457320ebd2be8992bfe3501ed2dd74a770960aeac0af659c5932fba7bb74173dbefee0942b363bfd6d61d', 16)
    q = int('00cdad97a17851981cb796928c6527fc04d6efb16596e6bf93e193e50c0758c81f49f6d50fa730f2b5fbd30d523c28cd40f03b434602741af095933f51ffa8128873e0a8ec442c031cea2d89e59dead884c6ed99de10d313ba40f779aa49dcc5d9c9f6526127c9b37e9a8c5fb79a5bdcb8b5a39971e36ac96c1334b824b5b9a4cc7d4ab9e47e05e9d0d1dbea0a90384e1b81fc9f8fc0e1aa033a269604a715b89cd50d96746a9fedd9141413636d67075997e7be88dfb33642a66c8064fc862cf3', 16)
    n = int( '00ab57419949ecdcf5f2328f0372ad3aef490f6a6853039b60dde4c2cde08175c3b9a9e663d338f8507a16faa0ab293b2462ee7db49640cbf9def6c3460e5a3a8241978d71521ccb7f9a322a71be2e8158e740eecd36845c42e0c7fbce6dda41029eec26b41b1fdb7cce9c6a306770410117a90dd2c52ab1c3a9f2dd6365e8dd974efc132fee6ecdb826d617de95940e7e0e3455f3f9dc55d0747617c6c5291219fd322497128aacb9c169254a144e292ef09392e226e1aed465365b4ae9662925f6bc28f7fa8b0c95c7b4e51037fac390081295f797e96d0645fb75e1a26d38e389964bd92ef8a79825bf54451146d7df6d5a089c23380d008f1f2ff530152a1f03fd2529a30aba173f3b65129d28eeabc0efa4b2546befca60954c2065ba1162677041cfb1be9d1368ea5ddb022be82cc10c3fd02d37f32cb33d30422f78608f1a5075cb35a28558feab868257c530583214da2c5ba685c57c8535bcb656dd7c0fc71fb506e2113356e4a9a739db2632e1a615bdc2c6abdfd5697534a4e83987', 16)
    d = int( '0b62c1fe30b667bc843aaddc39cb9f25f581ebbd40fef55d4b817f1c7535c5209b7ed9cb7a66c7c1794b7b9e1fa19ec77d3781ecf52b1b22e0991f42d183576dfe73d6b7581087c953f2cf753d8113a157c4add9bf2cae80d73512db95db3204bd90cdc59c23d2cf095fc582afecfab4dae0a605828aa2c370d0adbb8433243e80c629743ef0e804bbb7f0601f2a768813e3906ea504ea42eeea460c345fd54f1acf313544cb284d33b80bfd4f3a1e6c7b1a236199d9d7674fce7be48f7bf571ef8b90a8206d50ad1dc8a86acf42c94f742208c8e21975ebf273ae2c48625efd4d91e5643bb5b5a5fe0c70cb95956ee00ce2d8250cebd08581f91bd3559db65edc3b76cbb902a29b317c0e982afaf1d881b1ab04cfd8d39310aa7bee235f222fecd5095094f62327749d9e8f95de270584832f4553ef3a1aaa2b8e5d0e32caa6beec1904077cdf058855a74f24213b37c25099355b85a4d97c44d7504af57edb42e8f98e171c5afe85c4a3e9229cccb518cb019c08a0f4e63da891de5cd69b69', 16)
    e = 65537
    lamN = lcm(p-1, q-1)
    if(p * q == n):
        print("p * q does equal n!")
    print("d * e mod lambda(n):", (d * e) % lamN)

def lcm(x, y):
    return x * y // math.gcd(x,y)

if __name__ == "__main__":
    main()