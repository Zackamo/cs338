''' passwords.py
    By: Zack Johnson

    Code for the password cracking assignment of CS338 Computer Security
'''
import hashlib
import binascii

def main():
    words = [line.strip().lower() for line in open('words.txt')]
    #phase1(words)
    phase2(words)
    #phase3(words)
    

def phase1(words):
    output_file = open("cracked1.txt", "a")
    accounts = [line.strip() for line in open('example_passwords1.txt')]
    found = 0
    hashes = 0
    for word in words:
        hasher = hashlib.sha256(word.encode('utf-8'))
        digest = binascii.hexlify(hasher.digest())
        digest_string = digest.decode('utf-8')
        hashes += 1
        for account in accounts:
            account_list = account.split(':')
            username = account_list[0]
            password_hash = account_list[1]
            if(password_hash == digest_string):
                output_file.write(username + ":" + word + "\n")
                found += 1
        print("Found:", found)
    output_file.close()
    print("=====================")
    print("Passwords Found:", found)
    print("Hashes Computed:", hashes)

def phase2(words):
    output_file = open("cracked2.txt", "a")
    hash_users = {}
    for line in open('example_passwords2.txt'):
        account_list = line.split(':')
        username = account_list[0]
        password_hash = account_list[1]
        hash_users[password_hash] = username
    print("Initialization Finished")
    found = 0
    hashes = 0
    for word1 in words:
        for word2 in words:
            password = word1+word2
            hasher = hashlib.sha256(password.encode('utf-8'))
            digest = binascii.hexlify(hasher.digest())
            digest_string = digest.decode('utf-8')
            hashes += 1
            result = hash_users.get(digest_string, "false")
            if result != "false":
                output_file.write(result + ":" + password + "\n")
                found += 1
        print("Found:", found)
    output_file.close()
    print("=====================")
    print("Passwords Found:", found)
    print("Hashes Computed:", hashes)

def phase3(words):
    output_file = open("cracked3.txt", "a")
    accounts = [line.strip() for line in open('example_passwords3.txt')]
    found = 0
    hashes = 0
    for account in accounts:
        account_list = account.split(':')
        username = account_list[0]
        hash_list = account_list[1].split('$')
        #hash_list[0] = '' and hash_list[1] is the algoritm indicator
        salt = hash_list[2]
        password_hash = hash_list[3]
        for word in words:
            salted_word = salt + word
            hasher = hashlib.sha256(salted_word.encode('utf-8'))
            digest = binascii.hexlify(hasher.digest())
            digest_string = digest.decode('utf-8')
            hashes += 1
            if(password_hash == digest_string):
                output_file.write(username + ":" + word + "\n")
                found += 1
    print("Found:", found)
    output_file.close()
    print("=====================")
    print("Passwords Found:", found)
    print("Hashes Computed:", hashes)

if __name__ == '__main__':
    main()