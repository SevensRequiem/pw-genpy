# pw-genpy
simple token/password generator written in python

usage:
`python tokens.py`  
enter how many u want to generate  
copy/paste them to notepad  
get a notebook ready   
when you want to use a token for an online service, write down the 4 char identifier for that service(s), and the service name  
say `12dD.4YBNvqre5XDsW01OUMmW99Fh4bXSOPvJf2hAvb1tln4piiDGen19foPHEoBhxyI3` is the token,  
`12dD` would be the identifier. so you use `12dD` to match the service to that whole token and copy/paste that token to login to your service.  
`12dD - My Service`  

just generate 100 tokens and only use 5~, how will anyone know which token is used for what? :P  


bruteforcing using ur tokens as a wordlist? unlikely, ratelimits + login attempts exist for your service (hopefully, get fail2ban on that!)
